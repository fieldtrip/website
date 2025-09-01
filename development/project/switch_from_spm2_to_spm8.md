---
title: Switch from SPM2 to SPM8
---

{% include /shared/development/warning.md %}


It would be nice to get rid of the spm2 dependency and switch to spm8 instead. The following FieldTrip functions depend on spm

    jansch@mentat001> grep -l spm_ *.m private/*.m fileio/*.m forward/*.m inverse/*.m
    ft_volumedownsample.m
    ft_volumenormalise.m
    ft_volumesegment.m
    private/avw_img_read.m
    private/mni2tal.m
    private/prepare_dipole_grid.m
    private/prepare_mesh_segmentation.m
    private/tal2mni.m
    private/volumewrite_spm.m
    fileio/ft_read_mri.m
    fileio/read_mri.m

-ft_volumeXXX have been adjusted to work with spm8 as default. One can switch back to spm2 by setting cfg.spmversion = 'spm2'.

-avw_img_read.m only refers to spm_flip_analyze_images in the documentation, so no changes here.

-mni2tal.m and tal2mni.m added hastoolbox('SPM8',1), these call spm_matrix; the spm version is anyhow inconsequential here.

-prepare_dipole_grid.m and prepare_mesh_segmentation.m rely on spm_smooth for some configurations; added hastoolbox in which spm8 takes precedence.

-volumewrite_spm.m has been adjusted to work with both spm8 and spm2, a 4th input argument is added which denotes the spmversion (as a string).

-ft_read_mri.m works

-read_mri.m seems to be the old version of what is now known as ft_read_mri.
