---
title: ft_specest_hilbert
---
```
 FT_SPECEST_HILBERT performs a spectral estimation of data by repeatedly applying a
 bandpass filter and then doing a Hilbert transform.

 Use as
   [spectrum,freqoi,timeoi] = ft_specest_hilbert(dat,time,...)
 where
   dat       = matrix of chan*sample
   time      = vector, containing time in seconds for each sample
   spectrum  = matrix of chan*freqoi*timeoi of fourier coefficients
   freqoi    = vector of frequencies in spectrum
   timeoi    = vector of timebins in spectrum

 Optional arguments should be specified in key-value pairs and can include
   timeoi     = vector, containing time points of interest (in seconds)
   freqoi     = vector, containing frequencies (in Hz)
   pad        = number, indicating time-length of data to be padded out to in seconds (split over pre/post; used for spectral interpolation, NOT filtering)
   padtype    = string, indicating type of padding to be used (see ft_preproc_padding, default: zero)
   width      = number or vector, width of band-pass surrounding each element of freqoi
   filttype   = string, filter type, 'but', 'firws', 'fir', 'firls'
   filtorder  = number or vector, filter order
   filtdir    = string, filter direction, 'onepass', 'onepass-reverse', 'twopass', 'twopass-reverse', 'twopass-average', 'onepass-zerophase', 'onepass-reverse-zerophase', 'onepass-minphase'
   verbose    = output progress to console (0 or 1, default 1)
   polyorder  = number, the order of the polynomial to fitted to and removed from the data prior to the fourier transform (default = 0 -> remove DC-component)
   edgeartnan = 0 (default) or 1, replace edge artifacts due to filtering with NaNs (only applicable for filttype = 'fir'/'firls'/'firws')

 See also FT_FREQANALYSIS, FT_SPECEST_MTMFFT, FT_SPECEST_TFR, FT_SPECEST_MTMCONVOL, FT_SPECEST_WAVELET
```
