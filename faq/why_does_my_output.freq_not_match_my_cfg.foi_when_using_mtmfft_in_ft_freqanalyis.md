---
title: Why does my output.freq not match my cfg.foi when using 'mtmfft' in ft_freqanalyis
category: faq
tags: [freq]
---

# Why does my output.freq not match my cfg.foi when using 'mtmfft' in ft_freqanalyis

The length of your time window determines the spectral resolution. If you have a time window of 1 second, you will get 1 Hz resolution, i.e. you can get estimates of power at integer multiples of 1 Hz. If you have a time window of 1.5 second, you will get a frequency resolution of 1/1.5=0.6667 Hz. That means that you can estimate power at [0.6667 1.3333 2.0000 2.6667 ...] Hz.

You can use the option cfg.pad to zero-pad the data. By making the data longer, you can increase the "virtual" resolution of the Fourier transform and get power estimates on the frequencies of interest. This is handy if your data is for example segmented in windows of 0.9 seconds: padding it to 1.0 seconds gives a more handy frequency axis.
