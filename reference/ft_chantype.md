---
layout: default
---

##  FT_CHANTYPE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_chantype".

`<html>``<pre>`
    `<a href=/reference/ft_chantype>``<font color=green>`FT_CHANTYPE`</font>``</a>` determines for each individual channel what chantype of data it
    represents, e.g. a planar gradiometer, axial gradiometer, magnetometer,
    trigger channel, etc. If you want to know what the acquisition system is
    (e.g. ctf151 or neuromag306), you should not use this function but
    `<a href=/reference/ft_senstype>``<font color=green>`FT_SENSTYPE`</font>``</a>` instead.
 
    Use as
    type = ft_chantype(hdr)
    type = ft_chantype(sens)
    type = ft_chantype(label)
    or as
    type = ft_chantype(hdr,   desired)
    type = ft_chantype(sens,  desired)
    type = ft_chantype(label, desired)
 
    If the desired unit is not specified as second input argument, this
    function returns a Nchan*1 cell-array with a string describing the type
    of each channel.
 
    If the desired unit is specified as second input argument, this function
    returns a Nchan*1 boolean vector with "true" for the channels of the
    desired type and "false" for the ones that do not match.
 
    The specification of the channel types depends on the acquisition system,
    for example the ctf275 system includes the following tyoe of channel
    meggrad, refmag, refgrad, adc, trigger, eeg, headloc, headloc_gof.
 
    See also `<a href=/reference/ft_read_header>``<font color=green>`FT_READ_HEADER`</font>``</a>`, `<a href=/reference/ft_senstype>``<font color=green>`FT_SENSTYPE`</font>``</a>`, `<a href=/reference/ft_chanunit>``<font color=green>`FT_CHANUNIT`</font>``</a>`
`</pre>``</html>`

