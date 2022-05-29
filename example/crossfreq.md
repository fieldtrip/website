---
title: Cross-frequency analysis
tags: [example, freq]
---

# Cross-frequency analysis

There are several ways in which cross-frequency interactions might occur. In [Jensen and Colgin TICS 2007]https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(07)00127-1?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS1364661307001271%3Fshowall%3Dtrue) different principles of cross-frequency interactions are shown in Figure 1.

{% include image src="/assets/img/example/crossfreq/jensencolgin.png" width="700" %}

With the **[ft_freqsimulation](/reference/ft_freqsimulation)** function you can generate simulated data in FieldTrip format which the different types of cross-frequency interactions. The different methods are:

- [phalow_amphigh (is phase to power in Jensen and Colgin)](/example/crossfreq/phalow_amphigh)
- [amplow_amphigh (is power to power in Jensen and Colgin](/example/crossfreq/amplow_amphigh)
- [phalow_freqhigh (is phase to frequency in Jensen and Colgin)](/example/crossfreq/phalow_freqhigh)
