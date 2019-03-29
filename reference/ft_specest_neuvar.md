---
title: ft_specest_neuvar
---
```
 FT_SPECEST_NEUVAR computes a time-domain estimation of overall signal 
 power, having compensated for the 1/f distribution of spectral content.

 Use as
   [spectrum,ntaper,freqoi] = ft_specest_neuvar(dat,time...)
 where
   dat        = matrix of chan*sample
   time       = vector, containing time in seconds for each sample
   neuvar     = matrix of chan*neuvar

 Optional arguments should be specified in key-value pairs and can include
   order      = number, the order of differentation for compensating for the 1/f (default: 1)
   pad        = number, total length of data after zero padding (in seconds)
   padtype    = string, indicating type of padding to be used (see ft_preproc_padding, default: 0)
   verbose    = output progress to console (0 or 1, default 1)

 See also FT_FREQANALYSIS, FT_SPECEST_MTMFFT, FT_SPECEST_MTMCONVOL, FT_SPECEST_TFR, FT_SPECEST_HILBERT, FT_SPECEST_WAVELET
```
