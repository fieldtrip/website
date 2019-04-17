---
title: ft_realtime_powerestimate
---
```
 FT_REALTIME_POWERESTIMATE is an example realtime application for online
 power estimation. It should work both for EEG and MEG.

 Use as
   ft_realtime_powerestimate(cfg)
 with the following configuration options
   cfg.channel    = cell-array, see FT_CHANNELSELECTION (default = 'all')
   cfg.foilim     = [Flow Fhigh] (default = [0 120])
   cfg.blocksize  = number, size of the blocks/chuncks that are processed (default = 1 second)
   cfg.bufferdata = whether to start on the 'first or 'last' data that is available (default = 'last')

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
