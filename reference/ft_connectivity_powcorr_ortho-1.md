---
title: ft_connectivity_powcorr_ortho
---
```
 FT_CONNECTIVITY_POWCORR_ORTHO computes power correlation after removing the
 zero-lag contribution on a trial-by-trial basis. This implements the method
 described in JF Hipp, DJ Hawellek, M Corbetta, M Siegel, AK Engel. Large-scale
 cortical correlation structure of spontaneous oscillatory activity. Nature
 neuroscience 15 (6), 884-890.

 Use as
   c = ft_connectivity_powcorr(mom, ...)

 The input argument mom should be a NchanxNrpt matrix containing the complex-valued
 amplitude and phase information at a given frequency, and the optional key refindx
 specifies the

 Additional optional input arguments come as key-value pairs:
   refindx   = index/indices of the channels that serve as a reference channel (default is all)

 The output c is a NchanxNrefchan matrix that contain the power correlation
 for all channels orthogonalised relative to the reference channel in the first
 Nrefchan columns, and the power correlation for the reference channels
 orthogonalised relative to the channels in the second Nrefchan columns.

 See also FT_CONNECTIVITYANALYSIS
```
