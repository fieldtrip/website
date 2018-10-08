---
layout: default
---

##  FT_SPIKETRIGGEREDINTERPOLATION

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_spiketriggeredinterpolation".

`<html>``<pre>`
    `<a href=/reference/ft_spiketriggeredinterpolation>``<font color=green>`FT_SPIKETRIGGEREDINTERPOLATION`</font>``</a>` interpolates the data in the LFP channels
    around the spikes that are detected in the spike channels, or replaces
    the LFP around the spike with NaNs. The purpose of this procedure is to
    allow analysis of spikes and LFPs recorded from the same electrode, as
    the spike energy would bleed in the LFP.
 
    Use as
    [data] = ft_spiketriggeredinterpolation(cfg, data)
 
    The input data should be organised in a structure as obtained from the
    `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>` function. The configuration should be according to
 
    cfg.method       = string, The interpolation method can be 'nan',
                      'cubic', 'linear', 'nearest', spline', 'pchip'
                      (default = 'nan'). See INTERP1 for more details.
    cfg.timwin       = [begin end], duration of LFP segment around each spike (default =
                       [-0.005 0.005]) to be removed
    cfg.interptoi    = value, time in seconds used for interpolation, which
                       must be larger than timwin (default = 0.2)
    cfg.spikechannel = string, name of single spike channel to trigger on
    cfg.channel      = Nx1 cell-array with selection of channels (default = 'all'),
                       see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.feedback     = 'no', 'text', 'textbar', 'gui' (default = 'no')
 
    The output will contain all channels of the input, only the data in the
    selected channels will be interpolated or replaced with NaNs.
 
    See also `<a href=/reference/ft_spiketriggeredspectrum>``<font color=green>`FT_SPIKETRIGGEREDSPECTRUM`</font>``</a>`, `<a href=/reference/ft_spiketriggeredaverage>``<font color=green>`FT_SPIKETRIGGEREDAVERAGE`</font>``</a>`
`</pre>``</html>`

