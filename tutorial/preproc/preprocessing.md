---
title: Preprocessing - Segmenting and reading trial-based EEG and MEG data
category: tutorial
tags: [meg, raw, preprocessing, meg-language]
redirect_from:
    - /tutorial/preprocessing/
---

# Preprocessing - Segmenting and reading trial-based EEG and MEG data

## Introduction

This tutorial describes how to define epochs-of-interest (trials) from MEG data, and how to apply the different preprocessing steps. This tutorial does not show yet how to analyze (e.g., average) your data.

If you are interested in how to do preprocessing on your data prior to segmenting it into trials, you can check the [Preprocessing - Reading continuous data](/tutorial/continuous) tutorial, which also introduces some preprocessing options that are specific for EEG. If you want to learn how to segment continuous data into trials, check the [Preprocessing of EEG data and computing ERPs](/tutorial/preprocessing_erp) tutorial.

## Background

In FieldTrip the preprocessing of data refers to the reading of the data, segmenting the data around interesting events such as triggers, temporal filtering and optionally rereferencing. The **[ft_preprocessing](/reference/ft_preprocessing)** function takes care of all these steps, i.e., it reads the data and applies the preprocessing options.

There are largely two alternative approaches for preprocessing, which especially differ in the amount of memory required. The first approach is to read all data from the file into memory, apply filters, and subsequently cut the data into interesting segments. The second approach is to first identify the interesting segments, read those segments from the data file and apply the filters to those segments only. The remainder of this tutorial explains the second approach, as that is the most appropriate for large data sets such as the MEG data used in this tutorial. The approach for reading and filtering continuous data and segmenting afterwards is explained in another tutorial.

Preprocessing involves several steps including identifying individual trials from the dataset, filtering and artifact rejections. This tutorial covers how to identify trials using the trigger signal. Defining data segments of interest can be done

- according to a specified trigger channel
- according to your own criteria when you write your own trial function

Examples for both ways are described in this tutorial, and both ways depend on **[ft_definetrial](/reference/ft_preprocessing)**.

The output of ft_definetrial is a configuration structure containing the field cfg.trl. This is a matrix representing the relevant parts of the raw datafile which are to be selected for further processing. Each row in the `trl` matrix represents a single epoch-of-interest, and the `trl` matrix has at least 3 columns. The first column defines (in samples) the beginpoint of each epoch with respect to how the data are stored in the raw datafile. The second column defines (in samples) the endpoint of each epoch, and the third column specifies the offset (in samples) of the first sample within each epoch with respect to timepoint 0 within that epoch.

### The dataset used in this tutorial

{% include /shared/tutorial/meg_language.md %}

## Procedure

The following steps are taken in this tutorial:

- Define segments of data of interest (the trial definition) using **[ft_definetrial](/reference/ft_definetrial)**
- Read the data into MATLAB using **[ft_preprocessing](/reference/ft_preprocessing)**
- Split up the data for the different conditions **[ft_selectdata](/reference/utilities/ft_selectdata)**

## Reading and preprocessing the interesting trials

Using the FieldTrip function **[ft_definetrial](/reference/ft_definetrial)** you can define the pieces of data that will be read in for preprocessing. Trials are defined by their begin and end sample in the data file and each trial has an offset that defines where the relative t=0 point (usually the point of the stimulus-trigger) is for that trial.

{% include /shared/tutorial/definetrial_all.md %}

This results in a cfg.trl that contains the trial definitions of all conditions (since we specified all three trigger values: 3, 5, and 9). In cfg.trl the beginning, the trigger offset and the end of each trial relative to the beginning of the raw data are defined. Additionally, cfg.trl contains a column that contains the trigger values, i.e., it tells you to which condition each trial belongs.

The output of **[ft_definetrial](/reference/ft_definetrial)** can be used for **[ft_preprocessing](/reference/ft_preprocessing)**.

    cfg.channel    = {'MEG' 'EOG'};
    cfg.continuous = 'yes'; % see https://www.fieldtriptoolbox.org/faq/continuous/
    data_all = ft_preprocessing(cfg);

    Save the data to disk

        save PreprocData data_all


The output of **[ft_preprocessing](/reference/ft_preprocessing)** is the structure data_all which has the following fields:

    data_all =
               hdr: [1x1 struct]
             label: {152x1 cell}
              time: {1x261 cell}
             trial: {1x261 cell}
           fsample: 300
        sampleinfo: [261x2 double]
         trialinfo: [261x1 double]
              grad: [1x1 struct]
               cfg: [1x1 struct]

The `data_all` structure contains a field `data_all.trialinfo`, which contains the 4th column of the `trl` (trial definition) that contains the trigger values. The most important fields are `data_all.trial` containing the individual trials and `data_all.time` containing the time vector for each trial. To visualize the single-trial data (trial 1) on one channel (channel 130) do the following:

    plot(data_all.time{1}, data_all.trial{1}(130,:))

{% include image src="/assets/img/tutorial/preprocessing/figure1.png" %}

