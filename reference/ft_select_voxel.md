---
layout: default
---

##  FT_SELECT_VOXEL

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_select_voxel".

`<html>``<pre>`
    `<a href=/reference/ft_select_voxel>``<font color=green>`FT_SELECT_VOXEL`</font>``</a>` is a helper function that can be used as callback function
    in a figure. It allows the user to select a voxel from a (resliced) 3-D volume.
 
    Use as
    voxel = ft_select_voxel(h, eventdata, ...)
    The first two arguments are automatically passed by MATLAB to any
    callback function.
 
    Additional options should be specified in key-value pairs and can be
    'callback'  = function handle to be executed after channels have been selected
 
    You can pass additional arguments to the callback function in a cell-array
    like {@function_handle,arg1,arg2}
 
    Example
    % create a figure with a random 3-D volume
    mri = rand(128,128,128);
    ft_plot_slice(mri, 'location', [64 64 64], 'orientation', [1 1 1]);
    view(120,30)
    xlabel('x'); ylabel('y'); zlabel('z'); grid on
    axis([0 128 0 128 0 128])
    axis equal; axis vis3d
    axis([0 128 0 128 0 128])
 
    % add this function as the callback to make a single selection
    set(gcf, 'WindowButtonDownFcn', {@ft_select_voxel, 'callback', @disp})
 
    Subsequently you can click in the figure and you'll see that the disp
    function is executed as callback and that it displays the selected
    voxel.
 
    See also `<a href=/reference/ft_select_box>``<font color=green>`FT_SELECT_BOX`</font>``</a>`, `<a href=/reference/ft_select_channel>``<font color=green>`FT_SELECT_CHANNEL`</font>``</a>`, `<a href=/reference/ft_select_point>``<font color=green>`FT_SELECT_POINT`</font>``</a>`, `<a href=/reference/ft_select_point3d>``<font color=green>`FT_SELECT_POINT3D`</font>``</a>`, `<a href=/reference/ft_select_range>``<font color=green>`FT_SELECT_RANGE`</font>``</a>`
`</pre>``</html>`

