---
title: ft_statfun_diff_itc
---
```
 FT_STATFUN_DIFF_ITC computes the difference in the inter-trial coherence between
 two conditions. The input data for this test should consist of complex-values
 spectral estimates, e.g. computed using FT_FREQANALYSIS with method=mtmfft, wavelet
 or mtmconvcol.

 The ITC is a measure of phase consistency over trials. By randomlly shuffling the
 trials  between the two consitions and repeatedly computing the ITC difference, you
 can test the significance of the two conditions having a different ITC.

 A difference in the number of trials poer condition will affect the ITC, however
 since the number of trials remains the same for each random permutation, this bias
 is reflected in the randomization distribution.

 Use this function by calling the high-level statistic functions as
   [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)
 with the following configuration options
   cfg.method    = 'montecarlo'
   cfg.statistic = 'diff_itc'
 and optionally the options
  cfg.complex    = 'diffabs' to compute the difference of the absolute ITC values (default), or
                   'absdiff' to compute the absolute value of the difference in the complex ITC values.
 
 For this specific statistic there is no known parametric distribution, hence the
 probability and critical value cannot be computed. This specific statistic can
 therefore only be used with cfg.method='montecarlo'. If you want to do this in
 combination with cfg.correctm='cluster', you also need either
 cfg.clusterthreshold='nonparametric_common' or 'nonparametric_individual'.

 See FT_FREQSTATISTICS and FT_STATISTICS_MONTECARLO for more details
```
