---
title: ft_specest_tfr
---
```
 FT_SPECEST_TFR performs time-frequency analysis on any time series trial data using
 the 'wavelet method' based on Morlet wavelets, doing convolution in the time
 domain.

 Use as
   [spectrum,freqoi,timeoi] = ft_specest_convol(dat,time,...)
 where
   dat       = matrix of chan*sample
   time      = vector, containing time in seconds for each sample
   spectrum  = array of chan*freqoi*timeoi of fourier coefficients
   freqoi    = vector of frequencies in spectrum
   timeoi    = vector of timebins in spectrum

 Optional arguments should be specified in key-value pairs and can include
   timeoi    = vector, containing time points of interest (in seconds, analysis window will be centered around these time points)
   freqoi    = vector, containing frequencies (in Hz)
   width     = number or vector, width of the wavelet, determines the temporal and spectral resolution (default = 7)
   gwidth    = number, determines the length of the used wavelets in standard deviations of the implicit Gaussian kernel
   verbose   = output progress to console (0 or 1, default 1)
   polyorder = number, the order of the polynomial to fitted to and removed from the data prior to the fourier transform (default = 0 -> remove DC-component)

 See also FT_FREQANALYSIS, FT_SPECEST_MTMFFT, FT_SPECEST_MTMCONVOL, FT_SPECEST_HILBERT, FT_SPECEST_NANFFT, FT_SPECEST_WAVELET
```
