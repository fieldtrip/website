---
layout: default
---

##  FT_REJECTCOMPONENT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_rejectcomponent".

`<html>``<pre>`
    `<a href=/reference/ft_rejectcomponent>``<font color=green>`FT_REJECTCOMPONENT`</font>``</a>` backprojects an ICA (or similar) decomposition to the
    channel level after removing the independent components that contain
    the artifacts. This function does not automatically detect the artifact
    components, you will have to do that yourself.
 
    Use as
     [data] = ft_rejectcomponent(cfg, comp)
    or as
     [data] = ft_rejectcomponent(cfg, comp, data)
 
    where the input comp is the result of `<a href=/reference/ft_componentanalysis>``<font color=green>`FT_COMPONENTANALYSIS`</font>``</a>`. The output
    data will have the same format as the output of `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    An optional input argument data can be provided. In that case
    componentanalysis will do a subspace projection of the input data
    onto the space which is spanned by the topographies in the unmixing
    matrix in comp, after removal of the artifact components.  Please use
    this option of including data as input, if you wish to use the output
    data.grad in further computation, for example for leadfield computation.
 
    The configuration structure can contain
    cfg.component  = list of components to remove, e.g. [1 4 7] or see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>`
    cfg.demean     = 'no' or 'yes', whether to demean the input data (default = 'yes')
    cfg.updatesens = 'no' or 'yes' (default = 'yes')
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_componentanalysis>``<font color=green>`FT_COMPONENTANALYSIS`</font>``</a>`, `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`
`</pre>``</html>`

