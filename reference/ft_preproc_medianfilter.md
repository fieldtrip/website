---
title: ft_preproc_medianfilter
---
```
 FT_PREPROC_MEDIANFILTER applies a median filter, which smooths the data with a
 boxcar-like kernel, except that it keeps steps in the data. This function requires
 the MATLAB Signal Processing toolbox.

 Use as
   [dat] = ft_preproc_medianfilter(dat, order)
 where
   dat        data matrix (Nchans X Ntime)
   order      number, the length of the median filter kernel (default = 25)

 See also PREPROC
```
