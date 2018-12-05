---
title: Why does my TFR contain NaNs?
tags: [faq, freq]
---

## Why does my TFR contain NaNs?

Spectro-temporal reconstruction algorithms aim to achieve the following: A time series is converted into a 'series' of 'time series' containing the temporal course of amplitude&phase (or power) at a series of frequencies. Irrespective of the algorithm used, this always boils down to sliding a window through the original time series and estimating the quantities of interest at prespecified timepoints. Equivalently, one can convolve with a bandpass-filter kernel, or a wavelet. In order to get a good estimate of the quantities of interest, the sliding window should be completely filled with data (or the convolution-kernel should completely overlap with data). Either way, if the prespecified time points of interest are close to the boundaries of the original time series, NaNs will appear in the output of the TFR-analysis, because there is insufficient data at these locations.
Practically this means that if your data is defined e.g. between -1 and +1 seconds, and using a cfg.t_ftimwin of 0.5 seconds, freqanalysis_mtmconvol will only give non-NaN output only between -0.75 and 0.75 seconds. 

