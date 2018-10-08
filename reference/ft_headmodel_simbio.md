---
layout: default
---

##  FT_HEADMODEL_SIMBIO

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_headmodel_simbio".

`<html>``<pre>`
    `<a href=/reference/ft_headmodel_simbio>``<font color=green>`FT_HEADMODEL_SIMBIO`</font>``</a>` creates a volume conduction model of the head
    using the finite element method (FEM) for EEG. This function takes
    as input a volumetric mesh (hexahedral or tetrahedral) and
    returns as output a volume conduction model which can be used to
    compute leadfields.
 
    This implements
        ...
 
    Use as
    headmodel = ft_headmodel_simbio(mesh,'conductivity', conductivities, ...)
 
    The mesh is given as a volumetric mesh, using ft_datatype_parcellation
    mesh.pos = vertex positions
    mesh.tet/mesh.hex = list of volume elements
    mesh.tissue = tissue assignment for elements
    mesh.tissuelabel = labels correspondig to tissues
 
    Required input arguments should be specified in key-value pairs and have
    to include
    conductivity   = vector containing tissue conductivities using ordered
                     corresponding to mesh.tissuelabel
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
    To run this on Windows the following packages are necessar
 
    Microsoft Visual C++ 2008 Redistributable
 
    Intel Visual Fortran Redistributables
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
    See also `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

