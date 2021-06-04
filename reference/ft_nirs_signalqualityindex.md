---
title: ft_nirs_signalqualityindex
---
```plaintext
 FT_NIRS_SIGNALQUALITYINDEX processes NIRS data and returns a copy of the 
 original data replaced with nans in the signal segements that are bellow 
 the specified quality threshold.

 Use as
   [out_data] = ft_nirs_signalqualityindex(cfg, in_data)
 where indata is raw NIRS-data (in optical densities, ODs)
 and cfg is a configuration structure.


   cfg.threshold    = scalar, the SQI (signal quality index) value that 
                      has to be exceeded to be labeled as a 'good' 
                      channel (default = 3.5)
   cfg.windowlength = scalar, the length (in seconds) of the signal
                      segments to be analyzed (default = 10)

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a *.mat
 file on disk and/or the output data will be written to a *.mat file. These mat
 files should contain only a single variable, corresponding with the% input/output structure.

 This function is based on:
 - Sappia, M. S., Hakimi, N., Colier, W. N., & Horschig, J. M. (2020). 
   Signal quality index: an algorithm for quantitative assessment of 
   functional near infrared spectroscopy signal quality. Biomedical Optics 
   Express, 11(11), 6732-6754. https://doi.org/10.1364/BOE.409317

 Please cite accordingly. Thank you!

 See also FT_NIRS_TRANSFORM_ODS, SQI
```
