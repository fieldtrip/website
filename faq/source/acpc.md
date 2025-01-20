---
title: What is the difference between the ACPC, MNI, SPM and TAL coordinate systems?
parent: Source reconstruction
grand_parent: Frequently asked questions
category: faq
tags: [mri, coordinate]
redirect_from:
    - /faq/acpc/
---

# What is the difference between the ACPC, MNI, SPM and TAL coordinate systems?

There are a number of coordinate systems that have the origin, i.e., the [0,0,0] point, at the Anterior Commissure and that have a RAS orientation (i.e. the x-axis pointing to the right, the y-axis pointing to anterior, the z-axis pointing to superior).

- ACPC is used if the geometry is according to the individual subject head/brain size.
- TAL is used if the geometry is piecewise scaled to match the Talairach-Tournoux (1988) atlas.
- MNI, MNI152 or SPM is used if the geometry is spatially warped to the MNI152 template brain.
- MNI305 or FSAVERAGE is used if the geometry is spatially warped to the MNI305 template brain.

In all cases the origin is at the [Anterior Commissure](https://en.wikipedia.org/wiki/Anterior_commissure) and the negative y-axis is passing through the [Posterior Commissure](https://en.wikipedia.org/wiki/Posterior_commissure).

Coordinates expressed in the TAL, MNI/MNI152/SPM, and MNI305/FSAVERAGE coordinate system all imply that some spatial deformation was done; they can be looked up in the corresponding template or atlas. For ACPC coordinates no deformation was done; they can be used to express location in an individual subject, or measure distance, volume or surface area.

See also [this page](http://imaging.mrc-cbu.cam.ac.uk/imaging/MniTalairach) which describes the TT and MNI space in more detail and [this page](https://www.lead-dbs.org/about-the-mni-spaces/) that explain the differences between MNI152 and MNI305.

See also this [frequently asked question](/faq/coordsys) that explains how different EEG, MEG and MRI coordinate systems are defined.
