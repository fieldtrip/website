---
title: Tutorials
category: tutorial
---

The tutorials contain background on the different analysis methods and include code that you can copy-and-paste in MATLAB to walk through the different analysis options. Some of these tutorials are also used during the "Advanced EEG/MEG analysis" [toolkit course](https://www.ru.nl/donders/agenda/donders-tool-kits/) that is presented at the Centre for Cognitive Neuroimaging of the Donders Institute for Brain, Cognition and Behaviour each year. Furthermore, we use or have used these tutorials during the various [workshops](/workshop).

The example datasets that are used in the documentation are listed in [this overview](/faq/other/datasets), including links to all pages that use a specific dataset. These datasets are in general available from our [download server](https://download.fieldtriptoolbox.org/tutorial/).

We invite you to [add your own](/development/contribute) tutorials to the website, considering the [documentation guidelines](/development/guideline/documentation). Whenever you explain somebody in person or over email how to do something with FieldTrip, please consider whether you could use the website for this, allowing others to learn from it as well.

See also the [frequently asked questions](/faq) and [example scripts](/example).

## Introduction to FieldTrip and MATLAB

{% include pagelist section="tutorial/intro" %}

## Reading and preprocessing data

{% include pagelist section="tutorial/preproc" %}

## Sensor-level analyses

{% include pagelist section="tutorial/sensor" %}

## Source reconstruction

- [Construct a headmodel for MEG source analysis](/tutorial/source/headmodel_meg)
- [Construct a BEM headmodel for EEG source analysis](/tutorial/source/headmodel_eeg_bem)
- [Construct a FEM headmodel for EEG source analysis](/tutorial/source/headmodel_eeg_fem)
- [Creating a source model for MEG or EEG source analysis](/tutorial/source/sourcemodel)
- [Coregistration of optically pumped magnetometer (OPM) data](/tutorial/source/coregistration_opm)
- [Localizing electrodes using a 3D-scanner](/tutorial/source/electrode)
- [Localizing oscillatory sources in MEG data using a beamformer](/tutorial/source/beamformer)
- [Beamforming oscillatory responses in combined MEG/EEG data](/tutorial/source/beamforming)
- [Localizing visual gamma and cortico-muscular coherence](/tutorial/source/beamformingextended)
- [Source reconstruction of event-related fields using minimum-norm estimation](/tutorial/source/minimumnormestimate)
- [Dipole fitting of combined MEG/EEG data](/tutorial/source/dipolefitting)
- [Computation of virtual MEG channels in source-space](/tutorial/source/virtual_sensors)
- [Virtual channel analysis of epilepsy MEG data](/tutorial/source/epilepsy)

## Analysis of intracranial data

{% include pagelist section="tutorial/intracranial" %}

## Analysis of TMS data

{% include pagelist section="tutorial/tms" %}

## Analysis of fNIRS data

{% include pagelist section="tutorial/nirs" %}

## Connectivity analysis

- [Analysis of corticomuscular coherence](/tutorial/connectivity/coherence)
- [Analysis of sensor- and source-level connectivity](/tutorial/connectivity/connectivity_sensor_source)
- [Extended analysis of sensor- and source-level connectivity](/tutorial/connectivity/connectivityextended)
- [Whole brain connectivity and network analysis](/tutorial/connectivity/networkanalysis)
- [Whole brain connectivity and network analysis (2) - EEG](/tutorial/connectivity/networkanalysis_eeg)

## Statistical analysis

{% include pagelist section="tutorial/stats" %}

## Plotting and visualization

{% include pagelist section="tutorial/plotting" %}

## Making your analyses more efficient

{% include pagelist section="tutorial/scripting" %}
