---
layout: default
---

##  FT_DATATYPE_COMP

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_datatype_comp".

`<html>``<pre>`
    `<a href=/reference/ft_datatype_comp>``<font color=green>`FT_DATATYPE_COMP`</font>``</a>` describes the FieldTrip MATLAB structure for comp data
 
    The comp data structure represents time-series channel-level data that has
    been decomposed or unmixed from the channel level into its components or
    "blind sources", for example using ICA (independent component analysis) or
    PCA. This data structure is usually generated with the `<a href=/reference/ft_componentanalysis>``<font color=green>`FT_COMPONENTANALYSIS`</font>``</a>`
    function.
 
    An example of a decomposed raw data structure with 100 components that resulted from
    a 151-channel MEG recording is shown her
 
            topo: [151x100 double]  the compoment topographies
        unmixing: [100x151 double]  the compoment unmixing matrix
       topolabel: {151x1 cell}      the channel labels (e.g. 'MRC13')
           label: {100x1 cell}      the component labels (e.g. 'runica001')
            time: {1x10 cell}       the time axis [1*Ntime double] per trial
           trial: {1x10 cell}       the numeric data [151*Ntime double] per trial
            grad: [1x1 struct]      information about the sensor array (for EEG it is called elec)
             cfg: [1x1 struct]      the configuration used by the function that generated this data structure
 
    The only difference to the raw data structure is that the comp structure contains
    the additional fields unmixing, topo and topolabel. Besides representing the time
    series information as a raw data structure (see `<a href=/reference/ft_datatype_raw>``<font color=green>`FT_DATATYPE_RAW`</font>``</a>`), it is also
    possible for time series information to be represented as timelock or freq
    structures (see `<a href=/reference/ft_datatype_timelock>``<font color=green>`FT_DATATYPE_TIMELOCK`</font>``</a>` or `<a href=/reference/ft_datatype_freq>``<font color=green>`FT_DATATYPE_FREQ`</font>``</a>`).
 
    Required field
    - unmixing, topo, topolabel
 
    Optional field
    - cfg, all fields from `<a href=/reference/ft_datatype_raw>``<font color=green>`FT_DATATYPE_RAW`</font>``</a>`, `<a href=/reference/ft_datatype_timelock>``<font color=green>`FT_DATATYPE_TIMELOCK`</font>``</a>` or `<a href=/reference/ft_datatype_freq>``<font color=green>`FT_DATATYPE_FREQ`</font>``</a>`
 
    Historical field
    - offset, fsample
 
    Revision histor
    (2014) The combination of comp with raw, timelock or freq has been defined explicitly.
 
    (2011) The unmixing matrix has been added to the component data structure.
 
    (2003) The initial version was defined
 
    See also `<a href=/reference/ft_datatype>``<font color=green>`FT_DATATYPE`</font>``</a>`, `<a href=/reference/ft_datatype_comp>``<font color=green>`FT_DATATYPE_COMP`</font>``</a>`, `<a href=/reference/ft_datatype_dip>``<font color=green>`FT_DATATYPE_DIP`</font>``</a>`, `<a href=/reference/ft_datatype_freq>``<font color=green>`FT_DATATYPE_FREQ`</font>``</a>`,
    `<a href=/reference/ft_datatype_mvar>``<font color=green>`FT_DATATYPE_MVAR`</font>``</a>`, `<a href=/reference/ft_datatype_raw>``<font color=green>`FT_DATATYPE_RAW`</font>``</a>`, `<a href=/reference/ft_datatype_source>``<font color=green>`FT_DATATYPE_SOURCE`</font>``</a>`, `<a href=/reference/ft_datatype_spike>``<font color=green>`FT_DATATYPE_SPIKE`</font>``</a>`,
    `<a href=/reference/ft_datatype_timelock>``<font color=green>`FT_DATATYPE_TIMELOCK`</font>``</a>`, `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>`
`</pre>``</html>`

