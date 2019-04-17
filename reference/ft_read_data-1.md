---
title: ft_read_data
---
```
 FT_READ_DATA reads electrophysiological data from a variety of EEG, MEG and LFP
 files and represents it in a common data-independent format. The supported formats
 are listed in the accompanying FT_READ_HEADER function.

 Use as
   dat = ft_read_data(filename, ...)

 Additional options should be specified in key-value pairs and can be
   'header'         header structure, see FT_READ_HEADER
   'begsample'      first sample to read
   'endsample'      last sample to read
   'begtrial'       first trial to read, mutually exclusive with begsample+endsample
   'endtrial'       last trial to read, mutually exclusive with begsample+endsample
   'chanindx'       list with channel indices to read
   'chanunit'       cell-array with strings, the desired unit of each channel
   'checkboundary'  boolean, whether to check for reading segments over a trial boundary
   'checkmaxfilter' boolean, whether to check that maxfilter has been correctly applied (default = true)
   'cache'          boolean, whether to use caching for multiple reads
   'dataformat'     string
   'headerformat'   string
   'fallback'       can be empty or 'biosig' (default = [])
   'blocking'       wait for the selected number of events (default = 'no')
   'timeout'        amount of time in seconds to wait when blocking (default = 5)

 This function returns a 2-D matrix of size Nchans*Nsamples for continuous
 data when begevent and endevent are specified, or a 3-D matrix of size
 Nchans*Nsamples*Ntrials for epoched or trial-based data when begtrial
 and endtrial are specified.

 The list of supported file formats can be found in FT_READ_HEADER.

 To use an external reading function, you can specify the function name as argument
 to 'dataformat'. The function needs to be on the path, and should take as input:
 filename, hdr, begsample, endsample, chanindx.

 See also FT_READ_HEADER, FT_READ_EVENT, FT_WRITE_DATA, FT_WRITE_EVENT
```
