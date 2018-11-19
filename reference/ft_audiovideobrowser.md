---
layout: default
---

##  FT_AUDIOVIDEOBROWSER

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_audiovideobrowser".

`<html>``<pre>`
    `<a href=/reference/ft_audiovideobrowser>``<font color=green>`FT_AUDIOVIDEOBROWSER`</font>``</a>` reads and vizualizes the audio and/or video data
    corresponding to the EEG/MEG data that is passed into this function.
 
    Use as
    ft_audiovideobrowser(cfg)
    or as
    ft_audiovideobrowser(cfg, data)
    where the input data is the result from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>` or from `<a href=/reference/ft_componentanalysis>``<font color=green>`FT_COMPONENTANALYSIS`</font>``</a>`.
 
    The configuration structure can contain the following options
    cfg.datahdr     = header structure of the EEG/MEG data, see `<a href=/reference/ft_read_header>``<font color=green>`FT_READ_HEADER`</font>``</a>`
    cfg.audiohdr    = header structure of the audio data, see `<a href=/reference/ft_read_header>``<font color=green>`FT_READ_HEADER`</font>``</a>`
    cfg.videohdr    = header structure of the video data, see `<a href=/reference/ft_read_header>``<font color=green>`FT_READ_HEADER`</font>``</a>`
    cfg.audiofile   = string with the filename
    cfg.videofile   = string with the filename
    cfg.trl         = Nx3 matrix, see `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>`
    cfg.anonymize   = [x1 x2 y1 y2], range in pixels for placing a bar over the eyes (default = [])
    cfg.interactive = 'yes' or 'no' (default = 'yes')
 
    If you do NOT specify cfg.datahdr, the header must be present in the input data.
    If you do NOT specify cfg.audiohdr, the header will be read from the audio file.
    If you do NOT specify cfg.videohdr, the header will be read from the video file.
    If you do NOT specify cfg.trl, the input data should contain a sampleinfo field.
 
    See also `<a href=/reference/ft_databrowser>``<font color=green>`FT_DATABROWSER`</font>``</a>`
`</pre>``</html>`

