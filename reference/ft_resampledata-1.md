---
title: ft_resampledata
---
```
 FT_RESAMPLEDATA performs a resampling or downsampling of the data

 Use as
   [data] = ft_resampledata(cfg, data)

 The data should be organised in a structure as obtained from
 the FT_PREPROCESSING function. The configuration should contain
   cfg.resamplefs      = frequency at which the data will be resampled (default = 256 Hz)
   cfg.detrend         = 'no' or 'yes', detrend the data prior to resampling (no default specified, see below)
   cfg.demean          = 'no' or 'yes', whether to apply baseline correction (default = 'no')
   cfg.baselinewindow  = [begin end] in seconds, the default is the complete trial (default = 'all')
   cfg.feedback        = 'no', 'text', 'textbar', 'gui' (default = 'text')
   cfg.trials          = 'all' or a selection given as a 1xN vector (default = 'all')
   cfg.sampleindex     = 'no' or 'yes', add a channel with the original sample indices (default = 'no')

 Instead of specifying cfg.resamplefs, you can also specify a time axis on
 which you want the data to be resampled. This is usefull for merging data
 from two acquisition devides, after resampledata you can call FT_APPENDDATA
 to concatenate the channles from the different acquisition devices.
   cfg.time        = cell-array with one time axis per trial (i.e. from another dataset)
   cfg.method      = interpolation method, see INTERP1 (default = 'pchip')

 Previously this function used to detrend the data by default. The
 motivation for this is that the data is filtered prior to resampling
 to avoid aliassing and detrending prevents occasional edge artifacts
 of the filters. Detrending is fine for removing slow drifts in data
 priot to frequency analysis, but detrending is not good if you
 subsequenlty want to look at the evoked fields. Therefore the old
 default value 'yes' has been removed. You now explicitely have to
 specify whether you want to detrend (probably so if you want to
 keep your analysis compatible with previous analyses that you did),
 or if you do not want to detrent (recommended in most cases).
 If you observe edge artifacts after detrending, it is recommended
 to apply a baseline correction to the data.

 The following fields in the structure 'data' are modified by this function
   data.fsample
   data.trial
   data.time

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a *.mat
 file on disk and/or the output data will be written to a *.mat file. These mat
 files should contain only a single variable, corresponding with the
 input/output structure.

 See also FT_PREPROCESSING, RESAMPLE, DOWNSAMPLE, INTERP1
```
