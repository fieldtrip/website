---
title: Dealing with the geometry of the forward model
---

{% include /shared/development/warning.md %}

# Dealing with the geometry of the forward model

This part overviews the available routines (and not yet available too!) to get an optimal description of the head geometry in order to build a forward model.

The functions' types available at the moment deal with different types of object

- **anatomies**: from MRI or CT scans (for example). They are volumetric matrices
- **segmentations**: they are volumetric binary masks of tissue compartments
- **surfaces**: triangulations (faces and nodes) of anatomical surfaces. Normally from anatomies or segmentations
- **meshes**: they are 3D meshes (nodes and elements) describing a wireframe structure. Used in FEM, FDM methods can be tetrahedrons, hexahedra (cubes) or others
- **head models**: a structure containing the necessary information to run a forward model algorithm (geometry+conductivity+others)

* The from (rows)-to (columns) matrix

| ^ ana ^ seg ^ surf ^ mesh ^ hdm |
| ------------------------------- |
| 1.ana                           | [11](#method 11 ) | [12](#method 12 ) | [10](#method 10 ) | n.a. | n.a. |
| 2.seg                           | n.a. | [13](#method 13):- |  | [10](#method 10 ) | [14](#method 14):- |  | [3](#method 3 ) |
| 3.surf                          | n.a. | [4](#method 4 ) | [15](#method 15) | [16](#method 16):- |  | [5](#method 5 ) |
| 4.mesh                          | n.a. | [8](#method 8 ) | [7](#method 7 ):- |  | [9](#method 9 ) | [6](#method 6 ) |
| 5.hdm                           | n.a. | [1](#method 1 ) | [2](#method 2 ):- |  | n.a. | n.a. |

## method 1

From hdm TO seg
ft_prepare_sourcemodel
[Back](#Dealing with the geometry of the forward model)

## method 2

From hdm TO surf
headmodel
[Back](#Dealing with the geometry of the forward model)

## method 3

From seg TO hdm
ft_headmodel_fdm_fns, used only for the available FDM method
[Back](#Dealing with the geometry of the forward model)

## method 4

From seg TO surf
bounding_mesh

Idea for a further improvement:
Use as:
ft_datatype(gris,'datatype','seg')
where grid comes from the ft_prepare_sourcemodel function.
This generates a surface outside a delimiting filled volume.

[Back](#Dealing with the geometry of the forward model)

## method 5

From surf TO hdm
all ft_headmodel_XXX functions
[Back](#Dealing with the geometry of the forward model)

## method 6

From mesh TO hdm
ft_headmodel_fem_simbio, used only for the available FEM method
[Back](#Dealing with the geometry of the forward model)

## method 7

From mesh TO surf
TBD
Useful for example to extract a surface from the wireframe
Implementation suggestion of mesh2surf.m:
for each triangle of the tetrahedron
count the number of belonging tetrahedra
end
keep the triangles with count == 1
[Back](#Dealing with the geometry of the forward model)

## method 8

From mesh TO seg
TBD
Useful for example to calculate if source points ly in or out of a wireframe element
[Back](#Dealing with the geometry of the forward model)

## method 9

From mesh TO mesh
TBD
Useful to reposition the elements elastically
[Back](#Dealing with the geometry of the forward model)

## method 10

From seg TO surf
ft_surfaceextract
[Back](#Dealing with the geometry of the forward model)

## method 11

From ana TO ana
spm_smooth or ft_volume_realign
[Back](#Dealing with the geometry of the forward model)

## method 12

From ana TO seg
ft_volumesegment
[Back](#Dealing with the geometry of the forward model)

## method 13

From seg TO seg
All morphological operators, e.g., imopen
[Back](#Dealing with the geometry of the forward model)

## method 14

From seg TO mesh
Builds a mesh directly from the segmentation, like in vgrid software
[Back](#Dealing with the geometry of the forward model)

## method 15

From surf TO surf
Manipulates surfaces: all ft_surfaceXXX functions
[Back](#Dealing with the geometry of the forward model)

## method 16

From surf TO mesh
Tetge software, interfaced by the external toolbox iso2mesh
[Back](#Dealing with the geometry of the forward model)

## method ?

From ? TO ?
TBD
[Back](#Dealing with the geometry of the forward model)
