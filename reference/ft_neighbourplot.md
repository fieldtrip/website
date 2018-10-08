---
layout: default
---

##  FT_NEIGHBOURPLOT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_neighbourplot".

`<html>``<pre>`
    `<a href=/reference/ft_neighbourplot>``<font color=green>`FT_NEIGHBOURPLOT`</font>``</a>` visualizes neighbouring channels in a particular channel
    configuration. The positions of the channel are specified in a
    gradiometer or electrode configuration or from a layout.
 
    Use as
    ft_neighbourplot(cfg)
    or as
    ft_neighbourplot(cfg, data)
 
    where the configuration can contain
    cfg.verbose       = string, 'yes' or 'no', whether the function will print feedback text in the command window
    cfg.neighbours    = neighbourhood structure, see `<a href=/reference/ft_prepare_neighbours>``<font color=green>`FT_PREPARE_NEIGHBOURS`</font>``</a>` (optional)
    cfg.visible       = string, 'on' or 'off', whether figure will be visible (default = 'on')
    cfg.enableedit    = string, 'yes' or 'no', allows the user to flexibly add or remove edges between vertices (default = 'no')
                        
    and either one of the following options
    cfg.layout        = filename of the layout, see `<a href=/reference/ft_prepare_layout>``<font color=green>`FT_PREPARE_LAYOUT`</font>``</a>`
    cfg.elec          = structure with electrode definition
    cfg.grad          = structure with gradiometer definition
    cfg.elecfile      = filename containing electrode definition
    cfg.gradfile      = filename containing gradiometer definition
 
    If cfg.neighbours is not defined, this function will call
    `<a href=/reference/ft_prepare_neighbours>``<font color=green>`FT_PREPARE_NEIGHBOURS`</font>``</a>` to determine the channel neighbours. The
    following data fields may also be used by `<a href=/reference/ft_prepare_neighbours>``<font color=green>`FT_PREPARE_NEIGHBOURS`</font>``</a>`
    data.elec     = structure with EEG electrode positions
    data.grad     = structure with MEG gradiometer positions
    If cfg.neighbours is empty, no neighbouring sensors are assumed.
 
    Use cfg.enableedit to create or extend your own neighbourtemplate
 
    See also `<a href=/reference/ft_prepare_neighbours>``<font color=green>`FT_PREPARE_NEIGHBOURS`</font>``</a>`, `<a href=/reference/ft_prepare_layout>``<font color=green>`FT_PREPARE_LAYOUT`</font>``</a>`
`</pre>``</html>`

