---
title: ft_trialfun_trial
---
```
 FT_TRIALFUN_TRIAL creates a trial definition that corresponds to the
 events that are returned by FT_READ_EVENT with type='trial'

 You can use this function as follows
   cfg           = [];   
   cfg.dataset   = string, containing filename or directory
   cfg.trialfun  = 'ft_trialfun_trial';
   cfg           = definetrial(cfg);
   data          = preprocessing(cfg);

 See also FT_DEFINETRIAL, FT_PREPROCESSING
```
