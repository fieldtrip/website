---
title: ft_realtime_signalproxy
---
```
 FT_REALTIME_SIGNALPROXY creates some random data and writes it to a FieldTrip buffer.

 The FieldTrip buffer is a network transparent server that allows the acquisition
 client to stream data to it. An analysis client can connect to read the data upon
 request. Multiple clients can connect simultaneously, each analyzing a specific
 aspect of the data concurrently.

 Use as
   ft_realtime_signalproxy(cfg)
 with the following configuration options
   cfg.blocksize            = number, in seconds (default = 0.5)
   cfg.channel              = cell-array with channel names
   cfg.fsample              = sampling frequency
   cfg.speed                = relative speed at which data is written (default = 1)
   cfg.precision            = numeric representation, can be double, single, int32, int16 (default = 'double')

 The target to write the data to is configured as
   cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
   cfg.target.dataformat    = string, default is determined automatic

 You can apply some filtering to the random number data to make it
 appear slightly more realistic with
   cfg.lpfilter      = 'no' or 'yes'  lowpass  filter (default = 'no')
   cfg.hpfilter      = 'no' or 'yes'  highpass filter (default = 'no')
   cfg.bpfilter      = 'no' or 'yes'  bandpass filter (default = 'no')
   cfg.lpfreq        = lowpass  frequency in Hz
   cfg.hpfreq        = highpass frequency in Hz
   cfg.bpfreq        = bandpass frequency range, specified as [low high] in Hz

 To stop this realtime function, you have to press Ctrl-C

 See also FT_REALTIME_SIGNALPROXY, FT_REALTIME_SIGNALVIEWER
```
