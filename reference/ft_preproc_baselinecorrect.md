---
title: ft_preproc_baselinecorrect
---
```
 FT_PREPROC_BASELINECORRECT performs a baseline correction, e.g. using the
 prestimulus interval of the data or using the complete data

 Use as
   [dat] = ft_preproc_baselinecorrect(dat, begin, end)
 where
   dat        data matrix (Nchans X Ntime)
   begsample  index of the begin sample for the baseline estimate
   endsample  index of the end sample for the baseline estimate

 If no begin and end sample are specified for the baseline estimate, it
 will be estimated on the complete data.

 See also FT_PREPROC_DETREND, FT_PREPROC_POLYREMOVAL
```
