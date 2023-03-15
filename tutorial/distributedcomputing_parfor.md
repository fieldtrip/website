---
title: Speeding up your analysis using distributed computing with parfor
tags: [tutorial, matlab, script, parfor, distcomp, meg-language]
---

# Speeding up your analysis using distributed computing with parfor

## Introduction

Many times you are faced with the analysis of multiple subjects and experimental conditions, or with the analysis of your data using multiple analysis parameters (e.g., frequency bands). Parallel computing in MATLAB can help you to speed up these types of analysis. This tutorial describes an approach for distributing the analysis of multiple subjects using the [MATLAB Parallel Computing toolbox](http://www.mathworks.com/products/parallel-computing/).

Goals of this tutorial:

-   introduce looping to perform the same analysis on multiple subjects
-   use the [MATLAB Parallel Computing toolbox](http://www.mathworks.com/products/parallel-computing/) to do parallel computations and analyze multiple subjects at once
-   set up the code to deal with problematic subjects, such that successful analysis steps do not have to be repeated

This tutorial is focused on parallel computing, hence the code samples are set up to bring this aspect to the front. To keep it simple, as a consequence most of the code samples do NOT follow the recommendations in [Creating a clean analysis pipeline](/tutorial/scripting) regarding separating subject details from the analysis code, writing wrapper analysis functions, or handling of the input and output data through files. The final example also does not completely follow the guidelines, but does show what functions to use when interacting with files and paths to files in a parallel computing setting.

## Background on parallel computing

Parallel computing is different from sequential computing, especially when the actual computing is done on another computer than where the script is started. Some minimal information that you should be aware of:

-   **Variables indexing**: Parfor does have certain requirements on how variables are accessed that are used both inside and outside the loop. The Matlab editor will give hints, noticable by red and orange squigly lines, on code that is incompatible with the parfor requirements.
-   **Local versus remote**: The parallel loop will use a parallel pool of compute resources. This can be your local machine, but also a compute cluster elsewhere that has been made available, depending on what is specified in your Matlab settings. To check, and switch, where the code is run go to the Home tab, then in the Environment section, use the Parallel drowdown menu item. More information on the parallel settings can be found on the [MathWorks website](https://mathworks.com/help/parallel-computing/parallel-preferences.html), and in the local MATLAB  documentation. For instance how to find remote clusters, and how to change the default number of parallel workers.
-   **Memory usage**: Especially when running on your local machine, computer memory can be a problem. Since analysis in parallel, will use more computer memory. If total is more than actually available, will actually be slower than running sequential.  
-   **Paths to files**: When running on a remote cluster, and data is read from or written to file, the (relative) paths to the files as used in the code, should be such that they match the location of the data files as seen by the cluster.
-   **Parallel on the outside:** There is some overhead in transferring the work of a loop iteration to the parallel workers, even on your local machine. Thus, it is beneficial to have the worker do as much work as possible per loop iteration. This means that in general, the most outer loop should be the one that is parallelized.

## Prerequisites for this tutorial

To use parallel computing, the minimum requirement is to have the [Parallel Computing Toolbox](https://nl.mathworks.com/products/parallel-computing.html) installed and a valid license to use it. This can be checked with the below code:

    try
        poolObject = gcp();
        disp('Success, you can use parallel computing!')

    catch MExc
        disp(MExc)
        disp('Error, you do not have the correct prerequisites!')

        % If the error is like
        %       'gcp' requires Parallel Computing Toolbox.
        % then Parallel Computing Toolbox is not installed for this Matlab.
        % If the error is like
        %       Error using gcp (line 49)
        %       Unable to check out a license for the Parallel Computing Toolbox.
        % then PCT is installed, but you do not have a valid license to use it.
    end

This tutorial requires the original MEG datasets for the four subjects, and one additional dataset that is on purpose incorrect, which are available from:  

-   [Subject01.zip](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip)
-   [Subject02.zip](https://download.fieldtriptoolbox.org/tutorial/Subject02.zip)
-   [Subject03.zip](https://download.fieldtriptoolbox.org/tutorial/Subject03.zip)
-   [Subject04.zip](https://download.fieldtriptoolbox.org/tutorial/Subject04.zip)
-   [SubjectSEF.zip](https://download.fieldtriptoolbox.org/tutorial/SubjectSEF.zip)

Additional prerequisites:

-   Make sure FieldTrip is on your path, see this [FAQ](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path)
-   Have the necessary data next to each other in a single directory: the directories 'Subject01.ds', 'Subject02.ds', 'Subject03.ds', 'Subject04.ds', 'SubjectSEF.ds' should all be next to each other.
-   Put your test scripts also in this directory

## Starting code: single-subject, stripped version of eventrelatedaveraging

Here we give the code that will be the basis for the rest of the tutorial. It is an adaptation of the code in the [Event related averaging tutorial](/tutorial/eventrelatedstatistics). The adaptations were made to reduce the runtime and amount of generated files and plots, to be able to focus on the goals of this particular tutorial.

For reference, the changes in detail w.r.t. the [Event related averaging tutorial](/tutorial/eventrelatedstatistics):

-   Removed the line where select only trials that don't have artifacts. It is subject-specific, so needs to be handled on a per-subject basis. See [Creating a clean analysis pipeline](/tutorial/scripting) on how to define and use subject-specific settings. For this tutorial, we will ignore the fact that certain trials have artifacts.
-   Only use FIC condition, removed the IC and FC related lines. This to reduce the amount of code and calculation time.
-   No separate ft_selectdata call and saving of the intermediate data. Replaced with condition-data-selection inside ft_timelockanalysis call.
-   All data plotting removed (including setting `cfg.feedback = 'no'` for ft_prepare_neighbours), because useful when developing the analysis, but less so when applying analysis to multiple subjects.
-   The cfg and call signature of ft_timelockgrandaverage have been filled in.

### Exercise

{% include markup/info %}
-   Add a loop, such that both Subject01 and Subject02 are analyzed, and the results from both analyses are available at the end
-   Use the combined results in a call to ft_timelockgrandaverage  
{% include markup/end %}

    %% Trial definition
    cfg = [];
    cfg.dataset             = 'Subject01.ds';
    cfg.trialfun            = 'ft_trialfun_general';          % this is the default
    cfg.trialdef.eventtype  = 'backpanel trigger';
    cfg.trialdef.eventvalue = [3 5 9];                        % condition are: 3 = fully incongruent (FIC), 5 = initially congruent (IC), 9 = fully congruent (FC)
    cfg.trialdef.prestim    = 1; % in seconds
    cfg.trialdef.poststim   = 2; % in seconds

    cfg = ft_definetrial(cfg);

    %% Preprocess the data
    cfg.channel         = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
    cfg.demean          = 'yes';
    cfg.baselinewindow  = [-0.2 0];
    cfg.lpfilter        = 'yes';                              % apply lowpass filter
    cfg.lpfreq          = 35;                                 % lowpass at 35 Hz.

    data_all = ft_preprocessing(cfg);

    %% Timelockanalysis
    cfg = [];
    cfg.trials = data_all.trialinfo == 3;
    avgFIC = ft_timelockanalysis(cfg, data_all);

    %% HERE you would save intermediate results to file, in a non-tutorial script

    %% Planar gradient
    cfg = [];
    cfg.feedback        = 'no';
    cfg.method          = 'template';
    cfg.neighbours      = ft_prepare_neighbours(cfg, avgFIC);
    cfg.planarmethod    = 'sincos';
    avgFICplanar        = ft_megplanar(cfg, avgFIC);

    cfg = [];
    avgFICplanarComb = ft_combineplanar(cfg, avgFICplanar);

    %% HERE you would definitely save the results to file, in a non-tutorial script, since this is the end of the per-subject analysis

    %% Calculate grand average
    % Grand average is on multiple subjects, so first need to do the analysis
    % on multiple subjects.
    % cfg = [];
    % cfg.channel   = 'all';
    % cfg.latency   = 'all';
    % cfg.parameter = 'avg';
    % grandavgFIC = ft_timelockgrandaverage(cfg, allsubj_FIC_pc{:});

## Multi-subject, sequential loop

To do the same analysis on multiple subjects, in short:

-   put a loop around the analysis
-   within the loop, select the correct dataset
-   keep the final result data for each subject

Compared to the single-subject code above, the below code shows that for multi-subject analysis, the per-subject part has only minimal changes. To show where the change from single-subject to multi-subject happens, and how such code differs in its inputs, an actual ft_timelockgrandaverage call has been implemented. Grand average is on a combination of subjects, so that is an analysis that comes only after the per-subject analyses.

Note that, as mentioned earlier, the data organization for this tutorial deviates from the recommendations in [Creating a clean analysis pipeline](/tutorial/scripting).

### Exercise

{% include markup/info %}
-   Add SubjectSEF in the middle of the list of datasets, observe what happens.
-   What results are available?
-   Adapt the code so the loop runs in parallel.
{% include markup/end %}

    %% Loop over subjects
    datasets = {'Subject01.ds', 'Subject02.ds', 'Subject03.ds', 'Subject04.ds'};
    nr_subjects = length(datasets);
    allsubj_FIC_pc = cell(1, nr_subjects); % Initialize the output variable

    for i_set = 1:nr_subjects

        %% Select current subject
        % Get the info of the subject for this loop iteration
        % In this case, only the dataset name
        subjectinfo = datasets{i_set};

        %% Trial definition
        cfg = [];
        cfg.dataset             = subjectinfo;
        cfg.trialfun            = 'ft_trialfun_general';          % this is the default
        cfg.trialdef.eventtype  = 'backpanel trigger';
        cfg.trialdef.eventvalue = [3 5 9];                        % condition are: 3 = fully incongruent (FIC), 5 = initially congruent (IC), 9 = fully congruent (FC)
        cfg.trialdef.prestim    = 1; % in seconds
        cfg.trialdef.poststim   = 2; % in seconds

        cfg = ft_definetrial(cfg);

        %% Preprocess the data
        cfg.channel         = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
        cfg.demean          = 'yes';
        cfg.baselinewindow  = [-0.2 0];
        cfg.lpfilter        = 'yes';                              % apply lowpass filter
        cfg.lpfreq          = 35;                                 % lowpass at 35 Hz.

        data_all = ft_preprocessing(cfg);

        %% Timelockanalysis
        cfg = [];
        cfg.trials = data_all.trialinfo == 3;
        avgFIC = ft_timelockanalysis(cfg, data_all);

        %% HERE you would save intermediate results to file, in a non-tutorial script

        %% Planar gradient
        cfg = [];
        cfg.feedback     = 'no';
        cfg.method       = 'template';
        cfg.neighbours   = ft_prepare_neighbours(cfg, avgFIC);
        cfg.planarmethod = 'sincos';
        avgFICplanar = ft_megplanar(cfg, avgFIC);

        cfg = [];
        avgFICplanarComb = ft_combineplanar(cfg, avgFICplanar);

        %% Save subject results
        allsubj_FIC_pc{i_set} = avgFICplanarComb;

        %% HERE you would definitely save the results to file, in a non-tutorial script, since this is the end of the per-subject analysis
    end

    %% Calculate grand average
    cfg = [];
    cfg.channel   = 'all';
    cfg.latency   = 'all';
    cfg.parameter = 'avg';
    grandavgFIC = ft_timelockgrandaverage(cfg, allsubj_FIC_pc{:});

    %% HERE you would save the grandaverage results to file, in a non-tutorial script

    cfg = [];
    cfg.showlabels  = 'yes';
    cfg.layout      = 'CTF151_helmet.mat';
    figure; % Create a fresh figure for the next plot
    ft_multiplotER(cfg, grandavgFIC)


## Multi-subject, parfor loop

To do the same analysis as above, but in parallel over the subjects, all we have to do is change the for to a parfor. This holds if the sequential loop was already set up as above. However, often a sequential loop is not directly ready for parallel computing, or can be improved to be more robust.

### Exercise

{% include markup/info %}
-   Add SubjectSEF.ds in the middle of the list of datasets. What happens when running the script? What results are available inside the allsubj_FIC_pc variable?
- Remove the line near the top that states "allsubj_FIC_pc = cell(1, nr_subjects); % Initialize the output variable", and change the last non-comment line within the loop to read "allsubj_FIC_pc{end+1} = avgFICplanarComb;" What happens when running the script?
-   After the comment line "%% HERE you would save intermediate results to file, in a non-tutorial script", add an actual save call, to save the intermediate result avgFIC to a mat file, e.g. "save('avgFIC.mat', 'avgFIC');". What happens when running the script?
{% include markup/end %}

    %% Loop over subjects
    datasets = {'Subject01.ds', 'Subject02.ds', 'Subject03.ds', 'Subject04.ds'};
    nr_subjects = length(datasets);
    allsubj_FIC_pc = cell(1, nr_subjects); % Initialize the output variable

    parfor i_set = 1:nr_subjects

        %% Select current subject
        % Get the info of the subject for this loop iteration
        % In this case, only the dataset name
        subjectinfo = datasets{i_set};

        %% Trial definition
        cfg                         = [];
        cfg.dataset                 = subjectinfo;
        cfg.trialfun                = 'ft_trialfun_general';          % this is the default
        cfg.trialdef.eventtype      = 'backpanel trigger';
        cfg.trialdef.eventvalue     = [3 5 9];
        cfg.trialdef.prestim        = 1; % in seconds
        cfg.trialdef.poststim       = 2; % in seconds

        cfg = ft_definetrial(cfg);

        %% Preprocess the data
        cfg.channel         = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
        cfg.demean          = 'yes';
        cfg.baselinewindow  = [-0.2 0];
        cfg.lpfilter        = 'yes';                              % apply lowpass filter
        cfg.lpfreq          = 35;                                 % lowpass at 35 Hz.

        data_all = ft_preprocessing(cfg);

        %% Timelockanalysis
        cfg = [];
        cfg.trials = data_all.trialinfo == 3;
        avgFIC = ft_timelockanalysis(cfg, data_all);

        %% HERE you would save intermediate results to file, in a non-tutorial script

        %% Planar gradient
        cfg                 = [];
        cfg.feedback        = 'no';
        cfg.method          = 'template';
        cfg.neighbours      = ft_prepare_neighbours(cfg, avgFIC);
        cfg.planarmethod    = 'sincos';
        avgFICplanar        = ft_megplanar(cfg, avgFIC);

        cfg = [];
        avgFICplanarComb = ft_combineplanar(cfg, avgFICplanar);

        %% Save subject results
        allsubj_FIC_pc{i_set} = avgFICplanarComb;

        %% HERE you would definitely save the results to file, in a non-tutorial script, since this is the end of the per-subject analysis
    end

    %% Calculate grand average
    cfg = [];
    cfg.channel   = 'all';
    cfg.latency   = 'all';
    cfg.parameter = 'avg';
    grandavgFIC  = ft_timelockgrandaverage(cfg, allsubj_FIC_pc{:});

    %% HERE you would save the grandaverage results to file, in a non-tutorial script

    cfg = [];
    cfg.showlabels  = 'yes';
    cfg.layout      = 'CTF151_helmet.mat';
    figure; % Create a fresh figure for the next plot
    ft_multiplotER(cfg, grandavgFIC)

## Error handling and saving results to file in (parallel) loops

Below an example that adds several improvements over the previous code, to show additional considerations when creating an analysis script. Note that most of these improvements are also beneficial in regular analysis scripts, not just when doing parallel loops.

-   Use separate files/scripts for the per-subject analysis part and for the analysis part that works on combined results
-   Use a single variable with the base path, and construct all other file and directory paths relative to that variable
-   Use the try-catch construct within the loop
-   Make sure the output directory exists by always doing mkdir (which will do-nothing when already available)
-   Save intermediate and final results to file
-   Check results after the end of the per-subject loop, because when a lot of subjects are analysed, any error messages displayed during the loop might be missed
-   Check the per-subject input before doing the combined analysis
-   Use fullfile() when working with filenames and directory paths

When done correctly, all problematic subjects will be known after just one run of the script. It is then still needed to go over the subjects in the problem list to see what is wrong, and whether it can be fixed, or the subject should be excluded.

### Exercise

{% include markup/info %}
-   Add SubjectSEF in the middle of the list of datasets, observe what happens.
-   What results are available in the output directory? What are the differences with the previous implementations?
{% include markup/end %}

    %% Set base path information
    is_pool_remote = false; % Set this to true when using a remote cluster for the parallel computations
    if is_pool_remote
        % The base path on the remote machine, to be used within the parallel loop
        base_path = 'PUT CORRECT BASE PATH ON REMOTE MACHINE HERE'; %#ok<UNRCH>
    else
        % The base path on the local machine
        base_path = pwd();
    end

    %% Loop over subjects
    subjects = {'Subject01', 'Subject02', 'Subject03', 'Subject04'};
    nr_subjects = length(subjects);
    allsubj_FIC_result_available = false(1, nr_subjects); % Initialize the output variable

    parfor i_set = 1:nr_subjects

        %% Select current subject
        % Get the info of the subject for this loop iteration
        % In this case, only the dataset name
        subjectinfo = subjects{i_set};

        try
            % Create the directory where the results will be saved
            save_file_directory = fullfile(base_path, 'results', subjectinfo);
            mkdir(save_file_directory);

            %% Trial definition
            cfg                     = [];
            cfg.dataset             = strcat(subjectinfo, '.ds');
            cfg.trialfun            = 'ft_trialfun_general';          % this is the default
            cfg.trialdef.eventtype  = 'backpanel trigger';
            cfg.trialdef.eventvalue = [3 5 9];                        % condition are: 3 = fully incongruent (FIC), 5 = initially congruent (IC), 9 = fully congruent (FC)
            cfg.trialdef.prestim    = 1; % in seconds
            cfg.trialdef.poststim   = 2; % in seconds

            cfg = ft_definetrial(cfg);

            %% Preprocess the data
            cfg.channel         = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
            cfg.demean          = 'yes';
            cfg.baselinewindow  = [-0.2 0];
            cfg.lpfilter        = 'yes';                              % apply lowpass filter
            cfg.lpfreq          = 35;                                 % lowpass at 35 Hz.

            data_all = ft_preprocessing(cfg);

            %% Timelockanalysis
            cfg = [];
            cfg.trials = data_all.trialinfo == 3;
            avgFIC = ft_timelockanalysis(cfg, data_all);

            % Save the intermediate result to file
            % Within a parfor loop, the save() function cannot be used.
            % However, it is possible to use a matfile object.
            save_file_name = fullfile(save_file_directory, 'avgFIC.mat');
            matObj = matfile(save_file_name, 'Writable', true);
            matObj.avgFIC = avgFIC;

            %% Planar gradient
            cfg = [];
            cfg.feedback        = 'no';
            cfg.method          = 'template';
            cfg.neighbours      = ft_prepare_neighbours(cfg, avgFIC);
            cfg.planarmethod    = 'sincos';
            avgFICplanar = ft_megplanar(cfg, avgFIC);

            cfg = [];
            avgFICplanarComb = ft_combineplanar(cfg, avgFICplanar);

            % Save the final per-subject result to file
            save_file_name = fullfile(save_file_directory, 'avgFICplanarComb.mat');
            matObj = matfile(save_file_name, 'Writable', true);
            matObj.avgFICplanarComb = avgFICplanarComb;

            % Mark this subject as processed
            allsubj_FIC_result_available(i_set) = true;
        catch ME
            disp(ME)
            disp("Error while analysing subject " + string(i_set) + " in the list of subjects.")
        end
    end

    %% Check the results
    if any(~allsubj_FIC_result_available)
        problem_ids = strjoin(string(find(~allsubj_FIC_result_available)));
        error(strcat("The following subjects had an error during analysis: ", problem_ids))
    end

Using the combined results goes in a different script, because that way it isn't needed to rerun the whole loop each time an analysis on combined results is done.

### Exercise

{% include markup/info %}
-   Add SubjectSEF in the middle of the list of datasets, observe what happens.
{% include markup/end %}

    %% Load and check the per-subject results
    % If the parallel loop of the first script ran on a remote cluster, results
    % files may have to be transfered from the remote location to (subdirectories
    % of) the current directory first.
    base_path = pwd();

    subjects = {'Subject01', 'Subject02', 'Subject03', 'Subject04'};
    nr_subjects = length(subjects);
    allsubj_FIC_pc = cell(1,nr_subjects);

    for i_set = 1:nr_subjects
        % Select current subject
        % Get the info of the subject for this loop iteration
        % In this case, only the dataset name
        subjectinfo = subjects{i_set};

        % Load result for this subject
        save_file_name = fullfile(base_path, 'results', subjectinfo, 'avgFICplanarComb.mat');
        result_name = 'avgFICplanarComb';
        mat_struct = load(save_file_name, result_name);

        % Check result
        if isempty(mat_struct) || isempty(mat_struct.(result_name))
            % Do have a hard error here, because only valid results are to be used.
            % If one of the subjects has a problem, either go back to the per-subject
            % script to fix the problem, or remove that subject from the list here.
            error(strcat("The following subject had an error during analysis: ", subjectinfo))
        end

        % Add to collection
        allsubj_FIC_pc{i_set} = mat_struct.(result_name);
    end

    %% Calculate grand average
    cfg = [];
    cfg.channel   = 'all';
    cfg.latency   = 'all';
    cfg.parameter = 'avg';
    grandavgFIC = ft_timelockgrandaverage(cfg, allsubj_FIC_pc{:});

    cfg = [];
    cfg.showlabels  = 'yes';
    cfg.layout      = 'CTF151_helmet.mat';
    figure; % Create a fresh figure for the next plot
    ft_multiplotER(cfg, grandavgFIC)

    %% HERE add follow up combined-results analyses
