---
title: Cross-frequency analysis
category: example
tags: [freq]
redirect_from:
    - /example/crossfreq/
---

# Cross-frequency analysis

There are several ways in which cross-frequency interactions might occur. In [Jensen and Colgin TICS 2007](https://doi.org/10.1016/j.tics.2007.05.003) different principles of cross-frequency interactions are shown in Figure 1.

{% include image src="/assets/img/example/crossfreq/jensencolgin.png" width="700" %}

With the **[ft_freqsimulation](/reference/ft_freqsimulation)** function you can generate simulated data in FieldTrip format which the different types of cross-frequency interactions. The different methods are:

- [phalow_amphigh (is phase to power in Jensen and Colgin)](/example/spectral/crossfreq/phalow_amphigh)
- [amplow_amphigh (is power to power in Jensen and Colgin](/example/spectral/crossfreq/amplow_amphigh)
- [phalow_freqhigh (is phase to frequency in Jensen and Colgin)](/example/spectral/crossfreq/phalow_freqhigh)
