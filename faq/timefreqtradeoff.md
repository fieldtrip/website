---
title: What is meant by time-frequency trade off?
---

# What is meant by time-frequency trade-off?

With the mtmconvol method of **[ft_freqanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_freqanalysis.m)** we compute time-resolved estimates of spectral power. As in most of the methods that achieve a time-frequency decomposition (irrespective of whether it used sliding window Fourier transforms, wavelet convolution, or Hilbert transforms) one important thing to keep in mind is that each point estimate of signal power (at a specific frequency and time point) is the result of integrating the signal over a certain time-frequency tile. In other words, each of the point estimates reflect the properties of the signal in a more or less well-defined time window, as well as in a more or less well-defined spectral band.
