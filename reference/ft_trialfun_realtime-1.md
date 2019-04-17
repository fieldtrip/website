---
title: ft_trialfun_realtime
---
```
 FT_TRIALFUN_REALTIME can be used to segment a continuous stream of
 data in real-time. Trials are defined as [begsample endsample offset
 condition]

 The configuration structure can contain the following specifications
   cfg.minsample  = the last sample number that was already considered (passed from rt_process)
   cfg.blocksize  = in seconds. In case of events, offset is with respect to the trigger.
   cfg.offset     = the offset wrt the 0 point. In case of no events, offset is wrt
                    prevSample. E.g., [-0.9 1] will read 1 second blocks with
                    0.9 second overlap
   cfg.bufferdata = {'first' 'last'}. If 'last' then only the last block of
                    interest is read. Otherwise, all well-defined blocks are read (default = 'first')
```
