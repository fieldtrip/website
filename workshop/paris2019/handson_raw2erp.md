---
title: From raw data to ERP
tags: [tutorial, meg, timelock, preprocessing, plot]
---

# From raw data to ERP

{% include markup/info %}
This tutorial was written specifically for the practicalMEEG workshop in Paris in December 2019.
{% include markup/end %}

## Introduction

In this tutorial, we will learn how to read in 'raw' data from a file, and to apply some basic processing and averaging in order to inspect event-related fields.

This tutorial only briefly covers the steps required to import data into FieldTrip and preprocess it. This is covered in more detail in the [preprocessing](/tutorial/preprocessing) tutorial, which you can refer to if you want more details.

## Reading in raw data from disk

 In FieldTrip the preprocessing of data refers to the reading of the data, segmenting the data around interesting events such as triggers, temporal filtering and optionally rereferencing. The **[ft_preprocessing](/reference/ft_preprocessing)** function takes care of all these steps, i.e., it reads the data and applies the preprocessing options.

There are largely two alternative approaches for preprocessing, which especially differ in the amount of memory required. The first approach is to read all data from the file into memory, apply filters, and subsequently cut the data into interesting segments. The second approach is to first identify the interesting segments, read those segments from the data file and apply the filters to those segments only. The remainder of this tutorial explains the second approach, as that is the most appropriate for large data sets such as the MEG data used in this tutorial. The approach for reading and filtering continuous data and segmenting afterwards is explained in another tutorial.

Preprocessing involves several steps including identifying individual trials from the dataset, filtering and artifact rejections. This tutorial covers how to identify trials using the trigger signal. Defining data segments of interest can be done

- according to a specified trigger channel
- according to your own criteria when you write your own trial function

This tutorial will focus on the first way, and briefly mention the second. Both ways depend on **[ft_definetrial](/reference/ft_definetrial)**. For more details, see the [preprocessing](/tutorial/preprocessing) tutorial.

The output of ft_definetrial is a configuration structure containing the field cfg.trl. This is a matrix representing the relevant parts of the raw datafile which are to be selected for further processing. Each row in the trl-matrix represents a single epoch-of-interest, and the trl-matrix has at least 3 columns. The first column defines (in samples) the beginpoint of each epoch with respect to how the data are stored in the raw datafile. The second column defines (in samples) the endpoint of each epoch, and the third column specifies the offset (in samples) of the first sample within each epoch with respect to timepoint 0 within that epoch.

We will demonstrate reading in data based on the localizer task for the experiment that was described at the start. These data are available from the [FieldTrip ftp server (SubjectCMC.zip)](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/SubjectCMC.zip). In this localizer task, a simple cue was presented 50 times, instructing the participant to lift the left or right wrist and keep the muscle contracted for 10 seconds. We will use the default trialfun `ft_trialfun_general` to define trials based on the triggers sent alongside these cues. We want to read in 1s of data before each trigger, and 10s of data after each trigger. This is achieved by the following:

    cfg = [];
    cfg.dataset = 'SubjectCMC.ds';
    cfg.trialfun = 'ft_trialfun_general';
    cfg.trialdef.eventtype = 'backpanel trigger'; % the name of your trigger channel
    cfg.trialdef.eventvalue = 1:50; % which triggers to look for
    cfg.trialdef.prestim = 1; % 1s of data before each trigger
    cfg.trialdef.poststim = 10; % 10s of data after each trigger
    cfg = ft_definetrial(cfg);

Note that we're taking the output of `ft_definetrial` and storing it in our `cfg` variable. The output `cfg` now additionally has a field `cfg.trl` that contains our trial definition. Using the created trial definition, we can add some preprocessing options and read in the data:

    % the following tells the reading functions that the data on disk is
    % continuous and not already segmented
    cfg.continuous = 'yes';

    cfg.channel = {'MEG' 'EMGlft' 'EMGrgt' 'EOG' 'ECG'};

    % just to show that you can apply a lowpass filter while reading in data
    cfg.lpfilter = 'yes';
    cfg.lpfreq = 40;
    cfg.lpfilttype = 'firws'; % windowed-sinc FIR filter

    % and use data padding for the filtering
    cfg.padding = 13; % pad our 11s-long trials to 13s before filtering
    cfg.padtype = 'data'; % this is the default when reading from disk

    data = ft_preprocessing(cfg);

Now you could start working with these localizer data.

## Reading in preprocessed data from the main task
