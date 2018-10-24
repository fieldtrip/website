---
layout: default
tags: tutorial meg raw preprocessing MEG-language
---


# Trigger-based trial selection

## Introduction

This tutorial describes how to define epochs-of-interest (trials) from your recorded MEG-data, and how to apply the different preprocessing steps. This tutorial does not show yet how to analyze (e.g. average) your data. 

If you are interested in how to do preprocessing on your data prior to segmenting it into trials, you can check  the [Preprocessing - Reading continuous data](/tutorial/continuous) tutorial. There, you  can also find information about how to preprocess EEG data. If you want to learn how to segment EEG data into trials, check the tutorial on [Preprocessing of EEG data and computing ERPs](/tutorial/preprocessing_ERP).
## Background

In FieldTrip the preprocessing of data refers to the reading of the data, segmenting the data around interesting events such as triggers, temporal filtering and optionally rereferencing. The **[ft_preprocessing](/reference/ft_preprocessing)** function takes care of all these steps, i.e., it reads the data and applies the preprocessing options. 

There are largely two alternative approaches for preprocessing, which especially differ in the amount of memory required. The first approach is to read all data from the file into memory, apply filters, and subsequently cut the data into interesting segments. The second approach is to first identify the interesting segments, read those segments from the data file and apply the filters to those segments only. The remainder of this tutorial explains the second approach, as that is the most appropriate for large data sets such as the MEG data used in this tutorial. The approach for reading and filtering continuous data and segmenting afterwards is explained in another tutorial.

Preprocessing involves several steps including identifying individual trials from the dataset, filtering and artifact rejections. This tutorial covers how to identify trials using the trigger signal. Defining data segments of interest can be done 

*  according to a specified trigger channel

*  according to your own criteria when you write your own trial function

Examples for both ways are described in this tutorial, and both ways depend on **[ft_definetrial](/reference/ft_preprocessing)**.

The output of ft_definetrial is a configuration structure containing the field cfg.trl. This is a matrix representing the relevant parts of the raw datafile which are to be selected for further processing. Each row in the trl-matrix represents a single epoch-of-interest, and the trl-matrix has at least 3 columns. The first column defines (in samples) the beginpoint of each epoch with respect to how the data are stored in the raw datafile. The second column defines (in samples) the endpoint of each epoch, and the third column specifies the offset (in samples) of the first sample within each epoch with respect to timepoint 0 within that epoch. 

# 

{{page>:tutorial:shared:dataset}}


## Procedure

The following steps are taken in this tutorial: 


*  Define segments of data of interest (the trial definition) using **[ft_definetrial](/reference/ft_definetrial)**

*  Read the data into MATLAB using **[ft_preprocessing](/reference/ft_preprocessing)**

## Reading and preprocessing the interesting trials

Using the FieldTrip function **[ft_definetrial](/reference/ft_definetrial)** you can define the pieces of data that will be read in for preprocessing. Trials are defined by their begin and end sample in the data file and each trial has an offset that defines where the relative t=0 point (usually the point of the stimulus-trigger) is for that trial. 

The **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)** functions require the original MEG dataset, which is available at [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip)

Do the trial definition for the fully incongruent (FIC) conditio


	  cfg                         = [];
	  cfg.dataset                 = 'Subject01.ds';
	  cfg.trialfun                = 'ft_trialfun_general'; % this is the default
	  cfg.trialdef.eventtype      = 'backpanel trigger';
	  cfg.trialdef.eventvalue     = 3; % the value of the stimulus trigger for fully incongruent (FIC).
	  cfg.trialdef.prestim        = 1; % in seconds
	  cfg.trialdef.poststim       = 2; % in seconds
	  
	  cfg = ft_definetrial(cfg);


This results in a cfg.trl in which the beginning, the trigger offset and the end of each trial relative to the beginning of the raw data is defined.


The output of **[ft_definetrial](/reference/ft_definetrial)** can be used for **[ft_preprocessing](/reference/ft_preprocessing)**.

    cfg.channel    = {'MEG' 'EOG'};
    cfg.continuous = 'yes';
    dataFIC = ft_preprocessing(cfg);


Save the preprocessed data to dis

    save PreprocData dataFIC

The output of **[ft_preprocessing](/reference/ft_preprocessing)** is the structure dataFIC which has the following field


	dataFIC = 
	           hdr: [1x1 struct]
	         label: {152x1 cell}
	          time: {1x87 cell}
	         trial: {1x87 cell}
	       fsample: 300
	    sampleinfo: [87x2 double]
	     trialinfo: [87x1 double]
	          grad: [1x1 struct]
	           cfg: [1x1 struct]


