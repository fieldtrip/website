---
title: ft_realtime_fmriproxy
---
```
 FT_REALTIME_FMRIPROXY simulates an fMRI acquisition system by writing volumes in a
 cycle of about 2 seconds. The voxel data is written as a column vector with X*Y*Z
 channels, where X and Y are the readout and phase-encoding resolution, and Z is the
 number of slices. The voxel data consists of a ellipsoid (a bit like a head) with
 added lateralized activation (20 scan cycle) and noise.

 This function also writes out events of type='scan' and value='pulse' when the
 simulated scanner initiates a scan, and value='ready' when a hypothetical
 processing pipeline is finished with that scan, just after writing out the volume
 data itself. There is an artificial delay of 1.3*TR between the two events.

 Use as
   ft_realtime_fmriproxy(cfg)

 The target to write the data to is configured as
   cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')

 You can also select a resolution of the simulated volumes (default = [64,64,20]) like
   cfg.voxels = [64 64 32]
 and the repetition time (TR, default = 0.08*number of slices) in seconds using
   cfg.TR = 2.0

 To stop this realtime function, you have to press Ctrl-C

 See also FT_REALTIME_SIGNALPROXY, FT_REALTIME_SIGNALVIEWER
```
