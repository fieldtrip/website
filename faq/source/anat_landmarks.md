---
title: How are the Left and Right Pre-Auricular (LPA and RPA) points defined?
parent: Source reconstruction
grand_parent: Frequently asked questions
category: faq
tags: [fiducial, mri, ctf, source, coordinate]
redirect_from:
    - /faq/how_are_the_lpa_and_rpa_points_defined/
    - /faq/anat_landmarks/
---

# How are the Left and Right Pre-Auricular (LPA and RPA) points defined?

The definition of the pre-auricular point taken from <http://www.medilexicon.com> is _"a point of the posterior root of the zygomatic arch lying immediately in front of the upper end of the tragus"_. The [zygomatic arch](https://en.wikipedia.org/wiki/Zygomatic_arch) or cheek bone is the skull bone in front of the ear as depicted in this figure

{% include image src="/assets/img/faq/anat_landmarks/zygomatic_arch.png" width="200" %}

and the [tragus](<https://en.wikipedia.org/wiki/Tragus_(ear)>) is a small backward-pointing eminence situated in front of the ear canal.

{% include image src="/assets/img/faq/anat_landmarks/tragus.png" width="200" %}

The approximate position of the pre-auricular point is indicated in the figure above by the green point. It can be palpated (i.e. felt with the finger tip) the best if the subject moves his jaw by opening and closing his or her mouth.

The problem with using the LPA and RPA according to this definition is that it can be really difficult to localize them precisely on the anatomical MRI. Mislocalization of these points can lead to severe misregistration between the MRI and MEG/EEG, and consequently affect the accuracy of source localization.

{% include markup/skyblue %}
Because of the challenge of localizing the LPA and RPA points when doing EEG or MEG measurements, in the anatomical MRI, and in 3D surface scans, various labs around the world have adopted slightly different conventions. These are discussed in more detail in the FAQ on [how to report the positions of the fiducial points on the head](/faq/how_should_i_report_the_positions_of_the_fiducial_points_on_the_head).
{% include markup/end %}

## The LPA/RPA in the Donders MEG and MRI labs

At the Donders Centre for Cognitive Neuroimaging (DCCN) in Nijmegen we use silicone ear molds with a hole in them (see below) to attach the markers: In the MEG scanner we insert a small tube into the hole (the tube is also used for auditory stimulation) and attach the MEG localizer coil to the tube. In the MRI scanner we use the same ear molds, but rather insert a custom-made marker with a small drop of vitamine E into the hole. The position thereby obtained with the MEG localizer coils is as precisely as possible reproduced in the MRI, given the movement that is allowed by the ear molds. We have various sizes of ear molds, both at the MEG and MRI scanner, and subjects should use the same size in both scanners.

{% include image src="/assets/img/faq/anat_landmarks/ear_molds_1.jpg" width="200" %}

{% include image src="/assets/img/faq/anat_landmarks/ear_molds_2.jpg" width="200" %}

When using different fiducial locations in the MEG and the MRI, the difference in the coordinates (which can be 5-20 mm) has to be taken into account in the coregistration procedure, otherwise the source localization would suffer from the systematic coregistration error. Luckily, most research labs acquire the EEG/MEG and the MRI using the same fiducial locations.

The consequence of different fiducial locations in different labs is that the terms "LPA" and "RPA", although used in software such as FieldTrip and other EEG/MEG tools, do not always refer to the same anatomical landmarks. In your analysis you have to take care that the positions consistently refer to the same landmarks, whether they are in front of the ear, on the tragus or in line with the ear canal. So whenever the software uses LPA and RPA, you have to be aware of your lab convention.

Note that for the [nasion](https://en.wikipedia.org/wiki/Nasion), where at the Donders Centre we also place one of the MEG localizer coils, we do not use a MRI marker. The nasion is easy to identify in the anatomical MRI images.

## See also

- BrainStorm documentation on [coordinate systems](http://neuroimage.usc.edu/brainstorm/CoordinateSystems)
- <http://www.proplugs.com> for the ear molds we use at the Donders Centre for Cognitive Neuroimaging (DCCN)
