---
title: ft_statistics_stats
---
```
 FT_STATISTICS_STATS performs a massive univariate statistical test using the
 MATLAB statistics toolbox. This function should not be called directly,
 instead you should call the function that is associated with the type of data
 on which you want to perform the test.

 Use as
   stat = ft_timelockstatistics(cfg, data1, data2, data3, ...)
   stat = ft_freqstatistics    (cfg, data1, data2, data3, ...)
   stat = ft_sourcestatistics  (cfg, data1, data2, data3, ...)

 Where the data is obtained from FT_TIMELOCKANALYSIS, FT_FREQANALYSIS
 or FT_SOURCEANALYSIS respectively, or from FT_TIMELOCKGRANDAVERAGE,
 FT_FREQGRANDAVERAGE or FT_SOURCEGRANDAVERAGE respectively and with
 cfg.method = 'montecarlo'

  This function uses the MATLAB statistics toolbox to perform various
  statistical tests on timelock, frequency or source data. Supported
  configuration options are
   cfg.alpha     = number, critical value for rejecting the null-hypothesis (default = 0.05)
   cfg.tail      = number, -1, 1 or 0 (default = 0)
   cfg.feedback  = string, 'gui', 'text', 'textbar' or 'no' (default = 'textbar')
   cfg.method    = 'stats'
   cfg.statistic = 'ttest'          test against a mean of zero
                   'ttest2'         compare the mean in two conditions
                   'paired-ttest'
                   'anova1'
                   'kruskalwallis'
                   'signtest'
                   'signrank'
                   'pearson'
                   'kendall'
                   'spearman'

 See also TTEST, TTEST2, KRUSKALWALLIS, SIGNTEST, SIGNRANK
```
