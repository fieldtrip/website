---
layout: default
---

##  FT_STATISTICS_ANALYTIC

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_statistics_analytic".

`<html>``<pre>`
    `<a href=/reference/ft_statistics_analytic>``<font color=green>`FT_STATISTICS_ANALYTIC`</font>``</a>` performs a parametric statistical test on the
    data, based on a known (i.e. analytic) distribution of the test
    statistic. This function should not be called directly, instead
    you should call the function that is associated with the type of
    data on which you want to perform the test.
 
    Use as
    stat = ft_timelockstatistics(cfg, data1, data2, data3, ...)
    stat = ft_freqstatistics    (cfg, data1, data2, data3, ...)
    stat = ft_sourcestatistics  (cfg, data1, data2, data3, ...)
    where the data is obtained from `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`, `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`
    or `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>` respectively, or from `<a href=/reference/ft_timelockgrandaverage>``<font color=green>`FT_TIMELOCKGRANDAVERAGE`</font>``</a>`,
    `<a href=/reference/ft_freqgrandaverage>``<font color=green>`FT_FREQGRANDAVERAGE`</font>``</a>` or `<a href=/reference/ft_sourcegrandaverage>``<font color=green>`FT_SOURCEGRANDAVERAGE`</font>``</a>` respectively.
 
    The configuration can contain
    cfg.statistic        = string, statistic to compute for each sample or voxel (see below)
    cfg.correctm         = string, apply multiple-comparison correction, 'no', 'bonferroni', 'holm', 'hochberg', 'fdr' (default = 'no')
    cfg.alpha            = number, critical value for rejecting the null-hypothesis (default = 0.05)
    cfg.tail             = number, -1, 1 or 0 (default = 0)
    cfg.ivar             = number or list with indices, independent variable(s)
    cfg.uvar             = number or list with indices, unit variable(s)
    cfg.wvar             = number or list with indices, within-block variable(s)
 
    The parametric statistic that is computed for each sample (and for
    which the analytic probability of the null-hypothesis is computed) is
    specified as
    cfg.statistic       = 'indepsamplesT'           independent samples T-statistic,
                          'indepsamplesF'           independent samples F-statistic,
                          'indepsamplesregrT'       independent samples regression coefficient T-statistic,
                          'indepsamplesZcoh'        independent samples Z-statistic for coherence,
                          'depsamplesT'             dependent samples T-statistic,
                          'depsamplesFmultivariate' dependent samples F-statistic MANOVA,
                          'depsamplesregrT'         dependent samples regression coefficient T-statistic,
                          'actvsblT'                activation versus baseline T-statistic.
    or you can specify your own low-level statistical function.
 
    See also `<a href=/reference/ft_timelockstatistics>``<font color=green>`FT_TIMELOCKSTATISTICS`</font>``</a>`, `<a href=/reference/ft_freqstatistics>``<font color=green>`FT_FREQSTATISTICS`</font>``</a>`, `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>`
`</pre>``</html>`

