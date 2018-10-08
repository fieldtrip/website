---
layout: default
---

##  FT_STATFUN_INDEPSAMPLEST

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_statfun_indepsamplesT".

`<html>``<pre>`
    `<a href=/reference/ft_statfun_indepsamplesT>``<font color=green>`FT_STATFUN_INDEPSAMPLEST`</font>``</a>` calculates the independent samples T-statistic on the
    biological data in dat (the dependent variable), using the information on the
    independent variable (ivar) in design.
 
    Use this function by calling one of the high-level statistics functions as
    [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)
    [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)
    [stat] = ft_sourcestatistics(cfg, source1, source2, ...)
    with the following configuration option
    cfg.statistic = 'ft_statfun_indepsamplesT'
 
    Configuration options
    cfg.computestat    = 'yes' or 'no', calculate the statistic (default='yes')
    cfg.computecritval = 'yes' or 'no', calculate the critical values of the test statistics (default='no')
    cfg.computeprob    = 'yes' or 'no', calculate the p-values (default='no')
 
    The following options are relevant if cfg.computecritval='yes' and/or
    cfg.computeprob='yes'.
    cfg.alpha = critical alpha-level of the statistical test (default=0.05)
    cfg.tail  = -1, 0, or 1, left, two-sided, or right (default=1)
                cfg.tail in combination with cfg.computecritval='yes'
                determines whether the critical value is computed at
                quantile cfg.alpha (with cfg.tail=-1), at quantiles
                cfg.alpha/2 and (1-cfg.alpha/2) (with cfg.tail=0), or at
                quantile (1-cfg.alpha) (with cfg.tail=1).
 
    Design specification
    cfg.ivar  = row number of the design that contains the labels of the conditions that must be
                compared (default=1). The labels are the numbers 1 and 2.
 
    See also `<a href=/reference/ft_timelockstatistics>``<font color=green>`FT_TIMELOCKSTATISTICS`</font>``</a>`, `<a href=/reference/ft_freqstatistics>``<font color=green>`FT_FREQSTATISTICS`</font>``</a>` or `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>`
`</pre>``</html>`

