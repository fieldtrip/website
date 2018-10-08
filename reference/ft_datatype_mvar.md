---
layout: default
---

##  FT_DATATYPE_MVAR

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_datatype_mvar".

`<html>``<pre>`
    `<a href=/reference/ft_datatype_mvar>``<font color=green>`FT_DATATYPE_MVAR`</font>``</a>` describes the FieldTrip MATLAB structure for multi-variate
    autoregressive model data.
 
    The mvar datatype represents multivariate model estimates in the time- or
    in the frequency-domain. This is usually obtained from `<a href=/reference/ft_mvaranalysis>``<font color=green>`FT_MVARANALYSIS`</font>``</a>`,
    optionally in combination with `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`.
 
    The following is an example of sensor level MVAR model data in the time domain
 
         dimord: 'chan_chan_lag'     defines how the numeric data should be interpreted
          label: {3x1 cell}          the channel labels
         coeffs: [3x3x5 double]      numeric data (MVAR model coefficients 3 channels x 3 channels x 5 time lags)
       noisecov: [3x3 double]        more numeric data (covariance matrix of the noise residuals 3 channels x 3 channels)
            dof: 500
    fsampleorig: 200
            cfg: [1x1 struct]
 
    The following is an example of sensor-level MVAR model data in the frequency domain
 
         dimord: 'chan_chan_freq'    defines how the numeric data should be interpreted
          label: {3x1 cell}          the channel labels
           freq: [1x101 double]      the frequencies, expressed in Hz
       transfer: [3x3x101 double]
      itransfer: [3x3x101 double]
       noisecov: [3x3 double]
      crsspctrm: [3x3x101 double]
            dof: 500
            cfg: [1x1 struct]
 
    Required field
    - label, dimord, freq
 
    Optional field
    - too many to mention
 
    Deprecated field
    - &lt;none&gt;
 
    Obsoleted field
    - &lt;none&gt;
 
    Revision histor
 
    (2011/latest) The description of the sensors has changed, see `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
    for further information.
 
    (2008) The initial version was defined.
 
    See also `<a href=/reference/ft_datatype>``<font color=green>`FT_DATATYPE`</font>``</a>`, `<a href=/reference/ft_datatype_comp>``<font color=green>`FT_DATATYPE_COMP`</font>``</a>`, `<a href=/reference/ft_datatype_dip>``<font color=green>`FT_DATATYPE_DIP`</font>``</a>`, `<a href=/reference/ft_datatype_freq>``<font color=green>`FT_DATATYPE_FREQ`</font>``</a>`,
    `<a href=/reference/ft_datatype_mvar>``<font color=green>`FT_DATATYPE_MVAR`</font>``</a>`, `<a href=/reference/ft_datatype_raw>``<font color=green>`FT_DATATYPE_RAW`</font>``</a>`, `<a href=/reference/ft_datatype_source>``<font color=green>`FT_DATATYPE_SOURCE`</font>``</a>`, `<a href=/reference/ft_datatype_spike>``<font color=green>`FT_DATATYPE_SPIKE`</font>``</a>`,
    `<a href=/reference/ft_datatype_timelock>``<font color=green>`FT_DATATYPE_TIMELOCK`</font>``</a>`, `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>`
`</pre>``</html>`

