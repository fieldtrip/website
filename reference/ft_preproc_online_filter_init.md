---
title: ft_preproc_online_filter_init
---
```
 function FM = ft_preproc_online_filter_init(B, A, x)

 Initialize an IIR filter model with coefficients B and A, as used in filter and butter etc.
 One sample x of the signal must be given as a column vector.

 This function will calculate the filter delay states such that the initial response
 is as if 'x' would have been applied since forever.

 See also FT_PREPROC_ONLINE_FILTER_APPLY
```
