---
title: ft_realtime_coillocalizer
---
```
 FT_REALTIME_COILLOCALIZER is a realtime application for online tracking
 of MEG localizer coils.

 Use as
   ft_realtime_coillocalizer(cfg)
 with the following configuration options
   cfg.blocksize  = number, size of the blocks/chuncks that are processed (default = 1 second)
   cfg.channel    = cell-array, see FT_CHANNELSELECTION (default = {'MEG', 'MEGREF'})
   cfg.bufferdata = whether to process the 'first or 'last' data that is available (default = 'last')
   cfg.jumptoeof  = whether to skip to the end of the stream/file at startup (default = 'yes')

 The settings for extracting the spatial topgraphy of each coil are configured as
   cfg.coilfreq      = single number in Hz or list of numbers
   cfg.refchan       = single string or cell-array with strings

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

 cfg.jumptoeof='yes' causes the realtime function to jump to the end
 when the function _starts_. It causes all data acquired prior to
 starting the RT function to be skipped.

 cfg.bufferdata=last causes the realtime function to jump to the last
 available data while _running_. If the realtime loop is not fast enough,
 it causes some data to be dropped.

 If you want to skip all data that was acquired before you start the
 realtime function, but don't want to miss any data that was acquired while
 the realtime function is started, then you should use jumptoeof=yes and
 bufferdata=first. If you want to analyze data from a file, then you
 should use jumptoeof=no and bufferdata=first.

 To stop this realtime function, you have to press Ctrl-C
```
