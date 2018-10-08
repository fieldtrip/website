---
layout: default
---

##  FT_MOVIEPLOTER

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_movieplotER".

`<html>``<pre>`
    `<a href=/reference/ft_movieplotER>``<font color=green>`FT_MOVIEPLOTER`</font>``</a>` makes a movie of the the event-related potentials, event-related
    fields or oscillatory activity (power or coherence) versus frequency.
 
    Use as
    ft_movieplotER(cfg, timelock)
    where the input data is from `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>` and the configuration
    can contain
    cfg.parameter    = string, parameter that is color coded (default = 'avg')
    cfg.xlim         = 'maxmin' or [xmin xmax] (default = 'maxmin')
    cfg.zlim         = plotting limits for color dimension, 'maxmin',
                           'maxabs', 'zeromax', 'minzero', or [zmin zmax] (default = 'maxmin')
    cfg.samperframe  = number, samples per fram (default = 1)
    cfg.framespersec = number, frames per second (default = 5)
    cfg.framesfile   = [], no file saved, or 'string', filename of saved frames.mat (default = []);
    cfg.layout       = specification of the layout, see below
    cfg.baseline     = 'yes','no' or [time1 time2] (default = 'no'), see `<a href=/reference/ft_timelockbaseline>``<font color=green>`FT_TIMELOCKBASELINE`</font>``</a>` or `<a href=/reference/ft_freqbaseline>``<font color=green>`FT_FREQBASELINE`</font>``</a>`
    cfg.baselinetype = 'absolute' or 'relative' (default = 'absolute')
    cfg.colorbar     = 'yes', 'no' (default = 'no')
 
    The layout defines how the channels are arranged. You can specify the
    layout in a variety of way
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
 
    See also `<a href=/reference/ft_multiplotER>``<font color=green>`FT_MULTIPLOTER`</font>``</a>`, `<a href=/reference/ft_topoplotER>``<font color=green>`FT_TOPOPLOTER`</font>``</a>`, `<a href=/reference/ft_singleplotER>``<font color=green>`FT_SINGLEPLOTER`</font>``</a>`, `<a href=/reference/ft_movieplotTFR>``<font color=green>`FT_MOVIEPLOTTFR`</font>``</a>`, `<a href=/reference/ft_sourcemovie>``<font color=green>`FT_SOURCEMOVIE`</font>``</a>`
`</pre>``</html>`

