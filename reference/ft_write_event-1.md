---
title: ft_write_event
---
```
 FT_WRITE_EVENT writes an event structure to a file, a message daemon
 listening on a network socked, or to another computer connected through
 the serial port.

 Use as
   ft_write_event(filename, event, ...)

 The first argument is a string containing the filename. The second
 argument is a structure with the event. Multiple events can be
 represented as a structure array.

 Events are represented as
   event.type      string
   event.sample    expressed in samples, the first sample of a recording is 1
   event.value     number or string
   event.offset    expressed in samples
   event.duration  expressed in samples
   event.timestamp expressed in timestamp units, which vary over systems (optional)

 Events can also be written to special communication streams
 by specifying the target as URI instead of a filename. Supported are
   buffer://<host>:<port>
   fifo://<filename>
   tcp://<host>:<port>
   udp://<host>:<port>
   mysql://<user>:<password>@<host>:<port>
   rfb://<password>@<host>:<port>
   serial:<port>?key1=value1&key2=value2&...
   rfb://<password>@<host>:<port>

 See also FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT, FT_WRITE_DATA
```
