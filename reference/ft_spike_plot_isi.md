---
layout: default
---

##  FT_SPIKE_PLOT_ISI

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_spike_plot_isi".

`<html>``<pre>`
    `<a href=/reference/ft_spike_plot_isi>``<font color=green>`FT_SPIKE_PLOT_ISI`</font>``</a>` makes an inter-spike-interval bar plot.
 
    Use as
    ft_spike_plot_isi(cfg, isih)
 
    Input
    ISIH is the output from `<a href=/reference/ft_spike_isi>``<font color=green>`FT_SPIKE_ISI`</font>``</a>`HIST
 
    Configuration
    cfg.spikechannel     = string or index or logical array to to select 1 spike channel.
                           (default = 1).
    cfg.ylim             = [min max] or 'auto' (default)
                           If 'auto', we plot from 0 to 110% of maximum plotted value);
    cfg.plotfit          = 'yes' (default) or 'no'. This requires that when calling
                           FT_SPIKESTATION_ISI, cfg.gammafit = 'yes'.
 
    Output
    hdl.fit              = handle for line fit. Use SET and GET to access.
    hdl.isih             = handle for bar isi histogram. Use SET and GET to access.
`</pre>``</html>`

