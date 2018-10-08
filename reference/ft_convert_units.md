---
layout: default
---

##  FT_CONVERT_UNITS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_convert_units".

`<html>``<pre>`
    `<a href=/reference/ft_convert_units>``<font color=green>`FT_CONVERT_UNITS`</font>``</a>` changes the geometrical dimension to the specified SI unit.
    The units of the input object is determined from the structure field
    object.unit, or is estimated based on the spatial extend of the structure,
    e.g. a volume conduction model of the head should be approximately 20 cm large.
 
    Use as
    [object] = ft_convert_units(object, target)
 
    The following geometrical objects are supported as inputs
    electrode or gradiometer array, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    volume conductor, see `<a href=/reference/ft_datatype_headmodel>``<font color=green>`FT_DATATYPE_HEADMODEL`</font>``</a>`
    anatomical mri, see `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>`
    segmented mri, see `<a href=/reference/ft_datatype_segmentation>``<font color=green>`FT_DATATYPE_SEGMENTATION`</font>``</a>`
    dipole grid definition, see `<a href=/reference/ft_datatype_source>``<font color=green>`FT_DATATYPE_SOURCE`</font>``</a>`
 
    Possible target units are 'm', 'dm', 'cm ' or 'mm'. If no target units
    are specified, this function will only determine the native geometrical
    units of the object.
 
    See also `<a href=/reference/ft_determine_units>``<font color=green>`FT_DETERMINE_UNITS`</font>``</a>`, `<a href=/reference/ft_convert_coordsys>``<font color=green>`FT_CONVERT_COORDSYS`</font>``</a>`, FT_DETERMINE_COODSYS
`</pre>``</html>`