The most important fields are dataFIC.trial containing the individual trials and dataFIC.time containing the time vector for each trial. To visualize the single trial data (trial 1) on one channel (channel 130) do the followin

    plot(dataFIC.time{1}, dataFIC.trial{1}(130,:))

![image](/media/tutorial/preprocessing/preprocess1.png)

The preprocessing steps will be repeated for the other conditions as well.

The initially congruent (IC) conditio
    
    cfg                         = [];
    cfg.dataset                 = 'Subject01.ds';
    cfg.trialdef.eventtype      = 'backpanel trigger';  
    cfg.trialdef.eventvalue     = 5; % the value of the stimulus trigger for initially congruent (IC).
    cfg.trialdef.prestim        = 1; % in seconds
    cfg.trialdef.poststim       = 2; % in seconds
    
    cfg = ft_definetrial(cfg);
    
    cfg.channel    = {'MEG' 'EOG'};
    cfg.continuous = 'yes';
    dataIC = ft_preprocessing(cfg);

Save the preprocessed data to dis

    save PreprocData dataIC -append

And the fully congruent (FC) conditio

    cfg                         = [];
    cfg.dataset                 = 'Subject01.ds';
    cfg.trialdef.eventtype      = 'backpanel trigger';
    cfg.trialdef.eventvalue     = 9; % the value of the stimulus trigger for fully congruent (FC).
    cfg.trialdef.prestim        = 1; % in seconds
    cfg.trialdef.poststim       = 2; % in seconds
    
    cfg = ft_definetrial(cfg);
    
    cfg.channel    = {'MEG' 'EOG'};
    cfg.continuous = 'yes';
    dataFC = ft_preprocessing(cfg);

Save the preprocessed data to dis

    save PreprocData dataFC -append

These functions demonstrate how to extract trials from a dataset based on trigger information. Note that some of these trials will be contaminated with various artifact such as eye blinks or MEG sensor jumps. Artifact rejection is described in [Preprocessing - Visual artifact rejection](/tutorial/visual_artifact_rejection)

## Use your own function for trial selection

There are often cases in which it is not sufficient to define a trial only according to a given trigger signal. For instance you might want to accept or reject a trial according to a button response recorded by the trigger channel as well. Another example might be that you want the signals from the EMG or A/D channel being part of the trial selection. In those cases it is necessary to define a specialized function for trial selections. Below is an example which can be adapted to your needs.

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
        trl(end+1, :) = [round([begsample endsample offset])  trigger]; 
      end
    end
    end

Save the trial function together with your other scripts as mytrialfun.m. To ensure that **[ft_preprocessing](/reference/ft_preprocessing)** is making use of the new trial function use the commands

    cfg = [];
    cfg.dataset  = 'Subject01.ds'; 
    cfg.trialfun = 'mytrialfun'; % ft_definetrial will call your function and pass on the cfg
    cfg.trialdef.eventtype  = 'backpanel trigger';
    cfg.trialdef.eventvalue = [3 5 9]; % read all conditions at once
    cfg.trialdef.prestim    = 1; % in seconds
    cfg.trialdef.poststim   = 2; % in seconds

    
    cfg = ft_definetrial(cfg);
    
    cfg.channel = {'MEG' 'STIM'};
    dataMytrialfun = ft_preprocessing(cfg);


When you do not specify cfg.trialfun, **[ft_definetrial](/reference/ft_definetrial)** will call a function named trialfun_general as default. Then trials will be defined as we have seen it in the earlier section (Reading and preprocessing the interesting trials).

The output dataMytrialfun now contains all of the trials of the three conditions (since we specified all three triggers values: 3, 5 and 9). It also contains a field dataMytrialfun.trialinfo, which contains the 4th column of the trl (trial definition) which contains the trigger values, i.e., it tells you to which condition each trial belong

	
	dataMytrialfun = 
	
	           hdr: [1x1 struct]
	         label: {152x1 cell}
	          time: {1x261 cell}
	         trial: {1x261 cell}
	       fsample: 300
	    sampleinfo: [261x2 double]
	     trialinfo: [261x1 double]
	          grad: [1x1 struct]
	           cfg: [1x1 struct]


More on the trialinfo field can be found in the [faq](/faq/is_it_possible_to_keep_track_of_trial-specific_information_in_my_fieldtrip_analysis_pipeline).

## Suggested further reading

After having finished this tutorial on preprocessing, you can continue with the [event related averaging](/tutorial/eventrelatedaveraging) or with the [time-frequency analysis](/tutorial/timefrequencyanalysis) tutorial. 

If you have more questions about preprocessing, you can also read the following faq-
{{topic>faq +preprocessing &list}}
Or you can also read the example script
{{topic>example +preprocessing &list}}

-----

This tutorial was last tested with version 20120501 of FieldTrip using MATLAB 2009b on a 64-bit Linux platform.

