---
title: ft_realtime_ctfproxy
---
```
 FT_REALTIME_CTFPROXY provides a  real-time interface to the MEG data stream.
 This application requires Acq to stream the data to shared memory, and ctf2ft_v1
 (formerly known as AcqBuffer) to be maintaining the shared memory and to prevent
 overruns. This MATLAB function will subsequently copy the data from shared
 memory to a FieldTrip buffer.

 The FieldTrip buffer is a network transparent server that allows the acquisition
 client to stream data to it. An analysis client can connect to read the data upon
 request. Multiple clients can connect simultaneously, each analyzing a specific
 aspect of the data concurrently.

 Since the CTF shared memory interface is only available on the acquisition machine
 itself, this function must run on the acquisition machine. The buffer to which the
 data is streamed is available through the network, so the actual analysis can be
 done elsewhere.

 Use as
   ft_realtime_ctfproxy(cfg)

 The target to write the data to is configured as
   cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
   cfg.target.dataformat    = string, default is determined automatic

 To stop this realtime function, you have to press Ctrl-C

 See also FT_REALTIME_SIGNALPROXY, FT_REALTIME_SIGNALVIEWER
```
