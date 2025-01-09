---
title: How are the different head and MRI coordinate systems defined?
parent: Source reconstruction
category: faq
tags: [headmodel, mri, source, fiducial, coordinate]
redirect_from:
    - /faq/how_are_the_different_head_and_mri_coordinate_systems_defined/
---

# How are the different head and MRI coordinate systems defined?

{% include markup/yellow %}
To understand the coordinate system in which data is expressed, you should consider:

- What is the definition of the origin of the coordinate system, i.e. where is [0,0,0]?
- In which directions are the x-, y- and z-axis pointing, i.e. is +x towards the right or towards anterior?
- In what units are coordinates expressed, i.e. does the number "1" mean 1 meter, 1 centimeter or 1 millimeter?
- Is the geometry scaled to some template or atlas, or does it still match the individual's head/brain size?
{% include markup/end %}

FieldTrip does not have its own coordinate system, but allows the user to use the coordinate system native to the original data. However, at the time of certain computations or visualization FieldTrip assumes that all geometrical data which are used together (i.e. mri, headmodel, electrodes, dipoles) are expressed in the same coordinate system and with the same geometrical units (e.g., mm or cm). In order to be able to compare these fundamental properties across data structures, FieldTrip defines two fields in the geometrical data `xxx` pertaining to the interpretation of the geometrical **units**, `xxx.unit`, and to the interpretation of the **coordinate system** in which the coordinates are expressed, `xxx.coordsys`.

If the `unit` field is not present in the data, FieldTrip uses the helper-function **[ft_determine_units](/reference/forward/ft_determine_units)** that tries to estimate the units from the range of values in the spatial data (e.g., the positions of the vertices in the boundaries that describe the volume conductor, or the positions of electrodes), assuming that the geometry corresponds to a human head that is approximately 0.25 meter, or 25 cm, or 250 mm in size.

The real-world interpretation of the coordinate system can typically not be determined automatically, and for this FieldTrip uses a helper-function **[ft_determine_coordsys](/reference/utilities/ft_determine_coordsys)**. This function requires some user-interaction for the specification of the origin and the orientation of the cardinal axes of the coordinate system. The only thing that this function does, is to add a `coordsys` field to the input data structure, specifying how the spatial coordinates in the data structure should be interpreted. Importantly, it does not change the values of the spatial coordinates that are present in the data structure.

The remainder of this page describes the native conventions for the coordinate systems for a number of standard atlases, MEG systems, EEG systems, MRI systems, and for various software packages involved in processing geometrical data. Of course it might always possible that the specific user of one of these systems uses a different coordinate system.

