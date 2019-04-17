---
title: ft_spike_plot_jpsth
---
```
 FT_SPIKE_PLOT_JPSTH makes a plot from JPSTH structure.

 Use as
   ft_spike_plot_jpsth(cfg, jpsth)

 Inputs:
   JPSTH must be the output structure from FT_SPIKE_JPSTH and contain the
   field JPSTH.avg. If cfg.psth = 'yes', the field JPSTH.psth must be
   present as well.

 General configurations:
   cfg.channelcmb  = string or index of single channel combination to trigger on.
       See SPIKESTATION_FT_SUB_CHANNELCOMBINATION for details.
   cfg.psth        = 'yes' (default) or 'no'. Plot PSTH with JPSTH if 'yes';
   cfg.latency     = [begin end] in seconds or 'max' (default), 'prestim' or 'poststim';
   cfg.colorbar    = 'yes' (default) or 'no'
   cfg.colormap    =  N-by-3 colormap (see COLORMAP). or 'auto' (default,hot(256))
   cfg.interpolate      = integer (default = 1), we perform interpolating
                          with extra number of spacings determined by
                          cfg.interpolate. For example cfg.interpolate = 5
                          means 5 times more dense axis.
   cfg.window      = 'string' or N-by-N matrix
     'no':           apply no smoothing
     ' gausswin'     use a Gaussian smooth function
     ' boxcar'       use a box-car to smooth
   cfg.gaussvar    =  variance  (default = 1/16 of window length in sec).
   cfg.winlen      =  window length in seconds (default = 5*binwidth).
     length of our window is 2*round*(cfg.winlen/binwidth)
     where binwidth is the binwidth of the jpsth (jpsth.time(2)-jpsth.time(1)).

 See also FT_SPIKE_JPSTH, FT_SPIKE_PSTH
```
