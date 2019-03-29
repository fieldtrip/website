---
title: ft_realtime_heartbeatdetect
---
```
 FT_REALTIME_HEARTBEATDETECT is an example realtime application for online
 detection of heart beats. It should work both for EEG and MEG.

 Use as
   ft_realtime_heartbeatdetect(cfg)
 with the following configuration options
   cfg.blocksize  = number, size of the blocks/chuncks that are processed (default = 1 second)
   cfg.channel    = cell-array, see FT_CHANNELSELECTION (default = 'all')
   cfg.jumptoeof  = whether to skip to the end of the stream/file at startup (default = 'yes')
   cfg.bufferdata = whether to start on the 'first or 'last' data that is available (default = 'first')
   cfg.threshold  = value, after normalization (default = 3)

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
