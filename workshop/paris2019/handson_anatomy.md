---
title: Creation of headmodels and sourcemodels for source reconstruction
tags: [tutorial, meg, headmodel, sourcemodel, sourceanalysis]
---

# Creation of headmodels and sourcemodels for source reconstruction

{% include markup/info %}
This tutorial was written specifically for the practicalMEEG workshop in Paris in December 2019, and is an adjusted version of the [headmodel for MEG tutorial](/tutorial/headmodel_meg).
{% include markup/end %}

## Introduction

In this tutorial you can find information about how to construct a volume conduction model of the head (headmodel) based on a single subject's MRI. We will use the anatomical images that belong to the same subject whose data were analyzed in the previous tutorials ([From raw data to ERP](/workshop/paris2019/handson_raw2erp), [Time-frequency analysis using Hanning window, multitapers and wavelets](/workshop/paris2019/handson_sensoranalysis)). Here, we will work with the anatomical data of subject sub-15 of the Face recognition [dataset](/workshop/meg-uk-2015/dataset).

The volume conduction model of the head that will be constructed here is specific for source reconstruction of MEG data. Different strategies can be used for the construction of headmodels. The processing pipeline of the tutorial is an example, which we think is appropriate for this tutorial-dataset.

This tutorial will **not** show how to perform the source reconstruction itself. If you are interested in source reconstruction methods, you can go to the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and to the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials, or to the [].

{% include markup/success %}
The volume conduction model created here is MEG specific and cannot be used for EEG source reconstruction. If you are interested in EEG source reconstruction methods, you can go to the corresponding [EEG tutorial](/tutorial/headmodel_eeg).
{% include markup/end %}

## Background
