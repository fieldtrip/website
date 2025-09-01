---
title: How can I process continuous data without triggers?
category: faq
tags: [preprocessing, continuous, raw]
redirect_from:
    - /faq/how_can_i_process_continuous_data_without_triggers/
    - /faq/preproc_continuous/
---

Most of the FieldTrip documentation is written for a cognitive neuroscience audience, i.e. researchers that usually are performing experiments in which different stimuli are presented and where the subject performs different mental tasks.

However, you can also use FieldTrip for analyzing continuous data that does not contain any triggers. One way for processing continuous data is to read it as a single, very long data segment. That is done by skipping **[ft_definetrial](/reference/ft_definetrial)** and by calling **[ft_preprocessing](/reference/ft_preprocessing)** like this

    cfg = [];
    cfg.dataset = 'yourfile.ext';
    ...                               % further specification of filter settings etc.
    data = ft_preprocessing(cfg);

This will give you a raw data structure containing all continuous data represented as a single, very long trial. You can plot it with

    plot(data.time{1}, data.trial{1});

## Reading subsequent segments from disk

For some analyses, e.g., spectral power estimation, it is better to have the data in smaller chunks. You can segment the continuous data while reading it in using the following configuration:

    cfg = [];
    cfg.dataset              = 'yourfile.ext';
    cfg.trialfun             = 'ft_trialfun_general';
    cfg.trialdef.triallength = 1;                   % in seconds
    cfg.trialdef.ntrials     = inf;                 % i.e. the complete file
    cfg = ft_definetrial(cfg);                      % this creates 1-second data segments

    ...                                             % further specification of filter settings etc.
    data = ft_preprocessing(cfg);

This uses the **ft_trialfun_general** function to segment the data. This function is included in FieldTrip, type _help trialfun_general_ for more details.

## Making overlapping segments while reading from disk

    cfg = [];
    cfg.dataset     = 'yourfile.ext';

    hdr             = ft_read_header(cfg.dataset);
    begsample       = 1:256:hdr.nSamples;             % slide with 256 samples
    endsample       = begsample + 512 - 1;            % the segment length is 512 samples
    offset          = zeros(size(begsample));

    cfg.trl         = [begsample(:) endsample(:) offset(:)]

    sel             = find(endsample>hdr.nSamples);
    cfg.trl(sel, :) = [];                             % remove the segments that are beyond the end of the file

    data = ft_preprocessing(cfg);

## Segmenting data that is already in memory

If you have read your data in into MATLAB and it is represented as a a single, very long trial, you can also segment it using **[ft_redefinetrial](/reference/ft_redefinetrial)**.

    cfg = [];
    cfg.dataset = 'yourfile.ext';
    data_continuous = ft_preprocessing(cfg);
    
    cfg = [];
    cfg.length = 1;
    data_segments = ft_redefinetrial(cfg, data);
    
    cfg = [];
    cfg.length = 1;
    cfg.overlap = 0.2; % expressed as percentage, i.e. 20%
    data_segments = ft_redefinetrial(cfg, data);
  
    
