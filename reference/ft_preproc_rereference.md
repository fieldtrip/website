---
title: ft_preproc_rereference
---
```plaintext
 FT_PREPROC_REREFERENCE computes the average reference over all EEG channels
 or rereferences the data to the selected channels

 Use as
   [dat] = ft_preproc_rereference(dat, refchan, method, handlenan,leadfield)
 REST example: [dat] = ft_preproc_rereference(dat, refchan,
                       'rest',[],leadfield);
 where
   dat        data matrix (Nchans X Ntime)
   refchan    vector with indices of the new reference channels, or 'all'
   method     string, can be 'avg', 'median', or 'rest'
              if select 'rest','leadfield' is required.
              The leadfield should be a matrix (channels X sources)
              which is calculated by using the forward theory, based on
              the electrode montage, head model and equivalent source
              model.
   handlenan  boolean, can be true or false

 If the new reference channel is not specified, the data will be
 rereferenced to the average of all channels.

 See also PREPROC
```
