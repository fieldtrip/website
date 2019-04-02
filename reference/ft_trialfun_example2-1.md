---
title: ft_trialfun_example2
---
```
 FT_TRIALFUN_EXAMPLE2 is an example trial function that detects muscle
 activity in an EMG channel and defines variable length trials from the
 EMG onset up to the EMG offset.

 You would use this function as follows
   cfg           = [];   
   cfg.dataset   = string, containing filename or directory
   cfg.trialfun  = 'ft_trialfun_example2';
   cfg           = definetrial(cfg);
   data          = preprocessing(cfg);

 Note that there are some parameters, like the EMG channel name and the
 processing that is done on the EMG channel data, which are hardcoded in
 this trial function. You should change these parameters if neccessary.

 See also FT_DEFINETRIAL, FT_PREPROCESSING
```
