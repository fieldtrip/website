---
layout: default
---

##  FT_WRITE_DATA

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_write_data".

`<html>``<pre>`
    `<a href=/reference/ft_write_data>``<font color=green>`FT_WRITE_DATA`</font>``</a>` exports electrophysiological data such as EEG to a file. 
 
    Use as
    ft_write_data(filename, dat, ...)
 
    The specified filename can contain the filename extension. If it has no filename
    extension not, it will be added automatically.
 
    Additional options should be specified in key-value pairs and can be
    'header'         header structure that describes the data, see `<a href=/reference/ft_read_header>``<font color=green>`FT_READ_HEADER`</font>``</a>`
    'dataformat'     string, see below
    'append'         boolean, not supported for all formats
    'chanindx'       1xN array
 
    The supported dataformats are
    edf
    gdf
    brainvision_eeg
    neuralynx_ncs
    neuralynx_sdma
    plexon_nex
    riff_wave
    fcdc_matbin
    fcdc_mysql
    fcdc_buffer
    matlab
 
    For EEG data formats, the input data is assumed to be scaled in microvolt.
 
    See also `<a href=/reference/ft_read_header>``<font color=green>`FT_READ_HEADER`</font>``</a>`, `<a href=/reference/ft_read_data>``<font color=green>`FT_READ_DATA`</font>``</a>`, `<a href=/reference/ft_read_event>``<font color=green>`FT_READ_EVENT`</font>``</a>`, `<a href=/reference/ft_write_event>``<font color=green>`FT_WRITE_EVENT`</font>``</a>`
`</pre>``</html>`

