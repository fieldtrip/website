---
title: ft_nirs_referencechannelsubtraction
---
```
 FT_NIRS_REFERENCECHANNELSUBTRACTION performs reference channel subtraction for NIRS data

 Use as
   outdata = ft_nirs_referencechannelsubtraction(cfg, indata)
 where indata is nirs data and cfg is a configuration structure that should contain

  cfg.shortdistance = scalar, below which distance a channel is regarded
                      as short in cm (default = 1.5)
  cfg.closedistance = scalar, defines the maximal distance between a
                      shallow and a short channel in cm (default = 15).
                      NOT APPLIED CURRENTLY!
  cfg.method        = string, 'regstat2', 'QR' or 'OLS' (default = 'QR')
  cfg.verbose       = boolean, whether text output is desired (default =
                      false)

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a *.mat
 file on disk and/or the output data will be written to a *.mat file. These mat
 files should contain only a single variable, corresponding with the
 input/output structure.

 See also FT_NIRS_SCALPCOUPLINGINDEX, FT_NIRS_TRANSFORM_ODS
```
