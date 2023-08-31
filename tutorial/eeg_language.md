---
title: Details on the EEG language dataset
tags: [eeg-language]
---

# Details on the EEG language dataset

This EEG dataset was acquired by [Irina Siminova et al.](https://doi.org/10.1371/journal.pone.0014465) in a study investigating semantic processing of stimuli presented as pictures (black line drawings on white background), visually displayed text or as auditory presented words. Stimuli consisted of concepts from three semantic categories: two relevant categories (animals, tools) and a task category that varied across subjects, either clothing or vegetables.

The data from one subject is shared for tutorial purposes on the FieldTrip download server. The full dataset is available from the [MPI for Psycholinguistics Archive](https://hdl.handle.net/1839/00-0000-0000-001B-860D-8).

All main stimuli were coded with 3-digits, i.e. as 'Sxxx':

- The first digit codes task/no task: _1_ for the non-target semantic categories: animals, tools and _2_ for the target semantic category: clothing. The subjects' task was to press the button in response to clothing items, these targets were not analyzed in the main study.

- The second digit codes the items, _1 to 4_ for animals (cow, bear, lion, ape) and _5 to 8_ for tools (ax, scissors, comb, pen). There were also 4 target items (clothing).

- The third digit codes the stimulus modality: _1_ for written words, _2_ for pictures, _3_ for spoken words.

The data also contains response events for the subjects' responses to the task category.

{% include image src="/assets/img/workshop/madrid2019/datasets/simanova_fig1.png" width="400" %}

_Figure 1. Experimental stimuli and conditions_

Continuous EEG was registered using a 64 channel ActiCap system (Brain Products GmbH) filtered at 0.2–200 Hz and sampled at 500 Hz with the BrainVision Recorder Professional software (Brain Products GmbH). An [equidistant electrode cap](/assets/img/template/layout/easycapm10.png) was used to position 60 electrodes on the scalp as follows:

{% include image src="/assets/img/workshop/madrid2019/datasets/simanova_fig2.png" width="400" %}

One electrode was placed under the right eye to compute bipolar signals ("vertical EOG" and "horizontal EOG"). During acquisition the reference at the right mastoid; an additional electrode measured the voltage on the left mastoid, Channels 1-60 correspond to electrodes that are located on the head, except for channel 53 which is located at the right mastoid. Channels 61, 62, 63 are not connected to an electrode at all. Channel 64 is connected to an electrode placed below the left eye.
