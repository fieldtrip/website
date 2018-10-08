---
layout: default
---

##  FT_TIMELOCKSIMULATION

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_timelocksimulation".

`<html>``<pre>`
    `<a href=/reference/ft_timelocksimulation>``<font color=green>`FT_TIMELOCKSIMULATION`</font>``</a>` computes a simulated signal that resembles an
    event-related potential or field
 
    Use as
    timelock = ft_timelockstatistics(cfg)
    which will return a datastructure that resembles the output of
    `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`.
 
    cfg.fsample    = simulated sample frequency (default = 1000)
    cfg.trllen     = length of simulated trials in seconds (default = 1)
    cfg.numtrl     = number of simulated trials (default = 10)
    cfg.baseline   = number (default = 0.3)
 
    The signal is constructed from three underlying functions. The shape is
    controlled with
    cfg.s1.numcycli = number (default = 1)
    cfg.s1.ampl     = number (default = 1.0)
    cfg.s2.numcycli = number (default = 2)
    cfg.s2.ampl     = number (default = 0.7)
    cfg.s3.numcycli = number (default = 4)
    cfg.s3.ampl     = number (default = 0.2)
    cfg.noise.ampl  = number (default = 0.1)
 
    Specifying numcycli=1 results in a monophasic signal, numcycli=2 is a biphasic,
    etc. The three signals are scaled to the indicated amplitude, summed up and a
    certain amount of noise is added.
 
    Following construction of the signal in each trial according to the
    specification, the signals are averaged over trials. Both the average, the
    variance and the individual trial signals are returned.
 
    See also `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`, `<a href=/reference/ft_timelockstatistics>``<font color=green>`FT_TIMELOCKSTATISTICS`</font>``</a>`, `<a href=/reference/ft_freqsimulation>``<font color=green>`FT_FREQSIMULATION`</font>``</a>`,
    `<a href=/reference/ft_dipolesimulation>``<font color=green>`FT_DIPOLESIMULATION`</font>``</a>`, `<a href=/reference/ft_connectivitysimulation>``<font color=green>`FT_CONNECTIVITYSIMULATION`</font>``</a>`
`</pre>``</html>`

