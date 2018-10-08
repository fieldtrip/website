---
layout: default
---

##  SPASS2FIELDTRIP

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help spass2fieldtrip".

`<html>``<pre>`
    `<a href=/reference/spass2fieldtrip>``<font color=green>`SPASS2FIELDTRIP`</font>``</a>` reads data from a set of SPASS data files and converts
    the contents into data structures that FieldTrip understands. Note that
    dependent on the SPASS data it might be required to change some
    hard-coded parameters inside this function.
 
    Use as
    [lfp, spike, stm, bhv] = spass2fieldtrip(dirname)
    Optionally you can specify the sample rate as key-value pairs
   'fsample_ana' - default 1000
   'fsample_swa' - default 32000
 
    The specified directory should contain the SPASS files, and the files should have
    the same name as the directory.
 
    The swa and sti input file are combined into the spike output structure.
    For the rest of the data it is trivial how the input and output relate.
 
    For example, if you specify
    [lfp, spike, bhv, stm] = spass2fieldtrip('jeb012a02')
    then the following files should exis
    'jeb012a02/jeb012a02.ana'
    'jeb012a02/jeb012a02.swa'
    'jeb012a02/jeb012a02.spi'
    'jeb012a02/jeb012a02.stm'
    'jeb012a02/jeb012a02.bhv'
 
    Subsequently you can analyze the data in FieldTrip, or write the spike
    waveforms to a nex file for offline sorting using
    ft_write_spike('jeb012a02_ch1.nex', spike, 'dataformat', 'plexon_nex', 'chanindx', 1)
    ft_write_spike('jeb012a02_ch2.nex', spike, 'dataformat', 'plexon_nex', 'chanindx', 2)
    ft_write_spike('jeb012a02_ch3.nex', spike, 'dataformat', 'plexon_nex', 'chanindx', 3)
 
    See also `<a href=/reference/nutmeg2fieldtrip>``<font color=green>`NUTMEG2FIELDTRIP`</font>``</a>`, `<a href=/reference/loreta2fieldtrip>``<font color=green>`LORETA2FIELDTRIP`</font>``</a>`, `<a href=/reference/fieldtrip2spss>``<font color=green>`FIELDTRIP2SPSS`</font>``</a>`
`</pre>``</html>`

