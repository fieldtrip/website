---
title: ft_nirs_scalpcouplingindex
---
```
 FT_NIRS_SCALPCOUPLINGINDEX computes the zero-lag cross-correlation 
 between pairs of raw NIRS-channels to identify bad channels. 

 Use as
   [outdata] = ft_scalpcouplingindex(cfg, indata)
 where indata is raw NIRS-data (in optical densities, ODs)
 and cfg is a configuration structure that should contain

  cfg.threshold    = scalar, the correlation value which has to be
                     exceeded to be labelled a 'good' channel (default
                     0.75)

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a *.mat
 file on disk and/or the output data will be written to a *.mat file. These mat
 files should contain only a single variable, corresponding with the
 input/output structure.
 
 This function is based on Pollonini et al 2014:
 Pollonini, L., Olds, C., Abaya, H., Bortfeld, H., Beauchamp, M. S., & Oghalai, J. S. (2014). 
 Auditory cortex activation to natural speech and simulated cochlear implant speech measured 
 with functional near-infrared spectroscopy. Hearing Research, 309, 84?93. doi:10.1016/j.heares.2013.11.007
 
 Please cite accordingly. Thank you!
 
 See also FT_NIRS_TRANSFORM_ODS
```
