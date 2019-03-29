---
title: ft_spike_plot_raster
---
```
 FT_SPIKE_PLOT_RASTER makes a raster plot of spike-trains and allows for a
 spike-density or a PSTH plot on top.

 Use as
   ft_spike_plot_raster(cfg, spike) 
 or 
   ft_spike_plot_raster(cfg, spike, timelock)

 The input SPIKE data structure should be organized as the spike or the
 raw datatype The optional input TIMELOCK should be organized as the
 timelock datatype, e.g. the output from FT_SPIKE_PSTH or FT_SPIKEDENSITY,
 having the average firing rate / spike count per time-point / time-bin.
 However, timelock could also be the output from FT_TIMELOCKANALYSIS.

 Configuration options 
   cfg.spikechannel     =  see FT_CHANNELSELECTION for details
   cfg.latency          =  [begin end] in seconds, 'maxperiod' (default), 'minperiod',
                           'prestim' (all t<=0), or 'poststim' (all t>=0).
   cfg.linewidth        =  number indicating the width of the lines (default = 1);
   cfg.cmapneurons      =  'auto' (default), or nUnits-by-3 matrix.
                           Controls coloring of spikes and psth/density
                           data if multiple cells are present.
   cfg.spikelength      =  number >0 and <=1 indicating the length of the spike. If
                           cfg.spikelength = 1, then no space will be left between
                           subsequent rows representing trials (row-unit is 1).
   cfg.trialborders     =  'yes' or 'no'. If 'yes', borders of trials are
                           plotted
   cfg.plotselection   =  'yes' or 'no' (default). If yes plot Y axis only for selection in cfg.trials
   cfg.topplotsize      =  number ranging from 0 to 1, indicating the proportion of the
                           rasterplot that the top plot will take (e.g., with 0.7 the top
                           plot will be 70% of the rasterplot in size). Default = 0.5.
   cfg.topplotfunc      =  'bar' (default) or 'line'.
   cfg.errorbars        = 'no', 'std', 'sem' (default), 'conf95%','var'

   cfg.interactive      = 'yes' (default) or 'no'. If 'yes', zooming and panning operate via callbacks.
   cfg.trials           =  numeric or logical selection of trials (default = 'all').
```
