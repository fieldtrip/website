---
title: ft_nirs_transform_ODs
---
```
 FT_NIRS_TRANSFORM_ODs computes the transformation from optical densities (OD)
 to chromophore concentrations such as (de-)oxygenated  hemoglobin, or the
 other way around.

 Use as either
   [data]      = ft_nirs_transform_ODs(cfg, data)
   [freq]      = ft_nirs_transform_ODs(cfg, freq)
   [timelock]  = ft_nirs_transform_ODs(cfg, timelock)
   [component] = ft_nirs_transform_ODs(cfg, component)

  The configuration "cfg" is a structure containing information about
  target of the transformation. The configuration should contain
  cfg.channel            = Nx1 cell-array with selection of channels
                           (default = 'nirs'), see FT_CHANNELSELECTION for
                           more details
  cfg.target             = Mx1 cell-array, can be 'O2Hb' (oxygenated hemo-
                           globin), 'HHb' de-oxygenated hemoglobin') or
                           'tHb' (total hemoglobin), or a combination of
                           those (default: {'O2Hb', 'HHb'})

 Optional configuration settings are
  cfg.age                = scalar, age of the subject (necessary to
                           automatically select the appropriate DPF, or
  cfg.dpf                = scalar, differential path length factor
  cfg.dpffile            = string, location to a lookup table for the
                           relation between participant age and DPF

 Note that the DPF might be different across channels, and is usually
 stored in the optode structure contained in the data.

 The function returns data transformed to the specified chromophore
 concentrations of the the requested

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
 If you specify this option the input data will be read from a *.mat
 file on disk. This mat files should contain only a single variable named 'data',
 corresponding to the input structure.

 See also FT_NIRS_PREPARE_ODTRANSFORMATION, FT_APPLY_MONTAGE
```
