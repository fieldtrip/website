---
layout: default
---

##  FT_VOLUMEWRITE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_volumewrite".

`<html>``<pre>`
    `<a href=/reference/ft_volumewrite>``<font color=green>`FT_VOLUMEWRITE`</font>``</a>` exports anatomical or functional volume data to a Analyze
    or BrainVoyager file. The data in the resulting file(s) can be
    further analyzed and/or visualized in MRIcro, SPM, BrainVoyager,
    AFNI or similar packages.
 
    Use as
    ft_volumewrite(cfg, volume)
    where the input volume structure should represent an anatomical MRI
    that was for example obtained from `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>`, the source
    reconstruction results from `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, the statistical
    results from `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>` or an otherwise processed anatomical
    or functional volume.
 
    The configuration structure should contain the following elements
    cfg.parameter     = string, describing the functional data to be processed,
                          e.g. 'pow', 'coh', 'nai' or 'anatomy'
    cfg.filename      = filename without the extension
    cfg.filetype      = 'analyze', 'nifti', 'nifti_img', 'analyze_spm', 'mgz',
                          'vmp' or 'vmr'
    cfg.vmpversion    = 1 or 2 (default) version of the vmp-format to use
 
    The default filetype is 'nifti', which means that a single *.nii file
    will be written using the SPM8 toolbox. The 'nifti_img' filetype uses SPM8 for
    a dual file (*.img/*.hdr) nifti-format file.
    The analyze, analyze_spm, nifti, nifti_img and mgz filetypes support a homogeneous
    transformation matrix, the other filetypes do not support a homogeneous transformation
    matrix and hence will be written in their native coordinate system.
 
    You can specify the datatype for the analyze_spm and analyze formats using
    cfg.datatype      = 'bit1', 'uint8', 'int16', 'int32', 'float' or 'double'
 
    By default, integer datatypes will be scaled to the maximum value of the
    physical or statistical parameter, floating point datatypes will not be
    scaled. This can be modified with
    cfg.scaling       = 'yes' or 'no'
 
    Optional configuration items are
    cfg.downsample    = integer number (default = 1, i.e. no downsampling)
    cfg.fiducial.nas  = [x y z] position of nasion
    cfg.fiducial.lpa  = [x y z] position of LPA
    cfg.fiducial.rpa  = [x y z] position of RPA
    cfg.markfiducial  = 'yes' or 'no', mark the fiducials
    cfg.markorigin    = 'yes' or 'no', mark the origin
    cfg.markcorner    = 'yes' or 'no', mark the first corner of the volume
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    If you specify this option the input data will be read from a *.mat
    file on disk. This mat files should contain only a single variable named 'data',
    corresponding to the input structure.
 
    See also `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>`, `<a href=/reference/ft_sourceinterpolate>``<font color=green>`FT_SOURCEINTERPOLATE`</font>``</a>`
`</pre>``</html>`

