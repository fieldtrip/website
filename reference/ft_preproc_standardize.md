---
title: ft_preproc_standardize
---
```
 FT_PREPROC_STANDARDIZE performs a z-transformation or standardization
 of the data. The standardized data will have a zero-mean and a unit
 standard deviation.

 Use as
   [dat] = ft_preproc_standardize(dat, begsample, endsample)
 where
   dat        data matrix (Nchans dat Ntime)
   begsample  index of the begin sample for the mean and stdev estimate
   endsample  index of the end sample for the mean and stdev estimate

 If no begin and end sample are specified, it will be estimated on the
 complete data.

 See also PREPROC
```
