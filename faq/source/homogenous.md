---
title: How do homogenous coordinate transformation matrices work?
category: faq
tags: [coordinate]
redirect_from:
    - /faq/homogenous/
---

# How do homogenous coordinate transformation matrices work? Or how do I get the coordinates for a specific voxel?

A coordinate system specifies the interpretation of how points are expressed in 3D space. This makes use of the three numbers (x, y, z) that represent the point, relative to a known origin (0,0,0), and making use of cardinal x-, y-, and z-axes that are pointing into a specific direction such as towards the nasion, or from the [posterior to the anterior commissure](/faq/acpc/).

A homogenous transformation matrix allows you to transform 3D points from one coordinate system to another. The conversion is achieved by simple matrix multiplication, as described in detail in the documentation of the [AIR](http://air.bmap.ucla.edu/AIR5) software by Roger P. Woods. This provides a very complete description of [homogenous coordinates](http://air.bmap.ucla.edu/AIR5/homogenous.html). Another, perhaps more accessible description can be found on the [brainvoyager website](https://www.brainvoyager.com/bv/doc/UsersGuide/CoordsAndTransforms/SpatialTransformationMatrices.html).

In FieldTrip, as in many other software packages that deal with volumetrically defined data, we also use a homogen(e)ous coordinate transformation matrix to describe the relation between voxels in the volumetric data, and real-world or "head" coordinates. The [real-world coordinates](/faq/coordsys) are usually related to anatomical landmarks and the voxel coordinates are directly related to the 3D array with the grey-scale numbers that represent the MRI images.

The FieldTrip data structure that describes **[volumetric data](/reference/utilities/ft_datatype_volume)** includes a `transform` field with the homogenous 4x4 transformation matrix that maps from voxel indices to the head (or device) coordinate system. If the head coordinate system is known, it is specified in the `coordsys` field.

Indexing of numerical arrays in MATLAB starts with 1, i.e., the first voxel in the volume is described by the indices (1,1,1). Thus, if you want to obtain the real world coordinate of a voxel with indices (i,j,k), you have to perform the following multiplication:

    voxpos = [i j k 1]'
    headpos = transform * voxpos

The first 3 elements of the resulting `headpos` vector correspond to the (x,y,z) coordinates in the head coordinate system.

Note that, if the MRI comes directly from the scanner, it still is expressed in DICOM or in NIFTI scanner coordinates, and not relative to actual anatomical landmarks of the individual participant whose data is represented in the MRI.
