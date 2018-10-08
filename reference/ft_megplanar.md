---
layout: default
---

##  FT_MEGPLANAR

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_megplanar".

`<html>``<pre>`
    `<a href=/reference/ft_megplanar>``<font color=green>`FT_MEGPLANAR`</font>``</a>` computes planar MEG gradients gradients for raw data or average
    event-related field data. It can also convert frequency-domain data that was computed
    using `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`, as long as it contains the complex-valued fourierspcrm and not
    only the powspctrm.
 
    Use as
     [interp] = ft_megplanar(cfg, data)
    where the input data corresponds to the output from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`,
    `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>` or `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>` (with output='fourierspcrm').
 
    The configuration should contain
    cfg.planarmethod   = string, can be 'sincos', 'orig', 'fitplane', 'sourceproject' (default = 'sincos')
    cfg.channel        =  Nx1 cell-array with selection of channels (default = 'MEG'), see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.trials         = 'all' or a selection given as a 1xN vector (default = 'all')
 
    The methods orig, sincos and fitplane are all based on a neighbourhood interpolation.
    For these methods you need to specify
    cfg.neighbours     = neighbourhood structure, see `<a href=/reference/ft_prepare_neighbours>``<font color=green>`FT_PREPARE_NEIGHBOURS`</font>``</a>`
 
    In the 'sourceproject' method a minumum current estimate is done using a large number
    of dipoles that are placed in the upper layer of the brain surface, followed by a
    forward computation towards a planar gradiometer array. This requires the
    specification of a volume conduction model of the head and of a source model. The
    'sourceproject' method is not supported for frequency domain data.
 
    A dipole layer representing the brain surface must be specified with
    cfg.inwardshift = depth of the source layer relative to the head model surface (default = 2.5 cm, which is appropriate for a skin-based head model)
    cfg.spheremesh  = number of dipoles in the source layer (default = 642)
    cfg.pruneratio  = for singular values, default is 1e-3
    cfg.headshape   = a filename containing headshape, a structure containing a
                      single triangulated boundary, or a Nx3 matrix with surface
                      points
    If no headshape is specified, the dipole layer will be based on the inner compartment
    of the volume conduction model.
 
    The volume conduction model of the head should be specified as
    cfg.headmodel     = structure with volume conduction model, see `<a href=/reference/ft_prepare_headmodel>``<font color=green>`FT_PREPARE_HEADMODEL`</font>``</a>`
 
    The following cfg fields are optiona
    cfg.feedback
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_combineplanar>``<font color=green>`FT_COMBINEPLANAR`</font>``</a>`, FT_NEIGHBOURSELECTION
`</pre>``</html>`

