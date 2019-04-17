---
title: ft_write_mri
---
```
 FT_WRITE_MRI exports volumetric data such as anatomical and functional
 MRI to a file.

 Use as
   ft_write_mri(filename, img, ...)
 where img represents the 3-D array with image values.

 The specified filename can already contain the filename extention, but that is not
 required since it will be added automatically.

 Additional options should be specified in key-value pairs and can be
   'dataformat'   = string, see below
   'transform'    = transformation matrix, specifying the transformation from voxel coordinates to head coordinates
   'spmversion'   = version of SPM to be used, in case data needs to be written in analyze format

 The supported dataformats are
   'analyze'
   'nifti'
   'vista'
   'mgz'   (freesurfer)

 See also FT_READ_MRI, FT_WRITE_DATA, FT_WRITE_HEADSHAPE
```
