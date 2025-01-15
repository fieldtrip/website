---
title: Why am I not getting integer frequencies?
parent: Spectral analysis
grand_parent: Frequently asked questions
category: faq
tags: [preprocessing, freq]
redirect_from:
    - /faq/why_am_i_not_getting_exact_integer_frequencies/
    - /faq/freqanalysis_foinoninteger/
---

# Why am I not getting integer frequencies?

Probably this is due to your time windows being one sample longer than you expect, at a sampling frequency of 1000 Hz you might have e.g., 1001 samples rather than 1000 samples.

When defining time and/or frequency intervals, you should be aware about the different behavior of FieldTrip functions of the specification of bounds. The problem is sketched in general on the websitepedia lemma on [interval notation](http://en.wikibooks.org/wiki/Algebra/Interval_Notation).

## Using ft_definetrial with INCLUSIVE and/or EXCLUSIVE interval selection

For trigger-based trial selection, when using the default trial function **ft_trialfun_general**, the cfg.trialdef.postim value is NOT inclusive. For example, if the configuration is like this:

    cfg                         = [];
    cfg.dataset                 = 'Subject01.ds';
    cfg.trialfun                = 'ft_trialfun_general'; % this is the default
    cfg.trialdef.eventtype      = 'backpanel trigger';
    cfg.trialdef.eventvalue     = 3; % fully incongruent condition (FIC)
    cfg.trialdef.prestim        = 1; % in seconds
    cfg.trialdef.poststim       = 2; % in seconds
    cfg = ft_definetrial(cfg);

    cfg.trl(1,:)
    ans =
           901        1800        -300           3

    cfg.trl(1,2)-cfg.trl(1,1)
    ans =
     899

You can see that the first trial is 900 samples long, starting at sample 901 and ending at sample 1800. Since the sample frequency is 300 Hz, the interval is 3 seconds long. We can continue with preprocessing.

    data = ft_preprocessing(cfg);

    data.time{1}(1)
    ans =

      -1

    data.time{1}(end)
    ans =
      1.9967

where you see that the first sample is at time -1 seconds and the last sample is at time 1.9967 seconds, i.e. 2 seconds minus one sample.

The interval notation here is therefore `[cfg.trialdef.prestim cfg.trialdef.poststim)` where the square bracket `[]` according to [math notation](https://en.wikipedia.org/wiki/Interval_(mathematics)) indicates the INCLUSION of the cfg.trialdef.prestim value and the rounded bracket `)` indicates the EXCLUSION of the value cfg.trialdef.poststim, being the convention that the last sample will not be included.

You can define your time window in inclusive terms. i.e. as `[-1 2]` with square brackets on both sides, by creating your own trialfun as the example below.

    function trl = trialfun_inclusive(cfg)

    % TRIALFUN_INCLUSIVE requires the following fields to be specified
    %   cfg.dataset
    %   cfg.trialdef.eventvalue
    %   cfg.trialdef.prestim
    %   cfg.trialdef.poststim

    hdr   = ft_read_header(cfg.dataset);
    event = ft_read_event(cfg.dataset);

    trl = [];

    for i=1:length(event)
    if strcmp(event(i).type, cfg.trialdef.eventtype)
      % it is a trigger, see whether it has the right value
      if ismember(event(i).value, cfg.trialdef.eventvalue)
        % add this to the trl definition
        begsample     = event(i).sample - cfg.trialdef.prestim*hdr.Fs;
        endsample     = event(i).sample + cfg.trialdef.poststim*hdr.Fs;
        offset        = -cfg.trialdef.prestim*hdr.Fs;
        trigger       = event(i).value;
        trl(end+1, :) = [round([begsample endsample offset]) trigger];
      end
    end
    end

Alternatively, you can add one sample (in seconds) to the poststim specification like this:

    hdr         = ft_read_header(cfg.dataset);

    cfg.trialdef.prestim  = 1;
    cfg.trialdef.poststim = 2 + 1/hdr.Fs;

## Using ft_redefinetrial with INCLUSIVE and/or EXCLUSIVE interval selection

You might wonder what to do if you preprocessed using ft_trialfun_general and you want to select a shorter time window, for example to epoch continuous data. This can be done using **[ft_redefinetrial](/reference/ft_redefinetrial)**. Using the proper cfg option, you can do bot

## cfg.toilim

The specification

    cfg.toilim    = [tmin tmax]

will work in INCLUSIVE terms: both tmin and tmax will be included in the data selection. The same it's true for cfg.latency and cfg.foilim in **[ft_selectdata](/reference/utilities/ft_selectdata)**.

If you want to follow the ft_trialfun_general convention and exclude the last sample, then you should exclude it from the input:

    hdr         = ft_read_header(cfg.dataset);
    cfg.toilim  = [tmin (tmax-(1/hdr.Fs))];

## cfg.length

The cfg.length option in ft_redefinetrial behaves excluding then the last sample.

Combining cfg.length and cfg.overlap you can cut data into NON-overlapping segments, starting from the beginning of each trial

    % make epochs of 1 sec duration with NO overlaping between epochs
    cfg = [];
    cfg.length  = 1;
    cfg.overlap = 0;
    data        = ft_redefinetrial(cfg,data);
