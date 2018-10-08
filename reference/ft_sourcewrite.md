---
layout: default
---

##  FT_SOURCEWRITE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_sourcewrite".

`<html>``<pre>`
    `<a href=/reference/ft_sourcewrite>``<font color=green>`FT_SOURCEWRITE`</font>``</a>` exports source-reconstructed results to gifti or nifti format file.
    The appropriate output file depends on whether the source locations are described by
    on a cortically constrained sheet (gifti) or by a regular 3D lattice (nifti).
 
    Use as
   ft_sourcewrite(cfg, source)
    where source is a source structure obtained from `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>` and
    cfg is a structure that should contain
 
   cfg.filename  = string, filename without the extension
   cfg.filetype  = string, can be 'nifti', 'gifti' or 'cifti' (default is automatic)
   cfg.parameter = string, functional parameter to be written to file
   cfg.precision = string, can be 'single', 'double', etc.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    If you specify this the input data will be read from a *.mat
    file on disk. This mat file should contain only a single variable,
    corresponding with the input data structure.
 
    See also `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, `<a href=/reference/ft_sourcedescriptives>``<font color=green>`FT_SOURCEDESCRIPTIVES`</font>``</a>`, `<a href=/reference/ft_volumewrite>``<font color=green>`FT_VOLUMEWRITE`</font>``</a>`
`</pre>``</html>`

