---
title: ft_statfun_roc
---
```
 FT_STATFUN_ROC computes the area under the curve (AUC) of the Receiver Operator
 Characteristic (ROC). This is a measure of the separability of the data divided
 over two conditions. The AUC can be used to test statistical significance of being
 able to predict on a single observation basis to which condition the observation
 belongs.
 
 Use this function by calling one of the high-level statistics functions as
   [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)
   [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)
   [stat] = ft_sourcestatistics(cfg, source1, source2, ...)
 with the following configuration option
   cfg.statistic    = 'ft_statfun_roc'

 Configuration options that are relevant for this function are
   cfg.ivar         = number, index into the design matrix with the independent variable
   cfg.logtransform = 'yes' or 'no' (default = 'no')
 
 Note that this statfun performs a one sided test in which condition "1"
 is assumed to be larger than condition "2".
```
