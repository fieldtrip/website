---
layout: default
---

##  FT_SOURCESTATISTICS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_sourcestatistics".

`<html>``<pre>`
    `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>` computes the probability for a given null-hypothesis using
    a parametric statistical test or using a non-parametric randomization test.
 
    Use as
    [stat] = ft_sourcestatistics(cfg, source1, source2, ...)
    where the input data is the result from `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, `<a href=/reference/ft_sourcedescriptives>``<font color=green>`FT_SOURCEDESCRIPTIVES`</font>``</a>`
    or `<a href=/reference/ft_sourcegrandaverage>``<font color=green>`FT_SOURCEGRANDAVERAGE`</font>``</a>`.  The source structures should be spatially alligned
    to each other and should have the same positions for the source grid.
 
    The configuration should contain the following option for data selection
    cfg.parameter  = string, describing the functional data to be processed, e.g. 'pow', 'nai' or 'coh'
 
    Furthermore, the configuration should contai
    cfg.method       = different methods for calculating the probability of the null-hypothesis,
                     'montecarlo'    uses a non-parametric randomization test to get a Monte-Carlo estimate of the probability,
                     'analytic'      uses a parametric test that results in analytic probability,
                     'stats'         (soon deprecated) uses a parametric test from the MATLAB statistics toolbox,
 
    The other cfg options depend on the method that you select. You
    should read the help of the respective subfunction FT_STATISTICS_XXX
    for the corresponding configuration options and for a detailed
    explanation of each method.
 
    See also `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, `<a href=/reference/ft_sourcedescriptives>``<font color=green>`FT_SOURCEDESCRIPTIVES`</font>``</a>`, `<a href=/reference/ft_sourcegrandaverage>``<font color=green>`FT_SOURCEGRANDAVERAGE`</font>``</a>`, `<a href=/reference/ft_math>``<font color=green>`FT_MATH`</font>``</a>`,
    `<a href=/reference/ft_statistics_montecarlo>``<font color=green>`FT_STATISTICS_MONTECARLO`</font>``</a>`, `<a href=/reference/ft_statistics_analytic>``<font color=green>`FT_STATISTICS_ANALYTIC`</font>``</a>`, `<a href=/reference/ft_statistics_crossvalidate>``<font color=green>`FT_STATISTICS_CROSSVALIDATE`</font>``</a>`, `<a href=/reference/ft_statistics_stats>``<font color=green>`FT_STATISTICS_STATS`</font>``</a>`
`</pre>``</html>`

