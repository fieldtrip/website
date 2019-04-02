---
title: ft_read_spike
---
```
 FT_READ_SPIKE reads spike timestamps and waveforms from various data
 formats.

 Use as
  [spike] = ft_read_spike(filename, ...)

 Additional options should be specified in key-value pairs and can be
   'spikeformat' = string, described the fileformat (default is automatic)

 The following file formats are supported
   'mclust_t'
   'neuralynx_ncs' 
   'neuralynx_nse'
   'neuralynx_nst'
   'neuralynx_ntt'
   'neuralynx_nts'
   'plexon_ddt'
   'plexon_nex'
   'plexon_plx'
   'neuroshare'
   'neurosim_spikes'
   'wave_clus'

 The output spike structure usually contains
   spike.label     = 1xNchans cell-array, with channel labels
   spike.waveform  = 1xNchans cell-array, each element contains a matrix (Nleads x Nsamples X Nspikes)
   spike.waveformdimord = '{chan}_lead_time_spike'
   spike.timestamp = 1xNchans cell-array, each element contains a vector (1 X Nspikes)
   spike.unit      = 1xNchans cell-array, each element contains a vector (1 X Nspikes)
 and is described in more detail in FT_DATATYPE_SPIKE

 See also FT_DATATYPE_SPIKE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT
```
