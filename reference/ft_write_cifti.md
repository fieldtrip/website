---
layout: default
---

##  FT_WRITE_CIFTI

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_write_cifti".

`<html>``<pre>`
    `<a href=/reference/ft_write_cifti>``<font color=green>`FT_WRITE_CIFTI`</font>``</a>` writes functional data or functional connectivity to a cifti-2
    file. The geometrical description of the brainordinates can consist of
    triangulated surfaces or voxels in a regular 3-D volumetric grid. The functional
    data can consist of a dense or a parcellated representation. Furthermore, it
    writes the geometrical description of the surfaces to one or multiple gifti
    files.
 
    Use as
    ft_write_cifti(filename, data, ...)
    where the filename is a string and the data according to the description below.
 
    If the input data describes a dense representation of functional data, the data
    structure should conform to the `<a href=/reference/ft_datatype_source>``<font color=green>`FT_DATATYPE_SOURCE`</font>``</a>` or `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>`
    definition.
 
    If the input data describes a parcellated representation of functional data, the
    data structure should conform to the `<a href=/reference/ft_datatype_timelock>``<font color=green>`FT_DATATYPE_TIMELOCK`</font>``</a>` or `<a href=/reference/ft_datatype_freq>``<font color=green>`FT_DATATYPE_FREQ`</font>``</a>`
    definition. In addition, the description of the geometry should be specified in
    the data.brainordinate field, which should conform to the `<a href=/reference/ft_datatype_source>``<font color=green>`FT_DATATYPE_SOURCE`</font>``</a>` or
    `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>` definition.
 
    Any optional input arguments should come in key-value pairs and may include
    'parameter'        = string, fieldname that contains the functional data
    'brainstructure'   = string, fieldname that describes the brain structures (default = 'brainstructure')
    'parcellation'     = string, fieldname that describes the parcellation (default = 'parcellation')
    'precision'        = string, can be 'single', 'double', 'int32', etc. (default ='single')
    'writesurface'     = boolean, can be false or true (default = true)
    'debug'            = boolean, write a debug.xml file (default = false)
 
    The brainstructure refers to the global anatomical structure, such as CortexLeft, Thalamus, etc.
    The parcellation refers to the the detailled parcellation, such as BA1, BA2, BA3, etc.
 
    See also `<a href=/reference/ft_read_cifti>``<font color=green>`FT_READ_CIFTI`</font>``</a>`, `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>`, `<a href=/reference/ft_write_mri>``<font color=green>`FT_WRITE_MRI`</font>``</a>`
`</pre>``</html>`

