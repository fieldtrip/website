---
title:
layout: default
---

The EEG/MEG signals measured on the scalp do not directly reflect the location of the activated neurons. To reconstruct the location and the time-course or spectral content of a source in the brain, various source-localization methods are available. You can read more about the different methods in review papers suggested [here](/references_to_implemented_methods#references_to_review_papers).   

The level of the activity at a source location is estimated from 
 1.  the EEG/MEG activity measured on (around) the scalp 
 2.  the spatial arrangement of the electrodes/sensors (**channel positions**), 
 3.  the geometrical and electrical/magnetic properties of the head (**head model**)
 4.  the location of the source (**source model**)

Using this information, source estimation comprises two major steps: (1) Estimation of the potential or field distribution for a known source and for a known model of the head is referred to as **forward modeling**. (2) Estimation of the unknown sources corresponding to the measured EEG or MEG is referred to as **inverse modeling**. 

The forward solution can be computed when the head model, the channel positions and the source is given. For distributed source models and for scanning approaches (such as beamforming), the source model is discretizing the brain volume into a volumetric or surface grid. When the forward solution is computed, the **lead field matrix** (= channels X source points matrix) is calculated for each grid point taking into account the head model and the channel positions. 

A prerequisite of forward modeling is that the geometrical description of all elements (channel positions, head model and source model) is registered in the same coordination system with the same units. There are different "conventions" how to define a coordinate system, but the precise coordinate system is not relevant, as long as all data is expressed in it consistently (i.e. in the same coordinate system). [Here](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined) read more about how the different head and mri coordinate systems are defined. The MEG sensors by default are defined relative to anatomical landmarks of the head (the fiducial coils), therefore when the anatomical images are also aligned to these landmarks, the MEG sensors do not need to be re-aligned. EEG data is typically not aligned to the head, therefore, the electrodes have to  be re-aligned prior to source-reconstruction (see also [this faq](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions) and [this example](/example/align_eeg_electrode_positions_to_bem_headmodel)).

{% include image src="/assets/img/tutorial/minimumnormestimate:source_analysis-03.png" width="500" %}
 
*Figure 1. Major steps in source reconstruction*
