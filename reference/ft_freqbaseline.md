---
title: ft_freqbaseline
tags: 
---
```
 FT_FREQBASELINE performs baseline normalization for time-frequency data

 Use as
    [freq] = ft_freqbaseline(cfg, freq)
 where the freq data comes from FT_FREQANALYSIS and the configuration
 should contain
   cfg.baseline     = [begin end] (default = 'no'), alternatively an
                      Nfreq x 2 matrix can be specified, that provides
                      frequency specific baseline windows.
   cfg.baselinetype = 'absolute', 'relative', 'relchange', 'normchange', 'db' or 'zscore' (default = 'absolute')
   cfg.parameter    = field for which to apply baseline normalization, or
                      cell array of strings to specify multiple fields to normalize
                      (default = 'powspctrm')

 See also FT_FREQANALYSIS, FT_TIMELOCKBASELINE, FT_FREQCOMPARISON,
 FT_FREQGRANDAVERAGE
```
