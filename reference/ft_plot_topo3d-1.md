---
title: ft_plot_topo3d
---
```
 FT_PLOT_TOPO3D makes a 3-D topographic representation of the electric
 potential or field at the sensor locations

 Use as
   ft_plot_topo3d(pos, val, ...)
 where the channel positions are given as a Nx3 matrix and the values are
 given as Nx1 vector.

 Optional input arguments should be specified in key-value pairs and can include
   'contourstyle' = string, 'none', 'black', 'color' (default = 'none')
   'isolines'     = vector with values at which to draw isocontours, or 'auto' (default = 'auto')
   'facealpha'    = scalar, between 0 and 1 (default = 1)
   'refine'       = scalar, number of refinement steps for the triangulation, to get a smoother interpolation (default = 0)

 See also FT_PLOT_TOPO, FT_PLOT_SENS, FT_TOPOPLOTER, FT_TOPOPLOTTFR
```
