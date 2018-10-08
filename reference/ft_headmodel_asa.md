---
layout: default
---

##  FT_HEADMODEL_ASA

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_headmodel_asa".

`<html>``<pre>`
    `<a href=/reference/ft_headmodel_asa>``<font color=green>`FT_HEADMODEL_ASA`</font>``</a>` reads a volume conduction model from an ASA *.vol
    file
 
    ASA is commercial software (http://www.ant-neuro.com) that supports
    among others the boundary element method (BEM) for EEG. This function
    allows you to read an EEG BEM volume conduction model from an ASA
    format file (*.vol) and use that for leadfield computations in
    MATLAB. Constructing the geometry of the head model from an anatomical
    MRI and the computation of the BEM system are both handled by ASA.
    
    Use as
    headmodel = ft_headmodel_asa(filename)
 
    See also `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

