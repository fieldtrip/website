---
title: ft_neighbourplot
---
```
 FT_NEIGHBOURPLOT visualizes neighbouring channels in a particular channel
 configuration. The positions of the channel are specified in a
 gradiometer or electrode configuration or from a layout.

 Use as
   ft_neighbourplot(cfg)
 or as
   ft_neighbourplot(cfg, data)

 Where the configuration can contain
   cfg.verbose       = string, 'yes' or 'no', whether the function will print feedback text in the command window
   cfg.neighbours    = neighbourhood structure, see FT_PREPARE_NEIGHBOURS (optional)
   cfg.visible       = string, 'on' or 'off', whether figure will be visible (default = 'on')
   cfg.enableedit    = string, 'yes' or 'no', allows you to interactively add or remove edges between vertices (default = 'no')

 and either one of the following options
   cfg.layout        = filename of the layout, see FT_PREPARE_LAYOUT
   cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS
   cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS
   cfg.opto          = structure with gradiometer definition or filename, see FT_READ_SENS

 If cfg.neighbours is not defined, this function will call
 FT_PREPARE_NEIGHBOURS to determine the channel neighbours. The
 following data fields may also be used by FT_PREPARE_NEIGHBOURS
   data.elec         = structure with electrode positions
   data.grad         = structure with gradiometer definition
   data.opto         = structure with optode definition

 If cfg.neighbours is empty, no neighbouring sensors are assumed.

 Use cfg.enableedit to interactively add or remove edges in your own neighbour structure.

 See also FT_PREPARE_NEIGHBOURS, FT_PREPARE_LAYOUT
```
