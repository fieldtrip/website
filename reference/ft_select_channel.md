---
layout: default
---

##  FT_SELECT_CHANNEL

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_select_channel".

`<html>``<pre>`
    `<a href=/reference/ft_select_channel>``<font color=green>`FT_SELECT_CHANNEL`</font>``</a>` is a helper function that can be used as callback function
    in a figure. It allows the user to select a channel. The channel labels
    are returned.
 
    Use as
    label = ft_select_channel(h, eventdata, ...)
    The first two arguments are automatically passed by MATLAB to any
    callback function.
 
    Additional options should be specified in key-value pairs and can be
    'callback'  = function handle to be executed after channels have been selected
 
    You can pass additional arguments to the callback function in a cell-array
    like {@function_handle,arg1,arg2}
 
    Example 1
    % create a figure
    figure
    cfg = [];
    cfg.channel = {'chan1', 'chan2', 'chan3', 'chan4'};
    cfg.layout  = 'ordered';
    lay = ft_prepare_layout(cfg);
    ft_plot_lay(lay)
 
    % add the required guidata
    info       = guidata(gcf)
    info.x     = lay.pos(:,1);
    info.y     = lay.pos(:,2);
    info.label = lay.label
    guidata(gcf, info)
 
    % add this function as the callback to make a single selection
    set(gcf, 'WindowButtonDownFcn', {@ft_select_channel, 'callback', @disp})
 
    % or to make multiple selections
    set(gcf, 'WindowButtonDownFcn',   {@ft_select_channel, 'multiple', true, 'callback', @disp, 'event', 'WindowButtonDownFcn'})
    set(gcf, 'WindowButtonUpFcn',     {@ft_select_channel, 'multiple', true, 'callback', @disp, 'event', 'WindowButtonDownFcn'})
    set(gcf, 'WindowButtonMotionFcn', {@ft_select_channel, 'multiple', true, 'callback', @disp, 'event', 'WindowButtonDownFcn'})
 
    Example 2 (executed from within a subplot
    % create a figure
    figure
    subplot(2,2,1)
    cfg = [];
    cfg.channel = {'chan1', 'chan2', 'chan3', 'chan4'};
    cfg.layout  = 'ordered';
    lay = ft_prepare_layout(cfg);
    ft_plot_lay(lay) 
 
    % add the channel information to guidata under identifier linked to this axis
    ident              = ['axh' num2str(round(sum(clock.*1e6)))]; % unique identifier for this axis
    set(gca,'tag',ident);
    info               = guidata(gcf);
    info.(ident).x     = lay.pos(:, 1);
    info.(ident).y     = lay.pos(:, 2);
    info.(ident).label = lay.label;
    guidata(gcf, info)
 
    % add this function as the callback to make a single selection
    set(gcf, 'WindowButtonDownFcn', {@ft_select_channel, 'callback', @disp})
 
    % or to make multiple selections
    set(gcf, 'WindowButtonDownFcn',   {@ft_select_channel, 'multiple', true, 'callback', @disp, 'event', 'WindowButtonDownFcn'})
    set(gcf, 'WindowButtonUpFcn',     {@ft_select_channel, 'multiple', true, 'callback', @disp, 'event', 'WindowButtonDownFcn'})
    set(gcf, 'WindowButtonMotionFcn', {@ft_select_channel, 'multiple', true, 'callback', @disp, 'event', 'WindowButtonDownFcn'})
       
 
    Subsequently you can click in the figure and you'll see that the disp
    function is executed as callback and that it displays the selected
    channels.
 
    See also `<a href=/reference/ft_select_box>``<font color=green>`FT_SELECT_BOX`</font>``</a>`, `<a href=/reference/ft_select_point>``<font color=green>`FT_SELECT_POINT`</font>``</a>`, `<a href=/reference/ft_select_point3d>``<font color=green>`FT_SELECT_POINT3D`</font>``</a>`, `<a href=/reference/ft_select_range>``<font color=green>`FT_SELECT_RANGE`</font>``</a>`, `<a href=/reference/ft_select_voxel>``<font color=green>`FT_SELECT_VOXEL`</font>``</a>` 
`</pre>``</html>`

