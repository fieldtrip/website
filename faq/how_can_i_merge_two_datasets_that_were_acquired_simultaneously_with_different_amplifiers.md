---
title: How can I merge two datasets that were acquired simultaneously with different amplifiers?
category: faq
tags: [preprocessing, raw, dataformat, eeg, meg]
---

# How can I merge two datasets that were acquired simultaneously with different amplifiers?

If your experimental setup requires you to acquire the data with two (or more) amplifiers, you end up with datasets that cannot easily be processed together. An example is an EEG setup with a separate GSR signal, or a MEG system with a non-standard EEG amplifier.

Below a piece of example code is given that outlines the approach that can be used to merge the two datasets. It assumes that both datasets can individually be preprocessed with FieldTrip, and that the triggers were sent to both acquisition systems.

    % define the trials for the first dataset
    cfg = [];
    cfg.dataset = 'dataset1.eeg'
    cfg.trialdef.eventtype  = 'trigger';
    cfg.trialdef.eventvalue = 1;
    cfg.trialdef.prestim = 1;            % in seconds
    cfg.trialdef.poststim = 2;            % in seconds
    cfg = ft_definetrial(cfg);

    % read the segments of interest around each trigger
    data1 = ft_preprocessing(cfg);

    % define the trials for the second dataset
    cfg = [];
    cfg.dataset = 'dataset2.eeg'
    cfg.trialdef.eventtype  = 'STATUS';  % see below
    cfg.trialdef.eventvalue = 127;
    cfg.trialdef.prestim = 1;            % in seconds
    cfg.trialdef.poststim = 2;            % in seconds
    cfg = ft_definetrial(cfg);

    % read the segments of interest around each trigger
    data2 = ft_preprocessing(cfg);

Note that the triggers in dataset2 might have a different descriptive name (event type) than in dataset 1, and that the values might be different (depending on how the triggers are wired up). Important is that the triggers in reality were send synchronously to both acquisition systems.

Immediately after preprocessing data1 and data2 represent the same segments of data from the two systems. They will have the same time-axis for each data segment/trial, even though the sampling frequencies are different. You can check this with

    % plot the first trial of both datasets
    figure
    plot(data1.time{1}, data1.trial{1}, 'b-.');
    hold on
    plot(data2.time{1}, data1.trial{2}, 'r-x');
    xlabel('time (s)')
    legend({'dataset1', 'dataset2'});

The idea now is to interpolate the timeseries of one dataset to the same resolution/frequency as the other dataset using **[ft_resampledata](/reference/ft_resampledata)**. Subsequently the datasets can be merged with **[ft_appenddata](/reference/ft_appenddata)**.

    % resample/interpolate dataset1 onto the sampled timepoints of dataset2
    cfg = [];
    cfg.time = data2.time;
    data1_resampled = ft_resampledata(cfg, data1);

    cfg = [];
    data_merged =  ft_appenddata(cfg, data1_resampled, data2);
