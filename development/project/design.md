---
title: Explain how to create cfg.design for ft_xxxstatistics
---

{% include /shared/development/warning.md %}

# Explain how to create cfg.design for ft_statistics

cfg.design as input into ft_statistics (freq, timelock, or source) should be designed as Windowssize MxN, where N is the number of trials/conditions.

M is variable length. Along with cfg.design, the other options cfg.ivar, cfg.uvar, cfg.wvar, and cfg.cvar may also need to be specified. They are an index (indices) into which row(s) of the cfg.design correspond to 'independent variables', 'units of observation', 'within-block variables' and 'control variables', respectively.

Not all are needed: see statistics_xxx_.m for what vectors it may include.

See https://www.fieldtriptoolbox.org/walkthrough#non-paired_comparison and https://www.fieldtriptoolbox.org/walkthrough#paired_comparison for examples on ivar and uvar, and https://www.fieldtriptoolbox.org/development/statistics for uvar.

Is there any explanation on the website for more on uvar and wvar? (Seems it is all on the email discussion list specific to people's questions).

## links to already existing pages with some mention of design matrix

- https://www.fieldtriptoolbox.org/walkthrough
- https://www.fieldtriptoolbox.org/getting_started/biosemi
- https://www.fieldtriptoolbox.org/tutorial/eventrelatedstatistics
- https://www.fieldtriptoolbox.org/tutorial/shared/cluster_permutation_background
- https://www.fieldtriptoolbox.org/tutorial/multivariateanalysis
- https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_freq
- https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock
- https://www.fieldtriptoolbox.org/example/source_statistics
- https://www.fieldtriptoolbox.org/example/stats_besa
- https://www.fieldtriptoolbox.org/development/statistics
- https://www.fieldtriptoolbox.org/development/multivariate

## Hierarchy of functions

(figure/diagram helpful https://www.fieldtriptoolbox.org/development/statistics)

User calls ft_xxxstatistics (freq, timelock, or source) with cfg.method=xxx as different methods for calculating probability of null hypothesis, will call function: statistics_xxx.

However, in ft_sourcestatistics, instead statistics_xxx is called, or statistics_wrapper if no method specified.

statistics_montecarlo.m (only) calls resampledesign.m

statistics_stat.m (deprecated: see https://www.fieldtriptoolbox.org/example/statistics_toolbox )
