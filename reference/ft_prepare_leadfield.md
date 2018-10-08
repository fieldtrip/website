---
layout: default
---

##  FT_PREPARE_LEADFIELD

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_prepare_leadfield".

`<html>``<pre>`
    `<a href=/reference/ft_prepare_leadfield>``<font color=green>`FT_PREPARE_LEADFIELD`</font>``</a>` computes the forward model for many dipole locations
    on a regular 2D or 3D grid and stores it for efficient inverse modelling
 
    Use as
    [grid] = ft_prepare_leadfield(cfg, data);
 
    It is neccessary to input the data on which you want to perform the
    inverse computations, since that data generally contain the gradiometer
    information and information about the channels that should be included in
    the forward model computation. The data structure can be either obtained
    from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`, `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>` or `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`. If the data is empty,
    all channels will be included in the forward model.
 
    The configuration should contain
    cfg.channel            = Nx1 cell-array with selection of channels (default = 'all'),
                             see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
 
    The positions of the sources can be specified as a regular 3-D
    grid that is aligned with the axes of the head coordinate system
    cfg.grid.xgrid      = vector (e.g. -20:1:20) or 'auto' (default = 'auto')
    cfg.grid.ygrid      = vector (e.g. -20:1:20) or 'auto' (default = 'auto')
    cfg.grid.zgrid      = vector (e.g.   0:1:20) or 'auto' (default = 'auto')
    cfg.grid.resolution = number (e.g. 1 cm) for automatic grid generation
    Alternatively the position of a few sources at locations of interest can
    be specified, for example obtained from an anatomical or functional MRI
    cfg.grid.pos        = N*3 matrix with position of each source
    cfg.grid.inside     = N*1 vector with boolean value whether grid point is inside brain (optional)
    cfg.grid.dim        = [Nx Ny Nz] vector with dimensions in case of 3-D grid (optional)
 
    The volume conduction model of the head should be specified as
    cfg.headmodel     = structure with volume conduction model, see `<a href=/reference/ft_prepare_headmodel>``<font color=green>`FT_PREPARE_HEADMODEL`</font>``</a>`
 
    The EEG or MEG sensor positions can be present in the data or can be specified as
    cfg.elec          = structure with electrode positions, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    cfg.grad          = structure with gradiometer definition, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    cfg.elecfile      = name of file containing the electrode positions, see `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`
    cfg.gradfile      = name of file containing the gradiometer definition, see `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`
 
    Optionally, you can modify the leadfields by reducing the rank (i.e.
    remove the weakest orientation), or by normalizing each column.
    cfg.reducerank      = 'no', or number (default = 3 for EEG, 2 for MEG)
    cfg.normalize       = 'yes' or 'no' (default = 'no')
    cfg.normalizeparam  = depth normalization parameter (default = 0.5)
    cfg.backproject     = 'yes' or 'no' (default = 'yes') determines when reducerank is applied
                          whether the lower rank leadfield is projected back onto the original
                          linear subspace, or not.
 
    Depending on the type of headmodel, some additional options may be
    specified. 
 
    For OPENMEEG based headmodel
    cfg.openmeeg.batchsize    = scalar (default 100e3), number of dipoles 
                                for which the leadfield is computed in a 
                                single call to the low-level code. Trades off
                                memory efficiency for speed.
    cfg.openmeeg.dsm          = 'no'/'yes', reuse existing DSM if provided
    cfg.openmeeg.keepdsm      = 'no'/'yes', option to retain DSM (no by default)
    cfg.openmeeg.nonadaptive  = 'no'/'yes'
   
    For SINGLESHELL based headmodel
    cfg.singleshell.batchsize = scalar or 'all' (default 1), number of dipoles
                                for which the leadfield is computed in a 
                                single call to the low-level code. Trades off
                                memory efficiency for speed.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    If you specify this option the input data will be read from a *.mat
    file on disk. This mat files should contain only a single variable named 'data',
    corresponding to the input structure.
 
    See also `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, `<a href=/reference/ft_dipolefitting>``<font color=green>`FT_DIPOLEFITTING`</font>``</a>`, `<a href=/reference/ft_prepare_headmodel>``<font color=green>`FT_PREPARE_HEADMODEL`</font>``</a>`,
    `<a href=/reference/ft_prepare_sourcemodel>``<font color=green>`FT_PREPARE_SOURCEMODEL`</font>``</a>`
`</pre>``</html>`

