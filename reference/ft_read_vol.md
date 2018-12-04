---
title: ft_read_vol
layout: default
tags: 
---
```
 FT_READ_VOL reads a volume conduction model from various manufacturer
 specific files. Currently supported are ASA, CTF, Neuromag, MBFYS
 and Matlab.

 Use as
   headmodel = ft_read_vol(filename, ...)

 Additional options should be specified in key-value pairs and can be
   'fileformat'   string

 The volume conduction model is represented as a structure with fields
 that depend on the type of model.

 See also FT_TRANSFORM_VOL, FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD
```
