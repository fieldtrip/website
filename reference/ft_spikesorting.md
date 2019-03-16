---
title: ft_spikesorting
---
```
 FT_SPIKESORTING performs clustering of spike-waveforms and returns the
 unit number to which each spike belongs.

 Use as
   [spike] = ft_spikesorting(cfg, spike)

 The configuration can contain
   cfg.channel         cell-array with channel selection (default = 'all'), see FT_CHANNELSELECTION for details
   cfg.method          'kmeans', 'ward'
   cfg.feedback        'no', 'text', 'textbar', 'gui' (default = 'textbar')
   cfg.kmeans          substructure with additional low-level options for this method
   cfg.ward            substructure with additional low-level options for this method
   cfg.ward.distance   'L1', 'L2', 'correlation', 'cosine'

 The input spike structure can be imported using READ_FCDC_SPIKE and should contain
   spike.label     = 1 x Nchans cell-array, with channel labels
   spike.waveform  = 1 x Nchans cell-array, each element contains a matrix (Nsamples x Nspikes), can be empty
   spike.timestamp = 1 x Nchans cell-array, each element contains a vector (1 x Nspikes)
   spike.unit      = 1 x Nchans cell-array, each element contains a vector (1 x Nspikes)

 See also FT_READ_SPIKE, FT_SPIKEDOWNSAMPLE
```
