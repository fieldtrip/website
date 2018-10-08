---
layout: default
---

##  FT_DENOISE_PCA

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_denoise_pca".

`<html>``<pre>`
    `<a href=/reference/ft_denoise_pca>``<font color=green>`FT_DENOISE_PCA`</font>``</a>` performs a principal component analysis (PCA) on specified reference
    channels and subtracts the projection of the data of interest onto this orthogonal
    basis from the data of interest. This is the algorithm which is applied by 4D to
    compute noise cancellation weights on a dataset of interest. This function has been
    designed for 4D MEG data, but can also be applied to data from other MEG systems.
 
    Use as
    [dataout] = ft_denoise_pca(cfg, data)
    or as
    [dataout] = ft_denoise_pca(cfg, data, refdata)
    where "data" is a raw data structure that was obtained with `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`. If
    you specify the additional input "refdata", the specified reference channels for
    the regression will be taken from this second data structure. This can be useful
    when reference-channel specific preprocessing needs to be done (e.g. low-pass
    filtering).
 
    The output structure dataout contains the denoised data in a format that is
    consistent with the output of `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    The configuration should contain
    cfg.refchannel = the channels used as reference signal (default = 'MEGREF')
    cfg.channel    = the channels to be denoised (default = 'MEG')
    cfg.truncate   = optional truncation of the singular value spectrum (default = 'no')
    cfg.zscore     = standardise reference data prior to PCA (default = 'no')
    cfg.pertrial   = 'no' (default) or 'yes'. Regress out the references on a per trial basis
    cfg.trials     = list of trials that are used (default = 'all')
    cfg.updatesens = 'no' or 'yes' (default = 'yes')
 
    if cfg.truncate is integer n &gt; 1, n will be the number of singular values kept.
    if 0 &lt; cfg.truncate &lt; 1, the singular value spectrum will be thresholded at the
    fraction cfg.truncate of the largest singular value.
 
    See also `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`, `<a href=/reference/ft_denoise_synthetic>``<font color=green>`FT_DENOISE_SYNTHETIC`</font>``</a>`
`</pre>``</html>`

