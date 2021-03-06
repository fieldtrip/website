---
title: ft_select_box
---
```plaintext
 FT_SELECT_BOX helper function for selecting a single rectangular region in the
 current figure using the mouse. This function is not used as a callabck, but blocks
 the execution of the code until a selection is made.

 Use as
   [x, y] = ft_select_box()

 It returns a 2-element vector x and a 2-element vector y
 with the corners of the selected region.

 See also FT_SELECT_CHANNEL, FT_SELECT_POINT, FT_SELECT_POINT3D, FT_SELECT_RANGE,
 FT_SELECT_VOXEL, GINPUT, RBBOX
```
