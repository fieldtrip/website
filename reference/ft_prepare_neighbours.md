---
title: ft_prepare_neighbours
---
```
 FT_PREPARE_NEIGHBOURS finds the channel neighbours for spatial clustering or
 interpolation of bad channels. Using the 'distance' method, neighbours are based on
 a minimum neighbourhood distance (in cfg.neighbourdist). Using the 'triangulation'
 method calculates a triangulation based on a 2D projection of the sensor positions.
 The 'template' method loads a default template for the given data type.

 Use as
   neighbours = ft_prepare_neighbours(cfg)
 or
   neighbours = ft_prepare_neighbours(cfg, data)
 with an input data structure with the channels of interest and that contains a
 sensor description.

 The configuration can contain
   cfg.method        = 'distance', 'triangulation' or 'template'
   cfg.template      = name of the template file, e.g. CTF275_neighb.mat
   cfg.neighbourdist = number, maximum distance between neighbouring sensors (only for 'distance')
   cfg.channel       = channels for which neighbours should be found
   cfg.feedback      = 'yes' or 'no' (default = 'no')

 The 3D sensor positions can be present in the data or can be specified as
   cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS
   cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS

 The 2D channel positions can be specified as
   cfg.layout        = filename of the layout, see FT_PREPARE_LAYOUT

 The output is an array of structures with the "neighbours" which is
 structured like this:
        neighbours(1).label = 'Fz';
        neighbours(1).neighblabel = {'Cz', 'F3', 'F3A', 'FzA', 'F4A', 'F4'};
        neighbours(2).label = 'Cz';
        neighbours(2).neighblabel = {'Fz', 'F4', 'RT', 'RTP', 'P4', 'Pz', 'P3', 'LTP', 'LT', 'F3'};
        neighbours(3).label = 'Pz';
        neighbours(3).neighblabel = {'Cz', 'P4', 'P4P', 'Oz', 'P3P', 'P3'};
        etc.

 Note that a channel is not considered to be a neighbour of itself.

 See also FT_NEIGHBOURPLOT, FT_PREPARE_LAYOUT, FT_DATATYPE_SENS, FT_READ_SENS
```
