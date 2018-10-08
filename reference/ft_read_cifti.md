---
layout: default
---

##  FT_READ_CIFTI

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_read_cifti".

`<html>``<pre>`
    `<a href=/reference/ft_read_cifti>``<font color=green>`FT_READ_CIFTI`</font>``</a>` read functional data or functional connectivity from a cifti-1 or
    cifti-2 file. The functional data can consist of a dense or a parcellated
    representation. The geometrical description of the brainordinates can consist of
    triangulated surfaces or voxels in a regular 3-D volumetric grid. If available,
    it also reads the geometrical description of the surfaces from the accompanying
    gifti files.
 
    Use as
    data = ft_read_cifti(filename, ...)
 
    If the file contains a dense representation of functional data, the output data
    structure is organized according to the `<a href=/reference/ft_datatype_source>``<font color=green>`FT_DATATYPE_SOURCE`</font>``</a>` or `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>`
    definition.
 
    If the contains a parcellated representation of functional data, the output data
    structure is organized according to the `<a href=/reference/ft_datatype_timelock>``<font color=green>`FT_DATATYPE_TIMELOCK`</font>``</a>` or `<a href=/reference/ft_datatype_freq>``<font color=green>`FT_DATATYPE_FREQ`</font>``</a>`
    definition. In addition, the description of the geometry wil be represented in a
    data.brainordinate field, which is organized according to the `<a href=/reference/ft_datatype_source>``<font color=green>`FT_DATATYPE_SOURCE`</font>``</a>`
    or `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>` definition.
 
    Any optional input arguments should come in key-value pairs and may include
    'readdata'         = boolean, can be false or true (default depends on file size)
    'readsurface'      = boolean, can be false or true (default = true)
    'cortexleft'       = string, filename with left cortex (optional, default is automatic)
    'cortexright'      = string, filename with right cortex (optional, default is automatic)
    'hemisphereoffset' = number, amount in milimeter to move the hemispheres apart from each other (default = 0)
    'mapname'          = string, 'field' to represent multiple maps separately, or 'array' to represent as array (default = 'field')
    'debug'            = boolean, write a debug.xml file (default = false)
 
    See also `<a href=/reference/ft_write_cifti>``<font color=green>`FT_WRITE_CIFTI`</font>``</a>`, `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>`, `<a href=/reference/ft_write_mri>``<font color=green>`FT_WRITE_MRI`</font>``</a>`
`</pre>``</html>`

