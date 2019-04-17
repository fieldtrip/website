---
title: ft_timelockgrandaverage
---
```
 FT_TIMELOCKGRANDAVERAGE computes ERF/ERP average and variance
 over multiple subjects or over blocks within one subject

 Use as
   [grandavg] = ft_timelockgrandaverage(cfg, avg1, avg2, avg3, ...)

 where
   avg1..N are the ERF/ERP averages as obtained from FT_TIMELOCKANALYSIS

 and cfg is a configuration structure with
  cfg.channel        = Nx1 cell-array with selection of channels (default = 'all'),
                       see FT_CHANNELSELECTION for details
  cfg.latency        = [begin end] in seconds or 'all' (default = 'all')
  cfg.keepindividual = 'yes' or 'no' (default = 'no')
  cfg.normalizevar   = 'N' or 'N-1' (default = 'N-1')
  cfg.method         = 'across' (default) or 'within', see below.
  cfg.parameter      = string or cell-array indicating which
                        parameter to average. default is set to
                        'avg', if it is present in the data.

 If cfg.method = 'across', a plain average is performed, i.e. the
 requested parameter in each input argument is weighted equally in the
 average. This is useful when averaging across subjects. The
 variance-field will contain the variance across the parameter of
 interest, and the dof-field will contain the number of input arguments.

 If cfg.method = 'within', a weighted average is performed, i.e. the
 requested parameter in each input argument is weighted according to the
 dof-field. This is useful when averaging across blocks within subjects.
 The variance-field will contain the variance across all input
 observations, and the dof-field will contain the number of observations.

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a *.mat
 file on disk and/or the output data will be written to a *.mat file. These mat
 files should contain only a single variable, corresponding with the
 input/output structure. For this particular function, the input should be
 structured as a cell-array.

 See also FT_TIMELOCKANALYSIS, FT_TIMELOCKSTATISTICS, FT_TIMELOCKBASELINE
```
