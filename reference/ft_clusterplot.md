---
layout: default
---

##  FT_CLUSTERPLOT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_clusterplot".

`<html>``<pre>`
    `<a href=/reference/ft_clusterplot>``<font color=green>`FT_CLUSTERPLOT`</font>``</a>` plots a series of topographies with highlighted clusters.
 
    Use as
    ft_clusterplot(cfg, stat)
    where the input data is obtained from `<a href=/reference/ft_timelockstatistics>``<font color=green>`FT_TIMELOCKSTATISTICS`</font>``</a>` or `<a href=/reference/ft_freqstatistics>``<font color=green>`FT_FREQSTATISTICS`</font>``</a>`.
 
    The configuration options can be
    cfg.alpha                     = number, highest cluster p-value to be plotted max 0.3 (default = 0.05)
    cfg.highlightseries           = 1x5 cell-array, highlight option series  with 'on', 'labels' or 'numbers' (default {'on', 'on', 'on', 'on', 'on'} for p &lt; [0.01 0.05 0.1 0.2 0.3]
    cfg.highlightsymbolseries     = 1x5 vector, highlight marker symbol series (default ['*', 'x', '+', 'o', '.'] for p &lt; [0.01 0.05 0.1 0.2 0.3]
    cfg.highlightsizeseries       = 1x5 vector, highlight marker size series   (default [6 6 6 6 6] for p &lt; [0.01 0.05 0.1 0.2 0.3])
    cfg.highlightcolorpos         = color of highlight marker for positive clusters (default = [0 0 0])
    cfg.highlightcolorneg         = color of highlight marker for negative clusters (default = [0 0 0])
    cfg.subplotsize               = layout of subplots ([h w], default [3 5])
    cfg.saveaspng                 = string, filename of the output figures (default = 'no')
    cfg.visible                   = string, 'on' or 'off' whether figure will be visible (default = 'on')
 
    You can also specify all cfg options that apply to `<a href=/reference/ft_topoplotER>``<font color=green>`FT_TOPOPLOTER`</font>``</a>` or `<a href=/reference/ft_topoplotTFR>``<font color=green>`FT_TOPOPLOTTFR`</font>``</a>`,
    except for cfg.xlim, any of the highlight options, cfg.comment and cfg.commentpos.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    If you specify this option the input data will be read from a *.mat
    file on disk. This mat files should contain only a single variable named 'data',
    corresponding to the input structure.
 
    See also `<a href=/reference/ft_topoplotTFR>``<font color=green>`FT_TOPOPLOTTFR`</font>``</a>`, `<a href=/reference/ft_topoplotER>``<font color=green>`FT_TOPOPLOTER`</font>``</a>`, `<a href=/reference/ft_movieplotTFR>``<font color=green>`FT_MOVIEPLOTTFR`</font>``</a>`, `<a href=/reference/ft_movieplotER>``<font color=green>`FT_MOVIEPLOTER`</font>``</a>`
`</pre>``</html>`

