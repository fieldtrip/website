---
layout: default
---

##  FT_PLOT_CROSSHAIR

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_plot_crosshair".

`<html>``<pre>`
    `<a href=/reference/ft_plot_crosshair>``<font color=green>`FT_PLOT_CROSSHAIR`</font>``</a>` plots a crosshair at a specified position in two [x, y] or three
    [x, y, z] dimensions. 
 
    Use as
    h = ft_plot_crosshair(pos, ...)
    where pos is the desired position of the crosshair. The handles of the lines are
    returned.
 
    Optional input arguments should be specified in key-value pairs and can include
    'color'    = [r g b] value or string, see PLOT
    'parent'   = handle of the parent axes
    'handle'   = handle of the existing line objects to be updated
    
    You can specify the handles of existing line objects which will be then updated,
    rather than creating a new set of lines. If both parent and handle ar specified,
    the handle option prevail.
    
    Example
    ft_plot_crosshair([0.5 0.5], 'color', 'r')
 
    See also `<a href=/reference/ft_plot_box>``<font color=green>`FT_PLOT_BOX`</font>``</a>`, `<a href=/reference/ft_plot_line>``<font color=green>`FT_PLOT_LINE`</font>``</a>`, TEXT, LINE
`</pre>``</html>`

