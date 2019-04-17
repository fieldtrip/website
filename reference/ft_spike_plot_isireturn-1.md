---
title: ft_spike_plot_isireturn
---
```
 FT_SPIKE_PLOT_ISIRETURN makes a return plot from ISIH structure. A return
 plot (also called Poincare plot) plots the isi to the next spike versus the isi
 from the next spike to the second next spike, and thus gives insight in
 the second order isi statistics. This func also plots the raw
 isi-histogram on left and bottom and thereby give a rather complete
 visualization of the spike-train interval statistics.

 Use as
   ft_spike_plot_isireturn(cfg, data) 

 Inputs:
   ISIH must be the output structure from FT_SPIKE_ISI and contain the field
   ISIH.isi. 

 General configurations:
   cfg.spikechannel     = string or index of single spike channel to trigger on (default = 1)
                          Only one spikechannel can be plotted at a time.
   cfg.density          = 'yes' or 'no', if 'yes', we will use color shading on top of
                          the individual datapoints to indicate the density.
   cfg.scatter          = 'yes' (default) or 'no'. If 'yes', we plot the individual values.
   cfg.dt               =  resolution of the 2-D histogram, or of the kernel plot in seconds. Since we 
                           have to smooth for a finite number of values, cfg.dt determines
                           the resolution of our smooth density plot.
   cfg.colormap         = N-by-3 colormap (see COLORMAP). Default = hot(256);
   cfg.interpolate      = integer (default = 1), we perform interpolating
                          with extra number of spacings determined by
                          cfg.interpolate. For example cfg.interpolate = 5
                          means 5 times more dense axis.
   cfg.window           = 'no', 'gausswin' or 'boxcar'
                           'gausswin' is N-by-N multivariate gaussian, where the diagonal of the 
                           covariance matrix is set by cfg.gaussvar.
                           'boxcar' is N-by-N rectangular window.
   cfg.gaussvar         =  variance  (default = 1/16 of window length in sec).
   cfg.winlen           =  window length in seconds (default = 5*cfg.dt). The total
                           length of our window is 2*round*(cfg.winlen/cfg.dt) +1;
```
