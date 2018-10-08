---
layout: default
---

##  FT_DENOISE_SYNTHETIC

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_denoise_synthetic".

`<html>``<pre>`
    `<a href=/reference/ft_denoise_synthetic>``<font color=green>`FT_DENOISE_SYNTHETIC`</font>``</a>` computes CTF higher-order synthetic gradients for
    preprocessed data and for the corresponding gradiometer definition.
 
    Use as
    [data] = ft_denoise_synthetic(cfg, data);
 
    where data should come from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>` and the configuration should contain
    cfg.gradient = 'none', 'G1BR', 'G2BR' or 'G3BR' specifies the gradiometer
                   type to which the data should be changed
    cfg.trials   = 'all' or a selection given as a 1xN vector (default = 'all')
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`, `<a href=/reference/ft_denoise_pca>``<font color=green>`FT_DENOISE_PCA`</font>``</a>`
`</pre>``</html>`

