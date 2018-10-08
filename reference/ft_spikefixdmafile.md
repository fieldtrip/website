---
layout: default
---

##  FT_SPIKEFIXDMAFILE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_spikefixdmafile".

`<html>``<pre>`
    `<a href=/reference/ft_spikefixdmafile>``<font color=green>`FT_SPIKEFIXDMAFILE`</font>``</a>` fixes the problem in DMA files due to stopping and
    restarting the acquisition. It takes one Neuralynx DMA file and and
    creates seperate DMA files, each corresponding with one continuous
    section of the recording.
 
    Use as
    ft_spikefixdmafile(cfg)
    where the configuration should contain
    cfg.dataset   = string with the name of the DMA log file
    cfg.output    = string with the name of the DMA log file, (default is determined automatic)
    cfg.numchans  = number of channels (default = 256)
 
    See also `<a href=/reference/ft_spikesplitting>``<font color=green>`FT_SPIKESPLITTING`</font>``</a>`
`</pre>``</html>`

