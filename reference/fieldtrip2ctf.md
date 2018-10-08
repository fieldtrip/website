---
layout: default
---

##  FIELDTRIP2CTF

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help fieldtrip2ctf".

`<html>``<pre>`
    `<a href=/reference/fieldtrip2ctf>``<font color=green>`FIELDTRIP2CTF`</font>``</a>` saves a FieldTrip data structures to a corresponding CTF file. The
    file to which the data is exported depends on the input data structure that you
    provide.
 
    Use as
    fieldtrip2ctf(filename, data, ...)
    where "filename" is a string, "data" is a FieldTrip data structure, and
    additional options can be specified as key-value pairs.
 
    The FieldTrip "montage" structure (see `<a href=/reference/ft_apply_montage>``<font color=green>`FT_APPLY_MONTAGE`</font>``</a>` and the cfg.montage
    option in `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`) can be exported to a CTF "Virtual Channels" file.
 
    At this moment the support for other FieldTrip structures and CTF fileformats is
    still limited, but this function serves as a placeholder for future improvements.
 
    See also `<a href=/reference/ft_volumewrite>``<font color=green>`FT_VOLUMEWRITE`</font>``</a>`, `<a href=/reference/ft_sourcewrite>``<font color=green>`FT_SOURCEWRITE`</font>``</a>`, `<a href=/reference/ft_write_data>``<font color=green>`FT_WRITE_DATA`</font>``</a>`
`</pre>``</html>`

