---
title: enginecellfun
---
```
 ENGINECELLFUN applies a function to each element of a cell-array. The function
 execution is done in parallel on locally or remotely running MATLAB engines.

 Use as
   argout = enginecellfun(fname, x1, x2, ...)

 Optional arguments can be specified in key-value pairs and can include
   UniformOutput  = boolean (default = false)
   StopOnError    = boolean (default = true)
   diary          = string, can be 'always', 'never', 'warning', 'error' (default = 'error')
   order          = string, can be 'random' or 'original' (default = 'random')

  Example
    x1 = {1, 2, 3, 4, 5};
    x2 = {2, 2, 2, 2, 2};
    enginepool open 4
    y  = enginecellfun(@power, x1, x2);
    enginepool close

 See also ENGINEPOOL, ENGINEFEVAL, ENGINEGET
```
