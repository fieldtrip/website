---
layout: default
---

##  FT_PREPARE_VOL_SENS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_prepare_vol_sens".

`<html>``<pre>`
    `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>` does some bookkeeping to ensure that the volume
    conductor model and the sensor array are ready for subsequent forward
    leadfield computations. It takes care of some pre-computations that can
    be done efficiently prior to the leadfield calculations.
 
    Use as
    [headmodel, sens] = ft_prepare_vol_sens(headmodel, sens, ...)
    with input arguments
    headmodel  structure with volume conductor definition
    sens       structure with gradiometer or electrode definition
 
    The headmodel structure represents a volume conductor model of the head,
    its contents depend on the type of model. The sens structure represents a
    sensor array, i.e. EEG electrodes or MEG gradiometers.
 
    Additional options should be specified in key-value pairs and can be
    'channel'    cell-array with strings (default = 'all')
    'order'      number, for single shell "Nolte" model (default = 10)
 
    The detailed behaviour of this function depends on whether the input
    consists of EEG or MEG and furthermoree depends on the type of volume
    conductor mode
 1.  in case of EEG single and concentric sphere models, the electrodes are
    projected onto the skin surface.
 2.  in case of EEG boundary element models, the electrodes are projected on
    the surface and a blilinear interpoaltion matrix from vertices to
    electrodes is computed.
 3.  in case of MEG and a localspheres model, a local sphere is determined
    for each coil in the gradiometer definition.
   - in case of MEG with a singleshell Nolte model, the volume conduction
     model is initialized
    In any case channel selection and reordering will be done. The channel
    order returned by this function corresponds to the order in the 'channel'
    option, or if not specified, to the order in the input sensor array.
 
    See also `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`, `<a href=/reference/ft_read_vol>``<font color=green>`FT_READ_VOL`</font>``</a>`, `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`, `<a href=/reference/ft_transform_vol>``<font color=green>`FT_TRANSFORM_VOL`</font>``</a>`,
    `<a href=/reference/ft_transform_sens>``<font color=green>`FT_TRANSFORM_SENS`</font>``</a>`
`</pre>``</html>`

