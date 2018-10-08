---
layout: default
---

##  FT_DIPOLESIMULATION

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_dipolesimulation".

`<html>``<pre>`
    `<a href=/reference/ft_dipolesimulation>``<font color=green>`FT_DIPOLESIMULATION`</font>``</a>` computes the field or potential of a simulated dipole
    and returns a datastructure identical to the `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>` function.
 
    Use as
    data = ft_dipolesimulation(cfg)
 
    The dipoles position and orientation have to be specified with
    cfg.dip.pos     = [Rx Ry Rz] (size Nx3)
    cfg.dip.mom     = [Qx Qy Qz] (size 3xN)
 
    The timecourse of the dipole activity is given as a single vector or as a
    cell-array with one vectors per trial
    cfg.dip.signal
    or by specifying a sine-wave signal
    cfg.dip.frequency    in Hz
    cfg.dip.phase        in radians
    cfg.dip.amplitude    per dipole
    cfg.ntrials          number of trials
    cfg.triallength      time in seconds
    cfg.fsample          sampling frequency in Hz
 
    Random white noise can be added to the data in each trial, either by
    specifying an absolute or a relative noise level
    cfg.relnoise    = add noise with level relative to simulated signal
    cfg.absnoise    = add noise with absolute level
    cfg.randomseed  = 'yes' or a number or vector with the seed value (default = 'yes')
 
    Optional input arguments are
    cfg.channel    = Nx1 cell-array with selection of channels (default = 'all'),
                     see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.dipoleunit = units for dipole amplitude (default nA*m)
    cfg.chanunit   = units for the channel data
 
    The volume conduction model of the head should be specified as
    cfg.headmodel     = structure with volume conduction model, see `<a href=/reference/ft_prepare_headmodel>``<font color=green>`FT_PREPARE_HEADMODEL`</font>``</a>`
 
    The EEG or MEG sensor positions should be specified as
    cfg.elec          = structure with electrode positions, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    cfg.grad          = structure with gradiometer definition, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    cfg.elecfile      = name of file containing the electrode positions, see `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`
    cfg.gradfile      = name of file containing the gradiometer definition, see `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`
 
    See also `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, `<a href=/reference/ft_dipolefitting>``<font color=green>`FT_DIPOLEFITTING`</font>``</a>`, `<a href=/reference/ft_timelocksimulation>``<font color=green>`FT_TIMELOCKSIMULATION`</font>``</a>`,
    `<a href=/reference/ft_freqsimulation>``<font color=green>`FT_FREQSIMULATION`</font>``</a>`, `<a href=/reference/ft_connectivitysimulation>``<font color=green>`FT_CONNECTIVITYSIMULATION`</font>``</a>`
`</pre>``</html>`

