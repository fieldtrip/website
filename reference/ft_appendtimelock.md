---
layout: default
---

##  FT_APPENDTIMELOCK

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_appendtimelock".

`<html>``<pre>`
    `<a href=/reference/ft_appendtimelock>``<font color=green>`FT_APPENDTIMELOCK`</font>``</a>` concatenates multiple timelock (ERP/ERF) data structures that
    have been processed seperately. If the input data structures contain different
    channels, it will be concatenated along the channel direction. If the channels are
    identical in the input data structures, the data will be concatenated along the
    repetition dimension.
 
    Use as
    combined = ft_appendtimelock(cfg, timelock1, timelock2, ...)
 
    The configuration can optionally contain
    cfg.appenddim  = string, the dimension to concatenate over which to append,
                     this can be 'chan' and 'rpt' (default is automatic)
    cfg.tolerance  = scalar, tolerance to determine how different the time axes
                     are allowed to still be considered compatible (default = 1e-5)
 
    See also `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`, `<a href=/reference/ft_datatype_timelock>``<font color=green>`FT_DATATYPE_TIMELOCK`</font>``</a>`, `<a href=/reference/ft_appenddata>``<font color=green>`FT_APPENDDATA`</font>``</a>`, `<a href=/reference/ft_appendfreq>``<font color=green>`FT_APPENDFREQ`</font>``</a>`,
    `<a href=/reference/ft_appendsource>``<font color=green>`FT_APPENDSOURCE`</font>``</a>`, `<a href=/reference/ft_appendsens>``<font color=green>`FT_APPENDSENS`</font>``</a>`
`</pre>``</html>`

