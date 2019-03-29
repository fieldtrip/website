---
title: ft_realtime_packettimer
---
```
 FT_REALTIME_PACKETTIMER can be used to time the rate at which data can be processed

 Use as
   ft_realtime_packettimer(cfg)
 with the following configuration options
   cfg.bcifun    = processing of the data (default = @bcifun_timer)
   cfg.npackets  = the number of packets shown in one plot (default=1000)
                     after reaching the end
   cfg.saveplot  = if path is specified, first plot is saved (default=[]);
   cfg.rellim = y limits of subplot 1 (default = [-100 100])

 SEE ALSO:
   FT_REALTIME_PROCESS
```
