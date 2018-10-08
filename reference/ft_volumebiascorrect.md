---
layout: default
---

##  FT_VOLUMEBIASCORRECT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_volumebiascorrect".

`<html>``<pre>`
    `<a href=/reference/ft_volumebiascorrect>``<font color=green>`FT_VOLUMEBIASCORRECT`</font>``</a>` corrects the image inhomogeneity bias in an anatomical MRI
 
    Use as
    mri_unbias = ft_volumebiascorrect(cfg, mri)
    where the input mri should be a single anatomical volume that was for example read with
    `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>`. 
 
    The configuration structure can contain
    cfg.spmversion     = string, 'spm8', 'spm12' (default = 'spm8')
    cfg.opts           = struct, containing spmversion specific options.
                         See the code below and the SPM-documentation for
                         more information.
 
    See also `<a href=/reference/ft_volumerealign>``<font color=green>`FT_VOLUMEREALIGN`</font>``</a>` `<a href=/reference/ft_volumesegment>``<font color=green>`FT_VOLUMESEGMENT`</font>``</a>` `<a href=/reference/ft_volumenormalise>``<font color=green>`FT_VOLUMENORMALISE`</font>``</a>`
`</pre>``</html>`

