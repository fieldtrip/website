The EEG/MEG signals measured on the scalp do not directly reflect the location of the activated neurons. To reconstruct the location and the time-course or spectral content of a source in the brain, various source-localization methods are available. You can read more about the different methods in review papers suggested [here](/references_to_implemented_methods#references_to_review_papers).

The activity in the brain responsible for the EEG or MEG signals is estimated from

1.  the EEG/MEG activity measured on or around the scalp
2.  the spatial arrangement of the electrodes/gradiometers (**sensor positions**),
3.  the geometrical and conductive properties of the head (**head model**)
4.  the location of the source (**source model**)

Using this information, source estimation comprises two major steps: (1) Estimation of the EEG potential or MEG field distribution for a known source is referred to as **forward modeling**. (2) Estimation of the unknown sources corresponding to the measured EEG or MEG is referred to as **inverse modeling**.

The forward solution can be computed when the head model, the sensor positions and the model for the source are given. For distributed source models and for scanning approaches (such as beamforming), the source model consists of a discrete description of the the brain volume or of the cortical sheet in many voxels or vertices. When the forward solution is computed, the **lead field matrix** (= channels X source points matrix) is calculated for each point, taking into account the head model and the sensor positions.

A prerequisite of forward modeling is that the geometrical description of all geometrical elements (sensor positions, head model and source model) is registered in the same coordination system and expressed with the same units (mm, cm, or m). There are different conventions for coordinate systems. The precise coordinate system is not relevant, as long as all data is expressed consistently. [Here](/faq/coordsys) you can read more about how the different head and MRI coordinate systems are defined. For most MEG systems, the gradometer sensors are by default defined relative to head localizer coils or anatomical landmarks, therefore when the anatomical MRI are aligned to the same landmarks, the position of the MEG sensors matches the MRI. EEG data is typically not explicitly aligned relatively to the head, therefore, the EEG electrodes also have to be re-aligned prior to source reconstruction (see also [this faq](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions) and [this example](/example/electrodes2bem)).

{% include image src="/assets/img/shared/tutorial/sourcelocalization_background/figure1.png" width="600" %}

_Figure 1. Overall outline of the pipeline used for source reconstruction_
