---
title: ft_timelocksimulation
---
```
 FT_TIMELOCKSIMULATION computes a simulated signal that resembles an
 event-related potential or field

 Use as
   timelock = ft_timelockstatistics(cfg)
 which will return a datastructure that resembles the output of
 FT_TIMELOCKANALYSIS.

   cfg.fsample    = simulated sample frequency (default = 1000)
   cfg.trllen     = length of simulated trials in seconds (default = 1)
   cfg.numtrl     = number of simulated trials (default = 10)
   cfg.baseline   = number (default = 0.3)

 The signal is constructed from three underlying functions. The shape is
 controlled with
   cfg.s1.numcycli = number (default = 1)
   cfg.s1.ampl     = number (default = 1.0)
   cfg.s2.numcycli = number (default = 2)
   cfg.s2.ampl     = number (default = 0.7)
   cfg.s3.numcycli = number (default = 4)
   cfg.s3.ampl     = number (default = 0.2)
   cfg.noise.ampl  = number (default = 0.1)

 Specifying numcycli=1 results in a monophasic signal, numcycli=2 is a biphasic,
 etc. The three signals are scaled to the indicated amplitude, summed up and a
 certain amount of noise is added.

 Following construction of the signal in each trial according to the
 specification, the signals are averaged over trials. Both the average, the
 variance and the individual trial signals are returned.

 See also FT_TIMELOCKANALYSIS, FT_TIMELOCKSTATISTICS, FT_FREQSIMULATION,
 FT_DIPOLESIMULATION, FT_CONNECTIVITYSIMULATION
```
