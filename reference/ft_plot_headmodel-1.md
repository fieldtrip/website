---
title: ft_plot_headmodel
---
```
 FT_PLOT_HEADMODEL visualizes the boundaries in the volume conduction model of the head as
 specified in the headmodel structure

 Use as
   hs = ft_plot_headmodel(headmodel, varargin)

 Optional arguments should come in key-value pairs and can include
   'facecolor'    = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of faces
   'vertexcolor'  = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of vertices
   'edgecolor'    = [r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r'
   'faceindex'    = true or false
   'vertexindex'  = true or false
   'facealpha'    = transparency, between 0 and 1 (default = 1)
   'edgealpha'    = transparency, between 0 and 1 (default = 1)
   'surfaceonly'  = true or false, plot only the outer surface of a hexahedral or tetrahedral mesh (default = false)
   'unit'         = string, convert to the specified geometrical units (default = [])
   'grad'         = gradiometer array, used in combination with local spheres model

 Example
   headmodel   = [];
   headmodel.r = [86 88 92 100];
   headmodel.o = [0 0 40];
   figure, ft_plot_headmodel(headmodel)

 See also FT_PREPARE_HEADMODEL, FT_PLOT_MESH, FT_PLOT_SENS
```
