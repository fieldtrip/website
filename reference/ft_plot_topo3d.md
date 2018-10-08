---
layout: default
---

##  FT_PLOT_TOPO3D

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_plot_topo3d".

`<html>``<pre>`
    `<a href=/reference/ft_plot_topo3d>``<font color=green>`FT_PLOT_TOPO3D`</font>``</a>` makes a 3-D topographic representation of the electric
    potential or field at the sensor locations
 
    Use as
    ft_plot_topo3d(pos, val, ...);
    where the channel positions are given as a Nx3 matrix and the values are
    given as Nx1 vector.
 
    Optional input arguments should be specified in key-value pairs and can include
    'contourstyle' = string, 'none', 'black', 'color' (default = 'none')
    'isolines'     = vector with values at which to draw isocontours, or 'auto' (default = 'auto')
    'facealpha'    = scalar, between 0 and 1 (default = 1)
    'refine'       = scalar, number of refinement steps for the triangulation, to get a smoother interpolation (default = 0)
 
    See also `<a href=/reference/ft_plot_topo>``<font color=green>`FT_PLOT_TOPO`</font>``</a>`, `<a href=/reference/ft_plot_sens>``<font color=green>`FT_PLOT_SENS`</font>``</a>`, `<a href=/reference/ft_topoplotER>``<font color=green>`FT_TOPOPLOTER`</font>``</a>`, `<a href=/reference/ft_topoplotTFR>``<font color=green>`FT_TOPOPLOTTFR`</font>``</a>`
`</pre>``</html>`

