---
title: xdf2fieldtrip
---
```plaintext
 XDF2FIELDTRIP reads data from a XDF file with multiple streams. It upsamples the
 data of all streams to the highest sampling rate and concatenates all channels in
 all streams into a raw data structure that is compatible with the output of
 FT_PREPROCESSING.

 Use as
   data = xdf2fieldtrip(filename, ...)

 Optional arguments should come in key-value pairs and can include
   streamindx  = list, indices of the streams to read (default is all)

 You can also use the standard procedure with FT_DEFINETRIAL and FT_PREPROCESSING
 for XDF files. This will return (only) the stream with the highest sampling rate,
 which is typically the EEG.

 You can use FT_READ_EVENT to read the events from the non-continuous data streams.
 To get them aligned with the samples in one of the specific data streams, you
 should specify the corresponding header structure.

 See also FT_PREPROCESSING, FT_DEFINETRIAL, FT_REDEFINETRIAL
```
