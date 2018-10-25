---
title: Example MATLAB scripts
layout: default
tags: [example]
---

# Example MATLAB scripts

Here you can find example MATLAB scripts together with documentation that show specific analyses done in FieldTrip or in MATLAB. The documentation here is often not as elaborate as the [tutorials](/tutorial), but goes more in detail into specific aspects of the data, code or analysis.

We invite you to [add your own](/contribute) example scripts or frequently asked questions to the wiki. Also tutorials can be added. Every time you explain somebody something about FieldTrip, please consider whether you could use the wiki for this so others can learn from it as well.
If you want to contribute one of your scripts, please [add it directly](/contribute) to the wiki or [contact](/contact) us.

See also the [tutorials](/tutorial) and [frequently asked questions](/faq).

### Reading and preprocessing data

*  [Getting started with reading raw EEG or MEG data](/example/getting_started_with_reading_raw_eeg_or_meg_data)
*  [Making your own trialfun for conditional trial definition](/example/making_your_own_trialfun_for_conditional_trial_definition)
*  [Fixing a missing sensor](/example/fixing_a_missing_sensor)
*  [Use independent component analysis (ICA)_to_remove_ECG_artifacts](/example/use_independent_component_analysis_ica_to_remove_ecg_artifacts)
*  [Use independent component analysis (ICA)_to_remove_EOG_artifacts](/example/use_independent_component_analysis_ica_to_remove_eog_artifacts)
*  [Interpolating data from the CTF151 to the CTF275 sensor array using ft_megrealign](/example/megrealign)
*  [Detect the muscle activity in an EMG channel and use that as trial definition](/example/detect_the_muscle_activity_in_an_emg_channel_and_use_that_as_trial_definition)
*  [How to incorporate head movements in MEG analysis](/example/how_to_incorporate_head_movements_in_meg_analysis)
*  [The correct pipeline order for combining planar MEG channels](/example/combineplanar_pipelineorder)

### Spectral analysis

*  [Fourier analysis of oscillatory power and coherence](/tutorial/Fourier)
*  [Cross-frequency analysis](/example/cross_frequency_analysis)
*  [Effects of tapering for power estimates](/example/effects_of_tapering_for_power_estimates_in_the_frequency_domain)
*  [Simulate an oscillatory signal with phase resetting](/example/phase_reset)
*  [Analyze Steady-State Visual Evoked Potentials (SSVEPs)](/example/ssvep)
*  [Effect of Signal-to-Noise Ratio on Coherence](/example/coherence_snr)
*  [Analysis of high-gamma band signals in human ECoG](/example/ecog_ny)

### Source reconstruction

*  [Align EEG electrode positions to BEM headmodel](/example/align_eeg_electrode_positions_to_bem_headmodel)
*  [Compute forward simulated data and apply a dipole fit](/example/compute_forward_simulated_data_and_apply_a_dipole_fit)
*  [Compute forward simulated data and apply a beamformer scan](/example/compute_forward_simulated_data_and_apply_a_beamformer_scan)
*  [Testing BEM created lead fields](/example/testing_bem_created_leadfields)
*  [Create MNI-aligned grids in individual head-space](/example/create_single-subject_grids_in_individual_head_space_that_are_all_aligned_in_mni_space)
*  [Determine the filter characteristics](/example/determine_the_filter_characteristics)
*  [Fit a dipole to the tactile ERF after mechanical stimulation](/example/fit_a_dipole_to_the_tactile_erf_after_mechanical_stimulation)
*  [Make leadfields using different headmodels](/example/make_leadfields_using_different_headmodels)
*  [Use your own forward leadfield model in an inverse beamformer computation](/example/use_your_own_forward_leadfield_model_in_an_inverse_beamformer_computation)
*  [Common filters in beamforming](/example/Common_filters_in_beamforming)
*  [Read neuromag .fif mri and create MNI-aligned single_shell grids in individual head-space](/example/read_neuromag_mri_and_create_single-subject_grids_in_individual_head_space_that_are_all_aligned_in_mni_space)
*  [Using the low-level compute_leadfield function](/example/compute_leadfield)
*  [Plotting the result of source reconstructing on a cortical mesh](/example/plotting_the_result_of_source_reconstructing_on_a_cortical_mesh)
*  [Combined EEG and MEG source reconstruction](/example/combined_eeg_and_meg_source_reconstruction)
*  [Localizing the sources underlying the difference in event related fields](/example/difference_erf)
*  [Check the quality of the anatomical coregistration](/example/coregistration_quality_control)
*  [Sphere fitting and scaling of the template (Colin27) MRI to the MEG polhemus headshape](/example/sphere_fitting_and_scaling_of_the_template_Colin_27_MRI_to_the_MEG_polhemus_headshape)

### Statistical analysis

*  [Stratify the distribution of two variables](/example/stratify)
*  [Source statistics](/example/Source_statistics)
*  [Apply clusterrandanalysis on TFRs of power that were computed with BESA](/example/apply_clusterrandanalysis_on_TFRs_of_power_that_were_computed_with_BESA)
*  [Use simulated ERPs to explore cluster statistics](/example/use_simulated_erps_to_explore_cluster_statistics)
*  [How can I compute and report the effect size?](/example/effectsize)

### Real-time analysis

*  [Measuring the timing delay and jitter for a real-time application](/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application)
*  [Realtime neurofeedback application based on hilbert phase estimation](/example/ft_realtime_hilbert)
*  [Example real-time average](/example/ft_realtime_average)
*  [Example real-time classification](/example/ft_realtime_classification)
*  [Example real-time power estimate](/example/ft_realtime_powerestimate)
*  [Example real-time selective average](/example/ft_realtime_selectiveaverage)
*  [Example real-time signal viewer](/example/ft_realtime_signalviewer)

### Miscellaneous

*  [Correlation analysis in fMRI data](/example/correlation_analysis_in_fmri_data)
*  [How to use checkconfig](/example/checkconfig)
*  [Writing simulated data to a CTF dataset](/example/writing_simulated_data_to_a_ctf_dataset)
*  [Example analysis pipeline for Biosemi bdf data](/example/biosemi)
*  [Find the orientation of planar gradiometer channels](/example/planar_orientation)
*  [How to import data from MNE-Python and FreeSurfer](/example/import_mne)
*  [Preparing an MEG+fMRI dataset for sharing](/example/bids)
*  [Preparing an EEG dataset for sharing](/example/bids_eeg)
