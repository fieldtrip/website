---
title: ft_connectivity_wpli
---
```
 FT_CONNECTIVITY_WPLI computes the weighted phase lag index from a data matrix
 containing the cross-spectral density. This implements the method described in
 Vinck M, Oostenveld R, van Wingerden M, Battaglia F, Pennartz CM. An improved index
 of phase-synchronization for electrophysiological data in the presence of
 volume-conduction, noise and sample-size bias. Neuroimage. 2011 Apr
 15;55(4):1548-65.

 Use as
   [wpi, v, n] = ft_connectivity_wpli(input, ...)

 The input data input should be organized as:
   Repetitions x Channel x Channel (x Frequency) (x Time)
 or
   Repetitions x Channelcombination (x Frequency) (x Time)

 The first dimension should contain repetitions and should not contain an
 average already. Also, it should not consist of leave one out averages.

 Additional optional input arguments come as key-value pairs:
   dojack   = 1 or 0,   compute a variance estimate, based on leave-one-out
   feedback = 'none', 'text', 'textbar' type of feedback showing progress of computation
   debias   = 1 (or true) or 0 (or false), compute debiased wpli or not

 The output wpli contains the wpli, v is a leave-one-out variance estimate
 which is only computed if dojack = 1,and n is the number of repetitions
 in the input data.

 See also FT_CONNECTIVITYANALYSIS
```
