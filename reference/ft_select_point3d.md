---
layout: default
---

##  FT_SELECT_POINT3D

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_select_point3d".

`<html>``<pre>`
    `<a href=/reference/ft_select_point3d>``<font color=green>`FT_SELECT_POINT3D`</font>``</a>` helper function for selecting one or multiple points on a 3D mesh
    using the mouse. It returns a list of the [x y z] coordinates of the selected
    points.
 
    Use as
    [selected] = ft_select_point3d(bnd, ...)
 
    Optional input arguments should come in key-value pairs and can include
    'multiple'    = true/false, make multiple selections, pressing "q" on the keyboard finalizes the selection (default = false)
    'nearest'     = true/false (default = true)
    'marker'      = character or empty, for example '.', 'o' or 'x' (default = [])
    'markersize'  = scalar, the size of the marker (default = 10)
    'markercolor' = character, for example 'r', 'b' or 'g' (default = 'k')
 
    Example
    [pos, tri] = icosahedron162;
    bnd.pos = pos;
    bnd.tri = tri;
    ft_plot_mesh(bnd)
    camlight
    ... do something here
 
    See also `<a href=/reference/ft_select_box>``<font color=green>`FT_SELECT_BOX`</font>``</a>`, `<a href=/reference/ft_select_channel>``<font color=green>`FT_SELECT_CHANNEL`</font>``</a>`, `<a href=/reference/ft_select_point>``<font color=green>`FT_SELECT_POINT`</font>``</a>`, `<a href=/reference/ft_select_range>``<font color=green>`FT_SELECT_RANGE`</font>``</a>`, `<a href=/reference/ft_select_voxel>``<font color=green>`FT_SELECT_VOXEL`</font>``</a>`
`</pre>``</html>`

