---
title: ft_spiketriggeredinterpolation
---
```
 FT_SPIKETRIGGEREDINTERPOLATION interpolates the data in the LFP channels
 around the spikes that are detected in the spike channels, or replaces
 the LFP around the spike with NaNs. The purpose of this procedure is to
 allow analysis of spikes and LFPs recorded from the same electrode, as
 the spike energy would bleed in the LFP.

 Use as
   [data] = ft_spiketriggeredinterpolation(cfg, data)

 The input data should be organised in a structure as obtained from the
 FT_PREPROCESSING function. The configuration should be according to

   cfg.method       = string, The interpolation method can be 'nan',
                     'cubic', 'linear', 'nearest', spline', 'pchip'
                     (default = 'nan'). See INTERP1 for more details.
   cfg.timwin       = [begin end], duration of LFP segment around each spike (default =
                      [-0.005 0.005]) to be removed
   cfg.interptoi    = value, time in seconds used for interpolation, which
                      must be larger than timwin (default = 0.2)
   cfg.spikechannel = string, name of single spike channel to trigger on
   cfg.channel      = Nx1 cell-array with selection of channels (default = 'all'),
                      see FT_CHANNELSELECTION for details
   cfg.feedback     = 'no', 'text', 'textbar', 'gui' (default = 'no')

 The output will contain all channels of the input, only the data in the
 selected channels will be interpolated or replaced with NaNs.

 See also FT_SPIKETRIGGEREDSPECTRUM, FT_SPIKETRIGGEREDAVERAGE
```
