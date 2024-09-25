---
title: 24 June 2020 - Bug in precomputed leadfields
category: news
---

### 24 June 2020

We are sorry to report that with merging the recent pull request [#1377](https://github.com/fieldtrip/fieldtrip/pull/1377) about a month ago, we introduced a bug in the FieldTrip release that might have affected your computations.

Specifically, the handling of the defaults for `cfg.reducerank` and the `cfg.backproject` changed a bit, which had an unforeseen sideeffect in `ft_prepare_leadfield`, **if** (and only if) you used this function for the computation of MEG-based leadfields, using the `singleshell` method. Specifically, `ft_prepare_leadfield` would by default compute MEG singleshell leadfields with `reducerank=2` (this is how it always has been), but it would wrongly backproject (i.e. the intended projection of the rank-reduced 2-column leadfield back into 3D space with a column for the x, y, and z dipole moment in Cartesian space) the rank-reduced leadfield. Rather, `ft_prepare_leadfield` would on [line 292](https://github.com/fieldtrip/fieldtrip/blob/af5f9822413d11e66f3821943e945e98ab766da6/ft_prepare_leadfield.m#L292) discard the last column. The error was due to MATLAB interpreting `if []` as false, causing on line 295 only the first two columns to be copied to the output. Consequently, the leadfield for the z-direction was discarded.

Are you affected? If you used the master branch from GitHub (which is the development version), or a release version between **20200529** and **20200607**, and if you have used `ft_prepare_leadfield` for MEG with singleshell models, then you are likely affected. You can check yourself: your precomputed leadfields should have three columns; if they only have two columns and you did not explicitly specify `reducerank` and `backproject` in your configuration, your leadfields are wrong. Other models than MEG singleshell are not affected.

To resolve the problem, please update to the latest **20200623** release version from the [download server](https://download.fieldtriptoolbox.org/) or from the [GitHub release page](https://github.com/fieldtrip/fieldtrip/releases) and recompute your leadfields, source estimates, etcetera.
