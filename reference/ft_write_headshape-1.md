---
title: ft_write_headshape
---
```
 FT_WRITE_HEADSHAPE writes a head surface, cortical sheet or
 geometrical descrition of the volume conduction model or source
 model to a file for further processing in external software.

 Use as
   ft_write_headshape(filename, bnd, ...)
 or
   ft_write_headshape(filename, pos, ...)
 where the bnd is a structure containing the vertices and triangles
 (bnd.pnt and bnd.tri), or where pos is a Nx3 matrix that describes the 
 surface or source points.

 Required input arguments should be specified as key-value pairs and
 should include
   'format'		  = string, see below

 Optional input arguments should be specified as key-value pairs and
 can include
   'data'        = data matrix, size(1) should be number of vertices
   'unit'        = string, e.g. 'mm'

 Supported output formats are
   'mne_tri'		MNE surface desciption in ascii format
   'mne_pos'		MNE source grid in ascii format, described as 3D points
   'off'
   'vista'
   'tetgen'
   'gifti'
   'stl'           STereoLithography file format, for use with CAD and generic 3D mesh editing programs
   'vtk'           Visualization ToolKit file format, for use with Paraview
   'ply'           Stanford Polygon file format, for use with Paraview or Meshlab
   'freesurfer'    Freesurfer surf-file format, using write_surf from FreeSurfer

 See also FT_READ_HEADSHAPE
```
