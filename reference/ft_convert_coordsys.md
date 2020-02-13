---
title: ft_convert_coordsys
---
```plaintext
 FT_CONVERT_COORDSYS changes the coordinate system of the input object to the
 specified coordinate system. The coordinate system of the input object is
 determined from the 'coordsys' field in the input data, or needs to be determined
 and specified interactively by the user.

 Use as
   [output] = ft_convert_coordsys(input, target)
   [output] = ft_convert_coordsys(input, target, method)
   [output] = ft_convert_coordsys(input, target, method, template)
 to determine and convert the coordinate system.

 With the optional method input argument you can determine whether to use SPM for an
 affine or non-linear transformation.
   method = 0: only an approximate coregistration (default for non-MRI data)
   method = 1: an approximate coregistration, followed by spm_affreg
   method = 2: an approximate coregistration, followed by spm_normalise (default for MRI data)

 The following input data structures are supported
   electrode or gradiometer array, see FT_DATATYPE_SENS
   volume conduction model, see FT_DATATYPE_HEADMODEL
   source model, see FT_DATATYPE_SOURCE and FT_PREPARE_SOURCEMODEL
   anatomical mri, see FT_DATATYPE_VOLUME
   segmented mri, see FT_DATATYPE_SEGMENTATION
   anatomical or functional atlas, see FT_READ_ATLAS

 Possible input coordinate systems are 'ctf', 'bti', '4d', 'neuromag' and 'itab'.
 Possible target coordinate systems are 'acpc'.

 Note that the conversion will be an automatic and approximate conversion, not
 taking into account differences in individual anatomies/differences in conventions
 where to put the fiducials.

 See also FT_DETERMINE_COORDSYS, FT_DETERMINE_UNITS, FT_CONVERT_UNITS, FT_PLOT_AXES, FT_PLOT_XXX
```
