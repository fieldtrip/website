---
title: ft_spike_maketrials
---
```
 FT_SPIKE_MAKETRIALS converts raw timestamps in a SPIKE structure to spike
 times that are relative to an event trigger in an SPIKE structure. This
 is a preprocessing step to use functions such as FT_SPIKE_PSTH.

 The main function of FT_SPIKE_MAKETRIALS is to create the field
 spike.time and spike.trial, which contain the trial numbers in which the
 spikes were recorded, and the onset and offset of the trial relative to
 trigger time t = 0.

 Use as
   [spike] = ft_spike_maketrials(cfg,spike)

 Inputs:
     spike: The raw spike datatype, obtained from FT_READ_SPIKE

 Configurations:

   cfg.trl  = is an nTrials-by-M matrix, with at least 3 columns:
     Every row contains start (col 1), end (col 2) and offset of the event
     trigger in the trial in timestamp or sample units (cfg.trlunit). 
     For example, an offset of -1000 means that the trigger (t = 0 sec) 
     occurred 1000 timestamps or samples after the
     trial start.
     If more columns are added than 3, these are used to construct the
     spike.trialinfo field having information about the trial.
     Note that values in cfg.trl get inaccurate above 2^53 (in that case 
     it is better to use the original uint64 representation)

   cfg.trlunit = 'timestamps' (default) or 'samples'. 
     If 'samples', cfg.trl should 
     be specified in samples, and cfg.hdr = data.hdr should be specified.
     This option can be used to reuse a cfg.trl that was used for
     preprocessing LFP data. 
     If 'timestamps', cfg.timestampspersecond should be
     specified, but cfg.hdr should not.

   cfg.hdr     = struct, should be specified if cfg.trlunit = 'samples'.
     This should be specified as cfg.hdr = data.hdr where data.hdr
     contains the subfields data.hdr.Fs (sampling frequency of the LFP),
     data.hdr.FirstTimeStamp, and data.hdr.TimeStampPerSecond.

   cfg.timestampspersecond = number of timestaps per second (for
     Neuralynx, 1000000 for example). This can be computed for example from
     the LFP hdr (cfg.timestampspersecond = data.hdr.Fs*data.hdr.TimeStampPerSecond)
     or is a priori known.

 Outputs appended to spike:
   spike.time                  = 1-by-nUnits cell-array, containing the spike times in
                                 seconds relative to the event trigger.
   spike.trial                 = 1-by-nUnits cell-array, containing the trial number for
                                 every spike telling in which trial it was recorded.
   spike.trialtime             = nTrials-by-2 matrix specifying the start and end of
                                 every trial in seconds.
   spike.trialinfo             = contains trial information
```
