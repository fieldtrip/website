---
title: ft_plot_headshape
---
```
 FT_PLOT_HEADSHAPE visualizes the shape of a head from a variety of
 acquisition system. Usually the head shape is measured with a
 Polhemus tracker and some proprietary software (e.g. from CTF, BTi
 or Yokogawa). The headshape and fiducials can be used for coregistration.
 If present in the headshape, the location of the fiducials will also
 be shown.

 Use as
   ft_plot_headshape(shape, ...)
 where the shape is a structure obtained from FT_READ_HEADSHAPE.

 Optional arguments should come in key-value pairs and can include
   'vertexcolor'  = color specification as [r g b] values or a string, for example 'brain', 'cortex', 'skin', 'red', 'r'
   'vertexsize'   = scalar value specifying the size of the vertices (default = 10)
   'fidcolor'     = color specification as [r g b] values or a string, for example 'brain', 'cortex', 'skin', 'red', 'r'
   'fidmarker'    = ['.', '*', '+',  ...]
   'fidlabel'     = ['yes', 'no', 1, 0, 'true', 'false']
   'transform'    = transformation matrix for the fiducials, converts MRI voxels into head shape coordinates
   'unit'         = string, convert to the specified geometrical units (default = [])

 Example
   shape = ft_read_headshape(filename);
   ft_plot_headshape(shape)

 See also FT_PLOT_MESH, FT_PLOT_ORTHO
```
