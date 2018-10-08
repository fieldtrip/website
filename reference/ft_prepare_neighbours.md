---
layout: default
---

##  FT_PREPARE_NEIGHBOURS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_prepare_neighbours".

`<html>``<pre>`
    `<a href=/reference/ft_prepare_neighbours>``<font color=green>`FT_PREPARE_NEIGHBOURS`</font>``</a>` finds the neighbours of the channels based on three
    different methods. Using the 'distance'-method, prepare_neighbours is
    based on a minimum neighbourhood distance (in cfg.neighbourdist). The
    'triangulation'-method calculates a triangulation based on a
    two-dimenstional projection of the sensor position. The 'template'-method
    loads a default template for the given data type. prepare_neighbours
    should be verified using cfg.feedback ='yes' or by calling
    ft_neighbourplot
 
    The positions of the channel are specified in a gradiometer or electrode configuration or
    from a layout. The sensor configuration can be passed into this function in three way
   (1) in a configuration field,
   (2) in a file whose name is passed in a configuration field, and that can be imported using `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`, or
   (3) in a data field.
 
    Use as
    neighbours = ft_prepare_neighbours(cfg, data)
 
    The configuration can contain
    cfg.method        = 'distance', 'triangulation' or 'template'
    cfg.neighbourdist = number, maximum distance between neighbouring sensors (only for 'distance')
    cfg.template      = name of the template file, e.g. CTF275_neighb.mat
    cfg.layout        = filename of the layout, see `<a href=/reference/ft_prepare_layout>``<font color=green>`FT_PREPARE_LAYOUT`</font>``</a>`
    cfg.channel       = channels for which neighbours should be found
    cfg.feedback      = 'yes' or 'no' (default = 'no')
 
    The EEG or MEG sensor positions can be present in the data or can be specified as
    cfg.elec          = structure with electrode positions, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    cfg.grad          = structure with gradiometer definition, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    cfg.elecfile      = name of file containing the electrode positions, see `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`
    cfg.gradfile      = name of file containing the gradiometer definition, see `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`
 
    The output is an array of structures with the "neighbours" which is
    structured like thi
         neighbours(1).label = 'Fz';
         neighbours(1).neighblabel = {'Cz', 'F3', 'F3A', 'FzA', 'F4A', 'F4'};
         neighbours(2).label = 'Cz';
         neighbours(2).neighblabel = {'Fz', 'F4', 'RT', 'RTP', 'P4', 'Pz', 'P3', 'LTP', 'LT', 'F3'};
         neighbours(3).label = 'Pz';
         neighbours(3).neighblabel = {'Cz', 'P4', 'P4P', 'Oz', 'P3P', 'P3'};
         etc.
    Note that a channel is not considered to be a neighbour of itself.
 
    See also `<a href=/reference/ft_neighbourplot>``<font color=green>`FT_NEIGHBOURPLOT`</font>``</a>`
`</pre>``</html>`

