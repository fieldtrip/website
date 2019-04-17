---
title: ft_statfun_mean
---
```
 FT_STATFUN_MEAN computes the mean over all replications for each of the
 observations (i.e. channel-time-frequency points or voxels).

 This function does not depend on the experimental design and cannot be used for any
 statistical testing. However, it serves as example how you can use the statistical
 framework in FieldTrip to perform a simple (or more complex) task, without having
 to worry about the representation of the data. The output of FT_TIMELOCKSTATISTICS,
 FT_FREQSTATISTICS or FT_SOURCESTATISTICS will be an appropriate structure, that
 contains the result of the computation inside this function in the stat field.

 See also FT_STATFUN_DIFF for another example statfun
```
