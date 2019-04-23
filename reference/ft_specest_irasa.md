---
title: ft_specest_irasa
---
```
 FT_SPECEST_IRASA estimates the powerspectral arrythmic component of the 
 time-domain using Irregular-Resampling Auto-Spectral Analysis. 

 Use as
   [spectrum,ntaper,freqoi] = ft_specest_irasa(dat,time...)
 where
   dat        = matrix of chan*sample
   time       = vector, containing time in seconds for each sample
   spectrum   = matrix of taper*chan*freqoi of fourier coefficients
   ntaper     = vector containing number of tapers per element of freqoi
   freqoi     = vector of frequencies in spectrum

 Optional arguments should be specified in key-value pairs and can include
   taper      = 'dpss', 'hanning' or many others, see WINDOW (default = 'hanning')
   pad        = number, total length of data after zero padding (in seconds)
   padtype    = string, indicating type of padding to be used (see ft_preproc_padding, default: zero)
   freqoi     = vector, containing frequencies of interest
   tapsmofrq  = the amount of spectral smoothing through multi-tapering. Note: 4 Hz smoothing means plus-minus 4 Hz, i.e. a 8 Hz smoothing box
   dimord     = 'tap_chan_freq' (default) or 'chan_time_freqtap' for memory efficiency (only used when variable number slepian tapers)
   polyorder  = number, the order of the polynomial to fitted to and removed from the data prior to the fourier transform (default = 0 -> remove DC-component)
   taperopt   = additional taper options to be used in the WINDOW function, see WINDOW
   verbose    = output progress to console (0 or 1, default 1)

 This implements: Wen H, Liu Z. Separating fractal and oscillatory components in the power spectrum of neurophysiological signal. Brain Topogr. 2016 Jan;29(1):13-26.

 See also FT_FREQANALYSIS, FT_SPECEST_MTMFFT, FT_SPECEST_MTMCONVOL, FT_SPECEST_TFR, FT_SPECEST_HILBERT, FT_SPECEST_WAVELET
```