The coordinate systems used in EEG and MEG measurements are usually defined in terms of anatomical landmarks on the outside of the head, such as the [nasion](https://en.wikipedia.org/wiki/Nasion), [inion](https://en.wikipedia.org/wiki/Inion) and the left and right pre-auricular points. Please see [this FAQ](/faq/how_are_the_lpa_and_rpa_points_defined) for a discussion of the LPA and RPA.

The coordinate systems used for imaging methods such as MRI, PET and CT are usually defined in terms of internal brain structures, such as the [anterior](https://en.wikipedia.org/wiki/Anterior_commissure) and [posterior](https://en.wikipedia.org/wiki/Posterior_commissure) commissure. Furthermore, imaging data is sometimes scaled to a specific standard size, e.g., based on the [Talairach-Tournoux atlas](https://en.wikipedia.org/wiki/Jean_Talairach) or one of the templates from the [Montreal Neurological Institute (MNI)](https://en.wikipedia.org/wiki/Montreal_Neurological_Institute). An elaborate discussion on the relation between the Talairach-Tournoux atlas and the MNI templates can be found [here](http://imaging.mrc-cbu.cam.ac.uk/imaging/MniTalairach).

Imaging methods such as MRI and CT result in 3-D volumetric representations of the data, e.g., with 256x256x256 voxels. You can think of this representation as having a "voxel" coordinate system, where voxel (1, 1, 1) is the first and (256, 256, 256) is the last in the volume. The voxel coordinate system however does not specify the geometrical dimensions (e.g., mm or cm) and does not specify how the head (which is somewhere within the volume) relates to the voxel indices. Therefore a volumetric description of imaging data as a 3-D array has to be complemented with a description of the head coordinate system. This description is commonly implemented using a [4x4 homogenous coordinate transformation matrix](/faq/homogenous).

## Summary

| system                  | units | orientation | origin                                      | scaling                                                                                                   | notes                        |
| ----------------------- | ----- | ----------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------- |
| ACPC                    | mm    | RAS         | anterior commissure                         | native, i.e., not normalized to a template                                                                |                              |
| Allen Institute         | mm    | RAS         | Bregma point                                |                                                                                                           |                              |
| Analyze                 | mm    | LAS         |                                             | native                                                                                                    |                              |
| BTi/4D                  | m     | ALS         | between the ears                            | native                                                                                                    |                              |
| CTF MRI                 | mm    | ALS         | between the ears                            | native                                                                                                    | voxel order can be arbitrary |
| CTF gradiometer         | cm    | ALS         | between the ears                            | native                                                                                                    |                              |
| CapTrak                 | mm    | RAS         | approximately between the ears              |                                                                                                           |                              |
| Chieti ITAB             | mm    | RAS         | between the ears                            | native                                                                                                    |                              |
| DICOM                   | mm    | LPS         | centre of MRI gradient coil                 | native, see [here](https://doi.org/10.1016/j.jneumeth.2016.03.001)                                        |                              |
| EEGLAB                  | mm    | ALS         | between the ears                            | native                                                                                                    |                              |
| FreeSurfer              | mm    | RAS         | center of isotropic 1 mm 256x256x256 volume |                                                                                                           |                              |
| MNI                     | mm    | RAS         | anterior commissure                         | scaled to match averaged template                                                                         |                              |
| NIfTI                   | mm    | RAS         |                                             | see [here](https://brainder.org/2012/09/23/the-nifti-file-format/), search for "Orientation information". |                              |
| Neuromag/Elekta/Megin   | m     | RAS         | between the ears                            | native                                                                                                    |                              |
| Paxinos-Franklin        | mm    | RSP         | Bregma point                                |                                                                                                           |                              |
| Scanner RAS (`scanras`) | mm    | RAS         | scanner origin                              | native                                                                                                    |                              |
| Talairach-Tournoux      | mm    | RAS         | anterior commissure                         | scaled to match atlas                                                                                     |                              |
| Yokogawa                |       | ALS         | center of device                            |                                                                                                           |                              |

A/P means anterior/posterior, L/R means left/right, S/I means superior/inferior.

As an example: **RAS** means that the first dimension orients towards **R**ight, the second dimension orients towards **A**nterior, the third dimension orients towards **S**uperior.

See also [this page](http://neuroimage.usc.edu/brainstorm/CoordinateSystems) from the BrainStorm documentation that also explains different MEG coordinate systems and [this page](http://www.grahamwideman.com/gw/brain/orientation/orientterms.htm) that discusses orientations in MRI.

## Details on the ACPC coordinate system

The ACPC coordinate system corresponds to that used in the Talairach atlas, but without the piecewise linear scaling applied to the brain, i.e. a brain in ACPC coordinates retains the individual shape and size. The landmarks used in the ACPC coordinate system are the anterior and posterior commisura (AC and PC) and the coordinate axes are defined according to

- the origin of the TT coordinate system is in the AC
- the y-axis goes towards the front of the brain, along the line connecting PC and AC
- the z-axis goes towards the top of the brain
- the x-axis goes towards the right side of the brain

See also this [frequently asked question](/faq/acpc).

## Details on the Allen Institute mouse coordinate system

The Allen Institute has created a [scalable mouse brain atlas (ABA12)](http://scalablebrainatlas.incf.org/ABA12). In this atlas, the coordinate system is defined as

- The origin of the coordinate system is at the [Bregma point](https://en.wikipedia.org/wiki/Bregma).
- The X-axis points from left (-) to right (+).
- The Y-axis points from posterior (-) to anterior (+).
- The Z-axis points from inferior (-) to superior (+).

## Details of the Analyze coordinate system

The **Analyze** coordinate system is defined by and used in the Analyze software developed by the [Mayo Clinic](http://www.mayo.edu/) (see also [this pdf](http://eeg.sourceforge.net/ANALYZE75.pdf)). The orientation is according to radiological conventions, and uses a left-handed coordinate system. The definition of the Analyze coordinate system is

- the x-axis goes from right to left
- the y-axis goes from posterior to anterior
- the z-axis goes from inferior to superior

Note that the Analyze .img/.hdr file format is also being used by other software (notably by older SPM version), but the conventions of the coordinate systems may be different. Typically, fMRI specific software will use neurological conventions instead of radiological conventions.

## Details of the BESA coordinate system

The **BESA** native coordinate system is expressed in spherical coordinates. If you want to express the location of a dipole in 3-D space, it is more convenient to translate from spherical coordinates (phi, theta, r) to cartesian coordinates (x, y, z). If you have measured electrode positions with a Polhemus 3-D digitizer or similar, a transformation from cartesian to spherical coordinates is needed.

In the BESA cartesian coordinate system, the principal (x, y, z) axes are defined as

- the x-axis passes through LPA and RPA. Positive x is towards the right.
- the y-axis passes through the nasion and is orthogonal to the x-axis. Positive y is anterior.
- the z-axis is orthogonal to x and y. Positive z is superior.

If you prefer to consider the center of the sphere to coincide with the origin of the coordinate system, the principal axes will not go exactly through the external landmarks (i.e. fiducials). The reason for the shift in the negative z-direction of LPA, RPA and Nasion is that, after the shift, the electrodes better fit on the spherical head model. I.e. the nose and ears are not in the middle of the sphere, but are lower.

See also [this documentation](http://wiki.besa.de/index.php?title=Electrodes_and_Surface_Locations) on the BESA wiki.

## Details of the BTi/4D coordinate system

The BTi or "4D Neuroimaging" coordinate system is expressed in meter, with the principal (X, Y, Z) axes going through fiducials placed on external anatomical landmarks. The details are

- the origin is exactly between LPA and RPA
- the X-axis goes towards NAS
- the Y-axis goes approximately towards LPA, orthogonal to X and in the plane spanned by the fiducials
- the Z-axis goes approximately towards the vertex, orthogonal to X and Y

{% include image src="/assets/img/faq/coordsys/bti.png" width="200" %}

## Details of the CapTrak coordinate system

**CapTrak** is an electrode digitization system manufactured by [Brain Products](http://pressrelease.brainproducts.com/captrak/). CapTrak consists of a hand-held scanner featuring two cameras that track EEG electrodes on a subject's scalp. CapTrak makes use of LEDs built into the Brain Products active electrodes and calculates the 3-D coordinates by comparing each LED position with the position of three "special LED" positions. These special LEDs form the coordinate system and are placed as fiducials onto anatomical landmarks (nasion, right and left preauricular points) on the subject's head.

The electrode coordinates are defined in millimeters as [x,y,z] with respect to the following coordinate system:

- the X-axis goes from LPA towards (through) RPA
- the Y-axis goes orthogonally to the X-axis and towards (through) NAS
- the Z-axis goes orthogonally to the X-Y-plane upwards

If the ears are not symmetric, the origin will not be precisely between the ears; e.g., if the right ear is more to the front, the origin will be shifted to the right side of the head.

See below a visualization of the coordinate system.

{% include image src="/assets/img/faq/coordsys/captrak.png" width="300" %}

## Details of the Chieti ITAB coordinate system

The **ITAB** coordinate system is expressed in meter, with the principal (X, Y, Z) axes going through fiducials that are placed at external landmarks. The details are

- X-axis from the origin towards the RPA point (exactly through)
- Y-axis from the origin towards the nasion (exactly through)
- Z-axis from the origin upwards orthogonal to the XY-plane
- Origin: Intersection of the line through LPA and RPA and a line orthogonal to L passing through the nasion.

## Details of the CTF coordinate system

The **CTF** coordinate system is expressed in centimeter (except the MRI, which is expressed in millimeter), with the principal (X, Y, Z) axes going through fiducials placed on external landmarks. The fiducials are small coils that prior to the MEG measurement are placed on the landmarks. At the DCCN we usually place them on nasion and on a tube that extends from the left and right ear canal, see [here](/faq/how_are_the_lpa_and_rpa_points_defined) for details. Although the left and right ear markers do not always correspond to the definition of the pre-auricular points (which is in front of the ear), they are commonly referred to in the CTF system as LPA and RPA. The definition of the coordinate system is

- the origin is exactly between LPA and RPA
- the X-axis goes towards NAS
- the Y-axis goes approximately towards LPA, orthogonal to X and in the plane spanned by the fiducials
- the Z-axis goes approximately towards the vertex, orthogonal to X and Y

{% include image src="/assets/img/faq/coordsys/ctf.png" width="200" %}

## Details of the DICOM coordinate system

**DICOM** is a standard for handling digital imaging in medicine. DICOM is also used for ultrasound and X-ray photography and each DICOM file by itself stores a 2D image. For MRI data a stack of those files is used to describe the volumetric data and the origin is at the magnet isocenter, which coincides with the center of the gradient coils. The definition of the coordinate system is

- the origin is at the scanner origin, which is the center of the gradient coil
- x increases from right to left
- y increases from anterior to posterior
- z increases from inferior to superior

{% include image src="/assets/img/faq/coordsys/dicom.jpg" width="200" %}

The paper [The first step for neuroimaging data analysis: DICOM to NIfTI conversion](https://doi.org/10.1016/j.jneumeth.2016.03.001) explains it very well. See also [this page](http://dicomiseasy.blogspot.com/2013/06/getting-oriented-using-image-plane.html) for more information about the DICOM coordinate system.

## Details of the EEGLAB coordinate system

The **EEGLAB** coordinate system is identical to the CTF coordinate system (see above), except that it is always expressed in millimeters.

- the origin is exactly between LPA and RPA
- the X-axis goes towards NAS
- the Y-axis goes approximately towards LPA, orthogonal to X and in the plane spanned by the fiducials
- the Z-axis goes approximately towards the vertex, orthogonal to X and Y

## Details of the FreeSurfer coordinate system

FreeSurfer is a software package that can be used to process anatomical MRIs, to obtain segmentations, cortical meshes, and inflated surfaces. The orientation of the coordinate system is RAS, and for volumetric (i.e. anatomical MRI) data the origin is defined to be the centre of a 256x256x256 isotropic 1 mm volume. Note that if the head is not centered in the volume, the origin of the coordinate system will not coincide with the center of the head.

For surface based data FreeSurfer uses the tkrRAS coordinate system.
See [this page](http://www.grahamwideman.com/gw/brain/fs/coords/fscoords.htm) for more information about this.

## Details of the MNI coordinate system

The Montreal Neurological Institute coordinate system is comparable to, but not exactly the same as the Talairach-Tournoux coordinate system. Rather than being based on a single specimen, it is the result from spatially transforming and averaging MRI scans of many subjects.

- The origin of the MNI coordinate system is the anterior commissure
- The X-axis extends from the left side of the brain to the right side
- The Y-axis points from posterior to anterior
- The Z-axis points from inferior to superior

See also this [frequently asked question](/faq/acpc). Note that the SPM software makes use of the MNI coordinate system.

## Details of the Neuromag coordinate system

The **Neuromag** coordinate system is expressed in meter, with the principal (X, Y, Z) axes going through external landmarks (i.e. fiducials). The details are

- X-axis from the origin towards the RPA point (exactly through)
- Y-axis from the origin towards the nasion (exactly through)
- Z-axis from the origin upwards orthogonal to the XY-plane
- Origin: Intersection of the line through LPA and RPA and a line orthogonal to L passing through the nasion.

{% include image src="/assets/img/faq/coordsys/neuromag.png" width="200" %}

## Details of the NIfTI coordinate system

The **NIfTI** format has been adapted from the Analyze 7.5 format (see [this website](http://nifti.nimh.nih.gov/) for more information). It supports two methods to specify the coordinate systems: one related to the scanner coordinate system (qform) and one related to a standard coordinate system (sform). From a technical point of view both can be used simultaneously and/or interchangeably. Depending on the `qform_code` or `sform_code`, the origin of the coordinate system corresponds (1) to the scanner origin, (2) is arbitrary, or (3,4) is aligned with AC according to the MNI or Talairach-Tournoux coordinate systems. The default orientation of the coordinate system axes is assumed to be

- The x-axis increases from left to right
- The y-axis increases from posterior to anterior
- The z-axis increases from inferior to superior

See also [here](https://brainder.org/2012/09/23/the-nifti-file-format/) (search for "Orientation information"). In case the `qform_code` or `sform_code` is 2, the coordinates are aligned to another file, or to the “truth” (with an arbitrary coordinate center). In that case the assumption that the orientation of the world coordinate system is RAS may not hold.

Warning: various software implementations that write NIfTI files are inconsistent with assigning the `qform_code` and/or `sform_code`, hence you should be cautious with the interpretation of the coordinate system.

## Details on the Paxinos-Franklin mouse coordinate system

The Paxinos-Franklin atlas [The Mouse Brain in Stereotaxic Coordinate (2001)](http://www.amazon.com/Mouse-Stereotaxic-Coordinates-Second-Edition/dp/0125476361) defines a commonly used coordinate system for the mouse brain anatomy. Note however, that other coordinate system definitions are also being used.

For the mouse coordinate system it is relevant to understand the similarities and differences in nomenclature between the human anatomy and that of most other animals. A nice explanation is provided on [Wikipedia](https://en.wikipedia.org/wiki/Anatomical_terms_of_location) and [here](http://johnhawks.net/explainer/laboratory/anatomical-directions/).

The Paxinos-Franklin atlas specifies two points of reference: the [Bregma point](https://en.wikipedia.org/wiki/Bregma) and the midpoint of the intra-aural line. Both are indicated as [0, 0, 0] in the atlas, here we will use the Bregma point as origin.

- The origin of the coordinate system is at the [Bregma point](https://en.wikipedia.org/wiki/Bregma).
- The X-axis extends along the Medial-Lateral direction, with positive towards the right (see below).
- The Y-axis points from Dorsal to Ventral, i.e. towards the top of the head.
- The Z-axis points from Cranial to Caudal, or Anterior to Posterior, i.e. towards the tail of the animal. The Z-axis extends from the [Bregma point](https://en.wikipedia.org/wiki/Bregma) to the [Lambda point](<https://en.wikipedia.org/wiki/Lambda_(anatomy)>)

The Paxinos-Franklin atlas is not explicit about the positive and negative x-direction. We observe that the y-axis is from Inferior to Superior and the z-axis from Anterior to Posterior, which means that we obtain a right-handed coordinate system by defining the x-axis from Medial to the _Right_ Lateral side.

Although we define the origin at the Bregma point, the Paxinos-Franklin atlas also refers to the interaural point as a possible origin. The interaural point is a logical choice if a stereotact is used with pins in both ear canals. Converting from interaural to Bregma as origin of the coordinate system involves a translation which can be described in the following homogenous transformation matrix

    interaural2bregma = [
        1 0 0 Tx
        0 1 0 Ty
        0 0 1 Tz
        0 0 0 1
    ];

Converting from Bregma to interaural as origin of the coordinate system involves a translation which can be described in the following homogenous transformation matrix

    bregma2interaural = [
        1 0 0 Tx
        0 1 0 Ty
        0 0 1 Tz
        0 0 0 1
    ];

## Details of the Polhemus coordinate system

The **Polhemus** coordinate system as such does not exist. [Polhemus](http://www.polhemus.com) is the company that manufactures electromagnetic 3-D trackers for a large variety of applications, and usually the trackers are sold to you by an EEG company. The EEG company bundles the tracker with specific software for recording the position of the electrodes. The software program communicates with the tracker, and presents the measured electrode locations on the computer screen and writes them to an ASCII file. Therefore, the software determines the coordinate system that is used. It is common to require the user first to record external anatomical landmarks (i.e. fiducials) on the head: usually the left and right pre-auricular points and the nasion. Using there fiducials, the software can convert all subsequent electrode positions into a head coordinate system.

The most common definition of the head coordinate system used by the software that accompanies the Polhemus tracker is

- the origin is exactly between LPA and RPA
- the X-axis goes towards NAS
- the Y-axis goes approximately towards LPA, orthogonal to X and in the plane spanned by the fiducials
- the Z-axis goes approximately towards the vertex, orthogonal to X and Y

## Details of the Scanner RAS coordinate system

The **Scanner RAS** coordinate system has the same origin as the DICOM coordinate system, but is rotated 180 degrees around the z-axis. The Scanner RAS coordinate system is identical to the NIfTI scanner coordinate system (qform). It is defined as

- the origin corresponds to the scanner origin, which is the center of the gradient coil
- the x-axis increases from left to right
- the y-axis increases from posterior to anterior
- the z-axis increases from inferior to superior

The process to generate data in this coordinate system can be done for any standard image format (e.g., `.nii`, `nii.gz`, `.mgz`) and is described in more detail in the [Nipy Documentation](https://nipy.org/nibabel/coordinate_systems.html).

Note that the origin of the **Scanner RAS** is defined differently than that of the **Freesurfer** (also known as "Surface RAS" or "TkReg RAS") origin, so they are generally not the same.

## Details of the Talairach-Tournoux coordinate system

The [Co-Planar Stereotaxic Atlas of the Human Brain](https://www.thieme.com/books-main/neurosurgery/product/414-co-planar-stereotaxic-atlas-of-the-human-brain) (1988) by Talairach and Tournoux defines a coordinate system using the Anterior and Posterior Commissure and applies that on a post-mortem dissection of an individual human brain. Furthermore, it introduces a strategy for piece-wise linear scaling to allow other brains to be compared to the template brain that is featured in the atlas.

The Talairach-Tournoux coordinate system is comparable to, but [not exactly the same as the MNI coordinate system](http://imaging.mrc-cbu.cam.ac.uk/imaging/MniTalairach). It is defined using landmarks inside the brain and therefore can only be determined from an MRI scan, CT scan, or X-ray photo. This is in contrast to the external landmarks that are used for EEG/MEG recording. The landmarks used in the TT coordinate system are the anterior and posterior commisura (AC and PC) and the coordinate axes are defined according to

- the origin of the TT coordinate system is in the AC
- the y-axis goes towards the front of the brain, along the line connecting PC and AC
- the z-axis goes towards the top of the brain
- the x-axis goes towards the right side of the brain

See also this [frequently asked question](/faq/acpc).

## Details of the Yokogawa coordinate system

Unlike other systems, the **Yokogawa** system software does not automatically analyze its sensorlocations relative to fiducial coils. Instead the positions of the fiducial points are saved in an external textfile - in the helmet's own coordinate system - using the property menu of the YOKOGAWA MEG-VISION software. The details are

- the origin is at the center of the helmet
- the X-axis goes towards the nose
- the Y-axis goes towards the left
- the Z-axis goes towards the top of the head
