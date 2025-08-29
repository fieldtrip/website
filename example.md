---
title: Examples
category: example
---

# Examples

Here you can find example MATLAB scripts together with documentation that show specific analyses done in FieldTrip or in MATLAB. The documentation here is often not as elaborate as the [tutorials](/tutorial), but goes more in detail into specific aspects of the data, code or analysis.

We invite you to [add your own](/development/contribute) example scripts or frequently asked questions to the website. Also tutorials can be added. Every time you explain somebody something about FieldTrip, please consider whether you could use the website for this, so others can learn from it as well. If you want to contribute one of your example scripts, please [add it directly](/development/contribute) to the website or [contact](/support) us.

See also the [tutorials](/tutorial) and [frequently asked questions](/faq).

## Reading and preprocessing data

- [Getting started with reading raw EEG or MEG data](/example/preproc/raw_meeg)
- [Making your own trialfun for conditional trial definition](/example/preproc/trialfun)
- [Detect the muscle activity in an EMG channel and use that as trial definition](/example/preproc/trialdef_emg)
- [Determine the filter characteristics](/example/preproc/filter_characteristics)
- [Independent component analysis (ICA) to remove ECG artifacts](/example/preproc/ica_ecg)
- [Independent component analysis (ICA) to remove EOG artifacts](/example/preproc/ica_eog)
- [Combine MEG with Eyelink eyetracker data](/example/preproc/meg_eyelink)
- [Use denoising source separation (DSS) to remove ECG artifacts](/example/preproc/dss_ecg)
- [Fixing a missing sensor](/example/preproc/fixing_a_missing_sensor)
- [Rereference EEG and iEEG data](/example/preproc/rereference)

## Sensor-level analysis

- [Analyzing NIRS data recorded during unilateral finger- and foot-tapping](/example/sensor/nirs_fingertapping)
- [Analyzing NIRS data recorded during listening to and repeating speech](/example/sensor/nirs_speech)
- [The correct pipeline order for combining planar MEG channels](/example/sensor/combineplanar_pipelineorder)
- [How to incorporate head movements in MEG analysis](/example/sensor/headmovement_meg)
- [Interpolating data from the CTF151 to the CTF275 sensor array using ft_megrealign](/example/sensor/megrealign)

## Spectral analysis

- [Analysis of high-gamma band signals in human ECoG](/example/spectral/ecog_ny)
- [Analyze steady-state visual evoked potentials (SSVEPs)](/example/spectral/ssvep)
- [Cross-frequency analysis](/example/spectral/crossfreq)
- [Effect of signal-to-noise ratio on coherence](/example/spectral/coherence_snr)
- [Effects of tapering for power estimates](/example/spectral/effects_of_tapering)
- [Fourier analysis of oscillatory power and coherence](/example/spectral/fourier)
- [Simulate an oscillatory signal with phase resetting](/example/spectral/phase_reset)
- [Irregular resampling auto-spectral analysis (IRASA)](/example/spectral/irasa)
- [Fitting oscillations and one-over-F (FOOOF)](/example/spectral/fooof)
- [Conditional Granger causality in the frequency domain](/example/spectral/granger_conditional)
- [Interpolate the time axis of single-trial TFRs](/example/spectral/tfr_interpolatetime)

## Source reconstruction

- [Align EEG electrode positions to BEM headmodel](/example/source/electrodes2bem)
- [Check the quality of the anatomical coregistration](/example/source/coregistration_quality_control)
- [Combined EEG and MEG source reconstruction](/example/source/sourcerecon_meeg)
- [Common filters in beamforming](/example/source/beamformer_commonfilter)
- [Compute EEG leadfields using a concentric spheres headmodel](/example/source/concentricspheres)
- [Compute EEG leadfields using a BEM headmodel](/example/source/bem)
- [Compute EEG leadfields using a FEM headmodel](/example/source/fem)
- [Compute forward simulated data and apply a beamformer scan](/example/source/simulateddata_beamformer)
- [Compute forward simulated data and apply a dipole fit](/example/source/simulateddata_dipolefit)
- [Compute forward simulated data using ft_dipolesimulation](/example/source/simulateddata)
- [Compute forward simulated data with the low-level ft_compute_leadfield](/example/source/compute_leadfield)
- [Create MNI-aligned grids in individual head coordinates](/example/source/sourcemodel_aligned2mni)
- [Read Neuromag .fif mri and create a MNI-aligned single-shell head model](/example/source/neuromag_aligned2mni)
- [Create a template source model aligned to MNI space](/example/source/sourcemodel_mnitemplate)
- [Use an MNI-aligned grid with a FEM headmodel in individual head coordinates](example/source/sourcemodel_fem_centroids)
- [How to create a head model if you do not have an individual MRI](/example/source/fittemplate)
- [Fit a dipole to the tactile ERF after mechanical stimulation](/example/source/dipolefit_somatosensory_erf)
- [Localizing the sources underlying the difference in event-related fields](/example/source/difference_erf)
- [Make MEG leadfields using different headmodels](/example/source/headmodel_various)
- [Symmetric dipole pairs for beamforming](/example/source/symmetry)
- [Testing BEM created lead fields](/example/source/bem_evaluation)
- [Use your own forward leadfield model in an inverse beamformer computation](/example/source/beamformer_ownforward)

