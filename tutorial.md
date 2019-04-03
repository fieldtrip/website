---
title: Overview of all tutorials
tags: [tutorial]
---

# Overview of all tutorials

The tutorials contain background on the different analysis methods and include code that you can copy-and-paste in MATLAB to walk through the different analysis options. The [frequently asked questions](/faq) and [example scripts](/example) are other forms of documentation.

Some of these tutorials are also used during the "Advanced EEG/MEG analysis" [toolkit course](https://www.ru.nl/donders/agenda/donders-tool-kits/) that is presented at the Centre for Cognitive Neuroimaging of the Donders Institute for Brain, Cognition and Behaviour each year. Furthermore, we use these tutorials during the various [workshops](/workshop).

For information on what types of datasets we have here on FieldTrip, and which datasets are used in which tutorials see this overview of the [datasets used in the tutorials](/faq/what_types_of_datasets_and_their_respective_analyses_are_used_on_fieldtrip).

When adding or contributing to the tutorials please consider the [documentation guidelines](/development/guideline/documentation).

## Introduction to FieldTrip and MATLAB

- [Introduction to the FieldTrip toolbox](/tutorial/introduction)
- [Creating a clean analysis script](/tutorial/scripting)
- [Making a memory efficient analysis script](/tutorial/memory)
- [Speeding up your analysis with distributed computing](/tutorial/distributedcomputing)

## Preprocessing of MEG and EEG data

- [Introduction on artifacts](/tutorial/artifacts)
- [Visual artifact detection](/tutorial/visual_artifact_rejection)
- [Automatic artifact detection](/tutorial/automatic_artifact_rejection)
- [Preprocessing - Trigger based trial selection](/tutorial/preprocessing)
- [Preprocessing - Reading continuous EEG data](/tutorial/continuous)
- [Preprocessing and event-related activity in combined MEG/EEG data](/workshop/natmeg/preprocessing)

## Sensor-level analyses of MEG and EEG data

- [Event related fields and MEG planar gradient](/tutorial/eventrelatedaveraging)
- [Preprocessing of EEG data and computing ERPs](/tutorial/preprocessing_erp)
- [Time-frequency analysis using Hanning window, multitapers and wavelets](/tutorial/timefrequencyanalysis)
- [Time-frequency analysis of combined MEG/EEG](/workshop/natmeg/timefrequency)
- [Sensor-level ERF, TFR and connectivity analyses](/tutorial/sensor_analysis)
- [Extracting the brain state and events from continuous sleep EEG](/tutorial/sleep)

## Source reconstruction of MEG and EEG data

- [Construct a headmodel for MEG source analysis](/tutorial/headmodel_meg)
- [Construct a BEM headmodel for EEG source analysis](/tutorial/headmodel_eeg_bem)
- [Construct a FEM headmodel for EEG source analysis](/tutorial/headmodel_eeg_fem)
- [Construct a sourcemodel for MEG or EEG source analysis](/tutorial/sourcemodel)
- [Localizing electrodes using a 3D-scanner](/tutorial/electrode)
- [Localizing oscillatory sources in MEG data using a beamformer](/tutorial/beamformer)
- [Beamforming oscillatory responses in combined MEG/EEG data](/workshop/natmeg/beamforming)
- [Localizing visual gamma and cortico-muscular coherence](/tutorial/beamformingextended)
- [Source reconstruction of event-related fields using minimum-norm estimation](/tutorial/minimumnormestimate)
- [Dipole fitting of combined MEG/EEG data](/workshop/natmeg/dipolefitting)
- [Computation of virtual MEG channels in source-space](/tutorial/virtual_sensors)

## Analysis of intracranial electrophysiological recordings

- [Analysis of human ECoG and sEEG recordings](/tutorial/human_ecog)
- [Analysis of monkey ECoG recordings](/tutorial/monkey_ecog)
- [Channel and source analysis of mouse EEG](/tutorial/mouse_eeg)
- [Preprocessing and analysis of spike-train data](/tutorial/spike)
- [Preprocessing and analysis of spike and local field potential data](/tutorial/spikefield)

## Analysis of TMS-EEG data

- [Dealing with TMS-EEG datasets](/tutorial/tms-eeg)

## Analysis of fNIRS data

- [Preprocessing and averaging of single-channel NIRS data](/tutorial/nirs_singlechannel)
- [Preprocessing and averaging of multi-channel NIRS data](/tutorial/nirs_multichannel)

## Connectivity analysis

- [Analysis of corticomuscular coherence](/tutorial/coherence)
- [Analysis of sensor- and source-level connectivity](/tutorial/connectivity)
- [Whole brain connectivity and network analysis](/tutorial/networkanalysis)

## Statistics

- [Parametric and non-parametric statistics on event related fields](/tutorial/eventrelatedstatistics)
- [Cluster-based permutation tests on event related fields](/tutorial/cluster_permutation_timelock)
- [Cluster-based permutation tests on time-frequency data](/tutorial/cluster_permutation_freq)
- [Statistical analysis and multiple comparison correction for combined MEG/EEG data](/workshop/natmeg/statistics)
- [Multivariate analysis of MEG/EEG data](/tutorial/multivariateanalysis) (based on the Donders Machine Learning Toolbox)
- [Multivariate analysis of MEG/EEG data](/tutorial/mvpa_light) (based on the MVPA light toolbox)

## Visualizing the results of an analysis

- [Specifying the channel layout for plotting](/tutorial/layout)
- [Plotting data at the channel and source level](/tutorial/plotting)

The data that is used for the tutorials is available from <ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/>. You can login with username 'anonymous' and use your email address as password.
