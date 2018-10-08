---
layout: default
---

##  FT_VOLTYPE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_voltype".

`<html>``<pre>`
    `<a href=/reference/ft_voltype>``<font color=green>`FT_VOLTYPE`</font>``</a>` determines the type of volume conduction model of the head
 
    Use as
    [type] = ft_voltype(headmodel)
    to get a string describing the type, or
    [flag] = ft_voltype(headmodel, desired)
    to get a boolean value.
 
    For EEG the following volume conduction models are recognized
    singlesphere       analytical single sphere model
    concentricspheres  analytical concentric sphere model with up to 4 spheres
    halfspace          infinite homogenous medium on one side, vacuum on the other
    openmeeg           boundary element method, based on the OpenMEEG software
    bemcp              boundary element method, based on the implementation from Christophe Phillips
    dipoli             boundary element method, based on the implementation from Thom Oostendorp
    asa                boundary element method, based on the (commercial) ASA software
    simbio             finite element method, based on the SimBio software
    fns                finite difference method, based on the FNS software
    interpolate        interpolate the potential based on pre-computed leadfields
 
    and for MEG the following volume conduction models are recognized
    singlesphere       analytical single sphere model
    localspheres       local spheres model for MEG, one sphere per channel
    singleshell        realisically shaped single shell approximation, based on the implementation from Guido Nolte
    infinite           magnetic dipole in an infinite vacuum
    interpolate        interpolate the potential based on pre-computed leadfields
 
    See also `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`, `<a href=/reference/ft_read_vol>``<font color=green>`FT_READ_VOL`</font>``</a>`, `<a href=/reference/ft_headmodel_bemcp>``<font color=green>`FT_HEADMODEL_BEMCP`</font>``</a>`,
    `<a href=/reference/ft_headmodel_asa>``<font color=green>`FT_HEADMODEL_ASA`</font>``</a>`, `<a href=/reference/ft_headmodel_dipoli>``<font color=green>`FT_HEADMODEL_DIPOLI`</font>``</a>`, `<a href=/reference/ft_headmodel_simbio>``<font color=green>`FT_HEADMODEL_SIMBIO`</font>``</a>`,
    `<a href=/reference/ft_headmodel_fns>``<font color=green>`FT_HEADMODEL_FNS`</font>``</a>`, `<a href=/reference/ft_headmodel_halfspace>``<font color=green>`FT_HEADMODEL_HALFSPACE`</font>``</a>`, `<a href=/reference/ft_headmodel_infinite>``<font color=green>`FT_HEADMODEL_INFINITE`</font>``</a>`,
    `<a href=/reference/ft_headmodel_openmeeg>``<font color=green>`FT_HEADMODEL_OPENMEEG`</font>``</a>`, `<a href=/reference/ft_headmodel_singlesphere>``<font color=green>`FT_HEADMODEL_SINGLESPHERE`</font>``</a>`,
    `<a href=/reference/ft_headmodel_concentricspheres>``<font color=green>`FT_HEADMODEL_CONCENTRICSPHERES`</font>``</a>`, `<a href=/reference/ft_headmodel_localspheres>``<font color=green>`FT_HEADMODEL_LOCALSPHERES`</font>``</a>`,
    `<a href=/reference/ft_headmodel_singleshell>``<font color=green>`FT_HEADMODEL_SINGLESHELL`</font>``</a>`, `<a href=/reference/ft_headmodel_interpolate>``<font color=green>`FT_HEADMODEL_INTERPOLATE`</font>``</a>`
`</pre>``</html>`

