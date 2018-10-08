---
layout: default
---

##  IMOTIONS2FIELDTRIP

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help imotions2fieldtrip".

`<html>``<pre>`
    `<a href=/reference/imotions2fieldtrip>``<font color=green>`IMOTIONS2FIELDTRIP`</font>``</a>` imports an iMotions *.txt file and represents it as a FieldTrip
    raw data structure.
 
    Use as
    data = imotions2fieldtrip(filename, ...)
 
    Additional options should be specified in key-value pairs and can be
    interpolate   = 'no', 'time' or 'data' (default = 'no')
    isnumeric     = cell-array with labels corresponding to numeric data (default = {})
    isinteger     = cell-array with labels corresponding to integer data that should be interpolated with nearest where applicable (default = {})
    isnotnumeric  = cell-array with labels not corresponding to numeric data (default = {})
    isevent       = cell-array with labels corresponding to events (default = {})
    isnotevent    = cell-array with labels not corresponding to events (default = {})
 
    The options 'isnumeric' and 'isnotnumeric' are mutually exclusive. Idem for
    'isevent' and 'isnotevent'.
 
    When using the interpolate='data' option, both the data and the time are interpolated
    to a regularly sampled representation, when using the interpolate='time' option, only
    the time axis is interpolated to a regularly sampled representation.  This addresses
    the case that the data was actually acquired with a regular sampling rate, but the time
    stamps in the file are not correctly representing this (a known bug with some type of
    iMotions data).
 
    See also `<a href=/reference/ft_datatype_raw>``<font color=green>`FT_DATATYPE_RAW`</font>``</a>`, `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`, `<a href=/reference/ft_heartrate>``<font color=green>`FT_HEARTRATE`</font>``</a>`, `<a href=/reference/ft_electrodermalactivity>``<font color=green>`FT_ELECTRODERMALACTIVITY`</font>``</a>`
`</pre>``</html>`

