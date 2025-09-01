---
title: What is the plotting convention for anatomical MRIs?
category: faq
tags: [anatomical, mri]
redirect_from:
    - /faq/what_is_the_plotting_convention_for_anatomical_mris/
    - /faq/anat_plottingconvention/
---

The convention used in FieldTrip for the plotting of anatomical MRI data in **[ft_sourceplot ](/reference/ft_sourceplot)** (when using cfg.method = 'ortho', or 'slice'), and in **[ft_volumerealign](/reference/ft_volumerealign)** is to plot the data along the voxel-indices' axes, rather than along the world coordinate system's axes. Statements such as 'the image appears flipped', or 'the image is presented in neurological/radiological convention' are basically dependent on the anatomical data. The question now of course is how it is possible to determine whether the data at hand is plotted in neurological/radiological convention, or otherwise stated: 'whether left is left, or left is right'.

The key to the solution lies in the transformation-matrix that is attached to the data structure (in X.transform). This matrix maps the voxel indices to the world coordinate system, where the voxel indices start counting from 1. For more information about coordinate systems, see the following [frequently asked question](/faq/source/coordsys).

The world coordinate system that is attached to a anatomical (or functional) image determines the interpretation of the X, Y and Z axes. The transformation matrix determines how the axes in the voxel coordinate system map to the X, Y and Z axes of the world coordinate system. In summary, in order to make a correct interpretation of 'what is left and what is right' we need to consider the transformation matrix in combination with the world coordinate system. For more information about the coregistration between an anatomical image and meaningful world coordinate systems, see the following [frequently asked question](/faq/source/anat_coreg).

One important concept to take into account in the interpretation is the handedness of the coordinate axes and the transformation matrix. This refers to the spatial relationship between the positive X, Y and Z axes. If the handedness of the voxel coordinate axes is different from the handedness of the world coordinate axes, the image is 'flipped'. Most commonly used real world coordinate systems are right-handed (such as CTF's ALS-convention, neuromag's and MNI's RAS-convention), but the handedness of the voxel coordinate system is usually not defined consistently. The handedness of the voxel coordinate axes is determined by the order in which the individual slices are stacked in the MRI-volume. The handedness of the voxel coordinate axes is indirectly represented in the transformation matrix. In practice, the transformation matrix is left-handed, when there is a discrepancy between the handedness of the voxel coordinate axes and the handedness of the world coordinate axes. To make a long story shor

**If the transformation matrix is describing the transformation from voxel space to a world coordinate system where the XYZ-axes are described with right-handed coordinate axes, AND the transformation matrix is also right-handed, then 'right is right, and left is left'**.

**If the transformation matrix is describing the transformation from voxel space to a world coordinate system where the XYZ-axes are described with right-handed coordinate axes, AND the transformation matrix is left-handed, then 'right is left, and left is right', and equivalently 'the image is flipped'**.

This leaves the question how to determine the handedness of the transformation matrix. This can be determined from the determinant of the upper-left part of this matrix. When `det(X.transform(1:3,1:3))` has a positive value, the transformation-matrix is right-handed, otherwise it's left-handed. Alternatively, you can also explore the data in **[ft_sourceplot ](/reference/ft_sourceplot)** (using cfg.method='interactive') and start clicking around on positions on the left/right axis. Pay special attention to what is happening with the real world coordinate that is describing the left/right axis. This should give you a clue as to what is left and what is right in the image.
