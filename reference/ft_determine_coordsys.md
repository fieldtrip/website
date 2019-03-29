---
title: ft_determine_coordsys
---
```
 FT_DETERMINE_COORDSYS plots a geometrical object, allowing you to perform
 a visual check on the coordinatesystem, the units and on the anatomical
 labels for the coordinate system axes.

 Use as
   [dataout] = ft_determine_coordsys(datain, ...)
 where the input data structure can be
  - an anatomical MRI
  - an electrode or gradiometer definition
  - a volume conduction model of the head
 or most other FieldTrip structures that represent geometrical information.

 Additional optional input arguments should be specified as key-value pairs
 and can include
   interactive  = string, 'yes' or 'no' (default = 'yes')
   axisscale    = scaling factor for the reference axes and sphere (default = 1)
   clim         = lower and upper anatomical MRI limits (default = [0 1])

 This function wil pop up a figure that allows you to check whether the
 alignment of the object relative to the coordinate system axes is correct
 and what the anatomical labels of the coordinate system axes are. You
 should switch on the 3D rotation option in the figure panel to rotate and
 see the figure from all angles. To change the anatomical labels of the
 coordinate system, you should press the corresponding keyboard button.

 Recognized and supported coordinate systems include: ctf, 4d, bti, itab,
 neuromag, spm, mni, tal, acpc, als, ras, paxinos.

 See also FT_VOLUMEREALIGN, FT_VOLUMERESLICE, FT_PLOT_ORTHO, FT_PLOT_AXES
```
