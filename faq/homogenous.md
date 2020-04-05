---
title: How do homogenous coordinate transformation matrices work?
tags: [faq, coordinate]
---

# How do homogenous coordinate transformation matrices work?

The documentation of the [AIR](http://air.bmap.ucla.edu/AIR5) software by Roger P. Woods provides a very nice description of [homogenous coordinates](http://air.bmap.ucla.edu/AIR5/homogenous.html).

In FieldTrip, as in many other software packages that deal with anatomical and functional MRI data, we use the homogenous coordinate transformation matrix to describe the relation between voxel coordinates. The first voxel in the volume is described by the indices [1,1,1], and coordinates in the [head-coordinate system](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined) are expressed in mm, cm or m relative to an origin that relates to specific anatomical landmarks. After reading anatomical MRI data with **[ft_read_mri](/reference/ft_read_mri)**, the `mri.transform` field contains the transformation matrix. Following **[ft_volumerealign](/reference/ft_volumerealign)** that matrix is updated.
