---
layout: default
---

##  FT_STATISTICS_STATS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_statistics_stats".

`<html>``<pre>`
    `<a href=/reference/ft_statistics_stats>``<font color=green>`FT_STATISTICS_STATS`</font>``</a>` performs a massive univariate statistical test using the
    MATLAB statistics toolbox. This function should not be called directly,
    instead you should call the function that is associated with the type of data
    on which you want to perform the test.
 
    Use as
    stat = ft_timelockstatistics(cfg, data1, data2, data3, ...)
    stat = ft_freqstatistics    (cfg, data1, data2, data3, ...)
    stat = ft_sourcestatistics  (cfg, data1, data2, data3, ...)
 
    Where the data is obtained from `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`, `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`
    or `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>` respectively, or from `<a href=/reference/ft_timelockgrandaverage>``<font color=green>`FT_TIMELOCKGRANDAVERAGE`</font>``</a>`,
    `<a href=/reference/ft_freqgrandaverage>``<font color=green>`FT_FREQGRANDAVERAGE`</font>``</a>` or `<a href=/reference/ft_sourcegrandaverage>``<font color=green>`FT_SOURCEGRANDAVERAGE`</font>``</a>` respectively and with
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
`</pre>``</html>`

