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
 where the transform should be a 4x4 homogeneous transformation matrix and the
 input data structure can be any of the FieldTrip data structures that
 describes geometrical data.

 The units of the transformation matrix must be the same as the units in which the
 geometric object is expressed.

 The type of geometric object constrains the type of allowed
 transformations.

 For sensor arrays:
 If the input is an MEG gradiometer array, only a rigid-body translation
 plus rotation are allowed. If the input is an EEG electrode or fNIRS
 optodes array, global rescaling and individual axis rescaling is also
 allowed.

 For volume conduction models:
 If the input is a volume conductor model of the following type:
   multi sphere model
   BEM model with system matrix already computed
   FEM model with volumetric elements
   single shell mesh with the spherical harmonic coefficients already
   computed
 only a rigid-body translation plus rotation are allowed.

 If the input is a volume conductor model of the following type:
   BEM model with the system matrix not yet computed
   single shell mesh with the spherical harmonic coefficients not yet
   computed
 global rescaling and individual axis rescaling is allowed, in addition to
 rotation and translation.

 If the input is a volume conductor model of the following type:
   single sphere
   concentric spheres
 global rescaling is allowed, in addition to rotation and translation.

 For source dipole models, either defined as a 3D regular grid, a 2D mesh
 or unstructred point cloud, global rescaling and individual axis
 rescaling is allowed, in addition to rotation and translation.

 For volumes rotation, translation, global rescaling and individual axis
 rescaling are allowed.

 See also FT_WARP_APPLY, FT_HEADCOORDINATES, FT_SCALINGFACTOR
```
