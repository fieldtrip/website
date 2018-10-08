---
layout: default
---

##  FT_SELECT_POINT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_select_point".

`<html>``<pre>`
    `<a href=/reference/ft_select_point>``<font color=green>`FT_SELECT_POINT`</font>``</a>` helper function for selecting a one or multiple points in the
    current figure using the mouse. It returns a list of the [x y] coordinates of the
    selected points.
 
    Use as
    [selected] = ft_select_point(pos, ...)
 
    Optional input arguments should come in key-value pairs and can include
    'multiple'   = true/false, make multiple selections, pressing "q" on the keyboard finalizes the selection (default = false)
    'nearest'    = true/false (default = true)
 
    Example
    pos = randn(10,2);
    figure
    plot(pos(:,1), pos(:,2), '.')
    ft_select_point(pos)
 
    See also `<a href=/reference/ft_select_box>``<font color=green>`FT_SELECT_BOX`</font>``</a>`, `<a href=/reference/ft_select_channel>``<font color=green>`FT_SELECT_CHANNEL`</font>``</a>`, `<a href=/reference/ft_select_point3d>``<font color=green>`FT_SELECT_POINT3D`</font>``</a>`, `<a href=/reference/ft_select_range>``<font color=green>`FT_SELECT_RANGE`</font>``</a>`, `<a href=/reference/ft_select_voxel>``<font color=green>`FT_SELECT_VOXEL`</font>``</a>` 
`</pre>``</html>`

