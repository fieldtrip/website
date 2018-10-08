---
layout: default
---

##  FT_CONNECTIVITYPLOT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_connectivityplot".

`<html>``<pre>`
    `<a href=/reference/ft_connectivityplot>``<font color=green>`FT_CONNECTIVITYPLOT`</font>``</a>` plots channel-level frequency resolved connectivity. The
    data are rendered in a square grid of subplots, each subplot containing the
    connectivity spectrum between the two respective channels.
 
    Use as
    ft_connectivityplot(cfg, data)
 
    The input data is a structure containing the output to `<a href=/reference/ft_connectivityanalysis>``<font color=green>`FT_CONNECTIVITYANALYSIS`</font>``</a>`
    using a frequency domain metric of connectivity. Consequently the input
    data should have a dimord of 'chan_chan_freq', or 'chan_chan_freq_time'.
 
    The cfg can have the following option
    cfg.parameter   = string, the functional parameter to be plotted (default = 'cohspctrm')
    cfg.xlim        = selection boundaries over first dimension in data (e.g., freq)
                      'maxmin' or [xmin xmax] (default = 'maxmin')
    cfg.ylim        = selection boundaries over second dimension in data
                      (i.e. ,time, if present), 'maxmin', or [ymin ymax]
                      (default = 'maxmin')
    cfg.zlim        = plotting limits for color dimension, 'maxmin', 'maxabs' or [zmin zmax] (default = 'maxmin')
    cfg.channel     = list of channels to be included for the plotting (default = 'all'), see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
 
    See also `<a href=/reference/ft_connectivityanalysis>``<font color=green>`FT_CONNECTIVITYANALYSIS`</font>``</a>`, `<a href=/reference/ft_connectivitysimulation>``<font color=green>`FT_CONNECTIVITYSIMULATION`</font>``</a>`, `<a href=/reference/ft_multiplotCC>``<font color=green>`FT_MULTIPLOTCC`</font>``</a>`, `<a href=/reference/ft_topoplotCC>``<font color=green>`FT_TOPOPLOTCC`</font>``</a>`
`</pre>``</html>`

