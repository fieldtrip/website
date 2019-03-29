---
title: ft_realtime_pooraudioproxy
---
```
 FT_REALTIME_POORAUDIOPROXY reads continuous data from the sound card using the
 standard Matlab API and writes it to a FieldTrip buffer. This proxy has poor timing
 and will produce dropped audio frames between blocks. Also the Matlab documentation
 warns about using this API for long recordings because this will fill up memory and
 degrade performance.

 The FieldTrip buffer is a network transparent server that allows the acquisition
 client to stream data to it. An analysis client can connect to read the data upon
 request. Multiple clients can connect simultaneously, each analyzing a specific
 aspect of the data concurrently.

 Use as
   ft_realtime_pooraudioproxy(cfg)

 The audio-specific configuration structure can contain
   cfg.channel     = number of channels (1 or 2, default=2)
   cfg.blocksize   = size of recorded audio blocks in seconds (default=1)
   cfg.fsample     = audio sampling frequency in Hz (default = 44100)
   cfg.nbits       = recording depth in bits (default = 16)

 Note that currently, the sound will be buffered in double precision irrespective of the sampling bit depth.

 The target to write the data to is configured as
   cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
   cfg.target.dataformat    = string, default is determined automatic

 Finally, there is an option for showing debug output
   cfg.debug       = show sample time and clock time (default = 'yes')

 To stop this realtime function, you have to press Ctrl-C

 See also FT_REALTIME_SIGNALPROXY, FT_REALTIME_SIGNALVIEWER
```
