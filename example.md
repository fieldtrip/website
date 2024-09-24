---
title: Example MATLAB scripts
tags: [example]
---

# Example MATLAB scripts

Here you can find example MATLAB scripts together with documentation that show specific analyses done in FieldTrip or in MATLAB. The documentation here is often not as elaborate as the [tutorials](/tutorial), but goes more in detail into specific aspects of the data, code or analysis.

We invite you to [add your own](/contribute) example scripts or frequently asked questions to the website. Also tutorials can be added. Every time you explain somebody something about FieldTrip, please consider whether you could use the website for this, so others can learn from it as well. If you want to contribute one of your example scripts, please [add it directly](/contribute) to the website or [contact](/contact) us.

See also the [tutorials](/tutorial) and [frequently asked questions](/faq).

### Reading and preprocessing data

- [Getting started with reading raw EEG or MEG data](/example/getting_started_with_reading_raw_eeg_or_meg_data)
- [Making your own trialfun for conditional trial definition](/example/trialfun)
- [Detect the muscle activity in an EMG channel and use that as trial definition](/example/detect_the_muscle_activity_in_an_emg_channel_and_use_that_as_trial_definition)
- [Independent component analysis (ICA) to remove ECG artifacts](/example/ica_ecg)
- [Independent component analysis (ICA) to remove EOG artifacts](/example/ica_eog)
- [Combine MEG with Eyelink eyetracker data](/example/meg_eyelink)
- [Use denoising source separation (DSS) to remove ECG artifacts](/example/use_denoising_source_separation_dss_to_remove_ecg_artifacts)
- [Fixing a missing sensor](/example/fixing_a_missing_sensor)
- [Re-reference EEG and iEEG data](/example/rereference)

### Sensor-level analysis

- [Analyzing NIRS data recorded during unilateral finger- and foot-tapping](/example/nirs_fingertapping)
- [Analyzing NIRS data recorded during listening to and repeating speech](/example/nirs_speech)
- [The correct pipeline order for combining planar MEG channels](/example/combineplanar_pipelineorder)
- [How to incorporate head movements in MEG analysis](/example/headmovement_meg)
- [Interpolating data from the CTF151 to the CTF275 sensor array using ft_megrealign](/example/megrealign)

### Spectral analysis

- [Analysis of high-gamma band signals in human ECoG](/example/ecog_ny)
- [Analyze Steady-State Visual Evoked Potentials (SSVEPs)](/example/ssvep)
- [Cross-frequency analysis](/example/crossfreq)
- [Effect of Signal-to-Noise Ratio on Coherence](/example/coherence_snr)
- [Effects of tapering for power estimates](/example/effects_of_tapering)
- [Fourier analysis of oscillatory power and coherence](/tutorial/fourier)
- [Simulate an oscillatory signal with phase resetting](/example/phase_reset)
- [Irregular Resampling Auto-Spectral Analysis (IRASA)](/example/irasa)
- [Fitting oscillations and one-over-F (FOOOF)](/example/fooof)
- [Conditional Granger causality in the frequency domain](/example/connectivity_conditional_granger)

### Source reconstruction

- [Align EEG electrode positions to BEM headmodel](/example/electrodes2bem)
- [Check the quality of the anatomical coregistration](/example/coregistration_quality_control)
- [Combined EEG and MEG source reconstruction](/example/combined_eeg_and_meg_source_reconstruction)
- [Common filters in beamforming](/example/common_filters_in_beamforming)
- [Compute EEG leadfields using a FEM headmodel](/example/fem)
- [Compute forward simulated data and apply a beamformer scan](/example/compute_forward_simulated_data_and_apply_a_beamformer_scan)
- [Compute forward simulated data and apply a dipole fit](/example/compute_forward_simulated_data_and_apply_a_dipole_fit)
- [Compute forward simulated data using ft_dipolesimulation](/example/compute_forward_simulated_data)
- [Compute forward simulated data with the low-level ft_compute_leadfield](/example/compute_leadfield)
- [Create MNI-aligned grids in individual head-space](/example/sourcemodel_aligned2mni)
- [Determine the filter characteristics](/example/determine_the_filter_characteristics)
- [Fit a dipole to the tactile ERF after mechanical stimulation](/example/dipolefit_somatosensory_erf)
- [How to create a head model if you do not have an individual MRI](/example/fittemplate)
- [Localizing the sources underlying the difference in event-related fields](/example/difference_erf)
- [Make MEG leadfields using different headmodels](/example/make_leadfields_using_different_headmodels)
- [Read neuromag .fif mri and create a MNI-aligned single-shell head model](/example/neuromag_aligned2mni)
- [Symmetric dipole pairs for beamforming](/example/symmetry)
- [Testing BEM created lead fields](/example/testing_bem_created_leadfields)
- [Use your own forward leadfield model in an inverse beamformer computation](/example/use_your_own_forward_leadfield_model_in_an_inverse_beamformer_computation)

