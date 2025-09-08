---
title: Why does my TFR contain NaNs?
tags: [freq]
category: faq
redirect_from:
    - /faq/why_does_my_tfr_contain_nans/
    - /faq/tfr_nans/
---

Spectro-temporal reconstruction algorithms aim to achieve the following: A time series is converted into a 'series' of 'time series' containing the temporal course of amplitude and phase (or power) at a series of frequencies. Irrespective of the algorithm used, this always boils down to sliding a window through the original time series and estimating the quantities of interest at pre-specified time points. Equivalently, one can convolve with a bandpass-filter kernel, or a wavelet. In order to get a good estimate of the quantities of interest, the sliding window should be completely filled with data (or the convolution-kernel should completely overlap with data). Either way, if the pre-specified time points of interest are close to the boundaries of the original time series, NaNs will appear in the output of the TFR-analysis, because there is insufficient data at these locations.

Practically this means that if your data is defined e.g., between -1 and +1 seconds, and using a `cfg.t_ftimwin` of 0.5 seconds, mtmconvol will only give non-NaN output only between -0.75 and 0.75 seconds. Similarly, when you use `cfg.method='wavelet'` using a `width` parameter that is a fixed number of cycles (per frequency) you may obtain a U-shaped TFR that is a direct consequence of the fact that the integration window of the wavelet convolution scales with the inverse of the frequency.
