---
layout: default
---

##  FT_APPLY_MONTAGE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_apply_montage".

`<html>``<pre>`
    `<a href=/reference/ft_apply_montage>``<font color=green>`FT_APPLY_MONTAGE`</font>``</a>` changes the montage of an electrode or gradiometer array. A
    montage can be used for EEG rereferencing, MEG synthetic gradients, MEG
    planar gradients or unmixing using ICA. This function applies the montage
    to the input EEG or MEG sensor array, which can subsequently be used for
    forward computation and source reconstruction of the data.
 
    Use as
    [sens]    = ft_apply_montage(sens,     montage,  ...)
    [data]    = ft_apply_montage(data,     montage,  ...)
    [freq]    = ft_apply_montage(freq,     montage,  ...)
    [montage] = ft_apply_montage(montage1, montage2, ...)
 
    A montage is specified as a structure with the fields
    montage.tra      = MxN matrix
    montage.labelold = Nx1 cell-array
    montage.labelnew = Mx1 cell-array
 
    As an example, a bipolar montage could look like this
    bipolar.labelold  = {'1',   '2',   '3',   '4'}
    bipolar.labelnew  = {'1-2', '2-3', '3-4'}
    bipolar.tra       = [
      +1 -1  0  0
       0 +1 -1  0
       0  0 +1 -1
    ];
 
    The montage can optionally also specify the channel type and unit of the input
    and output data with
    montage.chantypeold = Nx1 cell-array
    montage.chantypenew = Mx1 cell-array
    montage.chanunitold = Nx1 cell-array
    montage.chanunitnew = Mx1 cell-array
 
    Additional options should be specified in key-value pairs and can be
    'keepunused'    string, 'yes' or 'no' (default = 'no')
    'inverse'       string, 'yes' or 'no' (default = 'no')
    'balancename'   string, name of the montage (default = '')
    'feedback'      string, see `<a href=/reference/ft_progress>``<font color=green>`FT_PROGRESS`</font>``</a>` (default = 'text')
    'warning'       boolean, whether to show warnings (default = true)
    'showcallinfo'  string, 'yes' or 'no' (default = 'no')
 
    If the first input is a montage, then the second input montage will be
    applied to the first. In effect, the output montage will first do
    montage1, then montage2.
 
    See also `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`, `<a href=/reference/ft_transform_sens>``<font color=green>`FT_TRANSFORM_SENS`</font>``</a>`
`</pre>``</html>`

