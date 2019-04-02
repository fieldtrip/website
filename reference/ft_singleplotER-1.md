---
title: ft_singleplotER
---
```
 FT_SINGLEPLOTER plots the event-related fields or potentials of a single
 channel or the average over multiple channels. Multiple datasets can be
 overlayed.

 Use as
   ft_singleplotER(cfg, data)
 or
   ft_singleplotER(cfg, data1, data2, ..., datan)

 The data can be an erp/erf produced by FT_TIMELOCKANALYSIS, a power
 spectrum produced by FT_FREQANALYSIS or connectivity spectrum produced by
 FT_CONNECTIVITYANALYSIS.

 The configuration can have the following parameters:
   cfg.parameter     = field to be plotted on y-axis (default depends on data.dimord)
                       'avg', 'powspctrm' or 'cohspctrm'
   cfg.maskparameter = field in the first dataset to be used for masking of data
                       (not possible for mean over multiple channels, or when input contains multiple subjects
                       or trials)
   cfg.maskstyle     = style used for masking of data, 'box', 'thickness' or 'saturation' (default = 'box')
   cfg.maskfacealpha = mask transparency value between 0 and 1
   cfg.xlim          = 'maxmin' or [xmin xmax] (default = 'maxmin')
   cfg.ylim          = 'maxmin', 'maxabs', 'zeromax', 'minzero', or [ymin ymax] (default = 'maxmin')
   cfg.channel       = nx1 cell-array with selection of channels (default = 'all')
                       see ft_channelselection for details
   cfg.title          = string, title of plot
   cfg.refchannel    = name of reference channel for visualising connectivity, can be 'gui'
   cfg.baseline      = 'yes', 'no' or [time1 time2] (default = 'no'), see ft_timelockbaseline
   cfg.baselinetype  = 'absolute' or 'relative' (default = 'absolute')
   cfg.trials        = 'all' or a selection given as a 1xn vector (default = 'all')
   cfg.fontsize      = font size of title (default = 8)
   cfg.hotkeys       = enables hotkeys (leftarrow/rightarrow/uparrow/downarrow/m) for dynamic zoom and translation (ctrl+) of the axes
   cfg.interactive   = interactive plot 'yes' or 'no' (default = 'yes')
                       in a interactive plot you can select areas and produce a new
                       interactive plot when a selected area is clicked. multiple areas
                       can be selected by holding down the shift key.
   cfg.renderer      = 'painters', 'zbuffer', ' opengl' or 'none' (default = [])
   cfg.linestyle     = linestyle/marker type, see options of the PLOT function (default = '-')
                       can be a single style for all datasets, or a cell-array containing one style for each dataset
   cfg.linewidth     = linewidth in points (default = 0.5)
   cfg.graphcolor    = color(s) used for plotting the dataset(s) (default = 'brgkywrgbkywrgbkywrgbkyw')
                       alternatively, colors can be specified as nx3 matrix of rgb values
   cfg.directionality = '', 'inflow' or 'outflow' specifies for
                       connectivity measures whether the inflow into a
                       node, or the outflow from a node is plotted. The
                       (default) behavior of this option depends on the dimor
                       of the input data (see below).

 For the plotting of directional connectivity data the cfg.directionality
 option determines what is plotted. The default value and the supported
 functionality depend on the dimord of the input data. If the input data
 is of dimord 'chan_chan_XXX', the value of directionality determines
 whether, given the reference channel(s), the columns (inflow), or rows
 (outflow) are selected for plotting. In this situation the default is
 'inflow'. Note that for undirected measures, inflow and outflow should
 give the same output. If the input data is of dimord 'chancmb_XXX', the
 value of directionality determines whether the rows in data.labelcmb are
 selected. With 'inflow' the rows are selected if the refchannel(s) occur in
 the right column, with 'outflow' the rows are selected if the
 refchannel(s) occur in the left column of the labelcmb-field. Default in
 this case is '', which means that all rows are selected in which the
 refchannel(s) occur. This is to robustly support linearly indexed
 undirected connectivity metrics. In the situation where undirected
 connectivity measures are linearly indexed, specifying 'inflow' or
 'outflow' can result in unexpected behavior.

 to facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
 if you specify this option the input data will be read from a *.mat
 file on disk. this mat files should contain only a single variable named 'data',
 corresponding to the input structure.

 See also FT_SINGLEPLOTTFR, FT_MULTIPLOTER, FT_MULTIPLOTTFR, FT_TOPOPLOTER, FT_TOPOPLOTTFR
```
