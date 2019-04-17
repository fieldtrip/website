---
title: ft_trialfun_example1
---
```
 FT_TRIALFUN_EXAMPLE1 is an example trial function. It searches for events
 of type "trigger" and specifically for a trigger with value 7, followed
 by a trigger with value 64.
 
 You would use this function as follows
   cfg           = [];   
   cfg.dataset   = string, containing filename or directory
   cfg.trialfun  = 'ft_trialfun_example1';
   cfg           = definetrial(cfg);
   data          = preprocessing(cfg);

 You can use this example trial function as template for your own
 conditial trial definitions.

 See also FT_DEFINETRIAL, FT_PREPROCESSING
```
