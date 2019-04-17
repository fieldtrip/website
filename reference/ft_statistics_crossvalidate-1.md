---
title: ft_statistics_crossvalidate
---
```
 FT_STATISTICS_CROSSVALIDATE performs cross-validation using a prespecified
 multivariate analysis given by cfg.mva

 Use as
   stat = ft_timelockstatistics(cfg, data1, data2, data3, ...)
   stat = ft_freqstatistics    (cfg, data1, data2, data3, ...)
   stat = ft_sourcestatistics  (cfg, data1, data2, data3, ...)

 Options:
   cfg.mva           = a multivariate analysis (default = {dml.standardizer dml.svm})
   cfg.statistic     = a cell-array of statistics to report (default = {'accuracy' 'binomial'})
   cfg.nfolds        = number of cross-validation folds (default = 5)
   cfg.resample      = true/false; upsample less occurring classes during
                       training and downsample often occurring classes
                       during testing (default = false)

 Returns:
   stat.statistic    = the statistics to report
   stat.model        = the models associated with this multivariate analysis

 See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS, FT_SOURCESTATISTICS
```
