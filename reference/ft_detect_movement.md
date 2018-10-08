---
layout: default
---

##  FT_DETECT_MOVEMENT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_detect_movement".

`<html>``<pre>`
    FT_SACCADE_DETECTION performs micro/saccade detection on time series data
    over multiple trials
 
    Use as
    movement = ft_detect_movement(cfg, data)
 
    The input data should be organised in a structure as obtained from the
    `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>` function. The configuration depends on the type of
    computation that you want to perform.
 
    The configuration should contai
   cfg.method   = different methods of detecting different movement types
                 'velocity2D', Micro/saccade detection based on Engbert R,
                    Kliegl R (2003) Vision Res 43:1035-1045. The method
                    computes thresholds based on velocity changes from
                    eyetracker data (horizontal and vertical components).
                 'clustering', Micro/saccade detection based on
                    Otero-Millan et al., (2014) J Vis 14 (not implemented
                    yet)
    cfg.channel = Nx1 cell-array with selection of channels, see
                  `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details, (default = 'all')
    cfg.trials  = 'all' or a selection given as a 1xN vector (default = 'all')
 
    METHOD SPECIFIC OPTIONS AND DESCRIPTIONS
 
   VELOCITY2D
    VELOCITY2D detects micro/saccades using a two-dimensional (2D) velocity
    space velocity. The vertical and the horizontal eyetracker time series
    (one eye) are transformed into velocities and microsaccades are
    indentified as "outlier" eye movements that exceed a given velocity and
    duration threshold.
      cfg.velocity2D.kernel   = vector 1 x nsamples, kernel to compute velocity (default = [1 1 0 -1 -1].*(data.fsample/6);
      cfg.velocity2D.demean   = 'no' or 'yes', whether to apply centering correction (default = 'yes')
      cfg.velocity2D.mindur   = minimum microsaccade durantion in samples (default = 3);
      cfg.velocity2D.velthres = threshold for velocity outlier detection (default = 6);
 
    The output argument "movement" is a Nx3 matrix. The first and second
    columns specify the begining and end samples of a movement period
    (saccade, joystic...), and the third column contains the peak
    velocity/acceleration movement. This last thrid column will allow to
    convert movements into spike data representation, making the spike
    toolbox functions compatible (not implemented yet).
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also FT_PLOT_MOVEMENT (not implemented yet)
`</pre>``</html>`

