---
layout: default
---

##  FT_STATISTICS_CROSSVALIDATE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_statistics_crossvalidate".

`<html>``<pre>`
    `<a href=/reference/ft_statistics_crossvalidate>``<font color=green>`FT_STATISTICS_CROSSVALIDATE`</font>``</a>` performs cross-validation using a prespecified
    multivariate analysis given by cfg.mva
 
    Use as
    stat = ft_timelockstatistics(cfg, data1, data2, data3, ...)
    stat = ft_freqstatistics    (cfg, data1, data2, data3, ...)
    stat = ft_sourcestatistics  (cfg, data1, data2, data3, ...)
 
    Option
    cfg.mva           = a multivariate analysis (default = {dml.standardizer dml.svm})
    cfg.statistic     = a cell-array of statistics to report (default = {'accuracy' 'binomial'})
    cfg.nfolds        = number of cross-validation folds (default = 5)
    cfg.resample      = true/false; upsample less occurring classes during
                        training and downsample often occurring classes
                        during testing (default = false)
 
    Return
    stat.statistic    = the statistics to report
    stat.model        = the models associated with this multivariate analysis
 
    See also `<a href=/reference/ft_timelockstatistics>``<font color=green>`FT_TIMELOCKSTATISTICS`</font>``</a>`, `<a href=/reference/ft_freqstatistics>``<font color=green>`FT_FREQSTATISTICS`</font>``</a>`, `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>`
`</pre>``</html>`

