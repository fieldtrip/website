---
layout: default
---

##  FT_READ_SPIKE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_read_spike".

`<html>``<pre>`
    `<a href=/reference/ft_read_spike>``<font color=green>`FT_READ_SPIKE`</font>``</a>` reads spike timestamps and waveforms from various data
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
 
    The output spike structure usually contains
    spike.label     = 1xNchans cell-array, with channel labels
    spike.waveform  = 1xNchans cell-array, each element contains a matrix (Nleads x Nsamples X Nspikes)
    spike.waveformdimord = '{chan}_lead_time_spike'
    spike.timestamp = 1xNchans cell-array, each element contains a vector (1 X Nspikes)
    spike.unit      = 1xNchans cell-array, each element contains a vector (1 X Nspikes)
    and is described in more detail in `<a href=/reference/ft_datatype_spike>``<font color=green>`FT_DATATYPE_SPIKE`</font>``</a>`
 
    See also `<a href=/reference/ft_datatype_spike>``<font color=green>`FT_DATATYPE_SPIKE`</font>``</a>`, `<a href=/reference/ft_read_header>``<font color=green>`FT_READ_HEADER`</font>``</a>`, `<a href=/reference/ft_read_data>``<font color=green>`FT_READ_DATA`</font>``</a>`, `<a href=/reference/ft_read_event>``<font color=green>`FT_READ_EVENT`</font>``</a>`
`</pre>``</html>`

