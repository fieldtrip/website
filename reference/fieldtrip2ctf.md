---
title: fieldtrip2ctf
---
```
 FIELDTRIP2CTF saves a FieldTrip data structures to a corresponding CTF file. The
 file to which the data is exported depends on the input data structure that you
 provide.

 Use as
   fieldtrip2ctf(filename, data, ...)
 where "filename" is a string, "data" is a FieldTrip data structure, and
 additional options can be specified as key-value pairs.

 The FieldTrip "montage" structure (see FT_APPLY_MONTAGE and the cfg.montage
 option in FT_PREPROCESSING) can be exported to a CTF "Virtual Channels" file.

 At this moment the support for other FieldTrip structures and CTF fileformats is
 still limited, but this function serves as a placeholder for future improvements.

 See also FT_VOLUMEWRITE, FT_SOURCEWRITE, FT_WRITE_DATA
```
