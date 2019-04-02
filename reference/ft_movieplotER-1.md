---
title: ft_movieplotER
---
```
 FT_MOVIEPLOTER makes a movie of the the event-related potentials, event-related
 fields or oscillatory activity (power or coherence) versus frequency.

 Use as
   ft_movieplotER(cfg, timelock)
 where the input data is from FT_TIMELOCKANALYSIS and the configuration
 can contain
   cfg.parameter    = string, parameter that is color coded (default = 'avg')
   cfg.xlim         = 'maxmin' or [xmin xmax] (default = 'maxmin')
   cfg.zlim         = plotting limits for color dimension, 'maxmin',
                          'maxabs', 'zeromax', 'minzero', or [zmin zmax] (default = 'maxmin')
   cfg.samperframe  = number, samples per fram (default = 1)
   cfg.framespersec = number, frames per second (default = 5)
   cfg.framesfile   = [], no file saved, or 'string', filename of saved frames.mat (default = []);
   cfg.layout       = specification of the layout, see below
   cfg.baseline     = 'yes','no' or [time1 time2] (default = 'no'), see FT_TIMELOCKBASELINE
   cfg.baselinetype = 'absolute' or 'relative' (default = 'absolute')
   cfg.colorbar     = 'yes', 'no' (default = 'no')

 The layout defines how the channels are arranged. You can specify the
 layout in a variety of ways:
  - you can provide a pre-computed layout structure (see prepare_layout)
  - you can give the name of an ascii layout file with extension *.lay
  - you can give the name of an electrode file
  - you can give an electrode definition, i.e. "elec" structure
  - you can give a gradiometer definition, i.e. "grad" structure
 If you do not specify any of these and the data structure contains an
 electrode or gradiometer structure, that will be used for creating a
 layout. If you want to have more fine-grained control over the layout
 of the subplots, you should create your own layout file.

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
 If you specify this option the input data will be read from a *.mat
 file on disk. This mat files should contain only a single variable named 'data',
 corresponding to the input structure.

 See also FT_MULTIPLOTER, FT_TOPOPLOTER, FT_SINGLEPLOTER, FT_MOVIEPLOTTFR, FT_SOURCEMOVIE
```
