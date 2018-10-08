---
layout: default
---

##  FT_ARTIFACT_TMS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_artifact_tms".

`<html>``<pre>`
    `<a href=/reference/ft_artifact_tms>``<font color=green>`FT_ARTIFACT_TMS`</font>``</a>` reads the data segments of interest from file and identifies artefacts in
    EEG recordings that were done during TMS stimulation.
 
    Use as
    [cfg, artifact] = ft_artifact_tms(cfg)
    with the configuration options
    cfg.dataset     = string with the filename
    or
    cfg.headerfile  = string with the filename
    cfg.datafile    = string with the filename
    and optionally
    cfg.headerformat
    cfg.dataformat
 
    Alternatively you can use it as
    [cfg, artifact] = ft_artifact_tms(cfg, data)
    where the input data is a structure as obtained from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    In both cases the configuration should also contain
    cfg.trl         = structure that defines the data segments of interest. See `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>`
    cfg.continuous  = 'yes' or 'no' whether the file contains continuous data (default   = 'yes')
    and
    cfg.method      = 'detect' or 'marker', see below.
                      markers written in the EEG.
    cfg.prestim     = scalar, time in seconds prior to onset of detected
                      event to mark as artifactual (default = 0.005 seconds)
    cfg.poststim    = scalar, time in seconds post onset of detected even to
                      mark as artifactual (default = 0.010 seconds)
 
    METHOD SPECIFIC OPTIONS AND DESCRIPTIONS
 
    With cfg.method='detect', TMS-artifacts are detected by preprocessing the data to be
    sensitive to transient high gradients, typical for TMS-pulses.  The data is preprocessed
    (again) with the following configuration parameters, which are optimal for identifying tms
    artifacts. This acts as a wrapper around ft_artifact_zvalue
    cfg.artfctdef.tms.derivative  = 'yes'
    Artifacts are identified by means of thresholding the z-transformed value
    of the preprocessed data.
    cfg.artfctdef.tms.channel     = Nx1 cell-array with selection of channels, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.artfctdef.tms.cutoff      = z-value at which to threshold (default = 4)
    cfg.artfctdef.tms.trlpadding  = 0.1
    cfg.artfctdef.tms.fltpadding  = 0.1
    cfg.artfctdef.tms.artpadding  = 0.01 
    Be aware that if one artifact falls within this specified range of another artifact, both
    artifact will be counted as one. Depending on cfg.prestim and cfg.poststim you may not mark
    enough data as artifactual.)
 
    With cfg.method='marker', TMS-artifact onset and offsets are based on markers/triggers that
    are written into the EEG dataset. This method acts as a wrapper around `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>` to
    determine on- and offsets of TMS pulses by reading markers in the EEG.
    cfg.trialfun            = function name, see below (default = 'ft_trialfun_general')
    cfg.trialdef.eventtype  = 'string'
    cfg.trialdef.eventvalue = number, string or list with numbers or strings
    The cfg.trialfun option is a string containing the name of a function that you wrote
    yourself and that `<a href=/reference/ft_artifact_tms>``<font color=green>`FT_ARTIFACT_TMS`</font>``</a>` will call. The function should take the cfg-structure as
    input and should give a NxM matrix with M equal to or larger than 3) in the same format as
    "trl" as the output. You can add extra custom fields to the configuration structure to
    pass as arguments to your own trialfun.  Furthermore, inside the trialfun you can use the
    `<a href=/reference/ft_read_event>``<font color=green>`FT_READ_EVENT`</font>``</a>` function to get the event information from your data file.
 
    The output argument "artifact" is a Nx2 matrix comparable to the
    "trl" matrix of `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>`. The first column of which specifying the
    beginsamples of an artifact period, the second column contains the
    endsamples of the artifactperiods.
 
    To facilitate data-handling and distributed computing with the peer-to-peer
    module, this function has the following optio
    cfg.inputfile   =  ...
    If you specify this option the input data will be read from a *.mat
    file on disk. This mat files should contain only a single variable named 'data',
    corresponding to the input structure.
 
    See also `<a href=/reference/ft_rejectartifact>``<font color=green>`FT_REJECTARTIFACT`</font>``</a>`, `<a href=/reference/ft_artifact_clip>``<font color=green>`FT_ARTIFACT_CLIP`</font>``</a>`, `<a href=/reference/ft_artifact_ecg>``<font color=green>`FT_ARTIFACT_ECG`</font>``</a>`, `<a href=/reference/ft_artifact_eog>``<font color=green>`FT_ARTIFACT_EOG`</font>``</a>`,
    `<a href=/reference/ft_artifact_jump>``<font color=green>`FT_ARTIFACT_JUMP`</font>``</a>`, `<a href=/reference/ft_artifact_muscle>``<font color=green>`FT_ARTIFACT_MUSCLE`</font>``</a>`, `<a href=/reference/ft_artifact_threshold>``<font color=green>`FT_ARTIFACT_THRESHOLD`</font>``</a>`, `<a href=/reference/ft_artifact_zvalue>``<font color=green>`FT_ARTIFACT_ZVALUE`</font>``</a>`
`</pre>``</html>`