## Statistical analysis

- [Apply non-parametric statistics with clustering on TFRs of power that were computed with BESA](/example/stats/stats_besa)
- [Computing and reporting the effect size](/example/stats/effectsize)
- [Defining electrodes as neighbours for cluster-level statistics](/example/stats/neighbours)
- [Source statistics](/example/stats/source_statistics)
- [Stratify the distribution of two variables](/example/stats/stratify)
- [Use simulated ERPs to explore cluster statistics](/example/stats/simulateddata_clusterstats)
- [Using general linear modeling to analyze NIRS timeseries data](/example/stats/nirs_glm)
- [Using general linear modeling over trials](/example/stats/glm_trials)
- [Using general linear modeling on time series data](/example/stats/glm_timeseries)
- [Using simulations to estimate the sample size for cluster-based permutation test](/example/stats/samplesize)
- [Using threshold-free cluster enhancement for cluster statistics](/example/stats/tfce)

## Real-time analysis

- [Example real-time average](/example/realtime/ft_realtime_average)
- [Example real-time classification](/example/realtime/ft_realtime_classification)
- [Example real-time power estimate](/example/realtime/ft_realtime_powerestimate)
- [Example real-time selective average](/example/realtime/ft_realtime_selectiveaverage)
- [Example real-time signal viewer](/example/realtime/ft_realtime_signalviewer)
- [Measuring the timing delay and jitter for a real-time application](/example/realtime/realtime_evaluation)
- [Realtime neurofeedback application based on Hilbert phase estimation](/example/realtime/ft_realtime_hilbert)

## Plotting and visualization

- [Creating a layout for plotting NIRS optodes and channels](/example/plotting/nirs_layout)
- [Plotting the result of source reconstructing on a cortical mesh](/example/plotting/plotting_source_surface)
- [Making a synchronous movie of EEG or NIRS combined with video recordings](/example/plotting/video_eeg)

## Various other examples

- [BIDS - the brain imaging data structure](/example/other/bids)
- [Combining simultaneous recordings in BIDS](/example/other/bids_pom)
- [Converting an example audio dataset for sharing in BIDS](/example/other/bids_audio)
- [Converting an example behavioral dataset for sharing in BIDS](/example/other/bids_behavioral)
- [Converting an example EEG dataset for sharing in BIDS](/example/other/bids_eeg)
- [Converting an example EMG dataset for sharing in BIDS](/example/other/bids_emg)
- [Converting an example eyetracker dataset for sharing in BIDS](/example/other/bids_eyetracker)
- [Converting an example MEG dataset for sharing in BIDS](/example/other/bids_meg)
- [Converting an example motion tracking dataset for sharing in BIDS](/example/other/bids_motion)
- [Converting an example NIRS dataset for sharing in BIDS](/example/other/bids_nirs)
- [Converting an example video dataset for sharing in BIDS](/example/other/bids_video)
- [Converting the combined MEG/fMRI MOUS dataset for sharing in BIDS](/example/other/bids_mous)
- [Making your analysis pipeline reproducible using reproducescript](/example/other/reproducescript)
- [Using reproducescript for a group analysis](/example/other/reproducescript_group)
- [Using reproducescript on a full study](/example/other/reproducescript_andersen)
- [Correlation analysis of fMRI data](/example/other/fmri_correlationanalysis)
- [Example analysis pipeline for BioSemi bdf data](/example/other/biosemi)
- [Find the orientation of planar gradiometer channels](/example/other/planar_orientation)
- [How to import data from MNE-Python and FreeSurfer](/example/other/import_mne)
- [How to use ft_checkconfig](/example/other/checkconfig)
- [Perform modified multiscale entropy (mMSE) analysis on EEG/MEG/LFP data](/example/other/entropy_analysis)
