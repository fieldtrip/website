---
layout: default
---

##  FT_CONVERT_COORDSYS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_convert_coordsys".

`<html>``<pre>`
    `<a href=/reference/ft_convert_coordsys>``<font color=green>`FT_CONVERT_COORDSYS`</font>``</a>` changes the coordinate system of the input object to
    the specified coordinate system. The coordinate system of the input
    object is determined from the structure field object.coordsys, or needs to
    be determined and specified interactively by the user.
 
    Use as
    [object] = ft_convert_coordsys(object)
    to only determine the coordinate system, or
    [object] = ft_convert_coordsys(object, target)
    [object] = ft_convert_coordsys(object, target, opt)
    [object] = ft_convert_coordsys(object, target, opt, template)
    to determine and convert the coordinate system.
 
    The optional input argument opt determines the behavior when converting
    to the spm coordinate system, and pertains to the functional behaviour of
    the private functions: align_ctf2acpc and align_neuromag2acpc.
 
    The following input objects are supported
    anatomical mri, see `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>`
    anatomical or functional atlas, see `<a href=/reference/ft_read_atlas>``<font color=green>`FT_READ_ATLAS`</font>``</a>`
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
 
    See also `<a href=/reference/ft_determine_coordsys>``<font color=green>`FT_DETERMINE_COORDSYS`</font>``</a>`, ALIGN_CTF2ACPC, ALIGN_NEUROMAG2ACPC, ALIGN_FSAVERAGE2MNI
`</pre>``</html>`

