---
title: ft_redefinetrial
---
```
 FT_REDEFINETRIAL allows you to adjust the time axis of your data, i.e. to
 change from stimulus-locked to response-locked. Furthermore, it allows
 you to select a time window of interest, or to resegment your long trials
 into shorter fragments.

 Use as
   data = ft_redefinetrial(cfg, data)
 where the input data should correspond to the output of FT_PREPROCESSING and
 the configuration should be specified as explained below. Note that some
 options are mutually exclusive, and require two calls to this function to
 avoid confusion about the order in which they are applied.

 For selecting a subset of trials you can specify
   cfg.trials    = 'all' or a selection given as a 1xN vector (default = 'all')

 For selecting trials with a minimum length you can specify
   cfg.minlength = length in seconds, can be 'maxperlen' (default = [])

 For realiging the time axes of all trials to a new reference time
 point (i.e. change the definition for t=0) you can use the following
 configuration option
   cfg.offset    = single number or Nx1 vector, expressed in samples relative to current t=0

 For selecting a specific subsection of (i.e. cut out a time window
 of interest) you can select a time window in seconds that is common
 in all trials
   cfg.toilim    = [tmin tmax] to specify a latency window in seconds, can be Nx2 vector

 Alternatively you can specify the begin and end sample in each trial
   cfg.begsample = single number or Nx1 vector, expressed in samples relative to the start of the input trial
   cfg.endsample = single number or Nx1 vector, expressed in samples relative to the start of the input trial

 Alternatively you can specify a new trial definition, expressed in
 samples relative to the original recording
   cfg.trl       = Nx3 matrix with the trial definition, see FT_DEFINETRIAL

 Alternatively you can specify the data to be cut into (non-)overlapping
 segments, starting from the beginning of each trial. This may lead to loss
 of data at the end of the trials
   cfg.length    = single number (in unit of time, typically seconds) of the required snippets
   cfg.overlap   = single number (between 0 and 1 (exclusive)) specifying the fraction of overlap between snippets (0 = no overlap)

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a *.mat
 file on disk and/or the output data will be written to a *.mat file. These mat
 files should contain only a single variable, corresponding with the
 input/output structure.

 See also FT_DEFINETRIAL, FT_RECODEEVENT, FT_PREPROCESSING
```
