---
title: ft_determine_units
---
```
 FT_DETERMINE_UNITS tries to determine the units of a geometrical object by
 looking at its size and by relating this to the approximate size of the
 human head according to the following table:
   from  0.050 to   0.500 -> meter
   from  0.500 to   5.000 -> decimeter
   from  5.000 to  50.000 -> centimeter
   from 50.000 to 500.000 -> millimeter

 Use as
   dataout = ft_determine_units(datain)
 where the input obj structure can be
  - an anatomical MRI
  - an electrode or gradiometer definition
  - a volume conduction model of the head
 or most other FieldTrip structures that represent geometrical information.

 See also FT_CONVERT_UNITS, FT_DETERMINE_COODSYS, FT_CONVERT_COORDSYS
```
