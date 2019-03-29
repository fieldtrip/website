---
title: ft_plot_dipole
---
```
 FT_PLOT_DIPOLE makes a 3-D representation of a dipole using a sphere and a stick
 pointing along the dipole orientation

 Use as
   ft_plot_dipole(pos, mom, ...)
 where pos and mom are the dipole mosition and moment.

 Optional input arguments should be specified in key-value pairs and can include
   'diameter'  = number indicating sphere diameter (default = 'auto')
   'length'    = number indicating length of the stick (default = 'auto')
   'thickness' = number indicating thickness of the stick (default = 'auto')
   'color'     = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r' (default = 'r')
   'unit'      = 'm', 'cm' or 'mm', used for automatic scaling (default = 'cm')
   'scale'     = scale the dipole with the amplitude, can be 'none',  'both', 'diameter', 'length' (default = 'none')
   'alpha'     = alpha value of the plotted dipole

 Example
   ft_plot_dipole([0 0 0], [1 2 3], 'color', 'r', 'alpha', 1)

 See also FT_PLOT_MESH, FT_PLOT_ORTHO
```
