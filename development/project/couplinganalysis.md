---
title: Implement a function which computes a variety of bivariate coupling measures from the input data
---

{% include /shared/development/warning.md %}



The goal is to create a multi-purpose function which takes raw/timelock/freq/source/mvar data as an input and computes coupling measures such as

1.  coherence
2.  coherency
3.  correlation
4.  any of the previous partial or multiple or canonical
5.  cross-correlation
6.  granger causality
7.  partial directed coherence
8.  directed transfer function
9.  amplitude correlation
10. cross-frequency interactions

Furthermore create a simulator for

1.  dipolesimulation
2.  freqsimulation
3.  connectivitysimulation

Status: the connectivityanalysis and connectivitysimulation function have been implemented.
