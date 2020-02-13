---
title: ft_transform_geometry
---
```plaintext
 FT_TRANSFORM_GEOMETRY applies a homogeneous coordinate transformation to a
 structure with geometric information, for example a volume conduction model for the
 head, gradiometer of electrode structure containing EEG or MEG sensor positions and
 MEG coil orientations, a head shape or a source model.

 Use as
   [output] = ft_transform_geometry(transform, input)
 where the transform should be a 4x4 homogenous transformation matrix and the
 input data structure can be any of the FieldTrip data structures that
 describes geometrical data.

 The units of the transformation matrix must be the same as the units in which the
 geometric object is expressed.

 Depending on the input object, the homogeneous transformation matrix should be
 limited to a rigid-body translation plus rotation (MEG-gradiometer array), or to a
 rigid-body translation plus rotation plus a global rescaling (volume conductor
 geometry).

 See also FT_WARP_APPLY, FT_HEADCOORDINATES, FT_SCALINGFACTOR
```
