---
title: ft_spike_plot_isi
---
```
 FT_SPIKE_PLOT_ISI makes an inter-spike-interval bar plot.

 Use as
   ft_spike_plot_isi(cfg, isih)

 Inputs:
   ISIH is the output from FT_SPIKE_ISIHIST

 Configurations:
   cfg.spikechannel     = string or index or logical array to to select 1 spike channel.
                          (default = 1).
   cfg.ylim             = [min max] or 'auto' (default)
                          If 'auto', we plot from 0 to 110% of maximum plotted value);
   cfg.plotfit          = 'yes' (default) or 'no'. This requires that when calling
                          FT_SPIKESTATION_ISI, cfg.gammafit = 'yes'.

 Outputs:
   hdl.fit              = handle for line fit. Use SET and GET to access.
   hdl.isih             = handle for bar isi histogram. Use SET and GET to access.
```
