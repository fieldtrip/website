---
layout: default
---

##  FT_PLOT_AXES

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_plot_axes".

`<html>``<pre>`
    `<a href=/reference/ft_plot_axes>``<font color=green>`FT_PLOT_AXES`</font>``</a>` adds three axes of 150 mm and a 10 mm sphere at the origin to the
    present 3-D figure. The axes and sphere are scaled according to the units of the
    geometrical object that is passed to this function. Furthermore, when possible,
    the axes labels will represent the aanatomical labels corresponding to the
    specified coordinate system.
 
    Use as
    ft_plot_axes(object)
 
    Additional optional input arguments should be specified as key-value pairs
    and can include
    'axisscale'    = scaling factor for the reference axes and sphere (default = 1)
    'unit'         = string, convert the data to the specified geometrical units (default = [])
    'coordsys'     = string, assume the data to be in the specified coordinate system (default = 'unknown')
    'fontcolor'    = string, color specification (default = [1 .5 0], i.e. orange)
    'fontsize'     = number, sets the size of the text (default is automatic)
    'fontunits'    =
    'fontname'     =
    'fontweight'   =
 
    See also `<a href=/reference/ft_plot_sens>``<font color=green>`FT_PLOT_SENS`</font>``</a>`, `<a href=/reference/ft_plot_mesh>``<font color=green>`FT_PLOT_MESH`</font>``</a>`, `<a href=/reference/ft_plot_ortho>``<font color=green>`FT_PLOT_ORTHO`</font>``</a>`, `<a href=/reference/ft_plot_headshape>``<font color=green>`FT_PLOT_HEADSHAPE`</font>``</a>`, `<a href=/reference/ft_plot_dipole>``<font color=green>`FT_PLOT_DIPOLE`</font>``</a>`, `<a href=/reference/ft_plot_vol>``<font color=green>`FT_PLOT_VOL`</font>``</a>`
`</pre>``</html>`

