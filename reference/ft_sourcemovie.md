---
layout: default
---

##  FT_SOURCEMOVIE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_sourcemovie".

`<html>``<pre>`
    `<a href=/reference/ft_sourcemovie>``<font color=green>`FT_SOURCEMOVIE`</font>``</a>` displays the source reconstruction on a cortical mesh
    and allows the user to scroll through time with a movie. 
 
    Use as
    ft_sourcemovie(cfg, source)
    where the input source data is obtained from `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, or a 
    a parcellated source structure (i.e. contains a brainordinate field) and 
    cfg is a configuration structure that should contain
 
   cfg.funparameter    = string, functional parameter that is color coded (default = 'avg.pow')
   cfg.maskparameter   = string, functional parameter that is used for opacity (default = [])
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    If you specify this option the input data will be read from a *.mat
    file on disk. This mat files should contain only a single variable named 'data',
    corresponding to the input structure.
 
    See also `<a href=/reference/ft_sourceplot>``<font color=green>`FT_SOURCEPLOT`</font>``</a>`, `<a href=/reference/ft_sourceinterpolate>``<font color=green>`FT_SOURCEINTERPOLATE`</font>``</a>`, `<a href=/reference/ft_sourceparcellate>``<font color=green>`FT_SOURCEPARCELLATE`</font>``</a>`
`</pre>``</html>`

