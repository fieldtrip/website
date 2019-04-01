---
title: ft_statfun_depsamplesregrT
---
```
 FT_STATFUN_DEPSAMPLESREGRT calculates dependent samples regression T-statistic on
 the biological data in dat (the dependent variable), using the information on the
 independent variable (ivar) in design.

 Use this function by calling one of the high-level statistics functions as
   [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)
   [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)
   [stat] = ft_sourcestatistics(cfg, source1, source2, ...)
 with the following configuration option
   cfg.statistic = 'ft_statfun_depsamplesregrT'

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
   cfg.ivar  = row number of the design that contains the independent variable.
   cfg.uvar  = row number of design that contains the labels of the units-of-observation (subjects or trials)
               (default=2). The labels are assumed to be integers ranging from 1 to
               the number of units-of-observation.

 See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS
```
