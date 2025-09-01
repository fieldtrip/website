---
title: How to select the correct SPM toolbox?
category: faq
tags: [spm, mex, toolbox, path]
redirect_from:
    - /faq/how_to_select_the_correct_spm_toolbox/
    - /faq/spmversion/
---

FieldTrip relies on SPM code to do operations on volumetric images. These operations entail volumetric smoothing, spatial normalisation, segmentation, the reading and writing of a certain (old-style) mri-filetypes, and spatial clustering. Over the years that FieldTrip has been developing, the SPM developers have released a newer versions of the software, each of which with slightly different functionalities. The older the version of SPM, the more likely it is that it will not run smoothly on current computers. For instance, the SPM2 code dates from 2002 and the toolbox does not run correctly on recent versions of MATLAB. In particular, some MATLAB functions (on which the SPM2 code relied) do not exist in recent versions of MATLAB anymore. Moreover, some relevant functions are compiled mex-files and these functions don't work if they the computer's operating system is too different from the one on which the original files was compiled.

FieldTrip includes functional (subparts of the) SPM-toolbox in fieldtrip/external/spm2, fieldtrip/external/spm8, fieldtrip/external/spm12, ensuring a fully functional version of FieldTrip without requiring the user to maintain a separate installation of SPM.

FieldTrip functions that rely on SPM functionality have a cfg.spmversion option, which can be 'spm2', 'spm5', 'spm8' or 'spm12'. As of May 2020, the default spmversion is 'spm12', to ensure robust behavior of the mex-files on various operating systems. Thus, in principle users don't need to specify a particular spmversion in their scripts, unless they want to:

1) emulate the old default behavior, in which case cfg.spmversion = 'spm8';
2) read or write volumetric images in the old-style '.mnc' format (ft_read_mri, ft_write_mri), in which case cfg.spmversion = 'spm2';

You can check in the MATLAB command window which SPM is currently in your path with:

    which spm
