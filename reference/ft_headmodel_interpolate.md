---
layout: default
---

##  FT_HEADMODEL_INTERPOLATE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_headmodel_interpolate".

`<html>``<pre>`
    `<a href=/reference/ft_headmodel_interpolate>``<font color=green>`FT_HEADMODEL_INTERPOLATE`</font>``</a>` describes a volume conduction model of the head in which
    subsequent leadfield computations can be performed using a simple interpolation
    scheme.
 
    Use as
    headmodel = ft_headmodel_interpolate(filename, sens, leadfield)
    or
    headmodel = ft_headmodel_interpolate(filename, sens, leadfield)
 
    The input parameters are the filename to which the model will be written,
    the electrode definition (see ft_DATATYPE_SENS). The third input argument
    is either a pre-computed leadfield structure from `<a href=/reference/ft_prepare_leadfield>``<font color=green>`FT_PREPARE_LEADFIELD`</font>``</a>`
    or a the output of a previous call to `<a href=/reference/ft_headmodel_interpolate>``<font color=green>`FT_HEADMODEL_INTERPOLATE`</font>``</a>`.
 
    The output volume conduction model is stored on disk in a MATLAB file together with a
    number of NIFTi files. The mat file contains a structure with the following fields
    headmodel.sens        = structure, electrode sensor description, see FT_DATATYE_SENS
    headmodel.filename    = cell-array with NIFTI filenames, one file per channel
    and contains
    headmodel.dim         = [Nx Ny Nz] vector with the number of grid points along each dimension
    headmodel.transform   = 4x4 homogenous transformation matrix
    headmodel.unit        = string with the geometrical units of the positions, e.g. 'cm' or 'mm'
    to describe the source positions.
 
    See also `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

