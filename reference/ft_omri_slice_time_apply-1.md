---
title: ft_omri_slice_time_apply
---
```
 function [STM, Xs] = ft_omri_slice_time_apply(STM, X)

 Put new scan X through slice time correction, by linear interpolation
 with last scan. The return value Xs is the signal sampled at deltaT = 0
 relative to the most recent scan.
```
