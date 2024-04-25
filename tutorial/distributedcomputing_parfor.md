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
-   set up the code to deal with problematic subjects, such that successfully completed analyses do not have to be repeated if one fails

This tutorial is focused on parallel computing, hence the code samples are set up to bring this aspect to the front. To keep it simple, as a consequence most of the code samples do NOT follow the recommendations in [Creating a clean analysis pipeline](/tutorial/scripting) regarding separating subject details from the analysis code, writing wrapper analysis functions, or handling of the input and output data through files. The final example also does not completely follow the guidelines, but does show what functions to use when interacting with files and paths to files in a parallel computing setting.

## Background on parallel computing

Parallel computing is different from sequential computing, especially when the actual computing is done on another computer than where the script is started. Some minimal information that you should be aware of:

-   **Variables indexing**: Parfor does have certain requirements on how variables are accessed that are used both inside and outside the loop. The Matlab editor will give hints, noticable by red and orange squiggly lines, on code that is incompatible with the parfor requirements.
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

A very quick thing to try out next is the following. When using the normal `for` function, it will execute the pause sequentially. When using the `parfor` function the pause is executed in parallel.

    tic; for i=1:4; pause(1); end; toc
      Elapsed time is 4.001463 seconds.

    tic; parfor i=1:4; pause(1); end; toc
      Elapsed time is 1.084468 seconds.

This tutorial requires the original MEG datasets for the four subjects, plus one additional dataset that is on purpose inconsistent with the others. These are available from:

