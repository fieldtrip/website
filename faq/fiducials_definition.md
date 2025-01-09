---
title: How should I report the positions of the fiducial points on the head?
parent: Source reconstruction
category: faq
tags: [electrode, fiducial, polhemus, coordinate]
redirect_from:
    - /faq/how_should_i_report_the_positions_of_the_fiducial_points_on_the_head/
---

# How should I report the positions of the fiducial points on the head?

_The documentation on this page follows careful considerations and discussions with Clement Lee and Scott Makeig and aligns with the EEGLAB recommendations._

Consistency is key when using fiducials or anatomical landmark points; the accuracy of collaborative or comparative analysis is severely diminished without accurate knowledge about the electrode positions. This is particularly the case when source estimation can use individual head models based on individual subject MRIs, but is also the case when electrode positions are warped to a template head model for source location estimation.

Traditionally in EEG, and in line with the 10-20 electrode placement standard (see [here](https://en.wikipedia.org/wiki/10–20_system_(EEG)) and links therein), the terms Nasion and Left/Right Pre Auricular point (LPA/RPA) are used to refer to the anatomical landmarks used to determine the electrode placement. The nasion is easy to find and point out, it is the critical point between the forehead and the 'bridge' of the nose. While LPA/RPA are palpable anatomical features when you have your subject in the lab (see also [here](/faq/how_are_the_lpa_and_rpa_points_defined)), they are difficult to locate during analysis on a computer in the anatomical MRIs and 3D scans of the scalp surface.

To address this issue and allow for MRI coregistration, various labs utilize in-house standards for fiducials or anatomical landmarks slightly different from the pre-auricular points. Unfortunately, some (including the Donders MEG lab) do so while retaining the LPA/RPA label.

{% include markup/red %}
Regardless of which convention you use for the points representing the left and right ear landmarks, you have to be aware of it and use it consistently throughout.
{% include markup/end %}

Clarity and precision in the definition and measurement of the fiducial points can greatly simplify and improve the accuracy of EEG and MEG analyses, especially when working with shared datasets for which the details might have been known by the person who acquired the data, but not by the person who analyzes it. To make the description of the anatomical landmarks unambiguous, we recommend using the terms:

- LPA/RPA - Left and Right Pre Auricular point - green dot
- LEC/REC - Left and Right Ear canal - grey dot
- LHS/RHS - Left and Right Helix-Scalp junction - blue dot
- LHJ/RHJ - Left and Right Helix-Tragus Junction - red dot

{% include image src="/assets/img/faq/fiducials_definition/fiducial_points.png" width="350" %}

{% include markup/skyblue %}
The Helix-Tragus Junction (i.e. LHJ and RHJ) is the best defined in anatomical MRIs and in 3D scans.
{% include markup/end %}

## See also

- [How are the Left and Right Pre-Auricular (LPA and RPA) points defined?](/faq/how_are_the_lpa_and_rpa_points_defined)
- [How are the different head and MRI coordinate systems defined?](/faq/coordsys)
- BrainStorm documentation on [coordinate systems](http://neuroimage.usc.edu/brainstorm/CoordinateSystems)
- EEGLAB documentation on [lateral fiducials](https://sccn.ucsd.edu/mediawiki/images/1/19/Fiducials.pdf)
