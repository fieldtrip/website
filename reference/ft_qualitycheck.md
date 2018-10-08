---
layout: default
---

##  FT_QUALITYCHECK

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_qualitycheck".

`<html>``<pre>`
    `<a href=/reference/ft_qualitycheck>``<font color=green>`FT_QUALITYCHECK`</font>``</a>` performs a quality inspection of a given MEG/EEG dataset,
    stores (.mat), and visualizes the result (.png and .pdf).
 
    This function segments the data into 10-second pieces and performs the
    following analyse
   1) reads the properties of the dataset
   2) computes the headpositions and distance covered from recording onset (CTF only)
   3) computes the mean, max, min, and range of the signal amplitude
   4) detects trigger events
   5) detects jump artifacts
   6) computes the powerspectrum
   7) estimates the low-frequency (&lt;2 Hz) and line noise (~50 Hz)
 
    Use as
    [info, timelock, freq, summary, headpos] = ft_qualitycheck(cfg)
    where info contains the dataset properties, timelock the timelocked data,
    freq the powerspectra, summary the mean descriptives, and headpos the
    headpositions throughout the recording
 
    The configuration should contai
    cfg.dataset = a string (e.g. 'dataset.ds')
 
    The following parameters can be use
    cfg.analyze   = string, 'yes' or 'no' to analyze the dataset (default = 'yes')
    cfg.savemat   = string, 'yes' or 'no' to save the analysis (default = 'yes')
    cfg.matfile   = string, filename (e.g. 'previousoutput.mat'), preferably in combination
                     with analyze = 'no'
    cfg.visualize = string, 'yes' or 'no' to visualize the analysis (default = 'yes')
    cfg.saveplot  = string, 'yes' or 'no' to save the visualization (default = 'yes')
    cfg.linefreq  = scalar, frequency of power line (default = 50)
    cfg.plotunit  = scalar, the length of time to be plotted in one panel (default = 3600)
 
    See also `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`, `<a href=/reference/ft_read_header>``<font color=green>`FT_READ_HEADER`</font>``</a>`, `<a href=/reference/ft_read_data>``<font color=green>`FT_READ_DATA`</font>``</a>`, `<a href=/reference/ft_read_event>``<font color=green>`FT_READ_EVENT`</font>``</a>`
`</pre>``</html>`

