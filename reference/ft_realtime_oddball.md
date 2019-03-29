---
title: ft_realtime_oddball
---
```
 FT_REALTIME_ODDBALL is an realtime application that computes an online
 average for a standard and deviant condition. The ERPs/ERFs are plotted,
 together with the difference as t-values. It should work both for EEG and
 MEG, as long as there are two triggers present

 Use as
   ft_realtime_oddball(cfg)
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
