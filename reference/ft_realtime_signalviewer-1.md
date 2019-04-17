---
title: ft_realtime_signalviewer
---
```
 FT_REALTIME_SIGNALVIEWER is an example realtime application for online viewing of
 the data. It should work both for EEG and MEG.

 Use as
   ft_realtime_signalviewer(cfg)
 with the following configuration options
   cfg.blocksize  = number, size of the blocks/chuncks that are processed (default = 1 second)
   cfg.channel    = cell-array, see FT_CHANNELSELECTION (default = 'all')
   cfg.jumptoeof  = whether to skip to the end of the stream/file at startup (default = 'yes')
   cfg.bufferdata = whether to start on the 'first or 'last' data that is available (default = 'first')
   cfg.readevent  = whether or not to copy events (default = 'no')
   cfg.demean     = 'no' or 'yes', whether to apply baseline correction (default = 'yes')

 The source of the data is configured as
   cfg.dataset       = string
 or alternatively to obtain more low-level control as
   cfg.datafile      = string
   cfg.headerfile    = string
   cfg.eventfile     = string
   cfg.dataformat    = string, default is determined automatic
   cfg.headerformat  = string, default is determined automatic
   cfg.eventformat   = string, default is determined automatic

 Some notes about skipping data and catching up with the data stream:

 cfg.jumptoeof='yes' causes the realtime function to jump to the end when the
 function _starts_. It causes all data acquired prior to starting the realtime
 function to be skipped.

 cfg.bufferdata='last' causes the realtime function to jump to the last available data
 while _running_. If the realtime loop is not fast enough, it causes some data to be
 dropped.

 If you want to skip all data that was acquired before you start the RT function,
 but don't want to miss any data that was acquired while the realtime function is
 started, then you should use jumptoeof=yes and bufferdata=first. If you want to
 analyze data from a file, then you should use jumptoeof=no and bufferdata=first.

 To stop this realtime function, you have to press Ctrl-C
```
