---
layout: default
---

##  FT_ELECTRODERMALACTIVITY

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_electrodermalactivity".

`<html>``<pre>`
    `<a href=/reference/ft_electrodermalactivity>``<font color=green>`FT_ELECTRODERMALACTIVITY`</font>``</a>` estimates the electrodermal activity from a recording of
    the electric resistance of the skin.
 
    Use as
    eda = ft_electrodermalactivity(cfg, data)
    where the input data is a structure as obtained from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    The configuration structure has the following options
    cfg.channel        = selected channel for processing, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>`
    cfg.feedback       = 'yes' or 'no'
    cfg.medianwindow   = scalar, length of window for median filter in seconds (default = 8)
 
    After using this function you can use `<a href=/reference/ft_redefinetrial>``<font color=green>`FT_REDEFINETRIAL`</font>``</a>` and FT_TIMELOCKANLAYSIS to
    investigate electrodermal responses (EDRs) to stimulation. You can use
    `<a href=/reference/ft_artifact_threshold>``<font color=green>`FT_ARTIFACT_THRESHOLD`</font>``</a>` to determine the timing and frequency of nonspecific EDRs.
 
    See https://doi.org/10.1111/j.1469-8986.2012.01384.x "Publication recommendations
    for electrodermal measurements" by the SPR for an introduction in electrodermal
    methods and for recommendations.
 
    See also `<a href=/reference/ft_heartrate>``<font color=green>`FT_HEARTRATE`</font>``</a>`, `<a href=/reference/ft_headmovement>``<font color=green>`FT_HEADMOVEMENT`</font>``</a>`, `<a href=/reference/ft_regressconfound>``<font color=green>`FT_REGRESSCONFOUND`</font>``</a>`
`</pre>``</html>`

