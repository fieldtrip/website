---
title: ft_preproc_slidingrange
---
```
 FT_PREPROC_SLIDINGRANGE computes the range of the data in a sliding time
 window of the width specified. Width should be an odd number (since the
 window needs to be centered on an individual sample).

 Use as
   y = ft_preproc_slidingrange(dat, width, ...)

 Optional key-value pair arguments are:
   'normalize', whether to normalize the range of the data with the square
                root of the window size
```
