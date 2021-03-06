---
title: How do homogenous coordinate transformation matrices work?
tags: [faq, coordinate]
---

# How do homogenous coordinate transformation matrices work? Or how do I get the coordinates for a specific voxel?

The documentation of the [AIR](http://air.bmap.ucla.edu/AIR5) software by Roger P. Woods provides a very nice description of [homogenous coordinates](http://air.bmap.ucla.edu/AIR5/homogenous.html). Another, perhaps more accessible description can be found on the [brainvoyager website](https://www.brainvoyager.com/bv/doc/UsersGuide/CoordsAndTransforms/SpatialTransformationMatrices.html).

The long story short is, that a homogen(e)ous transformation matrix allows you to toggle between 3-dimensional points in space that are expressed in different coordinate systems (i.e. the points are expressed relative to an origin (with coordinate (0,0,0)), and where the three (orthogonal) coordinate axes are pointing into a specific direction). The conversion is achieved by simple matrix multiplication, as described in detail by one of the links above.    

In FieldTrip, as in many other software packages that deal with volumetrically defined data, we use a homogen(e)ous coordinate transformation matrix to describe the relation between voxels in the volumetric image, and real world coordinates (typically a coordinate system that is defined based on the anatomy of the experimental subject). In FieldTrip, a **[volume data object](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_volume.m)** always contains a `transform` field that maps from voxel indices to the coordinate system, which, if it is known, is specified in the `coordsys`. You can read more about coordinate systems [here](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/). The convention is that the indexing of the voxels starts with 1, i.e. the first voxel in the volume is described by the indices [1,1,1]. Thus, if you want to obtain the real world coordinate of a voxel with indices (i,j,k), you have to perform the following multiplication:

    coord = T * [i;j;k;1];

The variable `T` is the transform field of the data structure, and the first 3 elements of the `coord` vector are the (x,y,z) coordinates of the voxel-of-interest.
