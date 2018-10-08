---
layout: default
---

##  FT_INTERACTIVEREALIGN

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_interactiverealign".

`<html>``<pre>`
    `<a href=/reference/ft_interactiverealign>``<font color=green>`FT_INTERACTIVEREALIGN`</font>``</a>` allows the user to interactively translate, rotate and scale an
    individual geometrical object to a template geometrical object. It can for example be used
    to align EEG electrodes to a model of the scalp surface.
 
    Use as
    [cfg] = ft_interactiverealign(cfg)
 
    The configuration structure should contain the individuals geometrical object that
    has to be realigned
    cfg.individual.elec           = structure
    cfg.individual.grad           = structure
    cfg.individual.headmodel      = structure, see `<a href=/reference/ft_prepare_headmodel>``<font color=green>`FT_PREPARE_HEADMODEL`</font>``</a>`
    cfg.individual.headshape      = structure, see `<a href=/reference/ft_read_headshape>``<font color=green>`FT_READ_HEADSHAPE`</font>``</a>`
    cfg.individual.mri            = structure, see `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>`
    You can specify the style with which the objects are displayed using
    cfg.individual.headmodelstyle = 'vertex', 'edge', 'surface' or 'both' (default = 'edge')
    cfg.individual.headshapestyle = 'vertex', 'edge', 'surface' or 'both' (default = 'vertex')
 
    The configuration structure should also contain the geometrical object of a
    template that serves as target
    cfg.template.axes           = string, 'yes' or 'no (default = 'no')
    cfg.template.elec           = structure
    cfg.template.grad           = structure
    cfg.template.headmodel      = structure, see `<a href=/reference/ft_prepare_headmodel>``<font color=green>`FT_PREPARE_HEADMODEL`</font>``</a>`
    cfg.template.headshape      = structure, see `<a href=/reference/ft_read_headshape>``<font color=green>`FT_READ_HEADSHAPE`</font>``</a>`
    cfg.template.mri            = structure, see `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>`
    You can specify the style with which the objects are displayed using
    cfg.template.headmodelstyle = 'vertex', 'edge', 'surface' or 'both' (default = 'edge')
    cfg.template.headshapestyle = 'vertex', 'edge', 'surface' or 'both' (default = 'vertex')
 
    You can specify one or multiple individual objects which will all be realigned and
    one or multiple template objects.
 
    See also `<a href=/reference/ft_volumerealign>``<font color=green>`FT_VOLUMEREALIGN`</font>``</a>`, `<a href=/reference/ft_electroderealign>``<font color=green>`FT_ELECTRODEREALIGN`</font>``</a>`, `<a href=/reference/ft_determine_coordsys>``<font color=green>`FT_DETERMINE_COORDSYS`</font>``</a>`,
    `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`, `<a href=/reference/ft_read_vol>``<font color=green>`FT_READ_VOL`</font>``</a>`, `<a href=/reference/ft_read_headshape>``<font color=green>`FT_READ_HEADSHAPE`</font>``</a>`
`</pre>``</html>`

