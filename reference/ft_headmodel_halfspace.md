---
layout: default
---

##  FT_HEADMODEL_HALFSPACE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_headmodel_halfspace".

`<html>``<pre>`
    `<a href=/reference/ft_headmodel_halfspace>``<font color=green>`FT_HEADMODEL_HALFSPACE`</font>``</a>` creates an EEG volume conduction model that
    is described with an infinite conductive halfspace. You can think
    of this as a plane with on one side a infinite mass of conductive
    material (e.g. water) and on the other side non-conductive material
    (e.g. air).
 
    Use as
     headmodel = ft_headmodel_halfspace(mesh, Pc, ...)
    where
    mesh.pos = Nx3 vector specifying N points through which a plane is fitted 
    Pc       = 1x3 vector specifying the spatial position of a point lying in the conductive halfspace 
               (this determines the plane normal's direction)
 
    Additional optional arguments should be specified as key-value pairs and can include
    'sourcemodel'  = string, 'monopole' or 'dipole' (default = 'dipole')
    'conductivity' = number,  conductivity value of the conductive halfspace (default = 1)
 
    See also `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

