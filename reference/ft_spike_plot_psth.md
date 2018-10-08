---
layout: default
---

##  FT_SPIKE_PLOT_PSTH

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_spike_plot_psth".

`<html>``<pre>`
    `<a href=/reference/ft_spike_plot_psth>``<font color=green>`FT_SPIKE_PLOT_PSTH`</font>``</a>` makes a bar plot of PSTH structure with error bars.
 
    Use as
    ft_spike_plot_psth(cfg, psth)
    
 	Input
 		PSTH typically is a structure from `<a href=/reference/ft_spike_psth>``<font color=green>`FT_SPIKE_PSTH`</font>``</a>`.
 
    Configuration
    cfg.latency          = [begin end] in seconds, 'maxperiod' (default), 'prestim'(t&lt;=0), or
                           'poststim' (t&gt;=0).
    cfg.errorbars        = 'no', 'std', 'sem' (default), 'conf95%' (requires statistic toolbox,
                           according to student-T distribution), 'var'
    cfg.spikechannel     = string or index of single spike channel to trigger on (default = 1)
                           Only one spikechannel can be plotted at a time.
    cfg.ylim             = [min max] or 'auto' (default)
                           If 'standard', we plot from 0 to 110% of maximum plotted value);
    Output
 	  cfg.hdl.avg              = figure handle for the bar plot, psth average.
 	  cfg.hdl.var              = figure handle for the error lines. 
 
    See also `<a href=/reference/ft_spike_psth>``<font color=green>`FT_SPIKE_PSTH`</font>``</a>`
`</pre>``</html>`

