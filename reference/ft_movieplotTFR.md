---
title: ft_movieplotTFR
---
```
 FT_MOVIEPLOTTFR makes a movie of the time-frequency representation of power or
 coherence.

 Use as
   ft_movieplotTFR(cfg, data)
 where the input data comes from FT_FREQANALYSIS or FT_FREQDESCRIPTIVES and the
 configuration is a structure that can contain
   cfg.parameter    = string, parameter that is color coded (default = 'avg')
   cfg.xlim         = selection boundaries over first dimension in data (e.g., time)
                          'maxmin' or [xmin xmax] (default = 'maxmin')
   cfg.ylim         = selection boundaries over second dimension in data (e.g., freq)
                          'maxmin' or [xmin xmax] (default = 'maxmin')
   cfg.zlim         = plotting limits for color dimension, 'maxmin',
                          'maxabs', 'zeromax', 'minzero', or [zmin zmax] (default = 'maxmin')
   cfg.samperframe  = number, samples per fram (default = 1)
   cfg.framespersec = number, frames per second (default = 5)
   cfg.framesfile   = [] (optional), no file saved, or 'string', filename of saved frames.mat (default = []);
   cfg.moviefreq    = number, movie frames are all time points at the fixed frequency moviefreq (default = []);
   cfg.movietime    = number, movie frames are all frequencies at the fixed time movietime (default = []);
   cfg.layout       = specification of the layout, see below
   cfg.interactive  = 'no' or 'yes', make it interactive
   cfg.baseline     = 'yes','no' or [time1 time2] (default = 'no'), see FT_TIMELOCKBASELINE or FT_FREQBASELINE
   cfg.baselinetype = 'absolute', 'relative', 'relchange', 'normchange', 'db' or 'zscore' (default = 'absolute')
   cfg.colorbar     = 'yes', 'no' (default = 'no')

 the layout defines how the channels are arranged. you can specify the
 layout in a variety of ways:
  - you can provide a pre-computed layout structure (see prepare_layout)
  - you can give the name of an ascii layout file with extension *.mat
  - you can give the name of an electrode file
  - you can give an electrode definition, i.e. "elec" structure
  - you can give a gradiometer definition, i.e. "grad" structure
 if you do not specify any of these and the data structure contains an
 electrode or gradiometer structure, that will be used for creating a
 layout. if you want to have more fine-grained control over the layout
 of the subplots, you should create your own layout file.

 to facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
 if you specify this option the input data will be read from a *.mat
 file on disk. this mat files should contain only a single variable named 'data',
 corresponding to the input structure.

 See also FT_MULTIPLOTTFR, FT_TOPOPLOTTFR, FT_SINGLEPLOTTFR, FT_MOVIEPLOTER, FT_SOURCEMOVIE
```
