---
layout: default
---

##  FT_DIPOLEFITTING

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_dipolefitting".

`<html>``<pre>`
    `<a href=/reference/ft_dipolefitting>``<font color=green>`FT_DIPOLEFITTING`</font>``</a>` perform grid search and non-linear fit with one or multiple
    dipoles and try to find the location where the dipole model is best able
    to explain the measured EEG or MEG topography.
 
    This function will initially scan the whole brain with a single dipole on
    a regular coarse grid, and subsequently start at the most optimal location
    with a non-linear search. Alternatively you can specify the initial
    location of the dipole(s) and the non-linear search will start from there.
 
    Use as
    [source] = ft_dipolefitting(cfg, data)
 
    The configuration has the following general fields
    cfg.numdipoles  = number, default is 1
    cfg.symmetry    = 'x', 'y' or 'z' symmetry for two dipoles, can be empty (default = [])
    cfg.channel     = Nx1 cell-array with selection of channels (default = 'all'),
                      see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.gridsearch  = 'yes' or 'no', perform global search for initial
                      guess for the dipole parameters (default = 'yes')
    cfg.nonlinear   = 'yes' or 'no', perform nonlinear search for optimal
                      dipole parameters (default = 'yes')
 
    If you start with a grid search, the complete grid with dipole
    positions and optionally precomputed leadfields should be specified
    cfg.grid            = structure, see `<a href=/reference/ft_prepare_sourcemodel>``<font color=green>`FT_PREPARE_SOURCEMODEL`</font>``</a>` or `<a href=/reference/ft_prepare_leadfield>``<font color=green>`FT_PREPARE_LEADFIELD`</font>``</a>`
    The positions of the dipoles can be specified as a regular 3-D
    grid that is aligned with the axes of the head coordinate system
    cfg.grid.xgrid      = vector (e.g. -20:1:20) or 'auto' (default = 'auto')
    cfg.grid.ygrid      = vector (e.g. -20:1:20) or 'auto' (default = 'auto')
    cfg.grid.zgrid      = vector (e.g.   0:1:20) or 'auto' (default = 'auto')
    cfg.grid.resolution = number (e.g. 1 cm) for automatic grid generation
    cfg.grid.inside     = N*1 vector with boolean value whether grid point is inside brain (optional)
    cfg.grid.dim        = [Nx Ny Nz] vector with dimensions in case of 3-D grid (optional)
    If the source model destribes a triangulated cortical sheet, it is described as
    cfg.grid.pos        = N*3 matrix with the vertex positions of the cortical sheet
    cfg.grid.tri        = M*3 matrix that describes the triangles connecting the vertices
    Alternatively the position of a few dipoles at locations of interest can be
    specified, for example obtained from an anatomical or functional MRI
    cfg.grid.pos        = N*3 matrix with position of each source
 
    If you do not start with a grid search, you have to give a starting location
    for the nonlinear search
    cfg.dip.pos     = initial dipole position, matrix of Ndipoles x 3
 
    The conventional approach is to fit dipoles to event-related averages, which
    within FieldTrip can be obtained from the `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>` or from
    the `<a href=/reference/ft_timelockgrandaverage>``<font color=green>`FT_TIMELOCKGRANDAVERAGE`</font>``</a>` function. This has the additional options
    cfg.latency     = [begin end] in seconds or 'all' (default = 'all')
    cfg.model       = 'moving' or 'regional'
    A moving dipole model has a different position (and orientation) for each
    timepoint, or for each component. A regional dipole model has the same
    position for each timepoint or component, and a different orientation.
 
    You can also fit dipoles to the spatial topographies of an independent
    component analysis, obtained from the `<a href=/reference/ft_componentanalysis>``<font color=green>`FT_COMPONENTANALYSIS`</font>``</a>` function.
    This has the additional options
    cfg.component   = array with numbers (can be empty -&gt; all)
 
    You can also fit dipoles to the spatial topographies that are present
    in the data in the frequency domain, which can be obtained using the
    `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>` function. This has the additional options
    cfg.frequency   = single number (in Hz)
 
    Low level details of the fitting can be specified in the cfg.dipfit structure
    cfg.dipfit.display  = level of display, can be 'off', 'iter', 'notify' or 'final' (default = 'iter')
    cfg.dipfit.optimfun = function to use, can be 'fminsearch' or 'fminunc' (default is determined automatic)
    cfg.dipfit.maxiter  = maximum number of function evaluations allowed (default depends on the optimfun)
 
    Optionally, you can modify the leadfields by reducing the rank, i.e. remove the weakest orientation
    cfg.reducerank      = 'no', or number (default = 3 for EEG, 2 for MEG)
 
 
    The volume conduction model of the head should be specified as
    cfg.headmodel     = structure with volume conduction model, see `<a href=/reference/ft_prepare_headmodel>``<font color=green>`FT_PREPARE_HEADMODEL`</font>``</a>`
 
    The EEG or MEG sensor positions can be present in the data or can be specified as
    cfg.elec          = structure with electrode positions, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    cfg.grad          = structure with gradiometer definition, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    cfg.elecfile      = name of file containing the electrode positions, see `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`
    cfg.gradfile      = name of file containing the gradiometer definition, see `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, `<a href=/reference/ft_prepare_leadfield>``<font color=green>`FT_PREPARE_LEADFIELD`</font>``</a>`, `<a href=/reference/ft_prepare_headmodel>``<font color=green>`FT_PREPARE_HEADMODEL`</font>``</a>`
`</pre>``</html>`

