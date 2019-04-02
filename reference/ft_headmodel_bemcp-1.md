---
title: ft_headmodel_bemcp
---
```
 FT_HEADMODEL_BEMCP creates a volume conduction model of the head
 using the boundary element method (BEM) for EEG. This function
 takes as input the triangulated surfaces that describe the boundaries
 and returns as output a volume conduction model which can be used
 to compute leadfields.

 The implementation of this function is based on Christophe Phillips'
 MATLAB code, hence the name "bemcp".

 Use as
   headmodel = ft_headmodel_bemcp(mesh, ...)

 See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD
```
