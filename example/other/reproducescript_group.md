---
title: Using reproducescript for a group analysis
parent: Various other examples
grand_parent: Examples
category: example
tags: [reproducescript]
redirect_from:
    - /example/reproducescript_group/
---

# Using reproducescript for a group analysis

This example script will introduce you to functionality in the FieldTrip toolbox designed to aid in making your analysis pipeline - including code, data and results - more easily reproducible and shareable. It is based on the manuscript [Reducing the efforts to create reproducible analysis code with FieldTrip](http://dx.doi.org/10.21105/joss.05566). We assume that you have already had a look at the example on [Making your analysis pipeline reproducible using reproducescript](/example/reproducescript).

## Example 2

The first example contained only a few analysis steps in a single subject. More realistic data analysis pipelines consist of many more steps in which often the same (or similar) pipelines are used for multiple subjects. In this section, we will show how the reproducescript functionality applies in such a case.

### Original analysis

The analysis example follows the strategy outlined in the [Literate Programming](https://www-cs-faculty.stanford.edu/~knuth/lp.html) book by Donald Knuth and starts with a single subject analysis pipeline that is repeated for four subjects. The directory is structured as depicted below.

{% include image src="/assets/img/example/reproducescript/filedir_example2_analysis.jpg" width="237" %}

After the single-subject analysis, all single-subject results are used in a group analysis. The single-subject and group analyses are executed from the master script `analyze.m`:

#### analyze.m

    clear
    close all

    subjlist = {
      'Subject01'
      'Subject02'
      'Subject03'
      'Subject04'
      };

    %% Loop single-subject analyses over subjects
    for i=1:numel(subjlist)
      subj = subjlist{i};
      doSingleSubjectAnalysis(subj);
    end

    %% Group analysis
    doGroupAnalysis(subjlist);

This is the control script from which the relevant analysis scripts and functions are called. The master script relies on two functions: `doSingleSubjectAnalysis` and `doGroupAnalysis`, which are each stored in separate m-files. The original source code for these scripts can be found below.

#### doSingleSubjectAnalysis.m

    function doSingleSubjectAnalysis(subj)

    % the details of each subject are in separate files
    % details_Subject01.m
    % details_Subject02.m
    % details_Subject03.m
    % details_Subject04.m

    fprintf('evaluating single subject analysis for %s\n', subj);
    eval(['details_' subj]);

    % this is for artifact detection
    interactive = false;

    %%

    cfg = [];
    cfg.dataset = fullfile(datadir, filename);
    cfg.trialfun = 'ft_trialfun_general';
    cfg.trialdef.eventtype = 'backpanel trigger';
    cfg.trialdef.eventvalue = [triggerFIC triggerIC triggerFC];
    cfg.trialdef.prestim = 1;
    cfg.trialdef.poststim = 2;
    cfg = ft_definetrial(cfg);

    % the EOG channel has a different name in the different datasets
    cfg.channel = {'MEG' eogchannel};
    cfg.continuous = 'yes'; % see https://www.fieldtriptoolbox.org/faq/continuous/
    data = ft_preprocessing(cfg);

    %%

    if interactive
      % visually identify the artifacts
      cfg = [];
      cfg.channel = eogchannel;
      cfg.method = 'channel';
      dummy1 = ft_rejectvisual(cfg, data);

      cfg = [];
      cfg.channel = 'MEG';
      cfg.method = 'summary';
      dummy2 = ft_rejectvisual(cfg, data);

      % combine the artifacts that have been detected
      artifact = [
        dummy1.cfg.artfctdef.channel.artifact
        dummy2.cfg.artfctdef.summary.artifact
        ];

      % print them and copy them to the subject details file
      disp(artifact);

      % use the MATLAB debugger to wait on this line
      disp('please copy these artifacts to the subject details file');
      keyboard
    end

    % remove the artifacts that were previously detected
    cfg = [];
    cfg.artfctdef.visual.artifact = artifact;
    data_clean = ft_rejectartifact(cfg, data);

    %%

    cfg = [];
    cfg.trials = data_clean.trialinfo==triggerFIC;
    avgFIC = ft_timelockanalysis(cfg, data_clean);

    cfg.trials = data_clean.trialinfo==triggerFC;
    avgFC = ft_timelockanalysis(cfg, data_clean);

    cfg.trials = data_clean.trialinfo==triggerIC;
    avgIC = ft_timelockanalysis(cfg, data_clean);

    %%

    cfg = [];
    cfg.showlabels = 'no';
    cfg.fontsize = 6;
    cfg.layout = 'CTF151_helmet.mat';
    cfg.baseline = [-0.2 0];
    cfg.xlim = [-0.2 1.0];
    cfg.ylim = [-3e-13 3e-13];
    ft_multiplotER(cfg, avgFC, avgIC, avgFIC);

    %%

    cfg = [];
    cfg.feedback = 'yes';
    cfg.method = 'template';
    cfg.neighbours = ft_prepare_neighbours(cfg, avgFIC);
    cfg.planarmethod = 'sincos';
    avgFICplanar = ft_megplanar(cfg, avgFIC);
    avgFCplanar = ft_megplanar(cfg, avgFC);
    avgICplanar = ft_megplanar(cfg, avgIC);

    %%

    cfg = [];
    avgFICplanarComb = ft_combineplanar(cfg, avgFICplanar);
    avgFCplanarComb  = ft_combineplanar(cfg, avgFCplanar);
    avgICplanarComb  = ft_combineplanar(cfg, avgICplanar);

    %%

    cfg = [];
    cfg.xlim = [0.3 0.5];
    cfg.zlim = 'maxmin';
    cfg.colorbar = 'yes';
    cfg.layout = 'CTF151_helmet.mat';
    subplot(2,3,1); ft_topoplotER(cfg, avgFIC)
    subplot(2,3,2); ft_topoplotER(cfg, avgFC)
    subplot(2,3,3); ft_topoplotER(cfg, avgIC)

    cfg.zlim = 'maxabs';
    cfg.layout = 'CTF151_helmet.mat';
    subplot(2,3,4); ft_topoplotER(cfg, avgFICplanarComb)
    subplot(2,3,5); ft_topoplotER(cfg, avgFCplanarComb)
    subplot(2,3,6); ft_topoplotER(cfg, avgICplanarComb)

    %%

    % save the results to disk
    outputdir = ['result_' subj];
    mkdir(outputdir)
    save(fullfile(outputdir, 'avgFIC'), 'avgFIC');
    save(fullfile(outputdir, 'avgFC'),  'avgFC');
    save(fullfile(outputdir, 'avgIC'),  'avgIC');
    save(fullfile(outputdir, 'avgFICplanarComb'), 'avgFICplanarComb');
    save(fullfile(outputdir, 'avgFCplanarComb'),  'avgFCplanarComb');
    save(fullfile(outputdir, 'avgICplanarComb'),  'avgICplanarComb');

#### doGroupAnalysis.m

    function doGroupAnalysis(allsubj)

    avgFIC = cell(size(allsubj));
    avgFC  = cell(size(allsubj));
    avgIC  = cell(size(allsubj));

    % load the results from disk
    for i=1:numel(allsubj)
      subj = allsubj{i};
      fprintf('loading data for subject %s\n', subj);

      inputdir = ['result_' subj];
      tmp = load(fullfile(inputdir, 'avgFIC')); avgFIC{i} = tmp.avgFIC;
      tmp = load(fullfile(inputdir, 'avgFC'));  avgFC{i}  = tmp.avgFC;
      tmp = load(fullfile(inputdir, 'avgIC'));  avgIC{i}  = tmp.avgIC;
      clear tmp
    end

    %%

    cfg = [];
    cfg.showlabels = 'no';
    cfg.fontsize = 6;
    cfg.layout = 'CTF151_helmet.mat';
    cfg.baseline = [-0.2 0];
    cfg.xlim = [-0.2 1.0];
    cfg.ylim = [-3e-13 3e-13];
    figure
    ft_multiplotER(cfg, avgFIC{:});
    title('Fully incongruent condition');

    figure
    ft_multiplotER(cfg, avgFC{:});
    title('Fully congruent condition');

    figure
    ft_multiplotER(cfg, avgIC{:});
    title('Initially congruent condition');

    %%

    avgFICvsFC = cell(size(allsubj));
    for i=1:numel(allsubj)
      cfg = [];
      cfg.parameter = 'avg';
      cfg.operation = 'x1-x2';
      avgFICvsFC{i} = ft_math(cfg, avgFIC{i}, avgFC{i});
    end

    cfg = [];
    cfg.showlabels = 'no';
    cfg.fontsize = 6;
    cfg.layout = 'CTF151_helmet.mat';
    cfg.baseline = [-0.2 0];
    cfg.xlim = [-0.2 1.0];
    cfg.ylim = [-3e-13 3e-13];
    ft_multiplotER(cfg, avgFICvsFC{:});
    title('FIC minus FC');

    %%

    % let's make a manual change to the data that is not caputured in the provenance
    for i=1:numel(allsubj)
      avgFIC{i}.avg = avgFIC{i}.avg * 1e15; % convert from T to fT
      avgFC{i}.avg  = avgFC{i}.avg  * 1e15; % convert from T to fT
      avgIC{i}.avg  = avgIC{i}.avg  * 1e15; % convert from T to fT
    end

    %%

    cfg = [];
    grandavgFIC = ft_timelockgrandaverage(cfg, avgFIC{:});
    grandavgFC  = ft_timelockgrandaverage(cfg, avgFC{:});
    grandavgIC  = ft_timelockgrandaverage(cfg, avgIC{:});

    %%

    % save the results to disk
    outputdir = 'result_Group';
    mkdir(outputdir)
    save(fullfile(outputdir, 'grandavgFIC'), 'grandavgFIC');
    save(fullfile(outputdir, 'grandavgFC'),  'grandavgFC');
    save(fullfile(outputdir, 'grandavgIC'),  'grandavgIC');

### Using reproducescript

To create a standard script from the analysis pipeline, the `ft_default` variable is initialized at the top of the `analyze.m` script. Note that we do not immediately initiate reproducescript, this is done in the loop just prior to `doSingleSubjectAnalysis` and just prior to `doGroupAnalysis`; this allows specifying unique directories for each subject and for the group. In fact, reproducescript can be stopped and restarted between different subjects, or even in between analysis steps, which is especially convenient in pipelines that require a lot of compute resources which you would rather split up to allow for parallel execution on a compute cluster.

#### analyze.m with reproducescript enabled

    clear
    close all

    % initialize the global variable
    global ft_default
    ft_default = [];
    ft_default.checksize = inf;

    subjlist = {
      'Subject01'
      'Subject02'
      'Subject03'
      'Subject04'
      };

    %% Loop single-subject analysis over subjects
    for i=1:numel(subjlist)
      subj = subjlist{i};
      % initiate reproducescript
      ft_default.reproducescript = ['reproduce_' subj];
      doSingleSubjectAnalysis(subj);
      ft_default.reproducescript = []; % disable
    end

    %% Group analysis
    % initiate reproducescript
    ft_default.reproducescript = 'reproduce_Group';
    doGroupAnalysis(subjlist);
    ft_default.reproducescript = []; % disable

### Reproduced analysis

{% include image src="/assets/img/example/reproducescript/filedir_example2_reproducescript.jpg" width="435" %}

We devoted a specific folder to the reproducescript content of each subject, and one for the group analysis. Thus, upon execution of the master script in `analyze.m`, folders are created for each of the subjects, and for the group analysis. These all contain the intermediate data, a standardized script, and a `hashes.mat` file for the bookkeeping. The reproducescript standardized scripts for the single-subject analysis and group analysis can be found below. Note that these are quite lengthy, but they unambiguously list all analysis steps.

#### Single subject reproduced analysis

This is the resulting code in the file `project/example2/reproduce_Subject01/script.m`

    %%

    cfg = [];
    cfg.dataset = '../rawdata/Subject01.ds';
    cfg.trialfun = 'ft_trialfun_general';
    cfg.trialdef.eventtype = 'backpanel trigger';
    cfg.trialdef.eventvalue = [3 5 9];
    cfg.trialdef.prestim = 1;
    cfg.trialdef.poststim = 2;
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg = ft_definetrial(cfg);

    %%

    cfg = [];
    cfg.dataset = '../rawdata/Subject01.ds';
    cfg.trialfun = 'ft_trialfun_general';
    cfg.trialdef.eventtype = 'backpanel trigger';
    cfg.trialdef.eventvalue = [3 5 9];
    cfg.trialdef.prestim = 1;
    cfg.trialdef.poststim = 2;
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.datafile = '../rawdata/Subject01.ds/Subject01.meg4';
    cfg.headerfile = '../rawdata/Subject01.ds/Subject01.res4';
    cfg.dataformat = 'ctf_meg4';
    cfg.headerformat = 'ctf_res4';
    cfg.representation = 'numeric';
    cfg.trl = 'reproduce_Subject01/20210112T113604_ft_preprocessing_largecfginput_trl.mat';
    cfg.outputfile = { 'reproduce_Subject01/20210112T113604_ft_preprocessing_output_data.mat' };
    cfg.channel = {'MEG', 'EOG'};
    cfg.continuous = 'yes';
    ft_preprocessing(cfg);

    %%

    cfg = [];
    cfg.artfctdef.visual.artifact = [8101 9000;
    68401 69300;
    99001 99900;
    ...
    228601 229500];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113604_ft_preprocessing_output_data.mat' };
    cfg.outputfile = { 'reproduce_Subject01/20210112T113611_ft_rejectartifact_output_data.mat' };
    ft_rejectartifact(cfg);

    %%

    cfg = [];
    cfg.trials = logical([true false ... false]);
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113611_ft_rejectartifact_output_data.mat' };
    cfg.outputfile = { 'reproduce_Subject01/20210112T113616_ft_timelockanalysis_output_timelock.mat' };
    ft_timelockanalysis(cfg);

    %%

    cfg = [];
    cfg.trials = logical([false false ... false]);
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113611_ft_rejectartifact_output_data.mat' };
    cfg.outputfile = { 'reproduce_Subject01/20210112T113621_ft_timelockanalysis_output_timelock.mat' };
    ft_timelockanalysis(cfg);

    %%

    cfg = [];
    cfg.trials = logical([false true ... true]);
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113611_ft_rejectartifact_output_data.mat' };
    cfg.outputfile = { 'reproduce_Subject01/20210112T113625_ft_timelockanalysis_output_timelock.mat' };
    ft_timelockanalysis(cfg);

    %%

    cfg = [];
    cfg.showlabels = 'no';
    cfg.fontsize = 6;
    cfg.layout = 'CTF151_helmet.mat';
    cfg.baseline = [-0.2 0];
    cfg.xlim = [-0.2 1];
    cfg.ylim = [-3e-13 3e-13];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Subject01/20210112T113621_ft_timelockanalysis_output_timelock.mat', 'reproduce_Subject01/20210112T113625_ft_timelockanalysis_output_timelock.mat', 'reproduce_Subject01/20210112T113616_ft_timelockanalysis_output_timelock.mat'
    };
    cfg.outputfile = 'reproduce_Subject01/20210112T113634_ft_multiplotER_output';
    figure;
    ft_multiplotER(cfg);

    %%

    cfg = [];
    cfg.feedback = 'yes';
    cfg.method = 'template';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113616_ft_timelockanalysis_output_timelock.mat' };
    cfg.outputfile = { 'reproduce_Subject01/20210112T113643_ft_prepare_neighbours_output_neighbours.mat' };
    ft_prepare_neighbours(cfg);

    %%

    cfg = [];
    cfg.feedback = 'yes';
    cfg.method = 'template';
    cfg.neighbours = 'reproduce_Subject01/20210112T113643_ft_megplanar_largecfginput_neighbours.mat';
    cfg.planarmethod = 'sincos';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113616_ft_timelockanalysis_output_timelock.mat' };
    cfg.outputfile = { 'reproduce_Subject01/20210112T113647_ft_megplanar_output_data.mat' };
    ft_megplanar(cfg);

    %%

    cfg = [];
    cfg.feedback = 'yes';
    cfg.method = 'template';
    cfg.neighbours = 'reproduce_Subject01/20210112T113643_ft_megplanar_largecfginput_neighbours.mat';
    cfg.planarmethod = 'sincos';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113621_ft_timelockanalysis_output_timelock.mat' };
    cfg.outputfile = { 'reproduce_Subject01/20210112T113650_ft_megplanar_output_data.mat' };
    ft_megplanar(cfg);

    %%

    cfg = [];
    cfg.feedback = 'yes';
    cfg.method = 'template';
    cfg.neighbours = 'reproduce_Subject01/20210112T113643_ft_megplanar_largecfginput_neighbours.mat';
    cfg.planarmethod = 'sincos';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113625_ft_timelockanalysis_output_timelock.mat' };
    cfg.outputfile = { 'reproduce_Subject01/20210112T113653_ft_megplanar_output_data.mat' };
    ft_megplanar(cfg);

    %%

    cfg = [];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113647_ft_megplanar_output_data.mat' };
    cfg.outputfile = { 'reproduce_Subject01/20210112T113657_ft_combineplanar_output_data.mat' };
    ft_combineplanar(cfg);

    %%

    cfg = [];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113650_ft_megplanar_output_data.mat' };
    cfg.outputfile = { 'reproduce_Subject01/20210112T113701_ft_combineplanar_output_data.mat' };
    ft_combineplanar(cfg);

    %%

    cfg = [];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113653_ft_megplanar_output_data.mat' };
    cfg.outputfile = { 'reproduce_Subject01/20210112T113704_ft_combineplanar_output_data.mat' };
    ft_combineplanar(cfg);

    %%

    cfg = [];
    cfg.xlim = [0.3 0.5];
    cfg.zlim = 'maxmin';
    cfg.colorbar = 'yes';
    cfg.layout = 'CTF151_helmet.mat';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113616_ft_timelockanalysis_output_timelock.mat' };
    cfg.outputfile = 'reproduce_Subject01/20210112T113708_ft_topoplotER_output';
    figure;
    ft_topoplotER(cfg);

    %%

    cfg = [];
    cfg.xlim = [0.3 0.5];
    cfg.zlim = 'maxmin';
    cfg.colorbar = 'yes';
    cfg.layout = 'CTF151_helmet.mat';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113621_ft_timelockanalysis_output_timelock.mat' };
    cfg.outputfile = 'reproduce_Subject01/20210112T113712_ft_topoplotER_output';
    figure;
    ft_topoplotER(cfg);

    %%

    cfg = [];
    cfg.xlim = [0.3 0.5];
    cfg.zlim = 'maxmin';
    cfg.colorbar = 'yes';
    cfg.layout = 'CTF151_helmet.mat';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113625_ft_timelockanalysis_output_timelock.mat' };
    cfg.outputfile = 'reproduce_Subject01/20210112T113716_ft_topoplotER_output';
    figure;
    ft_topoplotER(cfg);

    %%

    cfg = [];
    cfg.xlim = [0.3 0.5];
    cfg.zlim = 'maxabs';
    cfg.colorbar = 'yes';
    cfg.layout = 'CTF151_helmet.mat';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113657_ft_combineplanar_output_data.mat' };
    cfg.outputfile = 'reproduce_Subject01/20210112T113721_ft_topoplotER_output';
    figure;
    ft_topoplotER(cfg);

    %%

    cfg = [];
    cfg.xlim = [0.3 0.5];
    cfg.zlim = 'maxabs';
    cfg.colorbar = 'yes';
    cfg.layout = 'CTF151_helmet.mat';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113701_ft_combineplanar_output_data.mat' };
    cfg.outputfile = 'reproduce_Subject01/20210112T113726_ft_topoplotER_output';
    figure;
    ft_topoplotER(cfg);

    %%

    cfg = [];
    cfg.xlim = [0.3 0.5];
    cfg.zlim = 'maxabs';
    cfg.colorbar = 'yes';
    cfg.layout = 'CTF151_helmet.mat';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = { 'reproduce_Subject01/20210112T113704_ft_combineplanar_output_data.mat' };
    cfg.outputfile = 'reproduce_Subject01/20210112T113731_ft_topoplotER_output';
    figure;
    ft_topoplotER(cfg);

#### Group reproduced analysis

This is the resulting code in the file `project/example2/reproduce_Group/script.m`

    %%

    % a new input variable is entering the pipeline here: 20210112T114236_ft_multiplotER_input_varargin_1.mat
    % a new input variable is entering the pipeline here: 20210112T114236_ft_multiplotER_input_varargin_2.mat
    % a new input variable is entering the pipeline here: 20210112T114236_ft_multiplotER_input_varargin_3.mat
    % a new input variable is entering the pipeline here: 20210112T114236_ft_multiplotER_input_varargin_4.mat

    cfg = [];
    cfg.showlabels = 'no';
    cfg.fontsize = 6;
    cfg.layout = 'CTF151_helmet.mat';
    cfg.baseline = [-0.2 0];
    cfg.xlim = [-0.2 1];
    cfg.ylim = [-3e-13 3e-13];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Group/20210112T114236_ft_multiplotER_input_varargin_1.mat', 'reproduce_Group/20210112T114236_ft_multiplotER_input_varargin_2.mat', 'reproduce_Group/20210112T114236_ft_multiplotER_input_varargin_3.mat', 'reproduce_Group/20210112T114236_ft_multiplotER_input_varargin_4.mat'
    };
    cfg.outputfile = 'reproduce_Group/20210112T114246_ft_multiplotER_output';
    figure;
    ft_multiplotER(cfg);

    %%

    % a new input variable is entering the pipeline here: 20210112T114253_ft_multiplotER_input_varargin_1.mat
    % a new input variable is entering the pipeline here: 20210112T114253_ft_multiplotER_input_varargin_2.mat
    % a new input variable is entering the pipeline here: 20210112T114253_ft_multiplotER_input_varargin_3.mat
    % a new input variable is entering the pipeline here: 20210112T114253_ft_multiplotER_input_varargin_4.mat

    cfg = [];
    cfg.showlabels = 'no';
    cfg.fontsize = 6;
    cfg.layout = 'CTF151_helmet.mat';
    cfg.baseline = [-0.2 0];
    cfg.xlim = [-0.2 1];
    cfg.ylim = [-3e-13 3e-13];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Group/20210112T114253_ft_multiplotER_input_varargin_1.mat', 'reproduce_Group/20210112T114253_ft_multiplotER_input_varargin_2.mat', 'reproduce_Group/20210112T114253_ft_multiplotER_input_varargin_3.mat', 'reproduce_Group/20210112T114253_ft_multiplotER_input_varargin_4.mat'
    };
    cfg.outputfile = 'reproduce_Group/20210112T114303_ft_multiplotER_output';
    figure;
    ft_multiplotER(cfg);

    %%

    % a new input variable is entering the pipeline here: 20210112T114310_ft_multiplotER_input_varargin_1.mat
    % a new input variable is entering the pipeline here: 20210112T114310_ft_multiplotER_input_varargin_2.mat
    % a new input variable is entering the pipeline here: 20210112T114310_ft_multiplotER_input_varargin_3.mat
    % a new input variable is entering the pipeline here: 20210112T114310_ft_multiplotER_input_varargin_4.mat

    cfg = [];
    cfg.showlabels = 'no';
    cfg.fontsize = 6;
    cfg.layout = 'CTF151_helmet.mat';
    cfg.baseline = [-0.2 0];
    cfg.xlim = [-0.2 1];
    cfg.ylim = [-3e-13 3e-13];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Group/20210112T114310_ft_multiplotER_input_varargin_1.mat', 'reproduce_Group/20210112T114310_ft_multiplotER_input_varargin_2.mat', 'reproduce_Group/20210112T114310_ft_multiplotER_input_varargin_3.mat', 'reproduce_Group/20210112T114310_ft_multiplotER_input_varargin_4.mat'
    };
    cfg.outputfile = 'reproduce_Group/20210112T114321_ft_multiplotER_output';
    figure;
    ft_multiplotER(cfg);

    %%

    cfg = [];
    cfg.parameter = 'avg';
    cfg.operation = 'x1-x2';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Group/20210112T114236_ft_multiplotER_input_varargin_1.mat', 'reproduce_Group/20210112T114253_ft_multiplotER_input_varargin_1.mat'
    };
    cfg.outputfile = { 'reproduce_Group/20210112T114330_ft_math_output_data.mat' };
    ft_math(cfg);

    %%

    cfg = [];
    cfg.parameter = 'avg';
    cfg.operation = 'x1-x2';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Group/20210112T114236_ft_multiplotER_input_varargin_2.mat', 'reproduce_Group/20210112T114253_ft_multiplotER_input_varargin_2.mat'
    };
    cfg.outputfile = { 'reproduce_Group/20210112T114333_ft_math_output_data.mat' };
    ft_math(cfg);

    %%

    cfg = [];
    cfg.parameter = 'avg';
    cfg.operation = 'x1-x2';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Group/20210112T114236_ft_multiplotER_input_varargin_3.mat', 'reproduce_Group/20210112T114253_ft_multiplotER_input_varargin_3.mat'
    };
    cfg.outputfile = { 'reproduce_Group/20210112T114337_ft_math_output_data.mat' };
    ft_math(cfg);

    %%

    cfg = [];
    cfg.parameter = 'avg';
    cfg.operation = 'x1-x2';
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Group/20210112T114236_ft_multiplotER_input_varargin_4.mat', 'reproduce_Group/20210112T114253_ft_multiplotER_input_varargin_4.mat'
    };
    cfg.outputfile = { 'reproduce_Group/20210112T114340_ft_math_output_data.mat' };
    ft_math(cfg);

    %%

    cfg = [];
    cfg.showlabels = 'no';
    cfg.fontsize = 6;
    cfg.layout = 'CTF151_helmet.mat';
    cfg.baseline = [-0.2 0];
    cfg.xlim = [-0.2 1];
    cfg.ylim = [-3e-13 3e-13];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Group/20210112T114330_ft_math_output_data.mat', 'reproduce_Group/20210112T114333_ft_math_output_data.mat', 'reproduce_Group/20210112T114337_ft_math_output_data.mat', 'reproduce_Group/20210112T114340_ft_math_output_data.mat'
    };
    cfg.outputfile = 'reproduce_Group/20210112T114351_ft_multiplotER_output';
    figure;
    ft_multiplotER(cfg);

    %%

    % a new input variable is entering the pipeline here: 20210112T114358_ft_timelockgrandaverage_input_varargin_1.mat
    % a new input variable is entering the pipeline here: 20210112T114358_ft_timelockgrandaverage_input_varargin_2.mat
    % a new input variable is entering the pipeline here: 20210112T114358_ft_timelockgrandaverage_input_varargin_3.mat
    % a new input variable is entering the pipeline here: 20210112T114358_ft_timelockgrandaverage_input_varargin_4.mat

    cfg = [];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Group/20210112T114358_ft_timelockgrandaverage_input_varargin_1.mat', 'reproduce_Group/20210112T114358_ft_timelockgrandaverage_input_varargin_2.mat', 'reproduce_Group/20210112T114358_ft_timelockgrandaverage_input_varargin_3.mat', 'reproduce_Group/20210112T114358_ft_timelockgrandaverage_input_varargin_4.mat'
    };
    cfg.outputfile = { 'reproduce_Group/20210112T114403_ft_timelockgrandaverage_output_grandavg.mat' };
    ft_timelockgrandaverage(cfg);

    %%

    % a new input variable is entering the pipeline here: 20210112T114404_ft_timelockgrandaverage_input_varargin_1.mat
    % a new input variable is entering the pipeline here: 20210112T114404_ft_timelockgrandaverage_input_varargin_2.mat
    % a new input variable is entering the pipeline here: 20210112T114404_ft_timelockgrandaverage_input_varargin_3.mat
    % a new input variable is entering the pipeline here: 20210112T114404_ft_timelockgrandaverage_input_varargin_4.mat

    cfg = [];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Group/20210112T114404_ft_timelockgrandaverage_input_varargin_1.mat', 'reproduce_Group/20210112T114404_ft_timelockgrandaverage_input_varargin_2.mat', 'reproduce_Group/20210112T114404_ft_timelockgrandaverage_input_varargin_3.mat', 'reproduce_Group/20210112T114404_ft_timelockgrandaverage_input_varargin_4.mat'
    };
    cfg.outputfile = { 'reproduce_Group/20210112T114409_ft_timelockgrandaverage_output_grandavg.mat' };
    ft_timelockgrandaverage(cfg);

    %%

    % a new input variable is entering the pipeline here: 20210112T114411_ft_timelockgrandaverage_input_varargin_1.mat
    % a new input variable is entering the pipeline here: 20210112T114411_ft_timelockgrandaverage_input_varargin_2.mat
    % a new input variable is entering the pipeline here: 20210112T114411_ft_timelockgrandaverage_input_varargin_3.mat
    % a new input variable is entering the pipeline here: 20210112T114411_ft_timelockgrandaverage_input_varargin_4.mat

    cfg = [];
    cfg.tracktimeinfo = 'yes';
    cfg.trackmeminfo = 'yes';
    cfg.inputfile = {
    'reproduce_Group/20210112T114411_ft_timelockgrandaverage_input_varargin_1.mat', 'reproduce_Group/20210112T114411_ft_timelockgrandaverage_input_varargin_2.mat', 'reproduce_Group/20210112T114411_ft_timelockgrandaverage_input_varargin_3.mat', 'reproduce_Group/20210112T114411_ft_timelockgrandaverage_input_varargin_4.mat'
    };
    cfg.outputfile = { 'reproduce_Group/20210112T114415_ft_timelockgrandaverage_output_grandavg.mat' };
    ft_timelockgrandaverage(cfg);

## Conclusion

This example demonstrated how _reproducescript_ can be applied to a group analysis by enabling it separately for each subject, and then once for the group analysis. It would be possible as well to enable reproducescript only once at the top of the master script, but we found the current solution to have a more clear organisation. There is one more example in which we apply reproducescript to full study published by Andersen et al. This shows how _reproducescript_ would be applied in a more complex scenario.

Note that there are other strategies for improving shareability and reproducibility, and we don't claim that _reproducescript_ is the best way in every scenario. Rather, it is one of many tools that can aid the researcher to improve the community's standard in methodological transparency and robustness of results. For other strategies, we refer the reader to the pre-print in which we first described _reproducescript_.

## Suggested further reading

- [Reducing the efforts to create reproducible analysis code with FieldTrip](http://dx.doi.org/10.21105/joss.05566)
- [Using reproducescript on a full study](/example/reproducescript_andersen)
