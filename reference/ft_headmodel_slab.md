---
layout: default
---

##  FT_HEADMODEL_SLAB

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_headmodel_slab".

`<html>``<pre>`
    `<a href=/reference/ft_headmodel_slab>``<font color=green>`FT_HEADMODEL_SLAB`</font>``</a>` creates an EEG volume conduction model that
    is described with an infinite conductive slab. You can think
    of this as two parallel planes containing a mass of conductive
    material (e.g. water) and externally to them a non-conductive material
    (e.g. air).
 
    Use as
    headmodel = ft_headmodel_slab(mesh1, mesh2, Pc, varargin)
    where
    mesh1.pos = Nx3 vector specifying N points through which the 'upper' plane is fitted 
    mesh2.pos = Nx3 vector specifying N points through which the 'lower' plane is fitted 
    Pc        = 1x3 vector specifying the spatial position of a point lying in the conductive slab 
               (this determines the plane's normal's direction)
    
    Optional arguments should be specified in key-value pairs and can include
    'sourcemodel'  = 'monopole' 
    'conductivity' = number ,  conductivity value of the conductive halfspace (default = 1)
    
    See also `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

