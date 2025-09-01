---
title: Implement a function which computes an mvar-model based on the input data
---

{% include /shared/development/warning.md %}


1.  Define a 'mvar' datatype. The data dimord should look something like: 'rpt_chan_chan_latency_time'.
2.  The 'rpt' dimension in the previous could be jackknife based, i.e. computing model parameters on a single trials might be inaccurate.
