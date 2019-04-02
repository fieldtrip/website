---
title: ft_spikesplitting
---
```
 FT_SPIKESPLITTING reads a single Neuralynx DMA log file and writes each
 individual channel to a separate file.

 Use as
   [cfg] = ft_spikesplitting(cfg)

 The configuration should contain
   cfg.dataset   = string with the name of the DMA log file
   cfg.channel   = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details
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

 See also FT_SPIKEDOWNSAMPLE, FT_SPIKEANALYSIS
```
