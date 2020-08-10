---
title: ft_laggedcoherence
---
```plaintext
 FT_LAGGEDCOHERENCE calculates the lagged coherence for a set of
 channels pairs, a number of frequencies, and a number of lags. The channel
 pairs are the complete set of pairs that can be formed from the channels
 in datain, including the auto-pairs (one channel for which the lagged
 coherence is calculated at different lags).

 Use as
   outdata = ft_laggedcoherence(cfg, indata)
 where cfg is a configuration structure (see below) and indata is the
 output of FT_PREPROCESSING.

 The configuration structure should contain
   cfg.foi       = vector 1 x numfoi, frequencies of interest
   cfg.loi       = vector 1 x numloi, lags of interest, this must be a vector of
                   integers with starting value 0 or higher
   cfg.numcycles = integer, number of cycles of the Fourier basis functions that
                   are used to calculate the Fourier coefficients that are the
                   basis for calculating lagged coherence


 When using the results of this function in a publication, please cite:
   Fransen, A. M., van Ede, F., & Maris, E. (2015). Identifying neuronal
   oscillations using rhythmicity. Neuroimage, 118, 256-267.

 See also FT_PREPROCESSING, FT_FREQANALYSIS, FT_CONNECTIVITYANALYSIS
```
