---
layout: default
---

##  NUTMEG2FIELDTRIP

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help nutmeg2fieldtrip".

`<html>``<pre>`
    `<a href=/reference/nutmeg2fieldtrip>``<font color=green>`NUTMEG2FIELDTRIP`</font>``</a>` converts from NUTMEG either a sensor data structure
    ('nuts') to a valid FieldTrip 'raw' structure (plus 'grid' and 'mri' if
    available), OR a source structure 'beam' to a valid FieldTrip source
    structure
 
    Use as
     [data, mri, grid] = nutmeg2fieldtrip(cfg, fileorstruct)
 
    Inpu
       cfg
           .keepmri (required for either input): =1 calls ft_read_mri for 'mri' output; =0 not save out 'mri'
           .out     (required for source input): 's' (pos_freq_time) or 'trial' (pos_rpt)
       fileorstruct: may be one of followin
          1) *.mat file containing nuts sensor structure
          2) nuts sensor structure
          3) s*.mat file containing beam source structure
          4) beam source structure (output from Nutmeg (beamforming_gui, tfbf, or tfZ)
                (only scalar not vector results supported at the moment)
 
    Output: depending on input, one of options
          1) If nuts sensor structure input, then 'data' will be 'raw' and
             optionally 'grid' if Lp present, or 'mri' if individual MRI present
          2) If beam source structure input, then 'data' will be 'source'
             (May be an array of source structures (source{1} etc))
             'grid' and 'mri' may be output as well if present in beam structure
 
    See alo `<a href=/reference/ft_datatype_source>``<font color=green>`FT_DATATYPE_SOURCE`</font>``</a>`, `<a href=/reference/loreta2fieldtrip>``<font color=green>`LORETA2FIELDTRIP`</font>``</a>`, `<a href=/reference/spass2fieldtrip>``<font color=green>`SPASS2FIELDTRIP`</font>``</a>`, `<a href=/reference/fieldtrip2spss>``<font color=green>`FIELDTRIP2SPSS`</font>``</a>`
`</pre>``</html>`

