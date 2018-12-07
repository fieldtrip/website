---
title: How to select the correct SPM toolbox?
tags: [faq, spm, toolbox, path]
---

# How to select the correct SPM toolbox?

Before May 2010, FieldTrip relied on old SPM2 code to do some operations on volumetric images. These operations entailed volumetric smoothing, spatial normalisation, segmentation, and the reading in of a few mri-filetypes. The SPM2 code dates from 2002 and the toolbox does not run correctly on recent versions of matlab. In particular, some MATLAB functions (on which the SPM2 code relied) do not exist in recent versions of MATLAB anymore. Moreover, SPM2 is not compiled for a 64-bit architecture.

At some point, we included a functional (subpart of the) SPM2-toolbox in fieldtrip/external/spm2, dealing with the first problem. Yet, we recently implemented support for SPM8 throughout the FieldTrip code, so there is no need to rely on the external/spm2 toolbox anymore. To use SPM8 you will need to have a copy of SPM8 on your MATLAB path. 
 
In certain cases you may find (n)one or more spm toolboxes added to your path but still be unable to use the appropriate functions. An example is the reading of mri images with ft_read_mri which may give you the 'the SPM2 or SPM5 toolbox is required to read .mnc files' error. SPM8 does not support reading in .mnc files.

In such case you have to put a lower SPM-version higher on your MATLAB path. One way to do this is to add the following path to your path list. Use the following command:

    addpath fieldtrip/external/spm2

You can check in your command window which SPM is currently in your path with:

    which spm

    

