---
title: Details on the EEG language dataset
tags: [eeg-language]
---

# Details on the EEG language dataset

This EEG dataset was acquired by [Irina Siminova et al.]
(https://doi.org/10.1371/journal.pone.0014465) in a study investigating semantic
processing of stimuli presented as pictures (black line drawings on 
white background), visually displayed text or as auditorily presented 
words. Stimuli consisted of concepts from three semantic categories: 
two relevant categories (animals, tools) and a task category that varied 
across subjects, either clothing or vegetables.

{% include image src="/assets/img/workshop/madrid2019/datasets/simanova_fig1.png" width="800" %}
*Figure 1. Experimental stimuli and conditions*

Continuous EEG was registered using a 64 channel ActiCap system (Brain Products GmbH) filtered at 0.2–200 Hz and sampled at 500 Hz with the BrainVision Recorder Professional software (Brain Products GmbH). An [equidistant electrode
cap](http://www.fieldtriptoolbox.org/assets/img/template/layout/easycapm10.png) was used to position 60 electrodes on the scalp as follows:

{% include image src="/assets/img/workshop/madrid2019/datasets/simanova_fig2.png" width="800" %}

One electrode was placed under the right eye to compute bipolar signals
("vectical EOG" and "horizontal EOG"). During acquisition the reference
at the right mastoid; an additional electrode measured the voltage on the
left mastoid, Channels 1-60 correspond to electrodes that are located on
the head, except for channel 53 which is located at the right mastoid.
Channels 61, 62, 63 are not connected to an electrode at all. Channel 64
is connected to an electrode placed below the left eye.
