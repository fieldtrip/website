The EEG/MEG signals measured on or around the scalp do not directly reflect the activated neurons in the brain. To reconstruct the actual activity in the brain, source reconstruction techniques are used. You can read more about the different methods in the review papers that are listed [here](/references_to_review_papers_and_teaching_material/#source-estimation).

The activity in the brain is estimated from the EEG or MEG signals using

1.  the EEG/MEG activity itself that is measured on or around the scalp
2.  the spatial arrangement of the electrodes/gradiometers relative to the brain (**sensor positions**),
3.  the geometrical and conductive properties of the head (**head model**)
4.  the location of the source (**source model**)

Using this information, source estimation comprises two major steps: (1) Estimation of the EEG potential or MEG field distribution for a known source is referred to as **forward modeling**. (2) Estimation of the unknown sources corresponding to the measured EEG or MEG is referred to as **inverse modeling**.

The forward solution can be computed when the head model, the sensor positions and a model for the source are given. For distributed source models and for scanning approaches such as beamforming, the source model consists of a discrete description of the the brain volume or of the cortical sheet in many voxels or vertices. When the forward solution is computed, the **lead field matrix** (with dimensions Nchan \* Nsources) is calculated for each point, taking into account the head model and the sensor positions.

A prerequisite of forward modeling is that the geometrical description of the sensor positions, head model and source model are expressed in the same [coordinate system](/faq/source/coordsys) (e.g., CTF, MNI, Talairach) and with the same units (mm, cm, or m). There are different conventions for coordinate systems. The precise coordinate system is not relevant, as long as all data is consistent. [Here](/faq/source/coordsys) you can read how the different head and MRI coordinate systems are defined. For most MEG systems, the gradiometers are by default defined relative to head localizer coils or anatomical landmarks, therefore when the anatomical MRI are aligned to the same landmarks, the position of the MEG sensors directly matches the MRI. As EEG data is typically not explicitly aligned relatively to the head, therefore, the EEG electrodes usually have to be explicitly realigned prior to source reconstruction (see also [this faq](/faq/source/anat_coreg) and [this example](/example/source/electrodes2bem)).

{% include image src="/assets/img/shared/tutorial/sourcelocalization_background/figure1.png" width="600" %}

_Figure 1. Overall outline of the pipeline used for source reconstruction_
