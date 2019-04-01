---
title: ft_trialfun_general
---
```
 FT_TRIALFUN_GENERAL determines trials/segments in the data that are
 interesting for analysis, using the general event structure returned
 by read_event. This function is independent of the dataformat

 The trialdef structure can contain the following specifications
   cfg.trialdef.eventtype  = string
   cfg.trialdef.eventvalue = number, string or list with numbers or strings
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

 See also FT_DEFINETRIAL, FT_PREPROCESSING
```
