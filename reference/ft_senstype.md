---
layout: default
---

##  FT_SENSTYPE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_senstype".

`<html>``<pre>`
    `<a href=/reference/ft_senstype>``<font color=green>`FT_SENSTYPE`</font>``</a>` determines the type of acquisition device by looking at the channel
    names and comparing them with predefined lists.
 
    Use as
    [type] = ft_senstype(sens)
    or
    [flag] = ft_senstype(sens, desired)
 
    The output type can be any of the following
    'ctf64'
    'ctf151'
    'ctf151_planar'
    'ctf275'
    'ctf275_planar'
    'bti148'
    'bti148_planar'
    'bti248'
    'bti248_planar'
    'bti248grad'
    'bti248grad_planar'
    'itab28'
    'itab153'
    'itab153_planar'
    'yokogawa9'
    'yokogawa64'
    'yokogawa64_planar'
    'yokogawa160'
    'yokogawa160_planar'
    'yokogawa440'
    'neuromag122'
    'neuromag122_combined'
    'neuromag306'
    'neuromag306_combined'
    'babysquid74'         this is a BabySQUID system from Tristan Technologies
    'artemis123'          this is a BabySQUID system from Tristan Technologies
    'magview'             this is a BabySQUID system from Tristan Technologies
    'egi32'
    'egi64'
    'egi128'
    'egi256'
    'biosemi64'
    'biosemi128'
    'biosemi256'
    'ant128'
    'neuralynx'
    'plexon'
    'artinis'
    'nirs'
    'meg'
    'eeg'
    'ieeg'
    'seeg'
    'ecog'
    'eeg1020'
    'eeg1010'
    'eeg1005'
    'ext1020'             in case it is a small subset of eeg1020, eeg1010 or eeg1005
 
    The optional input argument for the desired type can be any of the above, or any of
    the following generic classes of acquisition systems
    'eeg'
    'ieeg'
    'ext1020'
    'ant'
    'biosemi'
    'egi'
    'meg'
    'meg_planar'
    'meg_axial'
    'ctf'
    'bti'
    'neuromag'
    'yokogawa'
    'itab'
    'babysquid'
    If you specify the desired type, this function will return a boolean flag
    indicating true/false depending on the input data.
 
    Besides specifiying a sensor definition (i.e. a grad or elec structure, see
    `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`), it is also possible to give a data structure containing a grad
    or elec field, or giving a list of channel names (as cell-arrray). So assuming that
    you have a FieldTrip data structure, any of the following calls would also be fine.
    ft_senstype(hdr)
    ft_senstype(data)
    ft_senstype(data.label)
    ft_senstype(data.grad)
    ft_senstype(data.grad.label)
 
    See also `<a href=/reference/ft_senslabel>``<font color=green>`FT_SENSLABEL`</font>``</a>`, `<a href=/reference/ft_chantype>``<font color=green>`FT_CHANTYPE`</font>``</a>`, `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`, `<a href=/reference/ft_datatype_sens>``<font color=green>`FT_DATATYPE_SENS`</font>``</a>`
`</pre>``</html>`

