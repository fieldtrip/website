---
title: ft_preproc_rereference
---
```
 FT_PREPROC_REREFERENCE computes the average reference over all EEG channels
 or rereferences the data to the selected channels

 Use as
   [dat] = ft_preproc_rereference(dat, refchan, method, handlenan)
 where
   dat        data matrix (Nchans X Ntime)
   refchan    vector with indices of the new reference channels, or 'all'
   method     string, can be 'avg' or 'median'
   handlenan  boolean, can be true or false

 If the new reference channel is not specified, the data will be
 rereferenced to the average of all channels.

 See also PREPROC
```
