---
title: ft_crossfrequencyanalysis
---
```
 FT_CROSSFREQUENCYANALYSIS performs cross-frequency analysis

 Use as
   crossfreq = ft_crossfrequencyanalysis(cfg, freq)
   crossfreq = ft_crossfrequencyanalysis(cfg, freqlo, freqhi)

 The input data should be organised in a structure as obtained from the
 FT_FREQANALYSIS function. The configuration should be according to

   cfg.freqlow    = scalar or vector, selection of frequencies for the low frequency data
   cfg.freqhigh   = scalar or vector, selection of frequencies for the high frequency data
   cfg.channel    = cell-array with selection of channels, see FT_CHANNELSELECTION
   cfg.method     = string, can be
                     'coh' - coherence
                     'plv' - phase locking value
                     'mvl' - mean vector length
                     'mi'  - modulation index
   cfg.keeptrials = string, can be 'yes' or 'no'

 Various metrics for cross-frequency coupling have been introduced in a number of
 scientific publications, but these do not use a sonsistent method naming scheme,
 nor implement it in exactly the same way. The particular implementation in this
 code tries to follow the most common format, generalizing where possible. If you
 want details about the algorithms, please look into the code.

 The modulation index implements
   Tort A. B. L., Komorowski R., Eichenbaum H., Kopell N. (2010). Measuring Phase-Amplitude
   Coupling Between Neuronal Oscillations of Different Frequencies. J Neurophysiol 104:
   1195?1210. doi:10.1152/jn.00106.2010

 See also FT_FREQANALYSIS, FT_CONNECTIVITYANALYSIS
```
