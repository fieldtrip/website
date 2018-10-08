---
layout: default
---

##  FT_HEADMODEL_DIPOLI

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_headmodel_dipoli".

`<html>``<pre>`
    `<a href=/reference/ft_headmodel_dipoli>``<font color=green>`FT_HEADMODEL_DIPOLI`</font>``</a>` creates a volume conduction model of the head
    using the boundary element method (BEM) for EEG. This function takes
    as input the triangulated surfaces that describe the boundaries and
    returns as output a volume conduction model which can be used to
    compute leadfields.
 
    This implements
    Oostendorp TF, van Oosterom A. "Source parameter estimation in
    inhomogeneous volume conductors of arbitrary shape." IEEE Trans
    Biomed Eng. 1989 Mar;36(3):382-91.
 
    The implementation of this function uses an external command-line
    executable with the name "dipoli" which is provided by Thom Oostendorp.
 
    Use as
    headmodel = ft_headmodel_dipoli(mesh, ...)
 
    The mesh is given as a boundary or a struct-array of boundaries (surfaces)
 
    Optional input arguments should be specified in key-value pairs and can
    include
    isolatedsource   = string, 'yes' or 'no'
    conductivity     = vector, conductivity of each compartment
 
    See also `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

