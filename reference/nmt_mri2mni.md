---
title: nmt_mri2mni
---
```
 [xyz_o]=nmt_mri2mni(xyz_i,mrifullpath,[doaffine])
 Takes MRI coords (mm) and converts them to MNI coordinates (mm)
 using normalization info from SPM8 (or SPM12 'OldNorm')

 XYZ_I: Nx3 list of coords in individual's MRI coordinates (mm)

 mrifullpath: path to normalized MRI volume (nifti)

 doaffine: (optional) applies affine transform for area outside of
           bounding box specified by SPM warping.
```
