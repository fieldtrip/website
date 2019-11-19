---
title: Creation of headmodels and sourcemodels for source reconstruction
tags: [tutorial, meg, headmodel, sourcemodel, sourceanalysis]
---

# Creation of headmodels and sourcemodels for source reconstruction

{% include markup/info %}
This tutorial was written specifically for the practicalMEEG workshop in Paris in December 2019, and is an adjusted version of the [headmodel for MEG tutorial](/tutorial/headmodel_meg).
{% include markup/end %}

## Introduction

This tutorial describes how to construct a volume conduction model of the head (headmodel) and a sourcemodel, based on an individual subject's MRI. These two geometrical objects are necessary ingredients (in combination with a specification of the MEG/EEG sensor array) for the construction of a forward model. The forward model itself is a necessary prerequisite for source reconstruction. It is a model that describes, for a given set of putative source locations (defined in the sourcemodel), the spatial distribution of the signals picked up by the sensor array. Each of the sources is modelled as an equivalent current dipole (ECD), which serve as elementary building blocks of arbitrarily complex source configurations. The headmodel is needed to account for the effect of volume currents.
We will use the anatomical images that belong to the same subject whose data were analyzed in the previous tutorials ([From raw data to ERP](/workshop/paris2019/handson_raw2erp), [Time-frequency analysis using Hanning window, multitapers and wavelets](/workshop/paris2019/handson_sensoranalysis)), thus using anatomical data of subject sub-15 of the Face recognition [dataset](/workshop/meg-uk-2015/dataset).

This tutorial will **not** show how to perform the source reconstruction itself. If you are interested in source reconstruction methods, you can go to the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and to the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials, or to the [].

{% include markup/success %}
The volume conduction model created here is MEG specific and cannot be used for EEG source reconstruction. If you are interested in EEG source reconstruction methods, you can go to the corresponding [EEG tutorial](/tutorial/headmodel_eeg).
{% include markup/end %}

## Background
