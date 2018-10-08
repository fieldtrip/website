---
layout: default
---

{{tag>faq mri coordinate}}

# What is the difference between the ACPC, MNI, SPM and TAL coordinate systems?

There are a number of coordinate systems that have the origin, i.e., the [0,0,0] point, at the Anterior Commissure and that have a RAS orientation (i.e. the x-axis pointing to the right, the y-axis pointing to anterior, the z-axis pointing to superior). 

*  ACPC is used if the geometry is according to the individual subject head/brain size.
*  TAL is used if the geometry is piecewise scaled to match the Talairach-Tournoux (1988) atlas.
*  MNI or SPM is used if the geometry is spatially warped to the MNI152 template brain.
*  MNI305 or FSAVERAGE is used if the geometry is spatially warped to the MNI305 template brain.

In all cases the origin is at the [Anterior Commissure](http://en.wikipedia.org/wiki/Anterior_commissure) and the negative y-axis is passing through the [Posterior Commissure](http://en.wikipedia.org/wiki/Posterior_commissure).

Coordinates in the tal, mni/mni152/spm, and mni305/fsaverage all imply that some spatial deformation was done; they can be looked up in a template or atlas. ACPC coordinates can be used to measure distance, volume or surface area in an individual subject.

See also [this page](http://imaging.mrc-cbu.cam.ac.uk/imaging/MniTalairach) which describes the TT and MNI space in more detail and [this page](http://www.nil.wustl.edu/labs/kevin/man/answers/mnispace.html) that explain the differences between MNI152 and MNI305.

See also this [frequently asked question](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined) that explains how the different EEG, MEG and MRI coordinate systems are defined. 

