---
title: ft_nirs_prepare_ODtransformation
---
```
 FT_NIRS_PREPARE_ODTRANSFORMATION returns the transformation matrix from
 optical densities (OD) to chromophore concentrations such as (de-)
 oxygenated hemoglobin.

 Use as
   [montage] = ft_prepare_ODtransformation(cfg, data)

 It is neccessary to input the data on which you want to perform the
 inverse computations, since that data generally contain the optode
 information and information about the channels that should be included in
 the transformation. The data structure can be either obtained
 from FT_PREPROCESSING, FT_FREQANALYSIS, FT_TIMELOCKANALYSIS or
 FT_COMPONENTANALYSIS. If the data is empty, all channels will be included
 in transformation.

 The configuration should contain
  cfg.channel            = Nx1 cell-array with selection of channels
                           (default = 'nirs'), see FT_CHANNELSELECTION for
                           more details

 Optional configuration settings are
  cfg.age                = scalar, age of the subject (necessary to
                           automatically select the appropriate DPF, or
  cfg.dpf                = scalar, differential path length factor
  cfg.dpffile            = string, location to a lookup table for the
                           relation between participant age and DPF

 Note that the DPF might be different across channels, and is usually
 contained in the optode structure contained in the data.

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
 If you specify this option the input data will be read from a *.mat
 file on disk. This mat files should contain only a single variable named 'data',
 corresponding to the input structure.

 See also FT_NIRS_TRANSFORM_ODS, FT_APPLY_MONTAGE
```
