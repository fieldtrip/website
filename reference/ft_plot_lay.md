---
layout: default
---

##  FT_PLOT_LAY

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_plot_lay".

`<html>``<pre>`
    `<a href=/reference/ft_plot_lay>``<font color=green>`FT_PLOT_LAY`</font>``</a>` plots a two-dimensional layout
 
    Use as
    ft_plot_lay(layout, ...)
    where the layout is a FieldTrip structure obtained from `<a href=/reference/ft_prepare_layout>``<font color=green>`FT_PREPARE_LAYOUT`</font>``</a>`.
 
    Additional options should be specified in key-value pairs and can be
    'chanindx'    = list of channels to plot (default is all)
    'point'       = yes/no
    'box'         = yes/no
    'label'       = yes/no
    'labeloffset' = offset of label from point (default = 0)
    'labelrotate' = scalar, vector with rotation angle (in degrees) per label (default = 0)
    'labelalignh' = string, or cell-array specifying the horizontal alignment of the text (default = 'left')
    'labelalignv' = string, or cell-array specifying the vertical alignment of the text (default = 'middle')
    'mask'        = yes/no
    'outline'     = yes/no
    'verbose'     = yes/no
    'pointsymbol' = string with symbol (e.g. 'o') - all three point options need to be used together
    'pointcolor'  = string with color (e.g. 'k')
    'pointsize'   = number indicating size (e.g. 8)
    'fontcolor'   = string, color specification (default = 'k')
    'fontsize'    = number, sets the size of the text (default = 10)
    'fontunits'   =
    'fontname'    =
    'fontweight'  =
 
    It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specfied as follows
    'hpos'        = horizontal position of the lower left corner of the local axes
    'vpos'        = vertical position of the lower left corner of the local axes
    'width'       = width of the local axes
    'height'      = height of the local axes
 
    See also `<a href=/reference/ft_prepare_layout>``<font color=green>`FT_PREPARE_LAYOUT`</font>``</a>`, `<a href=/reference/ft_plot_topo>``<font color=green>`FT_PLOT_TOPO`</font>``</a>`
`</pre>``</html>`

