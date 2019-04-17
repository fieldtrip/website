---
title: ft_realtime_fileproxy
---
```
 FT_REALTIME_FILEPROXY reads continuous data from an EEG/MEG file and writes it to a
 FieldTrip buffer. This works for any file format that is supported by FieldTrip.

 The FieldTrip buffer is a network transparent server that allows the acquisition
 client to stream data to it. An analysis client can connect to read the data upon
 request. Multiple clients can connect simultaneously, each analyzing a specific
 aspect of the data concurrently.

 Use as
   ft_realtime_fileproxy(cfg)
 with the following configuration options
   cfg.minblocksize         = number, in seconds (default = 0)
   cfg.maxblocksize         = number, in seconds (default = 1)
   cfg.channel              = cell-array, see FT_CHANNELSELECTION (default = 'all')
   cfg.jumptoeof            = jump to end of file at initialization (default = 'no')
   cfg.readevent            = whether or not to copy events (default = 'no'; event type can also be specified; e.g., 'UPPT002')
   cfg.speed                = relative speed at which data is written (default = inf)

 The source of the data is configured as
   cfg.source.dataset       = string
 or alternatively to obtain more low-level control as
   cfg.source.datafile      = string
   cfg.source.headerfile    = string
   cfg.source.eventfile     = string
   cfg.source.dataformat    = string, default is determined automatic
   cfg.source.headerformat  = string, default is determined automatic
   cfg.source.eventformat   = string, default is determined automatic

 The target to write the data to is configured as
   cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
   cfg.target.dataformat    = string, default is determined automatic

 To stop this realtime function, you have to press Ctrl-C

 See also FT_REALTIME_SIGNALPROXY, FT_REALTIME_SIGNALVIEWER
```