You can split up the conditions by selecting trials according to their trigger value in `data_all.trialinfo`.

    cfg=[];
    cfg.trials = (data_all.trialinfo==3);
    dataFIC = ft_selectdata(cfg, data_all);

    cfg.trials = (data_all.trialinfo==5);
    dataIC = ft_selectdata(cfg, data_all);

    cfg.trials = (data_all.trialinfo==9);
    dataFC = ft_selectdata(cfg, data_all);

Save the preprocessed data to disk

    save PreprocData dataFIC dataIC dataFC -append

These functions demonstrate how to extract trials from a dataset based on trigger information. Note that some of these trials will be contaminated with various artifact such as eye blinks or MEG sensor jumps. Artifact rejection is described in [Preprocessing - Visual artifact rejection](/tutorial/visual_artifact_rejection)

## Use your own function for trial selection

There are often cases in which it is not sufficient to define a trial only according to a given trigger signal. For instance you might want to accept or reject a trial according to a button response recorded by the trigger channel as well. Another example might be that you want the signals from the EMG or A/D channel being part of the trial selection. In those cases it is necessary to define a specialized function for trial selections. In this example we only select trials of which the previous trial was of a different condition. First, the condition of the current and the preceding trial are noted in the trial information. At the end, all trials in which these are the same, are removed. This is helpful when for example, you are interested in sequential trial effects, like: Is the signal different when it was preceded by a trial of type A rather than a trial of type B?


    function trl = mytrialfun(cfg);

    % this function requires the following fields to be specified
    % cfg.dataset
    % cfg.trialdef.eventtype
    % cfg.trialdef.eventvalue
    % cfg.trialdef.prestim
    % cfg.trialdef.poststim

    hdr   = ft_read_header(cfg.dataset);
    event = ft_read_event(cfg.dataset);

    trl = [];

    for i=1:length(event)
    if strcmp(event(i).type, cfg.trialdef.eventtype)
      % it is a trigger, see whether it has the right value
      if ismember(event(i).value, cfg.trialdef.eventvalue)
        % add this to the trl definition
        begsample     = event(i).sample - cfg.trialdef.prestim*hdr.Fs;
        endsample     = event(i).sample + cfg.trialdef.poststim*hdr.Fs - 1;
        offset        = -cfg.trialdef.prestim*hdr.Fs;
        trigger       = event(i).value; % remember the trigger (=condition) for each trial
        if isempty(trl)
          prevtrigger = nan;
        else
          prevtrigger   = trl(end, 4); % the condition of the previous trial
        end
        trl(end+1, :) = [round([begsample endsample offset])  trigger prevtrigger];
      end
    end
    end

    samecondition = trl(:,4)==trl(:,5); % find out which trials were preceded by a trial of the same condition
    trl(samecondition,:) = []; % delete those trials


Save the trial function together with your other scripts as `mytrialfun.m`. To ensure that **[ft_preprocessing](/reference/ft_preprocessing)** is making use of the new trial function use the commands

    cfg = [];
    cfg.dataset              = 'Subject01.ds';
    cfg.trialfun             = 'mytrialfun';     % it will call your function and pass the cfg
    cfg.trialdef.eventtype  = 'backpanel trigger';
    cfg.trialdef.eventvalue = [3 5 9];           % read all conditions at once
    cfg.trialdef.prestim    = 1; % in seconds
    cfg.trialdef.poststim   = 2; % in seconds

    cfg = ft_definetrial(cfg);

    cfg.channel = {'MEG' 'STIM'};
    dataMytrialfun = ft_preprocessing(cfg);

When you do not specify `cfg.trialfun`, **[ft_definetrial](/reference/ft_definetrial)** will call a function named trialfun_general as default. Then trials will be defined as we have seen it in the earlier section (Reading and preprocessing the interesting trials).

The output structure `dataMytrialfun` now contains fewer trials than before: only 192 instead of 261. Thus, we discarded 69 trials that had the same condition in the previous trial. The field `dataMytrialfun.trialinfo` contains the 4th column of the trl (trial definition) (trigger values of the current trial), and the 5th column of the trl (trigger values of the previous trial).

    dataMytrialfun =

               hdr: [1x1 struct]
             label: {152x1 cell}
              time: {1x192 cell}
             trial: {1x192 cell}
           fsample: 300
        sampleinfo: [192x2 double]
         trialinfo: [192x2 double]
              grad: [1x1 struct]
               cfg: [1x1 struct]

More on the `trialinfo` field can be found in the [faq](/faq/is_it_possible_to_keep_track_of_trial-specific_information_in_my_fieldtrip_analysis_pipeline).

## Suggested further reading

After having finished this tutorial on preprocessing, you can continue with the [event-related averaging](/tutorial/eventrelatedaveraging) or with the [time-frequency analysis](/tutorial/timefrequencyanalysis) tutorial.

### See also these frequently asked questions

{% include seealso category="faq" tag1="preprocessing" %}

### See also these examples

{% include seealso category="example" tag1="preprocessing" %}
