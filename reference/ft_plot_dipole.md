---
layout: default
---

##  FT_PLOT_DIPOLE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_plot_dipole".

`<html>``<pre>`
    `<a href=/reference/ft_plot_dipole>``<font color=green>`FT_PLOT_DIPOLE`</font>``</a>` makes a 3-D representation of a dipole using a sphere and a stick
    pointing along the dipole orientation
 
    Use as
    ft_plot_dipole(pos, mom, ...)
    where pos and mom are the dipole mosition and moment. 
 
    Optional input arguments should be specified in key-value pairs and can include
    'diameter' = number indicating sphere diameter (default = 'auto')
    'length'   = number indicating length of the stick (default = 'auto')
    'color'    = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r' (default = 'r')
    'unit'     = 'm', 'cm' or 'mm', used for automatic scaling (default = 'cm')
    'scale'    = scale the dipole with the amplitude, can be 'none',  'both', 'diameter', 'length' (default = 'none')
    'alpha'    = alpha value of the plotted dipole
 
    Example
    ft_plot_dipole([0 0 0], [1 2 3], 'color', 'r', 'alpha', 1)
 
    See also `<a href=/reference/ft_plot_mesh>``<font color=green>`FT_PLOT_MESH`</font>``</a>`, `<a href=/reference/ft_plot_ortho>``<font color=green>`FT_PLOT_ORTHO`</font>``</a>`
`</pre>``</html>`

