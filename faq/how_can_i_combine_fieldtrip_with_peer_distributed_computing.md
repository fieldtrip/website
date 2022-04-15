---
title: How can I combine FieldTrip with peer distributed computing?
tags: [faq, peer]
---

# How can I combine FieldTrip with peer distributed computing?

The peer distributed computing toolbox was implemented with FieldTrip (and SPM) in mind. At the moment however, FieldTrip itself does not yet make use of the peer toolbox, i.e. FieldTrip functions do not automatically distribute the workload. We are of course planning to make that possible, i.e. that a single cfg.parallel='yes' option will automatically distribute the computational load over all available nodes.

At the moment the only way of distributing the workload over multiple nodes requires that you adapt your scripts. The easiest is to distribute the workload of the analysis of multiple subjects over multiple nodes. Since each subject usually represents a lot of data, it is not always possible to keep multiple subjects simultaneously in memory. To facilitate the distributed analysis over multiple subjects, the FieldTrip functions therefore have the cfg.inputfile and cfg.outputfile options.

FieldTrip functions usually have two input arguments, the first is the configuration structure and the second is a structure with the input data. The cfg.inputfile option can be used to specify the name of the .mat file from which the input data is read. The .mat file is assumed to contain a single variable.

FieldTrip functions usually also have an output argument, which is a structure with the output data. The cfg.outputfile option specifies to which .mat file that data will be written.

So instead of preprocessing data like

  cfg = [];
  cfg.dataset = 'Subject01.ds'
  ...
  data = ft_preprocessing(cfg);
  save subject01_raw.mat data

followed by averaging the trials to get an ERP

  load subject01_raw.mat data % actually not needed here because the data is still in memory
  cfg = [];
  avg = ft_timelockanalysis(cfg, data);
  save subject01_avg.mat avg

you would do

  cfg = [];
  cfg.dataset = 'Subject01.ds'
  ...
  cfg.outputfile = 'subject01_raw.mat'
  ft_preprocessing(cfg);

and

  cfg = [];
  ...
  cfg.inputfile = 'subject01_raw.mat'
  cfg.outputfile = 'subject01_avg.mat'
  ft_timelockanalysis(cfg);

Note that when specifying the cfg.inputfile and/or cfg.outputfile options, that you should not specify an input and/or output variable.

## Example: processing the MEG data for all tutorial subjects

The MEG data used in the FieldTrip tutorials is available from <https://download.fieldtriptoolbox.org/tutorial/>. There is data for four subjects, which can be processed in parallel as follows.

    subj  = [1 2 3 4];

    cfg = {};
    % create a cell-array of configurations, one per subject
    for i=1:length(subj)

    % just like in the scripting tutorial, you may want to evaluate a
    % subject specific script that contains details such as the filename
    % of the MRI, the location of the raw data or the list of bad channels
    %
    % eval(sprintf('subject%02d_details', i));

    cfg{i} = [];
    cfg{i}.dataset = sprintf('Subject%02d.ds', i);
    cfg{i}.trialdef.eventtype  = 'backpanel trigger';
    cfg{i}.trialdef.eventvalue = 5;
    cfg{i}.trialdef.prestim    = 0.2;
    cfg{i}.trialdef.poststim   = 0.2;
    cfg{i}.outputfile = sprintf('subj%02d_raw.mat', i);
    end

    % define the trials, this returns an updated cfg
    % this does not take long and does not have to be done in parallel
    cfg = cellfun(@ft_definetrial, cfg, 'UniformOutput', 0);

    % read the raw data, preprocess it and save the result to disk
    peercellfun(@ft_preprocessing, cfg);

    cfg = {};
    % create a cell-array of configurations, one per subject
    for i=1:length(subj)
    cfg{i} = [];
    cfg{i}.inputfile  = sprintf('subj%02d_raw.mat', i);
    cfg{i}.outputfile = sprintf('subj%02d_avg.mat', i);
    end

    % load the raw data from disk, average it and save the result
    peercellfun(@ft_timelockanalysis, cfg);

Please note that file permissions can be problematic if you use peers that are running under another user (e.g., public). If you use a publicly writeable directory, e.g., in Linux:

    mkdir ~/public
    chmod 777 ~/public

For the cfg.outputfile and cfg.inputfile options, you should be fine.

## Bundling multiple functions in a single distributed job

If you don't want each function to read/write the intermediate files from/to disk, you can also bundle them into a function that executes them in sequence. For example

    function [source] = preproc_freq_source(cfg1, cfg2, cfg3)
    data = ft_preprocessing(cfg1);
    freq = ft_freqanalysis(cfg2, data);
    clear data % remove it from memory as soon as it is not needed any more
    source = ft_sourceanalysis(cfg3, freq);
    clear freq % remove it from memory as soon as it is not needed any more

And then you would call it in parallel for many subjects and conditions like this

    for subj=1:10
    for cond=1:4

    % here you would specify a different dataset for each subject
    % and perhaps a different trigger code
    cfg1{subj, cond} = ...

    cfg2{subj, cond} = ...

    cfg3{subj, cond} = ...

    end % cond
    end % subj

    sourceall = peercellfun(@preproc_freq_source, cfg1, cfg2, cfg3);

Here all the source reconstructions will be returned to the controller MATLAB session. Of course you can also save them to disk using unique filenames for each subject and condition. Alternatively you can use the cfg.inputfile option for the first step in your bundle of FieldTrip functions, and cfg.outputfile in the last step.

## Effective distribution of jobs

If one can make an estimation of the jobs to be distributed, one could distribute the jobs without obstructing the jobs of others. For example, say you have a job that takes half an hour to finish, it would be recommended to send that job to machines that are suitable for these kind of jobs. The limited amount of 'heavy' machines would then still be available to users with larger jobs (for example 2 hours). Id est, you don't recruit a team of strong persons to move just a chair (in stead of a heavy couch).

How to make sure that you are recruiting the right machines? Just call the peercellfun with the extra options, for example the memory required (memreq) and the time required (timreq). Two examples follow.

Small job (half a GB and half an hour

    peercellfun(@ft_timelockanalysis, cfg, 'memreq', .5*(1024^3), 'timreq', .5*3600);

Large job (two GB and 4 hours

    peercellfun(@ft_freqanalysis, cfg, 'memreq', 2*(1024^3), 'timreq', 4*3600);
