---
title: ft_select_box
---
```
 FT_SELECT_BOX helper function for selecting a rectangular region
 in the current figure using the mouse.

 Use as
   [x, y] = ft_select_box(...)

 It returns a 2-element vector x and a 2-element vector y
 with the corners of the selected region.

 Optional input arguments should come in key-value pairs and can include
   'multiple' = true/false, make multiple selections by dragging, clicking
                in one will finalize the selection (default = false)

 See also FT_SELECT_CHANNEL, FT_SELECT_POINT, FT_SELECT_POINT3D, FT_SELECT_RANGE, FT_SELECT_VOXEL 
```
