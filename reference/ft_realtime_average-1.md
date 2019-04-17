---
title: ft_realtime_average
---
```
 FT_REALTIME_AVERAGE is an example realtime application for online
 averaging of the data. It should work both for EEG and MEG.

 Use as
   ft_realtime_average(cfg)
 with the following configuration options
   cfg.channel    = cell-array, see FT_CHANNELSELECTION (default = 'all')
   cfg.trialfun   = string with the trial function

 The source of the data is configured as
   cfg.dataset       = string
 or alternatively to obtain more low-level control as
   cfg.datafile      = string
   cfg.headerfile    = string
   cfg.eventfile     = string
   cfg.dataformat    = string, default is determined automatic
   cfg.headerformat  = string, default is determined automatic
   cfg.eventformat   = string, default is determined automatic

 To stop the realtime function, you have to press Ctrl-C
```
