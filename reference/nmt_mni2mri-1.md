---
title: nmt_mni2mri
---
```
 [xyz_o_mm,xyz_o_vx]=nmt_mri2mni(xyz_i,mrifullpath,[doaffine])
 Takes MNI coordinates (mm) and converts to original MRI coordinates (mm
 and/or voxel) using normalization info from SPM8 (or SPM12 'OldNorm')

 XYZ_I: Nx3 list of coords in individual's MRI coordinates (mm)
 mrifullpath: path to normalized MRI volume (nifti)

 [wrapper for spm_get_orig_coord from SPM8/SPM12]
```
