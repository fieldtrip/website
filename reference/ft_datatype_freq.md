---
layout: default
---

##  FT_DATATYPE_FREQ

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_datatype_freq".

`<html>``<pre>`
    `<a href=/reference/ft_datatype_freq>``<font color=green>`FT_DATATYPE_FREQ`</font>``</a>` describes the FieldTrip MATLAB structure for freq data
 
    The freq data structure represents frequency or time-frequency decomposed
    channel-level data. This data structure is usually generated with the
    `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>` function.
 
    An example of a freq data structure containing the powerspectrum for 306 channels
    and 120 frequencies is
 
        dimord: 'chan_freq'          defines how the numeric data should be interpreted
     powspctrm: [306x120 double]     the power spectum
         label: {306x1 cell}         the channel labels
          freq: [1x120 double]       the frequencies expressed in Hz
           cfg: [1x1 struct]         the configuration used by the function that generated this data structure
 
    An example of a freq data structure containing the time-frequency resolved
    spectral estimates of power (i.e. TFR) for 306 channels, 120 frequencies
    and 60 timepoints is
 
        dimord: 'chan_freq_time'     defines how the numeric data should be interpreted
     powspctrm: [306x120x60 double]  the power spectum
         label: {306x1 cell}         the channel labels
          freq: [1x120 double]       the frequencies, expressed in Hz
          time: [1x60 double]        the time, expressed in seconds
           cfg: [1x1 struct]         the configuration used by the function that generated this data structure
 
    Required field
    - label, dimord, freq
 
    Optional field
    - powspctrm, fouriesspctrm, csdspctrm, cohspctrm, time, labelcmb, grad, elec, cumsumcnt, cumtapcnt, trialinfo
 
    Deprecated field
    - &lt;none&gt;
 
    Obsoleted field
    - &lt;none&gt;
 
    Revision histor
 
    (2011/latest) The description of the sensors has changed, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    for further information.
 
    (2008) The presence of labelcmb in case of crsspctrm became optional,
    from now on the crsspctrm can also be represented as Nchan * Nchan.
 
    (2006) The fourierspctrm field was added as alternative to powspctrm and
    crsspctrm. The fields foi and toi were renamed to freq and time.
 
    (2003v2) The fields sgn and sgncmb were renamed into label and labelcmb.
 
    (2003v1) The initial version was defined.
 
    See also `<a href=/reference/ft_datatype>``<font color=green>`FT_DATATYPE`</font>``</a>`, `<a href=/reference/ft_datatype_comp>``<font color=green>`FT_DATATYPE_COMP`</font>``</a>`, `<a href=/reference/ft_datatype_dip>``<font color=green>`FT_DATATYPE_DIP`</font>``</a>`, `<a href=/reference/ft_datatype_freq>``<font color=green>`FT_DATATYPE_FREQ`</font>``</a>`,
    `<a href=/reference/ft_datatype_mvar>``<font color=green>`FT_DATATYPE_MVAR`</font>``</a>`, `<a href=/reference/ft_datatype_raw>``<font color=green>`FT_DATATYPE_RAW`</font>``</a>`, `<a href=/reference/ft_datatype_source>``<font color=green>`FT_DATATYPE_SOURCE`</font>``</a>`, `<a href=/reference/ft_datatype_spike>``<font color=green>`FT_DATATYPE_SPIKE`</font>``</a>`,
    `<a href=/reference/ft_datatype_timelock>``<font color=green>`FT_DATATYPE_TIMELOCK`</font>``</a>`, `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>`
`</pre>``</html>`

