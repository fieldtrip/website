---
title: Getting started with ABM's B-Alert EEG data
category: getting_started
tags: [dataformat, b-alert, balert, abm, x10, x-10, x24, x-24]
---

# Getting started with ABM's B-Alert EEG data

## Introduction

The B-Alert systems are relatively new EEG systems developed by [Advanced Brain Monitoring](http://www.advancedbrainmonitoring.com/) (ABM) and are often used for real time assessment of workload, attention and distraction ([Berka et al., 2007](http://www.ingentaconnect.com/content/asma/asem/2007/00000078/A00105s1/art00032)), for which they have built-in algorithms in their paid software [B-Alert Live](http://www.advancedbrainmonitoring.com/b-alert-live/). Besides EEG, you can measure EKG with an EKG lead and head movements with 3D-accelerometers.

Because of these algorithms the data is structured in a slightly different way. Instead of one large array of data for each channel, the data is segmented in so-called 'epochs' of one second. Within each epoch, there are 256 samples (Fs = 256) in which the data is stored. This means that, if you have data of a 1000 seconds and you use **[ft_preprocessing](/reference/ft_preprocessing)**, you get segmented data with a 1000 separate trials. Another issue, is that the event-markers are saved in a different Event.edf file. Therefore, we need to take some additional steps before we can start analyzing the data with FieldTrip.

It is expected that you have basic knowledge of FieldTrip and the use of configurations (cfg). In this tutorial, we will only focus on restructuring and resegmenting data.

{% include markup/red %}
For the events to be extracted, you need ABM's paid software B-Alert Lab. For the time being, there is no possibility to extract the events via FieldTrip functions.
{% include markup/end %}

## Restructuring EEG data

As mentioned in the [introduction](#introduction), the data is stored in epochs of one second. This can easily be solved by using the function **[edf2fieldtrip](/reference/edf2fieldtrip)**. The function first reads the data and the sample frequency of each channel. If there is a mismatch in sample frequencies between channels, the channels with a lower sample frequency will be up-sampled with **[ft_resampledata](/reference/ft_resampledata)** to the highest sample frequency. This may greatly increase the size of your data! In this particular situation, one channel is even up-sampled from 8 Hz to 1024 **(i.e times 2^7.m)**. After up-sampling, the data is concatenated into one data structure.

    In read_edf (line 330)
    In ft_read_header (line 678)
    In edf2fieldtrip (line 36)
    reading 1 channels with 8 Hz sampling rate
    reading 3 channels with 128 Hz sampling rate
    reading 10 channels with 256 Hz sampling rate
    reading 1 channels with 512 Hz sampling rate
    reading 1 channels with 1024 Hz sampling rate

After using edf2fieldtrip, some extra fields need to be created with the correct values, as to make the data struct complete. Both steps are shown in the following code.

    rawDir = dir('*Raw.edf'); % find all raw-data files.
    % load data in continuous form
    cfg = [];
    cfg.dataset = rawDir(1).name; % select first file.
    % read header and read data. Add fields that are missing after edf2fieldtrip().
    hdr = ft_read_header(cfg.dataset);
    data = edf2fieldtrip(cfg.dataset);
    data.hdr = hdr;
    data.hdr.Fs = data.fsample;
    data.hdr.nChans = length(data.label);
    data.hdr.label = data.label;
    data.hdr.nSamples = length(data.trial{1}(1,:));

### Define trials

Now the data is structured nicely, we can continue with extracting the events. As mentioned before, you **must** have read the events via *readevents(*Events.edf,_Raw.edf)_ in ABM's B-Alert Lab software. Only after this, we can extract the events from a .csv file. Now, specify each of the configuration variables as shown below, so that **[ft_trialfun_balert](/reference/trialfun/ft_trialfun_balert)** can interpret it. There are no default values.

    eventDir = dir('*_Events.csv');
    % load in event markers
    % Each of these cfg variables is necessary!!
    cfg = [];
    cfg.dataset = eventDir(1).name; % specify name of the Event.csv file.
    cfg.newfs = data.fsample; % specify the new Fs.
    cfg.prestim = 3; % seconds pre-marker
    cfg.poststim = 1; % seconds post-marker
    cfg.eventvalue = [1 2]; % array of relevant event markers
    % B-alert Trial function. Save the ft_trialfun_balert in 'toolbox/fieldtrip/trialfun'
    cfg.trialfun = 'ft_trialfun_balert';
    cfg = ft_trialfun_balert(cfg); %  segment all trials

Nb. At the moment, **[ft_definetrial](/reference/ft_definetrial)** is not used for the segmentation. Instead, **[ft_trialfun_balert](/reference/trialfun/ft_trialfun_balert)** is called directly. This should be better integrated into FieldTrip, please contact the B-Alert support team for this.

## Combining EEG data with events

The data is structured and we have a configuration containing a cfg.trl, which is necessary to segment the data. The final step that needs to be taken is to redefine the trials one last time with **[ft_redefinetrial](/reference/ft_redefinetrial)**.

    dataSeg = ft_redefinetrial(cfg, data);

With these two snippets of code, and **[ft_trialfun_balert](/reference/trialfun/ft_trialfun_balert)** your data is ready to be preprocessed with **[ft_preprocessing](/reference/ft_preprocessing)**. Afterwards, when you are going to use **[ft_databrowser](/reference/ft_databrowser)**, you need to specify cfg.channel and cfg.headerfile, as defined in ''data.hdr'' earlier on:

    cfg = [];
    cfg.channel = {'Fz','POz','Cz','F3','F4','PO3','PO4','C3','C4'}; % All 9 EEG channels of the B-Alert X-10
    cfg.headerfile = data.hdr;
    ft_databrowser(cfg, dataPrep);
