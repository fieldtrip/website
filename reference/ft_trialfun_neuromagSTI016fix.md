---
title: ft_trialfun_neuromagSTI016fix
---
```plaintext
 FT_TRIALFUN_NAME is supposed to fix the error with STI016 in Neuromag
 data. It reads channels with name STI0* (i.e. the channels STI001-STI016)
 and combine the values into a new "STI101" channel. It then use the new
 channel to define trials.
 
 You would use this function as follows
   cfg                     = [];   
   cfg.dataset             = string, containing filename or directory
   cfg.trialdef.prestim    = pre stim time (in s)
   cfg.trialdef.poststim   = post stim time (in s)
   cfg.trialdef.eventvalue = trigger t 
   cfg.trialfun            = 'ft_trialfun_neuromagSTI016fix';
   cfg                     = definetrial(cfg);
   data                    = preprocessing(cfg);

 You can use this example trial function as template for your own
 conditial trial definitions.

 See also FT_DEFINETRIAL, FT_PREPROCESSING
```
