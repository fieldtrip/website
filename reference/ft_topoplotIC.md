---
layout: default
---

##  FT_TOPOPLOTIC

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_topoplotIC".

`<html>``<pre>`
    `<a href=/reference/ft_topoplotIC>``<font color=green>`FT_TOPOPLOTIC`</font>``</a>` plots the topographic distribution of an independent
    component that was computed using the `<a href=/reference/ft_componentanalysis>``<font color=green>`FT_COMPONENTANALYSIS`</font>``</a>` function,
    as a 2-D circular view (looking down at the top of the head).
 
    Use as
    ft_topoplotIC(cfg, comp)
    where the input comp structure should be obtained from `<a href=/reference/ft_componentanalysis>``<font color=green>`FT_COMPONENTANALYSIS`</font>``</a>`.
 
    The configuration should have the following parameter
    cfg.component          = field that contains the independent component(s) to be plotted as color
    cfg.layout             = specification of the layout, see below
 
    The configuration can have the following parameter
    cfg.colormap           = any sized colormap, see COLORMAP
    cfg.zlim               = plotting limits for color dimension, 'maxmin', 'maxabs', 'zeromax', 'minzero', or [zmin zmax] (default = 'maxmin')
    cfg.marker             = 'on', 'labels', 'numbers', 'off'
    cfg.markersymbol       = channel marker symbol (default = 'o')
    cfg.markercolor        = channel marker color (default = [0 0 0] (black))
    cfg.markersize         = channel marker size (default = 2)
    cfg.markerfontsize     = font size of channel labels (default = 8 pt)
    cfg.highlight          = 'on', 'labels', 'numbers', 'off'
    cfg.highlightchannel   =  Nx1 cell-array with selection of channels, or vector containing channel indices see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>`
    cfg.highlightsymbol    = highlight marker symbol (default = 'o')
    cfg.highlightcolor     = highlight marker color (default = [0 0 0] (black))
    cfg.highlightsize      = highlight marker size (default = 6)
    cfg.highlightfontsize  = highlight marker size (default = 8)
    cfg.colorbar           = 'yes'
                             'no' (default)
                             'North'              inside plot box near top
                             'South'              inside bottom
                             'East'               inside right
                             'West'               inside left
                             'NorthOutside'       outside plot box near top
                             'SouthOutside'       outside bottom
                             'EastOutside'        outside right
                             'WestOutside'        outside left
    cfg.interplimits       = limits for interpolation (default = 'head')
                             'electrodes' to furthest electrode
                             'head' to edge of head
    cfg.interpolation      = 'linear','cubic','nearest','v4' (default = 'v4') see GRIDDATA
    cfg.style              = plot style (default = 'both')
                             'straight' colormap only
                             'contour' contour lines only
                             'both' (default) both colormap and contour lines
                             'fill' constant color between lines
                             'blank' only the head shape
    cfg.gridscale          = scaling grid size (default = 67)
                             determines resolution of figure
    cfg.shading            = 'flat' 'interp' (default = 'flat')
    cfg.comment            = string 'no' 'auto' or 'xlim' (default = 'auto')
                             'auto': date, xparam and zparam limits are printed
                             'xlim': only xparam limits are printed
    cfg.commentpos         = string or two numbers, position of comment (default 'leftbottom')
                             'lefttop' 'leftbottom' 'middletop' 'middlebottom' 'righttop' 'rightbottom'
                             'title' to place comment as title
                             'layout' to place comment as specified for COMNT in layout
                             [x y] coordinates
    cfg.title              = string or 'auto' or 'off', specify a figure
                             title, or use 'component N' (auto) as the
                             title
 
    The layout defines how the channels are arranged. You can specify the
    layout in a variety of way
   - you can provide a pre-computed layout structure (see prepare_layout)
   - you can give the name of an ascii layout file with extension *.lay
   - you can give the name of an electrode file
   - you can give an electrode definition, i.e. "elec" structure
   - you can give a gradiometer definition, i.e. "grad" structure
    If you do not specify any of these and the data structure contains an
    electrode or gradiometer structure, that will be used for creating a
    layout. If you want to have more fine-grained control over the layout
    of the subplots, you should create your own layout file.
 
    See also `<a href=/reference/ft_componentanalysis>``<font color=green>`FT_COMPONENTANALYSIS`</font>``</a>`, `<a href=/reference/ft_rejectcomponent>``<font color=green>`FT_REJECTCOMPONENT`</font>``</a>`, `<a href=/reference/ft_topoplotTFR>``<font color=green>`FT_TOPOPLOTTFR`</font>``</a>`,
    `<a href=/reference/ft_singleplotTFR>``<font color=green>`FT_SINGLEPLOTTFR`</font>``</a>`, `<a href=/reference/ft_multiplotTFR>``<font color=green>`FT_MULTIPLOTTFR`</font>``</a>`, `<a href=/reference/ft_prepare_layout>``<font color=green>`FT_PREPARE_LAYOUT`</font>``</a>`
`</pre>``</html>`

