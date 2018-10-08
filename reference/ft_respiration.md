---
layout: default
---

##  FT_RESPIRATION

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_respiration".

`<html>``<pre>`
    `<a href=/reference/ft_respiration>``<font color=green>`FT_RESPIRATION`</font>``</a>` estimates the respiration rate from a respiration belt, temperature
    sensor, movement sensor or from the heart rate. It returns a new data structure
    with a continuous representation of the rate and phase.
 
    Use as
    dataout = ft_respiration(cfg, data)
    where the input data is a structure as obtained from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    The configuration structure has the following options
    cfg.channel          = selected channel for processing, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>`
    cfg.peakseparation   = scalar, time in seconds
    cfg.envelopewindow   = scalar, time in seconds
    cfg.feedback         = 'yes' or 'no'
    The input data can be preprocessed on the fly using
    cfg.preproc.bpfilter = 'yes' or 'no' (default = 'yes')
    cfg.preproc.bpfreq   = [low high], filter frequency in Hz
 
    See also `<a href=/reference/ft_heartrate>``<font color=green>`FT_HEARTRATE`</font>``</a>`, `<a href=/reference/ft_electrodermalactivity>``<font color=green>`FT_ELECTRODERMALACTIVITY`</font>``</a>`, `<a href=/reference/ft_headmovement>``<font color=green>`FT_HEADMOVEMENT`</font>``</a>`, `<a href=/reference/ft_regressconfound>``<font color=green>`FT_REGRESSCONFOUND`</font>``</a>`
`</pre>``</html>`

