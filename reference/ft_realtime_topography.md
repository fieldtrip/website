---
title: ft_realtime_topography
---
```
 FT_REALTIME_TOPOGRAPHY reads continuous data from a file or from a data stream,
 estimates the power and plots the scalp topography in real time.

 Use as
   ft_realtime_topography(cfg)
 with the following configuration options
   cfg.blocksize            = number, size of the blocks/chuncks that are processed (default = 1 second)
   cfg.overlap              = number, amojunt of overlap between chunks (default = 0 seconds)
   cfg.layout               = specification of the layout, see FT_PREPARE_LAYOUT

 The source of the data is configured as
   cfg.dataset       = string
 or alternatively to obtain more low-level control as
   cfg.datafile      = string
   cfg.headerfile    = string
   cfg.eventfile     = string
   cfg.dataformat    = string, default is determined automatic
   cfg.headerformat  = string, default is determined automatic
   cfg.eventformat   = string, default is determined automatic

 To stop this realtime function, you have to press Ctrl-C

 Example use
   cfg           = [];
   cfg.dataset   = 'PW02_ingnie_20061212_01.ds';
   cfg.layout    = 'CTF151.lay';
   cfg.channel   = 'MEG';
   cfg.blocksize = 0.5;
   cfg.overlap   = 0.25;
   cfg.demean    = 'yes';
   cfg.bpfilter  = [15 25];
   cfg.bpfreq    =	 'yes';
   ft_realtime_topography(cfg);
```
