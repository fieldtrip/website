---
layout: default
---

##  FT_SOURCEGRANDAVERAGE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_sourcegrandaverage".

`<html>``<pre>`
    `<a href=/reference/ft_sourcegrandaverage>``<font color=green>`FT_SOURCEGRANDAVERAGE`</font>``</a>` averages source reconstructions over either multiple
    subjects or conditions. It computes the average and variance for all
    known source parameters. The output can be used in `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>`
    with the method 'parametric'.
 
    Alternatively, it can construct an average for multiple input source
    reconstructions in two conditions after randomly reassigning the
    input data over the two conditions. The output then can be used in
    `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>` with the method 'randomization' or 'randcluster'.
 
    The input source structures should be spatially alligned to each other
    and should have the same positions for the source grid.
 
    Use as
   [grandavg] = ft_sourcegrandaverage(cfg, source1, source2, ...)
 
    where the source structures are obtained from `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>` or
    from `<a href=/reference/ft_volumenormalise>``<font color=green>`FT_VOLUMENORMALISE`</font>``</a>`, and the configuration can contain the
    following field
    cfg.parameter          = string, describing the functional data to be processed, e.g. 'pow', 'nai' or 'coh'
    cfg.keepindividual     = 'no' or 'yes'
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure. For this particular function, the input data
    should be structured as a single cell array.
 
    See also `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, `<a href=/reference/ft_sourcedescriptives>``<font color=green>`FT_SOURCEDESCRIPTIVES`</font>``</a>`, `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>`, `<a href=/reference/ft_math>``<font color=green>`FT_MATH`</font>``</a>`
`</pre>``</html>`

