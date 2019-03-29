---
title: ft_spike_plot_psth
---
```
 FT_SPIKE_PLOT_PSTH makes a bar plot of PSTH structure with error bars.

 Use as
   ft_spike_plot_psth(cfg, psth)
 
	Inputs:
		PSTH typically is a structure from FT_SPIKE_PSTH.

 Configurations:
   cfg.latency          = [begin end] in seconds, 'maxperiod' (default), 'prestim'(t<=0), or
                          'poststim' (t>=0).
   cfg.errorbars        = 'no', 'std', 'sem' (default), 'conf95%' (requires statistic toolbox,
                          according to student-T distribution), 'var'
   cfg.spikechannel     = string or index of single spike channel to trigger on (default = 1)
                          Only one spikechannel can be plotted at a time.
   cfg.ylim             = [min max] or 'auto' (default)
                          If 'standard', we plot from 0 to 110% of maximum plotted value);
 Outputs:
	  cfg.hdl.avg              = figure handle for the bar plot, psth average.
	  cfg.hdl.var              = figure handle for the error lines. 

 See also FT_SPIKE_PSTH
```
