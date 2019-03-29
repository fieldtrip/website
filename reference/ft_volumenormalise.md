---
title: ft_volumenormalise
---
```
 FT_VOLUMENORMALISE normalises anatomical and functional volume data
 to a template anatomical MRI.

 Use as
   [mri] = ft_volumenormalise(cfg, mri)
 where the input mri should be a single anatomical volume that was for
 example read with FT_READ_MRI.

 Configuration options are
   cfg.spmversion  = string, 'spm2', 'spm8', 'spm12' (default = 'spm8')
   cfg.template    = string, filename of the template anatomical MRI (default = 'T1.mnc'
                     for spm2 or 'T1.nii' for spm8)
   cfg.parameter   = cell-array with the functional data to be normalised (default = 'all')
   cfg.downsample  = integer number (default = 1, i.e. no downsampling)
   cfg.name        = string for output filename
   cfg.write       = 'no' (default) or 'yes', writes the segmented volumes to SPM2
                     compatible analyze-file, with the suffix
                     _anatomy for the anatomical MRI volume
                     _param   for each of the functional volumes
   cfg.nonlinear   = 'yes' (default) or 'no', estimates a nonlinear transformation
                     in addition to the linear affine registration. If a reasonably
                     accurate normalisation is sufficient, a purely linearly transformed
                     image allows for 'reverse-normalisation', which might come in handy
                     when for example a region of interest is defined on the normalised
                     group-average.

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a *.mat
 file on disk and/or the output data will be written to a *.mat file. These mat
 files should contain only a single variable, corresponding with the
 input/output structure.

 See also FT_READ_MRI, FT_VOLUMEDOWNSAMPLE, FT_SOURCEINTERPOLATE, FT_SOURCEPLOT
```
