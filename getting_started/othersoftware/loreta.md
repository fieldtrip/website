---
title: Getting started with LORETA
category: getting_started
tags: [dataformat, loreta]
redirect_from:
    - /getting_started/loreta/
---

LORETA-KEY is a software program implemented by Roberto Pascual-Marqui that implements the LORETA source localization algorithm ("low resolution brain electromagnetic tomography"). The software is available from the [LORETA home page](http://www.unizh.ch/keyinst/NewLORETA/LORETA01.htm). Using LORETA-KEY, you can make a distributed source reconstruction for EEG data, using a three-shell spherical head model registered to a standardized stereotactic space (based on MNI brain). The source reconstruction is restricted to cortical gray matter.

The LORETA2FIELDTRIP function can be used to read in the resulting files (.slor, .lorb) from the LORETA-KEY software. The output of the LORETA2FIELDTRIP function is a MATLAB structure that is equivalent to the structures that result from the **[ft_sourceanalysis](/reference/ft_sourceanalysis)** function in FieldTrip. Hence, you can use its output as input in the FieldTrip **[ft_sourcegrandaverage](/reference/ft_sourcegrandaverage)** and/or **[ft_sourcestatistics](/reference/ft_sourcestatistics)** functions.

Using sourcestatistics, you can perform a random-effect parametric or non-parametric statistical test based on a single-voxel statistic or based on a spatio-temporal cluster statistic (only non-parametric). Both the parametric and non-parametric statistical tests implemented in FieldTrip have support for correcting for the multiple comparison problem.

## STEPS

To use sLORETA data in FieldTrip, you need to do the following steps.

### Convert the sLORETA source to a text file

1.  In the LORETA program, you go to main utilities > Format converter.
2.  There you select: input binary file (sLORETA)
3.  It does not matter which format for output you choose, the code will figure it out. In the text file, rows are the time points, columns are the volume-gridpoints (called voxels).
4.  After using loreta2fieldtrip the data is in [FieldTrip volume](/reference/utilities/ft_datatype_volume) format in [MNI space](/faq/source/coordsys).

### Hints on plotting the LORETA source

For use in **[ft_sourceplot](/reference/ft_sourceplot)** with method _"slice"_ or _"ortho"_ you can use the MNI template as anatomy

    % Read in the MNI template from SP
    template = ft_read_mri([cur_path_FT, '\external\spm8\templates\T1.nii']);

    % Interpolate your LORETA volume on the MNI template:
    [interp_mean] = ft_sourceinterpolate(cfg, GA_mean, template);

For method _"surface"_ you don't need to interpolate. However, you have to use a large sphereradius (15 for instance) to pull the source to plot nicely on the surface.

Also see the [plotting tutorial](/tutorial/plotting#plotting#plotting_data_at_the_source_level).
