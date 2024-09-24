---
title: How should I specify the coordinate systems in a BIDS dataset?
category: faq
tags: [bids, sharing]
---

# How should I specify the coordinate systems in a BIDS dataset?

[BIDS](http://bids.neuroimaging.io) is a standard for formatting and documenting raw data resulting from a measurement in a MRI, MEG or EEG lab. Regarding the “data” elements that have a geometrical quality in an MEG measurement (i.e. that are described somewhere in three dimensional space and hence are described using three numbers) we have

- MEG sensors in the dataset are expressed in the MEGCoordinateSystem
- Anatomical Landmarks are expressed AnatomicalLandmarkCoordinateSystem
- EEG electrodes are (or would be) expressed in EEGCoordinateSystem
- Head localizer coils are expressed in HeadCoilCoordinateSystem
- Digitized head points are expressed DigitizedHeadPointsCoordinateSystem

When we say that the "thing" _xxx_ is expressed in the _XXXCoordinatesystem_, we mean that the position of _xxx_ is expressed (in the data file) as numbers, and those numbers are relative to some known origin [0,0,0], with the x, y and z-axis pointing in known directions (e.g., x to the right) and in some units (e.g., mm). So the position indicated with the three numbers [70,0,0] can be interpreted properly.

{% include markup/skyblue %}
Note that MRI measurements are not measurements of space, but measurements of intensity or grey-scale values. The position of voxels (after reconstruction) are the a-priori specified locations at which intensity is measured.
{% include markup/end %}

There are multiple "things" in the MEG lab. The measurement of some things is done with a Polhemus or optical tracker, some others are measured with the MEG system itself (by generating small magnetic fields, recording the spatial distribution and reconstructing the position of the source). There are also measurements done in the factory (the relative position of the MEG sensors to each other and to the dewar). Some of the things that we measure are not expressed in the original coordinates of the measurement, but recomputed. Lets first look at the actual measurements: We measure the position of the MEG sensors relative to each other and relative to the dewar in the factory, it remains fixed. We measure the position of the anatomical landmarks with the Polhemus relative to the big knob that is usually mounted to a wooden chair. We measure the position of the EEG electrodes and of the head shape relative to the same knob. We can also measure the position of the head localizer coils relative to the same knob.

But in the Polhemus software - prior to writing all data to disk - the anatomical landmarks are taken as the reference instead of the big knob, and the anatomical landmarks, electrodes head shape points and coil locations are all expressed and saved to disk relative to the coordinate system that is defined on basis of the anatomical landmarks. And in the CTF MEG system software - prior to writing the MEG sensor positions to disk - the position of the MEG sensors is expressed relative to the head localizer coils. In the Neuromag MEG system software the position of the MEG sensors is expressed relative to the anatomical landmarks (via the intermediate step of the head localizer coils). Note the difference between CTF and Neuromag. I don't know from the top of my head how it is with the BTi/4D system. So both for the measurements done with the Polhemus hardware and written to disk by the Polhemus software, and for the measurements (fixed sensor positions) written to disk by the MEG software, there is a transformation of the numbers (that represent positions) from device to some other coordinates.

## CTF system

For a typical recording with the CTF system and using the CTF Polhemus software (which writes it in a .pos file), you would have

- MEGCoordinateSystem=CTF, relative to the coils (see \* below)
- EEGCoordinateSystem=CTF, relative to the landmarks
- HeadCoilCoordinateSystem=CTF, relative to the landmarks in the Polhemus file, but relative to the head coils in the MEG file
- DigitizedHeadPointsCoordinateSystem=CTF, relative to the landmarks
- AnatomicalLandmarkCoordinateSystem=CTF, relative to the landmarks

Note that the head coils can IN PRINCIPLE be recorded twice: once with the Polhemus and once with the MEG system. And note that the anatomical landmarks are usually also recorded twice: once with the Polhemus and once in the anatomical MRI. Idem for the head shape.

(\*) If you place the coils on the anatomical landmarks, the CTF MEGCoordinateSystem is exactly the same as the CTF AnatomicalLandmarkCoordinateSystem. But if you move the coils a little bit, the two are slightly different. Hence the xxxCoordinateDescription field, where you can elaborate. In the [BIDS example](/example/bids_mous) you can recognize this in step 6.

## Neuromag system

For a typical recording with the Neuromag system and using the Neuromag Polhemus software (which writes it into the .fif file), you would have

- MEGCoordinateSystem=Neuromag, relative to the landmarks
- EEGCoordinateSystem=Neuromag, relative to the landmarks
- HeadCoilCoordinateSystem=Neuromag, relative to the landmarks
- DigitizedHeadPointsCoordinateSystem=Neuromag, relative to the landmarks
- AnatomicalLandmarkCoordinateSystem=Neuromag, relative to the landmarks

Note that the head coils are ALWAYS recorded twice: once with the Polhemus and once with the MEG system. And note that the anatomical landmarks are usually also recorded twice: once with the Polhemus and once in the anatomical MRI. Idem for the head shape.

## Comparing CTF and Neuromag

The difference between CTF and Neuromag is that the CTF Acq software (running on the Linux computer) does not take the Polhemus recording (on the windows computer) into account, whereas the Neuromag acquisition software does. If you were to attach the three head localizer coils in a triangle on the forehead, the sensor positions in the CTF dataset would be rather confusing, whereas the neuromag dataset it would be just like usual.

## Anatomical MRI

Note the relative insignificance of the anatomical MRI for MEG data represented in BIDS: although the position of the anatomical landmarks and head shape can also be determined from an anatomical MRI, the anatomical MRI does not change the actual MEG data files stored in the raw BIDS representation. Hence the metadata in the sidecar files (and the coordinates) are not different depending on whether there is a MRI or not. Only at the time of analysis we usually (FieldTrip, SPM) transform the anatomical MRI to the MEG coordinate system, and not the other way around. But I think that MNE-Python does it the other way around, i.e. it starts with the MRI (aligned to ACPC) and transforms the MEG.

Regarding the Anatomical landmarks in relation to the MRI. The BIDS spec (1.1.0) states that: _It is also RECOMMENDED that the MRI voxel coordinates of the actual anatomical landmarks for co-registration of MEG with structural MRI are stored in the AnatomicalLandmarkCoordinates field in the JSON sidecar of the corresponding T1w MRI anatomical data of the subject seen in the MEG session (see section 8.3) - for example: sub-01/ses-mri/anat/sub-01_ses-mri_acq-mprage_T1w.json_

So the T1w.json would have AnatomicalLandmarkCoordinates, AnatomicalLandmarkCoordinateSystem, AnatomicalLandmarkCoordinateSystemUnits and AnatomicalLandmarkCoordinateSystemDescription. Voxels in a particular MRI are (by means of the 4x4 transformation included in the nifti header) expressed in real world coordinates. The anatomical landmarks should be specified in the same coordinate system and units in which the voxel positions are expressed. You can imagine the position of voxels in the MRI to be expressed in mm relative to the lower left corner of the volume, or relative to AC, or relative to the ears and nose.

## Fiducials

In the FiducialsDescription you can add some optional text (i.e. story) that explains the procedure that is used in the specific lab. e.g., at the Donders we attach the head coils (and the vitamine E capsules in the MR lab) to ear molds, instead of attaching them with tape on the pre-auricular anatomical landmarks (i.e. points in front of the ears).
