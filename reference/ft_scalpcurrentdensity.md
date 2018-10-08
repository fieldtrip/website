---
layout: default
---

##  FT_SCALPCURRENTDENSITY

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_scalpcurrentdensity".

`<html>``<pre>`
    `<a href=/reference/ft_scalpcurrentdensity>``<font color=green>`FT_SCALPCURRENTDENSITY`</font>``</a>` computes an estimate of the SCD using the
    second-order derivative (the surface Laplacian) of the EEG potential
    distribution
 
    The relation between the surface Laplacian and the SCD is explained
    in more detail on http://tinyurl.com/ptovowl.
 
    Use as
    [data] = ft_scalpcurrentdensity(cfg, data)
    or
    [timelock] = ft_scalpcurrentdensity(cfg, timelock)
    where the input data is obtained from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>` or from
    `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`. The output data has the same format as the input
    and can be used in combination with most other FieldTrip functions
    such as FT_FREQNALYSIS or `<a href=/reference/ft_topoplotER>``<font color=green>`FT_TOPOPLOTER`</font>``</a>`.
 
    The configuration should contain
    cfg.method       = 'finite' for finite-difference method or
                       'spline' for spherical spline method
                       'hjorth' for Hjorth approximation method
    cfg.elecfile     = string, file containing the electrode definition
    cfg.elec         = structure with electrode definition
    cfg.trials       = 'all' or a selection given as a 1xN vector (default = 'all')
    cfg.feedback     = string, 'no', 'text', 'textbar', 'gui' (default = 'text')
 
    The finite method require the following
    cfg.conductivity = conductivity of the skin (default = 0.33 S/m)
 
    The spline and finite method require the following
    cfg.conductivity = conductivity of the skin (default = 0.33 S/m)
    cfg.lambda       = regularization parameter (default = 1e-05)
    cfg.order        = order of the splines (default = 4)
    cfg.degree       = degree of legendre polynomials (default for
                        &lt;=32 electrodes  = 9,
                        &lt;=64 electrodes  = 14,
                        &lt;=128 electrodes = 20,
                        else             = 32
 
    The hjorth method requires the following
    cfg.neighbours   = neighbourhood structure, see `<a href=/reference/ft_prepare_neighbours>``<font color=green>`FT_PREPARE_NEIGHBOURS`</font>``</a>`
 
    Note that the skin conductivity, electrode dimensions and the potential
    all have to be expressed in the same SI units, otherwise the units of
    the SCD values are not scaled correctly. The spatial distribution still
    will be correct.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    The 'finite' method implements
    TF Oostendorp, A van Oosterom; The surface Laplacian of the potentia
    theory and application. IEEE Trans Biomed Eng, 43(4): 394-405, 1996.
    G Huiskamp; Difference formulas for the surface Laplacian on a
    triangulated sphere. Journal of Computational Physics, 2(95): 477-496,
    1991.
 
    The 'spline' method implements
    F. Perrin, J. Pernier, O. Bertrand, and J. F. Echallier.
    Spherical splines for scalp potential and curernt density mapping.
    Electroencephalogr Clin Neurophysiol, 72:184-187, 1989
    including their corrections in
    F. Perrin, J. Pernier, O. Bertrand, and J. F. Echallier.
    Corrigenda: EEG 02274, Electroencephalography and Clinical
    Neurophysiology 76:565.
 
    The 'hjorth' method implements
    B. Hjort; An on-line transformation of EEG scalp potentials into
    orthogonal source derivation. Electroencephalography and Clinical
    Neurophysiology 39:526-530, 1975.
 
    See also `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`, `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`, FT_FREQNALYSIS, `<a href=/reference/ft_topoplotER>``<font color=green>`FT_TOPOPLOTER`</font>``</a>`.
`</pre>``</html>`

