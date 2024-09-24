---
title: How can I do time-frequency analysis on continuous data?
category: faq
tags: [continuous, freq]
---

# How can I do time-frequency analysis on continuous data?

There are cases where you have recorded continuous data without specific events of interest, e.g., resting state data. In the absence of events on the basis of which to segment the data into trials, you would proceed processing the data as [continuous data](/tutorial/continuous).

In continuous data you primarily would expect the EEG or MEG signal to be stationary, i.e. not change over time. Hence there is no point in doing time-frequency analysis, because you don't expect changes in the power spectrum over time, at least not on a very short time scale.

However, you might be interested in changes in the power spectrum at a much longer time scale. Regular time-frequency analysis (e.g., with method wavelet or mtmconvol in **[ft_freqanalysis](/reference/ft_freqanalysis)**) is not appropriate to reveal the dynamics of spectral changes over a long time scale. Below we outline an alternative approach that does work well and that is computationally efficient.

We start by reading the data as one long continuous segment. It may be useful at this stage to apply a high-pass filter to remove the slow drift from the data

    cfg = [];
    cfg.dataset  = 'subj2.vhdr'
    cfg.hpfilter = 'yes'
    cfg.hpfreq   = 1;
    data_continuous = ft_preprocessing(cfg)

Let us visually inspect the data

    cfg = [];
    cfg.viewmode = 'vertical'
    ft_databrowser(cfg, data_continuous)

Subsequently, we proceed by segmenting the data into "trials", i.e. data segments of constant length. If we were to concatenate all segments, we would again have the original data.

    cfg = [];
    cfg.length = 1;
    cfg.overlap = 0;
    data_segmented = ft_redefinetrial(cfg, data_continuous)

Using **[ft_freqanalysis](/reference/ft_freqanalysis)** with method mtmfft, we can compute the power spectrum for each trial/segment. Note that we keep the spectra for all individual trials/segments.

    cfg = [];
    cfg.method     = 'mtmfft'
    cfg.taper      = 'hanning'
    cfg.foilim     = [1 30];
    cfg.keeptrials = 'yes'
    freq_segmented = ft_freqanalysis(cfg, data_segmented)

Now comes the trick: the trials/segments in the data represent time at the level of the experiment, i.e. every subsequent trial is one second advanced in time. We can reformat the freq_segmented structure into a regular time-frequency representation.

The time or latency of each trial can be constructed using the sampleinfo from the segmented data, which specified for each trial the begin and the end-sample relative in the original datafile.

    begsample = data_segmented.sampleinfo(:,1);
    endsample = data_segmented.sampleinfo(:,2);
    time = ((begsample+endsample)/2) / data_segmented.fsample;

Then we proceed by copying the freq structure, in which we flip the power spectrum to change the "rpt" dimension into the "time" dimension:

    freq_continuous           = freq_segmented;
    freq_continuous.powspctrm = permute(freq_segmented.powspctrm, [2, 3, 1]);
    freq_continuous.dimord    = 'chan_freq_time'; % it used to be 'rpt_chan_freq'
    freq_continuous.time      = time;             % add the description of the time dimension

Finally we can plot it, just like a regular time-frequency representation

    cfg = []
    cfg.layout = 'easycapM10.mat'
    ft_multiplotTFR(cfg, freq_continuous);
