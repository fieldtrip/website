---
title: ft_realtime_downsample
---
```
 FT_REALTIME_DOWNSAMPLE reads realtime data from one buffer and writes it after downsampling
 to another buffer.

 Use as
   ft_realtime_downsample(cfg)
 with the following configuration options
   cfg.channel              = cell-array, see FT_CHANNELSELECTION (default = 'all')
   cfg.decimation           = integer, downsampling factor (default = 1, no downsampling)
   cfg.order                = interger, order of butterworth lowpass filter (default = 4)
   cfg.cutoff               = double, cutoff frequency of lowpass filter (default = 0.8*Nyquist-freq.)

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
```
