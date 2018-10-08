---
layout: default
---

##  FT_ANNOTATE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_annotate".

`<html>``<pre>`
    `<a href=/reference/ft_annotate>``<font color=green>`FT_ANNOTATE`</font>``</a>` returns the same output data as the user has provided as input, but allows
    to add comments to that data structure. These comments are stored along with the other
    provenance information and can be displayed with `<a href=/reference/ft_analysispipeline>``<font color=green>`FT_ANALYSISPIPELINE`</font>``</a>`. Adding comments
    is especially useful if you have manually (i.e. in plain MATLAB) modified ythe data
    structure, whereby some provenance information is missing.
 
    Use as
    outdata = ft_examplefunction(cfg, indata)
    where the input data structure can be any of the FieldTrip data structures and where
    cfg is a configuratioun structure that should contain
 
   cfg.comment    = string
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_analysispipeline>``<font color=green>`FT_ANALYSISPIPELINE`</font>``</a>`, `<a href=/reference/ft_math>``<font color=green>`FT_MATH`</font>``</a>`
`</pre>``</html>`

