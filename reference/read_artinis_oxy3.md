---
title: read_artinis_oxy3
---
```plaintext
 reads Artinix oxy3-files into FieldTrip format

 use as
   header = read_artinis_oxy3(filename)
 or 
   event  = read_artinis_oxy3(filename, read_event)
 where read_event is a Boolean with the value true, or  
   data   = read_artinis_oxy3(filename, header, [begsample], [endsample], [chanindx])
 where begsample, endsample and chanindx are optional.

 The returned variables will be in FieldTrip style. 

 See also FT_READ_HEADER, FT_READ_DATA, READ_ARTINIS_OXY4
```
