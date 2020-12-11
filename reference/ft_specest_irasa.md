---
title: ft_specest_irasa
---
```plaintext
 FT_SPECEST_IRASA separates fractal components from the orginal
 power spectrum using Irregular-Resampling Auto-Spectral Analysis (IRASA)

 Use as
   [spectrum,ntaper,freqoi] = ft_specest_irasa(dat,time...)
 where
   dat        = matrix of chan*sample
   time       = vector, containing time in seconds for each sample
   spectrum   = matrix of taper*chan*freqoi of fourier coefficients
   ntaper     = vector containing number of tapers per element of freqoi
   freqoi     = vector of frequencies in spectrum

 Optional arguments should be specified in key-value pairs and can include
   pad        = number, total length of data after zero padding (in seconds)
   padtype    = string, indicating type of padding to be used (see ft_preproc_padding, default: zero)
   freqoi     = vector, containing frequencies of interest
   polyorder  = number, the order of the polynomial to fitted to and removed from the data prior to the fourier transform (default = 0 -> remove DC-component)
   verbose    = boolean, output progress to console (0 or 1, default 1)
   output     = string, indicating type of output('fractal' or 'orignal', default 'fractal')

 This implements: Wen.H. & Liu.Z.(2016), Separating fractal and oscillatory components in the power 
 spectrum of neurophysiological signal. Brain Topogr. 29(1):13-26. The source code accompanying the 
 original paper is avaible from https://purr.purdue.edu/publications/1987/1

 For more information about the current version(2020) and application, see https://www.fieldtriptoolbox.org/example/irasa/
 
 See also FT_FREQANALYSIS, FT_SPECEST_MTMFFT, FT_SPECEST_MTMCONVOL, FT_SPECEST_TFR, FT_SPECEST_HILBERT, FT_SPECEST_WAVELET
```
