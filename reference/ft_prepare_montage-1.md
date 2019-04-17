---
title: ft_prepare_montage
---
```
 FT_PREPARE_MONTAGE creates a referencing scheme based on the input configuration
 options and the channels in the data structure. The resulting montage can be
 given as input to FT_APPLY_MONTAGE, or as cfg.montage to FT_PREPROCESSING.

 Use as
   montage = ft_prepare_montage(cfg, data)

 The configuration can contain the following fields:
   cfg.refmethod     = 'avg', 'bioloar', 'comp' (default = 'avg')
   cfg.implicitref   = string with the label of the implicit reference, or empty (default = [])
   cfg.refchannel    = cell-array with new EEG reference channel(s), this can be 'all' for a common average reference

 The implicitref option allows adding the implicit reference channel to the data as
 a channel with zeros.

 See also FT_PREPROCESSING, FT_APPLY_MONTAGE
```
