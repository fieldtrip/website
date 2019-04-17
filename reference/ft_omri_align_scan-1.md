---
title: ft_omri_align_scan
---
```
 function [model, mat_r, mat_a, Va] = ft_omri_align_scan(model, Vo)

 Estimate 6-DOF motion parameters and align volume Vo with reference model.

 INPUTS
 model - data structure containing reference image and flags
 Vo    - original image (to be registered to the reference model

 OUTPUTS
 model - same as input, but with modified voxel mask (for keeping track of "missing voxels")
 Va    - aligned image (possibly rotated + translated version of Vo)
 mat_r - parameters of 6-dof transformation in homogenous matrix form
         transformation from world coordinates of Vo to world coordinates of reference
 mat_a - pixel to world coordinate matrix of Vo (absolute "position" of Vo)
```
