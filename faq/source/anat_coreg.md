---
title: How to coregister an anatomical MRI with the gradiometer or electrode positions?
parent: Source reconstruction
grand_parent: Frequently asked questions
category: faq
tags: [eeg, meg, mri, headmodel, source, coordinate]
redirect_from:
    - /faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions/
    - /faq/anat_coreg/
---

# How to coregister an anatomical MRI with the gradiometer or electrode positions?

In general, volumetric data such as anatomical MRIs are represented in FieldTrip as a MATLAB-structure, containing the anatomical (and if applicable also the functional) information in a 3D numeric matrix, combined with a 4x4 affine transformation matrix. The 4x4 transformation matrix specified how to go from voxel space to source space, as explained in this [frequently asked question](/faq/homogenous).

When reading anatomical data with **[ft_read_mri](/reference/fileio/ft_read_mri)**, the transformation is extracted from the MRI file. In the case that the MRI has not been processed, it is likely that the coordinate system corresponds to DICOM or in NIfTI scanner coordinates, which do _not_ relate the coordinates to the actual anatomy represented in the data.

You can read more about how the different coordinate systems relate to the anatomy and/or to the scanner hardware in this [frequently asked question](/faq/coordsys).

## MEG

When reading MEG data from the original files, the gradiometer sensor data is automatically read along with the channel timeseries. With most MEG systems the sensor positions are automatically expressed relative to head localization coils that are placed on the head relative to well-defined anatomical landmarks. The `coordsys` option in **[ft_read_sens](/reference/fileio/ft_read_sens)** also allows you to get the sensor positions relative to the device or dewar.

For source reconstruction we need to express all geometrical data in a consistent coordinate system that is defined relative to the participant's head. In FieldTrip it is common to do MEG source reconstruction in the coordinate system of the MEG acquisition device. Consequently, the MRI needs to be updated using **[ft_volumerealign](/reference/ft_volumerealign)** so that it is expressed relative to the same anatomical landmarks as the MEG data.

{% include markup/red %}
Other MEG analysis software may use other conventions. For example in MNE-Python it is common to do MEG source reconstruction in a coordinate system that is the result of the Freesurfer pipeline which is used to extract the cortical sheet. That means that, rather than aligning the MRI to the MEG, it aligns the MEG to one of the Freesurfer outputs.
{% include markup/end %}

## EEG

EEG systems typically do not include an integrated way to record ans store EEG electrode positions. Although separate 3D tracking systems (e.g., Polhemus, Optotrack, Structure Sensor) can be used to record the electrode positions, the electrode positions are usually not stored directly along with the EEG data. So when reading the EEG data from disk, the position of the EEG electrodes is usually not known.

For EEG it is therefore common to use **[ft_read_mri](/reference/fileio/ft_read_mri)** and **[ft_volumerealign](/reference/ft_volumerealign)** to place the anatomical  MRI in a well-defined coordinate system, and to use **[ft_read_sens](/reference/fileio/ft_read_sens)** and **[ft_electroderealign](/reference/ft_electroderealign)** to place the electrodes in the same coordinate system.
