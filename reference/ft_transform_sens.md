---
title: ft_transform_sens
---
```
 FT_TRANSFORM_SENS applies a homogenous coordinate transformation to a
 structure with EEG electrodes or MEG gradiometers. For MEG gradiometers
 the homogenous transformation matrix should be limited to a rigid-body
 translation plus rotation.

 Use as
   sens = ft_transform_sens(transform, sens)

 See also FT_READ_SENS, FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD, FT_TRANSFORM_GEOMETRY
```
