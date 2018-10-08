---
layout: default
---

##  FT_ARTIFACT_NAN

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_artifact_nan".

`<html>``<pre>`
    `<a href=/reference/ft_artifact_nan>``<font color=green>`FT_ARTIFACT_NAN`</font>``</a>` identifies artifacts that are indicated in the data as nan (not a
    number) values.
 
    Use as
    [cfg, artifact] = ft_artifact_nan(cfg, data)
    where the input data is a structure as obtained from `<a href=/reference/ft_rejectartifact>``<font color=green>`FT_REJECTARTIFACT`</font>``</a>` with
    the option cfg.artfctdef.reject='nan'.
 
    The configuration can contain
    cfg.artfctdef.nan.channel = Nx1 cell-array with selection of channels, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
 
    The output argument "artifact" is a Nx2 matrix comparable to the
    "trl" matrix of `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>`. The first column of which specifying the
    beginsamples of an artifact period, the second column contains the
    endsamples of the artifactperiods.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    If you specify this option the input data will be read from a *.mat
    file on disk. This mat files should contain only a single variable named 'data',
    corresponding to the input structure.
 
    See also `<a href=/reference/ft_rejectartifact>``<font color=green>`FT_REJECTARTIFACT`</font>``</a>`, `<a href=/reference/ft_artifact_clip>``<font color=green>`FT_ARTIFACT_CLIP`</font>``</a>`, `<a href=/reference/ft_artifact_ecg>``<font color=green>`FT_ARTIFACT_ECG`</font>``</a>`, `<a href=/reference/ft_artifact_eog>``<font color=green>`FT_ARTIFACT_EOG`</font>``</a>`,
    `<a href=/reference/ft_artifact_jump>``<font color=green>`FT_ARTIFACT_JUMP`</font>``</a>`, `<a href=/reference/ft_artifact_muscle>``<font color=green>`FT_ARTIFACT_MUSCLE`</font>``</a>`, `<a href=/reference/ft_artifact_threshold>``<font color=green>`FT_ARTIFACT_THRESHOLD`</font>``</a>`, `<a href=/reference/ft_artifact_zvalue>``<font color=green>`FT_ARTIFACT_ZVALUE`</font>``</a>`
`</pre>``</html>`

