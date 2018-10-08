---
layout: default
---

##  FT_COMPUTE_LEADFIELD

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_compute_leadfield".

`<html>``<pre>`
    `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>` computes a forward solution for a dipole in a a volume
    conductor model. The forward solution is expressed as the leadfield
    matrix (Nchan*3), where each column corresponds with the potential or field
    distributions on all sensors for one of the x,y,z-orientations of the
    dipole.
 
    Use as
    [lf] = ft_compute_leadfield(dippos, sens, headmodel, ...)
    with input arguments
    dippos       = position dipole (1*3 or Ndip*3)
    sens      = structure with gradiometer or electrode definition
    headmodel = structure with volume conductor definition
 
    The headmodel represents a volume conductor model, its contents
    depend on the type of model. The sens structure represents a sensor
    array, i.e. EEG electrodes or MEG gradiometers.
 
    It is possible to compute a simultaneous forward solution for EEG and MEG
    by specifying sens and grad as two cell-arrays, e.g.
    sens       = {senseeg, sensmeg}
    headmodel  = {voleeg,  volmeg}
    This results in the computation of the leadfield of the first element of
    sens and headmodel, followed by the second, etc. The leadfields of the
    different imaging modalities are subsequently concatenated.
 
    Additional input arguments can be specified as key-value pairs, supported
    optional arguments are
    'reducerank'      = 'no' or number
    'normalize'       = 'no', 'yes' or 'column'
    'normalizeparam'  = parameter for depth normalization (default = 0.5)
    'weight'          = number or 1xN vector, weight for each dipole position (default = 1)
    'backproject'     = 'yes' (default) or 'no', in the case of a rank reduction
                        this parameter determines whether the result will be
                        backprojected onto the original subspace
 
    The leadfield weight may be used to specify a (normalized)
    corresponding surface area for each dipole, e.g. when the dipoles
    represent a folded cortical surface with varying triangle size.
 
    Depending on the specific input arguments for the sensor and volume, this
    function will select the appropriate low-level EEG or MEG forward model.
    The leadfield matrix for EEG will have an average reference over all the
    electrodes.
 
    The supported forward solutions for MEG are
    single sphere (Cuffin and Cohen, 1977)
    multiple spheres with one sphere per channel (Huang et al, 1999)
    realistic single shell using superposition of basis functions (Nolte, 2003)
    leadfield interpolation using a precomputed grid
    boundary element method (BEM)
 
    The supported forward solutions for EEG are
    single sphere
    multiple concentric spheres (up to 4 spheres)
    leadfield interpolation using a precomputed grid
    boundary element method (BEM)
 
    See also `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_headmodel_asa>``<font color=green>`FT_HEADMODEL_ASA`</font>``</a>`, `<a href=/reference/ft_headmodel_bemcp>``<font color=green>`FT_HEADMODEL_BEMCP`</font>``</a>`,
    `<a href=/reference/ft_headmodel_concentricspheres>``<font color=green>`FT_HEADMODEL_CONCENTRICSPHERES`</font>``</a>`, `<a href=/reference/ft_headmodel_dipoli>``<font color=green>`FT_HEADMODEL_DIPOLI`</font>``</a>`, `<a href=/reference/ft_headmodel_halfspace>``<font color=green>`FT_HEADMODEL_HALFSPACE`</font>``</a>`,
    `<a href=/reference/ft_headmodel_infinite>``<font color=green>`FT_HEADMODEL_INFINITE`</font>``</a>`, `<a href=/reference/ft_headmodel_localspheres>``<font color=green>`FT_HEADMODEL_LOCALSPHERES`</font>``</a>`, `<a href=/reference/ft_headmodel_openmeeg>``<font color=green>`FT_HEADMODEL_OPENMEEG`</font>``</a>`,
    `<a href=/reference/ft_headmodel_singleshell>``<font color=green>`FT_HEADMODEL_SINGLESHELL`</font>``</a>`, `<a href=/reference/ft_headmodel_singlesphere>``<font color=green>`FT_HEADMODEL_SINGLESPHERE`</font>``</a>`,
    `<a href=/reference/ft_headmodel_halfspace>``<font color=green>`FT_HEADMODEL_HALFSPACE`</font>``</a>`
`</pre>``</html>`

