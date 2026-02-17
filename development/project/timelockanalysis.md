---
title: Reimplement the avg/cov/trial handling
---

{% include /shared/development/warning.md %}

    cfg.output     = trial, cov
    cfg.keeptrials = yes, no

    timelock.avgtrial = Nchan X Ntime
    timelock.avgcov   = Nchan X Nchan
    timelock.trial    = Nrpt X Nchan X Ntime
    timelock.cov      = Nrpt X Nchan X Nchan

compute average over the single-trial covariance

compute the covariance of the average
