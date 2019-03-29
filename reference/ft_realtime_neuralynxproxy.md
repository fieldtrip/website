---
title: ft_realtime_neuralynxproxy
---
```
 FT_REALTIME_NEURALYNXPROXY reads continuous data from a Neuralynx Cheetah
 acquisition system and writes it to a FieldTrip buffer.

 The FieldTrip buffer is a network transparent server that allows the acquisition
 client to stream data to it. An analysis client can connect to read the data upon
 request. Multiple clients can connect simultaneously, each analyzing a specific
 aspect of the data concurrently.

 Use as
   ft_realtime_neuralynxproxy(cfg)

 The configuration should contain
   cfg.acquisition          = string, name of computer running the Cheetah software (default = 'fcdc284')
   cfg.channel              = cell-array, see FT_CHANNELSELECTION (default = 'all')

 The target to write the data to is configured as
   cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
   cfg.target.dataformat    = string, default is determined automatic

 To stop this realtime function, you have to press Ctrl-C

 See also FT_REALTIME_SIGNALPROXY, FT_REALTIME_SIGNALVIEWER
```
