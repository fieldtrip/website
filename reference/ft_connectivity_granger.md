---
title: ft_connectivity_granger
---
```
 FT_CONNECTIVITY_GRANGER computes spectrally resolved granger causality. This
 implementation is loosely based on the code used in Brovelli, et. al., PNAS 101,
 9849-9854 (2004).

 Use as
   [GRANGER, V, N] = FT_CONNECTIVITY_GRANGER(H, Z, S, ...)

 The input data should be
   H = spectral transfer matrix, Nrpt x Nchan x Nchan x Nfreq (x Ntime),
       or Nrpt x Nchancmb x Nfreq (x Ntime). Nrpt can be 1.
   Z = the covariance matrix of the noise, Nrpt x Nchan x Nchan (x Ntime),
       or Nrpt x Nchancmb (x Ntime).
   S = the cross-spectral density matrix with the same dimensionality as H.

 Additional optional input arguments come as key-value pairs:
   'dimord'  = required string specifying how to interpret the input data
               supported values are 'rpt_chan_chan_freq(_time) and
               'rpt_chan_freq(_time), 'rpt_pos_pos_XXX' and 'rpt_pos_XXX'
   'method'  = 'granger' (default), or 'instantaneous', or 'total'.
   'hasjack' = 0 (default) is a boolean specifying whether the input
               contains leave-one-outs, required for correct variance
               estimate
   'powindx' = is a variable determining the exact computation, see below

 If the inputdata is such that the channel-pairs are linearly indexed, granger
 causality is computed per quadruplet of consecutive entries, where the convention
 is as follows:

  H(:, (k-1)*4 + 1, :, :, :) -> 'chan1-chan1'
  H(:, (k-1)*4 + 2, :, :, :) -> 'chan1->chan2'
  H(:, (k-1)*4 + 3, :, :, :) -> 'chan2->chan1'
  H(:, (k-1)*4 + 4, :, :, :) -> 'chan2->chan2'

 The same holds for the Z and S matrices.

 Pairwise block-granger causality can be computed when the inputdata has
 dimensionality Nchan x Nchan. In that case powindx should be specified, as a 1x2
 cell-array indexing the individual channels that go into each 'block'.

 See also FT_CONNECTIVITYANALYSIS
```
