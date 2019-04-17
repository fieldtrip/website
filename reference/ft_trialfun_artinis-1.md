---
title: ft_trialfun_artinis
---
```
 FT_TRIALFUN_ARTINIS is adjoining the result of ft_trialfun_general and
 those events found by FT_TRIALFUN_GENERAL.

 The trialdef structure can contain the following specifications
   cfg.trialdef.eventtype  = 'string'
   cfg.trialdef.eventvalue = number, string or list with numbers or strings
   cfg.trialdef.oxyproj    = 'string', indicating an oxyproj-file, in
                             which information about the events for this
                             oxy3-file are stored
   cfg.trialdef.prestim    = latency in seconds (optional)
   cfg.trialdef.poststim   = latency in seconds (optional)

 If you want to read all data from a continuous file in segments, you can specify
    cfg.trialdef.triallength = duration in seconds (can be Inf)
    cfg.trialdef.ntrials     = number of trials

 If you specify
   cfg.trialdef.eventtype  = '?'
 a list with the events in your datafile will be displayed on screen.

 If you specify
   cfg.trialdef.eventtype = 'gui'
 a graphical user interface will allow you to select events of interest.

 See also FT_TRIALFUN_GENERAL, FT_DEFINETRIAL, FT_PREPROCESSING
```
