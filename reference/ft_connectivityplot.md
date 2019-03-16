---
title: ft_connectivityplot
---
```
 FT_CONNECTIVITYPLOT plots channel-level frequency resolved connectivity. The
 data are rendered in a square grid of subplots, each subplot containing the
 connectivity spectrum between the two respective channels.

 Use as
   ft_connectivityplot(cfg, data)

 The input data is a structure containing the output to FT_CONNECTIVITYANALYSIS
 using a frequency domain metric of connectivity. Consequently the input
 data should have a dimord of 'chan_chan_freq', or 'chan_chan_freq_time'.

 The cfg can have the following options:
   cfg.parameter   = string, the functional parameter to be plotted (default = 'cohspctrm')
   cfg.xlim        = selection boundaries over first dimension in data (e.g., freq)
                     'maxmin' or [xmin xmax] (default = 'maxmin')
   cfg.ylim        = selection boundaries over second dimension in data
                     (i.e. ,time, if present), 'maxmin', or [ymin ymax]
                     (default = 'maxmin')
   cfg.zlim        = plotting limits for color dimension, 'maxmin', 'maxabs' or [zmin zmax] (default = 'maxmin')
   cfg.channel     = list of channels to be included for the plotting (default = 'all'), see FT_CHANNELSELECTION for details

 See also FT_CONNECTIVITYANALYSIS, FT_CONNECTIVITYSIMULATION, FT_MULTIPLOTCC, FT_TOPOPLOTCC
```
