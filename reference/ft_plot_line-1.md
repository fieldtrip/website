---
title: ft_plot_line
---
```
 FT_PLOT_LINE helper function for plotting a line, which can also be used in
 combination with the multiple channel layout display in FieldTrip.

 Use as
   ft_plot_line(X, Y, ...)

 Optional arguments should come in key-value pairs and can include
   'color'           =
   'linestyle'       =
   'linewidth'       =
   'tag'             = string, the name assigned to the object. All tags with the same name can be deleted in a figure, without deleting other parts of the figure.

 It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specfied as follows
   'hpos'            = horizontal position of the center of the local axes
   'vpos'            = vertical position of the center of the local axes
   'width'           = width of the local axes
   'height'          = height of the local axes
   'hlim'            = horizontal scaling limits within the local axes
   'vlim'            = vertical scaling limits within the local axes

 See also FT_PLOT_BOX, FT_PLOT_CROSSHAIR
```
