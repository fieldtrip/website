---
title: ft_multiplotER
---
```plaintext
 FT_MULTIPLOTER plots the event-related potentials or event-related fields
 versus time, or the oscillatory activity (power or coherence) versus frequency. 
 Multiple datasets can be overlayed. The plots are arranged according to
 the location of the channels specified in the layout.

 Use as
   ft_multiplotER(cfg, data)
 or
   ft_multiplotER(cfg, data, data2, ..., dataN)

 The data can be an event-related potential or field produced by
 FT_TIMELOCKANALYSIS, a power spectrum produced by FT_FREQANALYSIS or a coherence
 spectrum produced by FT_FREQDESCRIPTIVES.

 If you specify multiple datasets they should contain the same channels, etc.

 The configuration can have the following parameters:
   cfg.parameter     = field to be plotted on y-axis, for example 'avg', 'powspctrm' or 'cohspctrm' (default is automatic)
   cfg.maskparameter = field in the first dataset to be used for marking significant data
   cfg.maskstyle     = style used for masking of data, 'box', 'thickness' or 'saturation' (default = 'box')
   cfg.maskfacealpha = mask transparency value between 0 and 1
   cfg.xlim          = 'maxmin' or [xmin xmax] (default = 'maxmin')
   cfg.ylim          = 'maxmin', 'maxabs', 'zeromax', 'minzero', or [ymin ymax] (default = 'maxmin')
   cfg.gradscale     = number, scaling to apply to the MEG gradiometer channels prior to display
   cfg.magscale      = number, scaling to apply to the MEG magnetometer channels prior to display
   cfg.channel       = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details
   cfg.refchannel    = name of reference channel for visualising connectivity, can be 'gui'
   cfg.baseline      = 'yes', 'no' or [time1 time2] (default = 'no'), see FT_TIMELOCKBASELINE or FT_FREQBASELINE
   cfg.trials        = 'all' or a selection given as a 1xN vector (default = 'all')
   cfg.axes          = string, 'yes' or 'no' whether to draw x- and y-axes for each graph (default = 'yes')
   cfg.box           = string, 'yes' or 'no' whether to draw a box around each graph (default = 'no')
   cfg.showlabels    = 'yes' or 'no' (default = 'no')
   cfg.showoutline   = 'yes' or 'no' (default = 'no')
   cfg.showscale     = 'yes' or 'no' (default = 'yes')
   cfg.showcomment   = 'yes' or 'no' (default = 'yes')
   cfg.comment       = string of text (default = date + limits)
                       Add 'comment' to graph (according to COMNT in the layout)
   cfg.limittext     = add user-defined text instead of cfg.comment, (default = cfg.comment)
   cfg.fontsize      = font size of comment and labels (default = 8)
   cfg.interactive   = 'yes' or 'no', make the plot interactive (default = 'yes')
                       In a interactive plot you can select areas and produce a new
                       interactive plot when a selected area is clicked. Multiple areas
                       can be selected by holding down the SHIFT key.
   cfg.renderer      = 'painters', 'zbuffer', ' opengl' or 'none' (default = [])
   cfg.colorgroups   = 'sequential', 'allblack', 'labelcharN' (N = Nth character in label), 'chantype' or a vector
                       with the length of the number of channels defining the groups (default = 'sequential')
   cfg.linestyle     = linestyle/marker type, see options of the PLOT function (default = '-')
                       can be a single style for all datasets, or a cell-array containing one style for each dataset
   cfg.linewidth     = linewidth in points (default = 0.5)
   cfg.linecolor     = color(s) used for plotting the dataset(s) (default = 'brgkywrgbkywrgbkywrgbkyw')
                       alternatively, colors can be specified as Nx3 matrix of RGB values
   cfg.directionality = '', 'inflow' or 'outflow' specifies for connectivity measures whether the
                       inflow into a node, or the outflow from a node is plotted. The (default) behavior
                       of this option depends on the dimord of the input data (see below).
   cfg.layout        = specify the channel layout for plotting using one of the supported ways (see below).
   cfg.select        = 'intersect' or 'union' (default = 'intersect')
                       with multiple input arguments determines the
                       pre-selection of the data that is considered for
                       plotting.
```
