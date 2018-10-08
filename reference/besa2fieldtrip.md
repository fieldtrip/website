---
layout: default
---

##  BESA2FIELDTRIP

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help besa2fieldtrip".

`<html>``<pre>`
    `<a href=/reference/besa2fieldtrip>``<font color=green>`BESA2FIELDTRIP`</font>``</a>` reads and converts various BESA datafiles into a FieldTrip
    data structure, which subsequently can be used for statistical analysis
    or other analysis methods implemented in Fieldtrip.
 
    Use as
    [data] = besa2fieldtrip(filename)
    where the filename should point to a BESA datafile (or data that
    was exported by BESA). The output is a MATLAB structure that is
    compatible with FieldTrip.
 
    The format of the output structure depends on the type of datafil

    *.avr is converted to a structure similar to the output of `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`
    *.mul is converted to a structure similar to the output of `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`
    *.swf is converted to a structure similar to the output of `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>` (*)
    *.tfc is converted to a structure similar to the output of `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`     (*)
    *.dat is converted to a structure similar to the output of FT_SOURCANALYSIS
    *.dat combined with a *.gen or *.generic is converted to a structure similar to the output of `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`
 
    Note (*): If the BESA toolbox by Karsten Hochstatter is found on your
    MATLAB path, the readBESAxxx functions will be used (where xxx=tfc/swf),
    alternatively the private functions from FieldTrip will be used.
 
    See also EEGLAB2FIELDTRIP, `<a href=/reference/spm2fieldtrip>``<font color=green>`SPM2FIELDTRIP`</font>``</a>`
`</pre>``</html>`