-   [Subject01.zip](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip)
-   [Subject02.zip](https://download.fieldtriptoolbox.org/tutorial/Subject02.zip)
-   [Subject03.zip](https://download.fieldtriptoolbox.org/tutorial/Subject03.zip)
-   [Subject04.zip](https://download.fieldtriptoolbox.org/tutorial/Subject04.zip)
-   [SubjectSEF.zip](https://download.fieldtriptoolbox.org/tutorial/SubjectSEF.zip) to show how to deal with errors

Additional prerequisites:

-   Make sure FieldTrip is on your path, see this [FAQ](/faq/installation)
-   Have the necessary data next to each other in a single directory: the directories 'Subject01.ds', 'Subject02.ds', 'Subject03.ds', 'Subject04.ds', 'SubjectSEF.ds' should all be next to each other.
-   Put your test scripts also in this directory

## Starting simple with a single-subject

Here we give the code that will be the basis for the rest of the tutorial. It is an adaptation of the code in the [event-related averaging tutorial](/tutorial/eventrelatedaveraging). The adaptations were made to reduce the runtime, the number of generated files and plots, and to be able to focus on the specific goals of this tutorial.

For reference, the changes in detail w.r.t. the [event-related averaging tutorial](/tutorial/eventrelatedaveraging) are:

-   Removed the line that selects trials without artifacts. It is subject-specific, so needs to be handled on a per-subject basis. See the tutorial on [creating a clean analysis pipeline](/tutorial/scripting) how you can handle subject-specific details. For this tutorial we will ignore the artifacts.
-   Only use FIC condition, removed the IC and FC related lines. This to reduce the amount of code and calculation time.
-   No separate ft_selectdata call and saving of the intermediate data. Replaced with trial selection with the ft_timelockanalysis call.
-   Removed the plotting of data and results, including setting `cfg.feedback = 'no'` for ft_prepare_neighbours. This is useful when developing the pipeline, but less so when applying it to many subjects.
-   Added a call to ft_timelockgrandaverage to get group results.

### Exercise

{% include markup/skyblue %}
-   Add a loop, such that both Subject01 and Subject02 are analyzed and that results from both analyses are available at the end
-   Use the combined results in a call to ft_timelockgrandaverage
{% include markup/end %}

    % Trial definition
    cfg = [];
    cfg.dataset             = 'Subject01.ds';
    cfg.trialfun            = 'ft_trialfun_general';          % this is the default
    cfg.trialdef.eventtype  = 'backpanel trigger';
    cfg.trialdef.eventvalue = [3 5 9];                        % condition are: 3 = fully incongruent (FIC), 5 = initially congruent (IC), 9 = fully congruent (FC)
    cfg.trialdef.prestim    = 1; % in seconds
    cfg.trialdef.poststim   = 2; % in seconds

    cfg = ft_definetrial(cfg);

    % Preprocess the data
    cfg.channel         = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
    cfg.demean          = 'yes';
    cfg.baselinewindow  = [-0.2 0];
    cfg.lpfilter        = 'yes';                              % apply lowpass filter
    cfg.lpfreq          = 35;                                 % lowpass at 35 Hz.

    data_all = ft_preprocessing(cfg);

    % Timelockanalysis
    cfg = [];
    cfg.trials = data_all.trialinfo == 3;
    avgFIC = ft_timelockanalysis(cfg, data_all);

    % HERE you would save intermediate results to file

    % Planar gradient
    cfg = [];
    cfg.feedback        = 'no';
    cfg.method          = 'template';
    cfg.neighbours      = ft_prepare_neighbours(cfg, avgFIC);
    cfg.planarmethod    = 'sincos';
    avgFICplanar        = ft_megplanar(cfg, avgFIC);

    cfg = [];
    avgFICplanarComb = ft_combineplanar(cfg, avgFICplanar);

    % HERE you would definitely save the results to file

    % Calculate the grand average over multiple subjects, this requires that we first do the analysis on multiple subjects
    %
    % cfg = [];
    % cfg.channel   = 'all';
    % cfg.latency   = 'all';
    % cfg.parameter = 'avg';
    % grandavgFIC = ft_timelockgrandaverage(cfg, avgFICplanarComb_subj1, avgFICplanarComb_subj2, ...);

## Multi-subject, sequential loop

To do the same analysis on multiple subjects, in short:

-   put a loop around the analysis
-   within the loop, select the correct dataset
-   keep the final result data for each subject

Compared to the single-subject code above, the below code shows that for multi-subject analysis, the per-subject part has only minimal changes. To show where the change from single-subject to multi-subject happens, and how such code differs in its inputs, an actual ft_timelockgrandaverage call has been implemented. Grand average is on a combination of subjects, so that is an analysis that comes only after the per-subject analyses.

Note that, as mentioned earlier, the data organization for this tutorial deviates from the recommendations in [Creating a clean analysis pipeline](/tutorial/scripting).

### Exercise

{% include markup/skyblue %}
-   Add SubjectSEF in the middle of the list of allsubj_dataset, observe what happens.
-   What results are available?
-   Adapt the code so the loop runs in parallel.
{% include markup/end %}

    nsubj = 4;
    allsubj_dataset = {'Subject01.ds', 'Subject02.ds', 'Subject03.ds', 'Subject04.ds'};
    allsubj_result  = cell(1, nsubj); % Initialize the output variable

    % Loop over subjects
    for subjectnr = 1:nsubj

        % Get the info of the subject for this loop iteration
        % Here the only subject-specific information is the name of the dataset
        subjectinfo = allsubj_dataset{subjectnr};

        % Trial definition
        cfg = [];
        cfg.dataset             = subjectinfo;
        cfg.trialfun            = 'ft_trialfun_general';          % this is the default
        cfg.trialdef.eventtype  = 'backpanel trigger';
        cfg.trialdef.eventvalue = [3 5 9];                        % condition are: 3 = fully incongruent (FIC), 5 = initially congruent (IC), 9 = fully congruent (FC)
        cfg.trialdef.prestim    = 1; % in seconds
        cfg.trialdef.poststim   = 2; % in seconds

        cfg = ft_definetrial(cfg);

        % Preprocess the data
        cfg.channel         = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
        cfg.demean          = 'yes';
        cfg.baselinewindow  = [-0.2 0];
        cfg.lpfilter        = 'yes';                              % apply lowpass filter
        cfg.lpfreq          = 35;                                 % lowpass at 35 Hz.

        data_all = ft_preprocessing(cfg);

        % Timelockanalysis
        cfg = [];
        cfg.trials = (data_all.trialinfo==3);
        avgFIC = ft_timelockanalysis(cfg, data_all);

        % HERE you could save intermediate results to file

        % Planar gradient
        cfg = [];
        cfg.feedback     = 'no';
        cfg.method       = 'template';
        cfg.neighbours   = ft_prepare_neighbours(cfg, avgFIC);
        cfg.planarmethod = 'sincos';
        avgFICplanar = ft_megplanar(cfg, avgFIC);

        cfg = [];
        avgFICplanarComb = ft_combineplanar(cfg, avgFICplanar);

        % Save the results from this subject
        allsubj_result{subjectnr} = avgFICplanarComb;

        % HERE you would definitely save the results to file
    end

    % Calculate the grand average over multiple subjects
    cfg = [];
    cfg.channel   = 'all';
    cfg.latency   = 'all';
    cfg.parameter = 'avg';
    grandavgFIC = ft_timelockgrandaverage(cfg, allsubj_result{:});

    % HERE you would save the grand average to file

    cfg = [];
    cfg.showlabels  = 'yes';
    cfg.layout      = 'CTF151_helmet.mat';
    cfg.figure      = figure; % Create a fresh figure
    ft_multiplotER(cfg, grandavgFIC)


{% include markup/skyblue %}
Saving data and figures to disk can be done using the MATLAB [save](https://www.mathworks.com/help/matlab/ref/save.html) and [savefig](https://www.mathworks.com/help/matlab/ref/savefig.html) or [saveas](https://www.mathworks.com/help/matlab/ref/saveas.html) commands. Since you want to distinguish the data from different subjects, you can use  [sprintf](https://www.mathworks.com/help/matlab/ref/sprintf.html) to construct a unique filenames.

For example:

    filename = sprintf('avgFIC_Subject%02d.mat', subjectnr);
    save(filename, 'avgFIC')

or to write the data in different directories for every subject:

    subjid = sprintf('Subject%02d', subjectnr);
    filename = fullfile('results', subjid, 'avgFIC.mat');
    save(filename, 'avgFIC')

Most FieldTrip functions also support the `cfg.inputfile` and `cfg.outputfile` options, which means that you can do something like

    subjid = sprintf('Subject%02d', subjectnr);
    filename = fullfile('results', subjid, 'avgFIC.mat');

    cfg = [];
    cfg.trials      = (data_all.trialinfo==3);
    cfg.outputfile  = filename;
    avgFIC = ft_timelockanalysis(cfg, data_all);

and

    subjid = sprintf('Subject%02d', subjectnr);
    filename = fullfile('results', subjid, 'avgFIC.fig');

    cfg = [];
    cfg.layout = 'CTF151_helmet';
    cfg.outputfile = filename;
    ft_multiplotER(cfg, avgFIC);
{% include markup/end %}


## Multi-subject, parfor loop

To do the same analysis as above, but in parallel over the subjects, all we have to do is change the `for` to a `parfor`. This holds if the sequential loop was already set up as above. However, often a sequential loop is not directly ready for parallel computing, or can be improved to be more robust.

### Exercise

{% include markup/skyblue %}
-   Add SubjectSEF.ds in the middle of the list of `allsubj_dataset`. What happens when running the script? What results are available inside the `allsubj_result` variable?
- Remove the line near the top that states `allsubj_result = cell(1, nsubj)` and change the last non-comment line within the loop to read `allsubj_result{end+1} = avgFICplanarComb`. What happens when running the script?
-   After the comment line `% HERE you could save intermediate results to file`, add the code to save the intermediate result to disk, e.g., `save('avgFIC.mat', 'avgFIC')`. What happens when running the script?
{% include markup/end %}

    nsubj = 4;
    allsubj_dataset = {'Subject01.ds', 'Subject02.ds', 'Subject03.ds', 'Subject04.ds'};
    allsubj_result  = cell(1, nsubj); % Initialize the output variable

    % Loop over subjects
    parfor subjectnr = 1:nsubj

        % Select current subject
        % Get the info of the subject for this loop iteration
        % In this case, only the dataset name
        subjectinfo = allsubj_dataset{subjectnr};

        % Trial definition
        cfg                         = [];
        cfg.dataset                 = subjectinfo;
        cfg.trialfun                = 'ft_trialfun_general';          % this is the default
        cfg.trialdef.eventtype      = 'backpanel trigger';
        cfg.trialdef.eventvalue     = [3 5 9];
        cfg.trialdef.prestim        = 1; % in seconds
        cfg.trialdef.poststim       = 2; % in seconds

        cfg = ft_definetrial(cfg);

        % Preprocess the data
        cfg.channel         = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
        cfg.demean          = 'yes';
        cfg.baselinewindow  = [-0.2 0];
        cfg.lpfilter        = 'yes';                              % apply lowpass filter
        cfg.lpfreq          = 35;                                 % lowpass at 35 Hz.

        data_all = ft_preprocessing(cfg);

        % Timelockanalysis
        cfg = [];
        cfg.trials = data_all.trialinfo == 3;
        avgFIC = ft_timelockanalysis(cfg, data_all);

        % HERE you would save intermediate results to file

        % Planar gradient
        cfg                 = [];
        cfg.feedback        = 'no';
        cfg.method          = 'template';
        cfg.neighbours      = ft_prepare_neighbours(cfg, avgFIC);
        cfg.planarmethod    = 'sincos';
        avgFICplanar        = ft_megplanar(cfg, avgFIC);

        cfg = [];
        avgFICplanarComb = ft_combineplanar(cfg, avgFICplanar);

        % Save subject results
        allsubj_result{subjectnr} = avgFICplanarComb;

        % HERE you would definitely save the results to file
    end

    % Calculate the grand average over multiple subjects
    cfg = [];
    cfg.channel   = 'all';
    cfg.latency   = 'all';
    cfg.parameter = 'avg';
    grandavgFIC  = ft_timelockgrandaverage(cfg, allsubj_result{:});

    % HERE you would save the grand average to file

    cfg = [];
    cfg.showlabels  = 'yes';
    cfg.layout      = 'CTF151_helmet.mat';
    cfg.figure      = figure; % Create a fresh figure
    ft_multiplotER(cfg, grandavgFIC)

## Error handling and saving results to file in (parallel) loops

Below an example analysis script that addresses several improvements and considerations. Most of these improvements are also beneficial in regular analysis scripts, not just when doing parallel loops.

-   Use separate files/scripts for the per-subject analysis part and for the analysis part that works on combined results
-   Use a single variable with the base path and construct all other file and directory paths relative to that variable
-   Use the try-catch construct within the loop
-   Make sure the output directory always exists by doing mkdir, this will do nothing when already available
-   Save intermediate and final results to file
-   Check results after the per-subject loop: when a lot of subjects are analysed, any error messages displayed during the loop might be missed
-   Check the per-subject input before doing the combined analysis
-   Use fullfile() when working with filenames and directory paths

When done correctly, all problematic subjects will be known after just one run of the script. It is then still needed to go over the subjects in the problem list to see what is wrong, and whether the script can be improved, whether exceptions for the subject can be handled, or whether the subject should be excluded from further analysis.

### Exercise

{% include markup/skyblue %}
-   Add SubjectSEF in the middle of the list of allsubj_dataset, observe what happens.
-   What results are available in the output directory? What are the differences with the previous implementations?
{% include markup/end %}

    % Set the base path, the example here assumes that the data is on a shared network drive
    base_path = pwd();

    nsubj = 5;
    allsubj_id = {'Subject01', 'Subject02', 'Subject03', 'Subject04', 'SubjectSEF'};
    allsubj_succes = false(1, nsubj); % Initialize the output variable

    % Loop over subjects
    parfor subjectnr = 1:nsubj

        % Select current subject
        % Get the info of the subject for this loop iteration
        % In this case, only the dataset name
        subjectid = allsubj_id{subjectnr};

        try
            % Create the directory where the results will be saved
            rawdata_directory = base_path;
            result_directory = fullfile(base_path, 'results', subjectid);
            mkdir(result_directory);

            % Trial definition
            cfg                     = [];
            cfg.dataset             = fullfile(rawdata_directory, [subjectid '.ds']);
            cfg.trialfun            = 'ft_trialfun_general';          % this is the default
            cfg.trialdef.eventtype  = 'backpanel trigger';
            cfg.trialdef.eventvalue = [3 5 9];                        % condition are: 3 = fully incongruent (FIC), 5 = initially congruent (IC), 9 = fully congruent (FC)
            cfg.trialdef.prestim    = 1; % in seconds
            cfg.trialdef.poststim   = 2; % in seconds

            cfg = ft_definetrial(cfg);

            % Preprocess the data
            cfg.channel         = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
            cfg.demean          = 'yes';
            cfg.baselinewindow  = [-0.2 0];
            cfg.lpfilter        = 'yes';                              % apply lowpass filter
            cfg.lpfreq          = 35;                                 % lowpass at 35 Hz.

            cfg.outputfile      = fullfile(result_directory, 'data_all.mat');
            data_all = ft_preprocessing(cfg);

            % Timelockanalysis
            cfg = [];
            cfg.trials      = data_all.trialinfo == 3;
            cfg.outputfile  = fullfile(result_directory, 'avgFIC.mat');
            avgFIC = ft_timelockanalysis(cfg, data_all);

            % Planar gradient
            cfg = [];
            cfg.feedback        = 'no';
            cfg.method          = 'template';
            cfg.neighbours      = ft_prepare_neighbours(cfg, avgFIC);
            cfg.planarmethod    = 'sincos';
            cfg.outputfile      = fullfile(result_directory, 'avgFICplanar.mat');
            avgFICplanar = ft_megplanar(cfg, avgFIC);

            cfg = [];
            cfg.outputfile = fullfile(result_directory, 'avgFICplanarComb.mat');
            avgFICplanarComb = ft_combineplanar(cfg, avgFICplanar);

            % Mark this subject as successfully processed
            allsubj_succes(subjectnr) = true;
        catch ME
            disp(ME)
            disp("Error while analysing subject " + string(subjectnr) + " in the list of subjects.")
        end
    end

    % Check the results
    if ~all(allsubj_succes)
        problem_ids = strjoin(string(find(~allsubj_succes)));
        error(strcat("The following subjects had an error during analysis: ", problem_ids))
    end

Using the combined results goes in a different script, because that way it isn't needed to rerun the whole loop each time an analysis on combined results is done.

{% include markup/skyblue %}
The MATLAB [save](https://nl.mathworks.com/help/matlab/ref/save.html?) function [cannot be used](https://nl.mathworks.com/matlabcentral/answers/135285-how-do-i-use-save-with-a-parfor-loop-using-parallel-computing-toolbox) within a parfor loop. However, it is possible to use a [matfile](https://nl.mathworks.com/help/matlab/ref/matlab.io.matfile.html) object. For example, following ft_timelockanalysis in the parfor loop you can do:

    result_filename = fullfile(result_directory, 'avgFIC.mat');
    matObj = matfile(result_filename, 'Writable', true);
    matObj.avgFIC = avgFIC;

In the tutorial code above we avoided the problem by using the `cfg.outputfile` option.
{% include markup/end %}

### Exercise

{% include markup/skyblue %}
-   Add SubjectSEF in the middle of the list of allsubj_dataset, observe what happens.
{% include markup/end %}

    % Load and check the per-subject results
    base_path = pwd();

    nsubj = 4;
    allsubj_id = {'Subject01', 'Subject02', 'Subject03', 'Subject04'};
    allsubj_result = cell(1, nsubj);

    parfor subjectnr = 1:nsubj
      % Select current subject
      % Get the info of the subject for this loop iteration
      % In this case, only the dataset name
      subjectid = allsubj_id{subjectnr};

      % When using cfgt.outputfile, the single variable contained in the file is called "data"
      % Use an anonymous function to load and rename this variable on the fly
      loadvar = @(file, var) load(file).(whos('-file', file).name);

      try
        % Load the result for this subject
        result_filename = fullfile(base_path, 'results', subjectid, 'avgFICplanarComb.mat');
        avgFICplanarComb = loadvar(result_filename, 'avgFICplanarComb');
      catch
        % Give a hard error here, because only valid results are to be used.
        % If one of the subjects has a problem, either go back to the per-subject
        % script to fix the problem, or remove that subject from the list here.
        error(strcat("The following subject had an error during analysis: ", subjectid))
      end

      % Add to the collection of results
      allsubj_result{subjectnr} = avgFICplanarComb;
    end

    % Check the history of the analysis, look at the original filename
    for subjectnr = 1:nsubj
      disp(allsubj_result{subjectnr}.cfg.previous.previous.previous.dataset)
    end

    % Calculate the grand average over multiple subjects
    cfg = [];
    cfg.channel   = 'all';
    cfg.latency   = 'all';
    cfg.parameter = 'avg';
    grandavgFIC = ft_timelockgrandaverage(cfg, allsubj_result{:});

    cfg = [];
    cfg.showlabels  = 'yes';
    cfg.layout      = 'CTF151_helmet.mat';
    cfg.figure      = figure; % Create a fresh figure
    ft_multiplotER(cfg, grandavgFIC)

    % HERE you could follow up with statistical analysis
