---
title: ft_convert_coordsys
---
```
 FT_CONVERT_COORDSYS changes the coordinate system of the input object to
 the specified coordinate system. The coordinate system of the input
 object is determined from the structure field object.coordsys, or needs to
 be determined and specified interactively by the user.

 Use as
   [object] = ft_convert_coordsys(object)
 to only determine the coordinate system, or
   [object] = ft_convert_coordsys(object, target)
   [object] = ft_convert_coordsys(object, target, method)
   [object] = ft_convert_coordsys(object, target, method, template)
 to determine and convert the coordinate system.

 With the optional method input argument you can determine whether to use
 SPM for an affine or non-linear transformation. This option is passed on
 to the private functions: align_ctf2acpc and align_neuromag2acpc.

 The following input objects are supported
   anatomical mri, see FT_READ_MRI
   anatomical or functional atlas, see FT_READ_ATLAS
   (not yet) electrode definition
   (not yet) gradiometer array definition
   (not yet) volume conductor definition
   (not yet) dipole grid definition

 Possible input coordinate systems are 'ctf', 'bti', '4d', 'neuromag' and 'itab'.
 Possible target coordinate systems are 'acpc'.

 Note that the conversion will be an automatic one, which means that it
 will be an approximate conversion, not taking into account differences in
 individual anatomies/differences in conventions where to put the
 fiducials.

 See also FT_DETERMINE_COORDSYS, ALIGN_CTF2ACPC, ALIGN_NEUROMAG2ACPC, ALIGN_FSAVERAGE2MNI
```
