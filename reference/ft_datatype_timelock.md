---
layout: default
---

##  FT_DATATYPE_TIMELOCK

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_datatype_timelock".

`<html>``<pre>`
    `<a href=/reference/ft_datatype_timelock>``<font color=green>`FT_DATATYPE_TIMELOCK`</font>``</a>` describes the FieldTrip MATLAB structure for timelock data
 
    The timelock data structure represents averaged or non-averaged event-releted
    potentials (ERPs, in case of EEG) or ERFs (in case of MEG). This data structure is
    usually generated with the `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>` or `<a href=/reference/ft_timelockgrandaverage>``<font color=green>`FT_TIMELOCKGRANDAVERAGE`</font>``</a>` function.
 
    An example of a timelock structure containing the ERF for 151 channels MEG data is
 
      dimord: 'chan_time'       defines how the numeric data should be interpreted
         avg: [151x600 double]  the average values of the activity for 151 channels x 600 timepoints
         var: [151x600 double]  the variance of the activity for 151 channels x 600 timepoints
       label: {151x1 cell}      the channel labels (e.g. 'MRC13')
        time: [1x600 double]    the timepoints in seconds
        grad: [1x1 struct]      information about the sensor array (for EEG data it is called elec)
         cfg: [1x1 struct]      the configuration used by the function that generated this data structure
 
    Required field
    - label, dimord, time
 
    Optional field
    - avg, var, dof, cov, trial, trialinfo, sampleinfo, grad, elec, opto, cfg
 
    Deprecated field
    - &lt;none&gt;
 
    Obsoleted field
    - fsample
 
    Revision histor
 
    (2017/latest) The data structure cannot contain an average and simultaneously single
    trial information any more, i.e. avg/var/dof and trial/individual are mutually exclusive.
 
    (2011v2) The description of the sensors has changed, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    for further information.
 
    (2011) The field 'fsample' was removed, as it was redundant.
 
    (2003) The initial version was defined.
 
    See also `<a href=/reference/ft_datatype>``<font color=green>`FT_DATATYPE`</font>``</a>`, `<a href=/reference/ft_datatype_comp>``<font color=green>`FT_DATATYPE_COMP`</font>``</a>`, `<a href=/reference/ft_datatype_freq>``<font color=green>`FT_DATATYPE_FREQ`</font>``</a>`, `<a href=/reference/ft_datatype_raw>``<font color=green>`FT_DATATYPE_RAW`</font>``</a>`
`</pre>``</html>`