### Statistical analysis

- [Apply non-parametric statistics with clustering on TFRs of power that were computed with BESA](/example/apply_clusterrandanalysis_on_tfrs_of_power_that_were_computed_with_besa)
- [Computing and reporting the effect size](/example/effectsize)
- [Defining electrodes as neighbours for cluster-level statistics](/example/neighbours)
- [Source statistics](/example/source_statistics)
- [Stratify the distribution of two variables](/example/stratify)
- [Use simulated ERPs to explore cluster statistics](/example/use_simulated_erps_to_explore_cluster_statistics)
- [Using GLM to analyze NIRS timeseries data](/example/nirs_glm)
- [Using General Linear Modeling over trials](/example/glm_trials)
- [Using General Linear Modeling on time series data](/example/glm_timeseries)
- [Using simulations to estimate the sample size for cluster-based permutation test](/example/samplesize)
- [Using threshold-free cluster enhancement for cluster statistics](/example/threshold_free_cluster_enhancement)

### Real-time analysis

- [Example real-time average](/example/ft_realtime_average)
- [Example real-time classification](/example/ft_realtime_classification)
- [Example real-time power estimate](/example/ft_realtime_powerestimate)
- [Example real-time selective average](/example/ft_realtime_selectiveaverage)
- [Example real-time signal viewer](/example/ft_realtime_signalviewer)
- [Measuring the timing delay and jitter for a real-time application](/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application)
- [Realtime neurofeedback application based on Hilbert phase estimation](/example/ft_realtime_hilbert)

## Plotting and visualization

- [Creating a layout for plotting NIRS optodes and channels](/example/nirs_layout)
- [Plotting the result of source reconstructing on a cortical mesh](/example/plotting_source_surface)
- [Making a synchronous movie of EEG or NIRS combined with video recordings](/example/video_eeg)

## Various other examples

- [BIDS - the brain imaging data structure](/example/bids)
- [Combining simultaneous recordings in BIDS](/example/bids_pom)
- [Converting an example audio dataset for sharing in BIDS](/example/bids_audio)
- [Converting an example behavioral dataset for sharing in BIDS](/example/bids_behavioral)
- [Converting an example EEG dataset for sharing in BIDS](/example/bids_eeg)
- [Converting an example EMG dataset for sharing in BIDS](/example/bids_emg)
- [Converting an example eyetracker dataset for sharing in BIDS](/example/bids_eyetracker)
- [Converting an example MEG dataset for sharing in BIDS](/example/bids_meg)
- [Converting an example motion tracking dataset for sharing in BIDS](/example/bids_motion)
- [Converting an example NIRS dataset for sharing in BIDS](/example/bids_nirs)
- [Converting an example video dataset for sharing in BIDS](/example/bids_video)
- [Converting the combined MEG/fMRI MOUS dataset for sharing in BIDS](/example/bids_mous)
- [Making your analysis pipeline reproducible using reproducescript](/example/reproducescript)
- [Using reproducescript for a group analysis](/example/reproducescript_group)
- [Using reproducescript on a full study](/example/reproducescript_andersen)
- [Correlation analysis of fMRI data](/example/correlation_analysis_in_fmri_data)
- [Example analysis pipeline for Biosemi bdf data](/example/biosemi)
- [Find the orientation of planar gradiometer channels](/example/planar_orientation)
- [How to import data from MNE-Python and FreeSurfer](/example/import_mne)
- [How to use ft_checkconfig](/example/checkconfig)
- [Perform modified Multiscale Entropy (mMSE) analysis on EEG/MEG/LFP data](/example/entropy_analysis)
