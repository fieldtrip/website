---
title: ft_read_headmodel
---
```
 FT_READ_HEADMODEL reads a volume conduction model from various manufacturer
 specific files. Currently supported are ASA, CTF, Neuromag, MBFYS
 and Matlab.

 Use as
   headmodel = ft_read_headmodel(filename, ...)

 Additional options should be specified in key-value pairs and can be
   'fileformat'   string

 The volume conduction model is represented as a structure with fields
 that depend on the type of model.

 See also FT_DATATYPE_HEADMODEL, FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD
```
