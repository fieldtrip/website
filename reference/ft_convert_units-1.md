---
title: ft_convert_units
---
```
 FT_CONVERT_UNITS changes the geometrical dimension to the specified SI unit.
 The units of the input object is determined from the structure field
 object.unit, or is estimated based on the spatial extend of the structure,
 e.g. a volume conduction model of the head should be approximately 20 cm large.

 Use as
   [object] = ft_convert_units(object, target)

 The following geometrical objects are supported as inputs
   electrode or gradiometer array, see FT_DATATYPE_SENS
   volume conductor, see FT_DATATYPE_HEADMODEL
   anatomical mri, see FT_DATATYPE_VOLUME
   segmented mri, see FT_DATATYPE_SEGMENTATION
   dipole grid definition, see FT_DATATYPE_SOURCE

 Possible target units are 'm', 'dm', 'cm ' or 'mm'. If no target units
 are specified, this function will only determine the native geometrical
 units of the object.

 See also FT_DETERMINE_UNITS, FT_CONVERT_COORDSYS, FT_DETERMINE_COODSYS
```
