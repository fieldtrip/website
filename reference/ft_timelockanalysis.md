---
title: ft_timelockanalysis
---
```
 FT_TIMELOCKANALYSIS computes the timelocked average ERP/ERF and
 optionally computes the covariance matrix. 

 Use as
   [timelock] = ft_timelockanalysis(cfg, data)

 The data should be organised in a structure as obtained from the
 FT_PREPROCESSING function. The configuration should be according to

   cfg.channel            = Nx1 cell-array with selection of channels (default = 'all'),
                            see FT_CHANNELSELECTION for details
   cfg.trials             = 'all' or a selection given as a 1xN vector (default = 'all')
   cfg.latency            = [begin end] in seconds, or 'all', 'minperiod', 'maxperiod',
                            'prestim', 'poststim' (default = 'all')
   cfg.covariance         = 'no' or 'yes' (default = 'no')
   cfg.covariancewindow   = [begin end] in seconds, or 'all', 'minperiod', 'maxperiod',
                            'prestim', 'poststim' (default = 'all')
   cfg.keeptrials         = 'yes' or 'no', return individual trials or average (default = 'no')
   cfg.removemean         = 'no' or 'yes' for covariance computation (default = 'yes')

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a *.mat
 file on disk and/or the output data will be written to a *.mat file. These mat
 files should contain only a single variable, corresponding with the
 input/output structure.

 See also FT_TIMELOCKGRANDAVERAGE, FT_TIMELOCKSTATISTICS
```
