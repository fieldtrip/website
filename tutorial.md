---
title: Tutorials
category: tutorial
---

# Tutorials

The tutorials contain background on the different analysis methods and include code that you can copy-and-paste in MATLAB to walk through the different analysis options. The [frequently asked questions](/faq) and [example scripts](/example) are other forms of documentation.

Some of these tutorials are also used during the "Advanced EEG/MEG analysis" [toolkit course](https://www.ru.nl/donders/agenda/donders-tool-kits/) that is presented at the Centre for Cognitive Neuroimaging of the Donders Institute for Brain, Cognition and Behaviour each year. Furthermore, we use or have used these tutorials during the various [workshops](/workshop).

For information on what types of datasets we have here on FieldTrip, and which datasets are used in which tutorials see this overview of the [datasets used in the tutorials](/faq/datasets). The datasets used in the tutorials are in general available from our [download server](https://download.fieldtriptoolbox.org/tutorial/).

When adding or contributing to the tutorials please consider the [documentation guidelines](/development/guideline/documentation).

## Introduction to FieldTrip and MATLAB

- [Introduction to the FieldTrip toolbox](/tutorial/intro/introduction)
- [Creating a clean analysis pipeline](/tutorial/intro/pipeline)

## Reading and preprocessing data

- [Preprocessing - Reading continuous EEG and MEG data](/tutorial/preproc/continuous)
- [Preprocessing - Trigger based trial selection](/tutorial/preproc/preprocessing)
- [Introduction on dealing with artifacts](/tutorial/preproc/artifacts)
- [Visual or manual artifact rejection](/tutorial/preproc/visual_artifact_rejection)
- [Automatic artifact rejection](/tutorial/preproc/automatic_artifact_rejection)
- [Cleaning artifacts using ICA](/tutorial/preproc/ica_artifact_cleaning)

## Sensor-level analyses

- [Event-related fields and MEG planar gradient](/tutorial/sensor/eventrelatedaveraging)
- [Preprocessing of EEG data and computing ERPs](/tutorial/sensor/preprocessing_erp)
- [Preprocessing and event-related activity in combined MEG/EEG data](/workshop/natmeg2014/preprocessing)
- [Preprocessing of Optically Pumped Magnetometer (OPM) data](/tutorial/sensor/preprocessing_opm)
- [Time-frequency analysis using Hanning window, multitapers and wavelets](/tutorial/sensor/timefrequencyanalysis)
- [Time-frequency analysis of combined MEG/EEG data](/workshop/natmeg2014/timefrequency)
- [Sensor-level ERF, TFR and connectivity analyses](/tutorial/sensor/sensor_analysis)
- [Extracting the brain state and events from continuous sleep EEG](/tutorial/sensor/sleep)

## Source reconstruction

- [Construct a headmodel for MEG source analysis](/tutorial/source/headmodel_meg)
- [Construct a BEM headmodel for EEG source analysis](/tutorial/source/headmodel_eeg_bem)
- [Construct a FEM headmodel for EEG source analysis](/tutorial/source/headmodel_eeg_fem)
- [Creating a source model for MEG or EEG source analysis](/tutorial/source/sourcemodel)
- [Localizing electrodes using a 3D-scanner](/tutorial/source/electrode)
- [Localizing oscillatory sources in MEG data using a beamformer](/tutorial/source/beamformer)
- [Beamforming oscillatory responses in combined MEG/EEG data](/workshop/natmeg2014/beamforming)
- [Localizing visual gamma and cortico-muscular coherence](/tutorial/source/beamformingextended)
- [Source reconstruction of event-related fields using minimum-norm estimation](/tutorial/source/minimumnormestimate)
- [Dipole fitting of combined MEG/EEG data](/workshop/natmeg2014/dipolefitting)
- [Computation of virtual MEG channels in source-space](/tutorial/source/virtual_sensors)
- [Virtual channel analysis of epilepsy MEG data](/tutorial/source/epilepsy)
- [Coregistration of optically pumped magnetometer (OPM) data](/tutorial/source/coregistration_opm)

## Analysis of intracranial data

- [Analysis of human ECoG and sEEG recordings](/tutorial/intracranial/human_ecog)
- [Analysis of monkey ECoG recordings](/tutorial/intracranial/monkey_ecog)
- [Channel and source analysis of mouse EEG](/tutorial/intracranial/mouse_eeg)
- [Preprocessing and analysis of spike-train data](/tutorial/intracranial/spike)
- [Preprocessing and analysis of spike and LFP data](/tutorial/intracranial/spikefield)

## Analysis of TMS data

- [Dealing with TMS-EEG datasets](/tutorial/tms/tms-eeg)

## Analysis of fNIRS data

- [Preprocessing and averaging of single-channel NIRS data](/tutorial/nirs/nirs_singlechannel)
- [Preprocessing and averaging of multi-channel NIRS data](/tutorial/nirs/nirs_multichannel)

## Connectivity analysis

- [Analysis of corticomuscular coherence](/tutorial/connectivity/coherence)
- [Analysis of sensor- and source-level connectivity](/tutorial/connectivity/connectivity_sensor_source)
- [Extended analysis of sensor- and source-level connectivity](/tutorial/connectivity/connectivityextended)
- [Whole brain connectivity and network analysis](/tutorial/connectivity/networkanalysis)
- [Whole brain connectivity and network analysis (2) - EEG](/tutorial/connectivity/networkanalysis_eeg)

## Statistical analysis

- [Parametric and non-parametric statistics on event-related fields](/tutorial/stats/eventrelatedstatistics)
- [Cluster-based permutation tests on event-related fields](/tutorial/stats/cluster_permutation_timelock)
- [Cluster-based permutation tests on time-frequency data](/tutorial/stats/cluster_permutation_freq)
- [Statistical analysis and multiple comparison correction for combined MEG/EEG data](/workshop/natmeg2014/statistics)
- [Multivariate analysis of MEG/EEG data](/tutorial/stats/mvpa_light) (based on the MVPA light toolbox)

## Plotting and visualization

- [Specifying the channel layout for plotting](/tutorial/plotting/layout)
- [Plotting data at the channel and source level](/tutorial/plotting/plotting)

## Making your analyses more efficient

- [Making a memory efficient analysis pipeline](/tutorial/scripting/memory)
- [Speeding up your analysis using distributed computing with qsub](/tutorial/scripting/distributedcomputing_qsub)
- [Speeding up your analysis using distributed computing with parfor](/tutorial/scripting/distributedcomputing_parfor)
