---
layout: default
---

##  FT_SPIKESPLITTING

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_spikesplitting".

`<html>``<pre>`
    `<a href=/reference/ft_spikesplitting>``<font color=green>`FT_SPIKESPLITTING`</font>``</a>` reads a single Neuralynx DMA log file and writes each
    individual channel to a seperate file.
 
    Use as
    [cfg] = ft_spikesplitting(cfg)
 
    The configuration should contain
    cfg.dataset   = string with the name of the DMA log file
    cfg.channel   = Nx1 cell-array with selection of channels (default = 'all'), see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.output    = string with the name of the splitted DMA dataset directory, (default is determined automatic)
    cfg.latency   = [begin end], (default = 'all')
    cfg.feedback  = string, (default = 'textbar')
    cfg.format    = 'int16' or 'int32' (default = 'int32')
    cfg.downscale = single number or vector (for each channel), corresponding to the number of bits removed from the LSB side (default = 0)
 
    This function expects the DMA file to be read as AD units (and not in uV)
    and will write the same AD values to the splitted DMA files. If you
    subsequently want to process the splitted DMA, you should look up the
    details of the headstage amplification and the Neuralynx amplifier and
    scale the values accordingly.
 
    See also `<a href=/reference/ft_spikedownsample>``<font color=green>`FT_SPIKEDOWNSAMPLE`</font>``</a>`, FT_SPIKEANALYSIS
`</pre>``</html>`

