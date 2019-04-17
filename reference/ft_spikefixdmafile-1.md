---
title: ft_spikefixdmafile
---
```
 FT_SPIKEFIXDMAFILE fixes the problem in DMA files due to stopping and
 restarting the acquisition. It takes one Neuralynx DMA file and and
 creates separate DMA files, each corresponding with one continuous
 section of the recording.

 Use as
   ft_spikefixdmafile(cfg)
 where the configuration should contain
   cfg.dataset   = string with the name of the DMA log file
   cfg.output    = string with the name of the DMA log file, (default is determined automatic)
   cfg.numchans  = number of channels (default = 256)

 See also FT_SPIKESPLITTING
```
