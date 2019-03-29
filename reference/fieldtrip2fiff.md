---
title: fieldtrip2fiff
---
```
 FIELDTRIP2FIFF saves a FieldTrip raw data structure as a fiff-file, allowing it
 to be further analyzed by the Elekta/Neuromag software, or in the MNE suite
 software.

 Use as
   fieldtrip2fiff(filename, data)
 where filename is the name of the output file, and data is a raw data structure
 as obtained from FT_PREPROCESSING, or a timelock structure obtained from
 FT_TIMELOCKANALYSIS.

 If the data comes from preprocessing and has only one trial, then it writes the
 data into raw continuous format. If present in the data, the original header
 from neuromag is reused (also removing the non-used channels). Otherwise, the
 function tries to create a correct header, which might or might not contain the
 correct scaling and channel location. If the data contains events in the cfg
 structure, it writes the events in the MNE format (three columns) into a file
 based on "filename", ending with "-eve.fif"

 See also FT_DATATYPE_RAW, FT_DATATYPE_TIMELOCK
```
