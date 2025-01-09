---
title: Why does my output.freq not match my cfg.foi when using 'mtmconvol' in ft_freqanalysis?
parent: Spectral analysis
category: faq
tags: [freq, mtmconvol]
redirect_from:
    - /faq/why_does_my_output.freq_not_match_my_cfg.foi_when_using_mtmconvol_in_ft_freqanalysis/
    - /faq/why_does_my_output.freq_not_match_my_cfg.foi_when_using_mtmconvol_in_ft_freqanalyis/
---

# Why does my output.freq not match my cfg.foi when using 'mtmconvol' in ft_freqanalysis?

Conceptually, a time frequency analysis can be thought of as a time domain convolution of a signal with a set of wavelets, each of these being designed to capture some feature in the data (i.e. the time dependent fluctuations of the amplitude (and phase) of band-limited signal components). To this end, the 'mtmconvol'-method uses sine/cosine waves, tapered with multitapers (or Hanning tapers). Computationally, the FieldTrip implementation uses the trick: "convolution in the time domain is equivalent to multiplication in the frequency domain". In other words, rather than convolving the time domain signal with the wavelets of different frequencies, the Fourier representation of the data is multiplied with the Fourier representation of the wavelets (and the inverse fourier transform is computed to get to the time domain representation again). This puts some constraints on the actual frequencies that can be returned by the algorithm. Specifically, only those frequency bins that are permitted by the inherent resolution determined by the length of the data (+potential zero-padding). Given a total length (data+zero padding) of T, which yields a frequency resolution of 1/T,  FieldTrip will return the frequencies that are closest (but not necessarily equal to) the requested frequencies in cfg.foi.

In the specification of cfg.foi it is therefore recommended to keep in mind the inherent spectral resolution of your data. For instance, you may want to consider to use zero-padding (the cfg.pad option) to pad with zeros up to an integer number of seconds in order to at least be able to capture all integer frequency bins. And note that zero padding is anyhow a good idea if the input data has trials of different length.
