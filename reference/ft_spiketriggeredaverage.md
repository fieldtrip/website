---
layout: default
---

##  FT_SPIKETRIGGEREDAVERAGE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_spiketriggeredaverage".

`<html>``<pre>`
    `<a href=/reference/ft_spiketriggeredaverage>``<font color=green>`FT_SPIKETRIGGEREDAVERAGE`</font>``</a>` computes the avererage of the LFP around the
    spikes.
 
    Use as
    [timelock] = ft_spiketriggeredaverage(cfg, data)
 
    The input data should be organised in a structure as obtained from
    the `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>` function. The configuration should be according to
 
    cfg.timwin       = [begin end], time around each spike (default = [-0.1 0.1])
    cfg.spikechannel = string, name of single spike channel to trigger on
    cfg.channel      = Nx1 cell-array with selection of channels (default = 'all'),
                       see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.latency 
    cfg.keeptrials   = 'yes' or 'no', return individual trials or average (default = 'no')
    cfg.feedback     = 'no', 'text', 'textbar', 'gui' (default = 'no')
`</pre>``</html>`

