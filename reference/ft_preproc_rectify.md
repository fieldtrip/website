---
title: ft_preproc_rectify
---
```plaintext
 FT_PREPROC_RECTIFY rectifies the data, i.e. converts all samples with a
 negative value into the similar magnitude positive value

 Use as
   [dat] = ft_preproc_rectify(dat)
 where
   dat        data matrix (Nchans X Ntime)

 If the data contains NaNs, these are ignored for the computation, but
 retained in the output.

 See also PREPROC
```
