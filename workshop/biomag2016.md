---
title: Biomag 2016 satellite meeting - Seoul, Korea
---

**From raw MEG to publication: How to perform MEG group analysis with free academic software.**

This page is currently still a placeholder. In due time it will contain the documentation on single subject and group analysis in line with the [other toolboxes](http://neuroimage.usc.edu/brainstorm/Biomag2016).

The full FieldTrip analysis pipelines are available from <https://github.com/fieldtrip/Wakeman-and-Henson-2015>

The FieldTrip presentation (slides) are available from <http://www.slideshare.net/RobertOostenveld/group-analyses-with-fieldtrip>

The corresponding group analysis was also done in other free software package

- SPM <http://www.fil.ion.ucl.ac.uk/spm/doc/manual.pdf#Chap:data:multi>
- MNE <http://mne-tools.github.io/mne-biomag-group-demo/>
- BrainStorm <http://neuroimage.usc.edu/brainstorm/Biomag2016>
- NutMEG

A single subject from this dataset was also analyzed for the MEG-UK workshop

- <https://www.fieldtriptoolbox.org/workshop/meg-uk-2015>
- <https://www.fieldtriptoolbox.org/workshop/meg-uk-2015/fieldtrip-stats-demo>
- <https://www.fieldtriptoolbox.org/workshop/meg-uk-2015/fieldtrip-beamformer-demo>

### Abstract (of the satellite meeting)

Free academic toolboxes have gained increasing prominence in MEG analysis as a means to disseminate cutting edge methods, share best practices between different research groups and pool resources for developing essential tools for the MEG community. In the recent years large and vibrant research communities have emerged around several of these toolboxes. Teaching events are regularly held around the world where the basics of each toolbox are explained by its respective developers and experienced power users. There are, however, two knowledge gaps that our BIOMAG satellite symposium aims to address. Firstly, most teaching examples only show analysis of a single 'typical best' subject whereas most real MEG studies involve analysis of group data. It is then left to the researchers in the field to figure out for themselves how to make the transition and obtain significant group results. Secondly, we are not familiar with any examples of fully analyzing the same group dataset with different academic toolboxes to assess the degree of agreement in scientific conclusions and compare strengths and weaknesses of various analysis methods and their independent implementations. Our workshop is organised by the lead developers of six most popular free academic MEG toolboxes (in alphabetic order): Brainstorm, EEGLAB, FieldTrip, MNE, NUTMEG, and SPM. Ahead of the workshop the research team for each toolbox will analyze the same group MEG/EEG dataset. This dataset containing evoked responses to face stimuli was acquired by Richard Henson and Daniel Wakeman, who won a special award at BIOMAG2010 to make it freely available to the community. All the raw data are available at <https://openfmri.org/dataset/ds000117/>.

Detailed instructions for each toolbox will be made available online including analysis scripts and figures of results. All analyses will show a full pipeline from the raw data to detailed publication quality results. Researchers who are interested in using the respective toolbox will then be able to reproduce the analysis in their lab and port it to their own data.

At the workshop each group will briefly introduce their software and present the key results from their analysis. This will be followed by a panel discussion and questions from the audience.

Following the event we plan to integrate the suggestions and questions from the workshop audience and to publish the analyses details as part of a special research topic in Frontiers in Neuroscience, section Brain Imaging Methods so that the proposed best practices will be endorsed by peer review and become citable in future publications. Other research groups will be invited to contribute to the research topic as long as they present detailed descriptions of analyses of group data that are freely available online and make it possible for others to fully reproduce their analysis and results.

We hope that this proposal will lead to creation of invaluable resource for the whole MEG community and the workshop will contribute to establishment of good practice and promoting consistent and reproducible analyses approaches. The event will also showcase all the toolboxes and will be of interest to beginners in the field with basic background in MEG who contemplate the most suitable analysis approach and software for their study as well as to experienced researchers who would like to get up to date with the latest methodological developments.

### Dataset description

This is a mulimodal dataset containing simultaneous M/EEG recordings on 19 healthy subjects. Subjects were presented with 6 sessions of 10 minutes duration each. In the original study, three subjects (sub001, sub005, sub016) were excluded from the analysis.

### Stimulation details

The start of a trial was indicated with a fixation cross of random duration between 400 to 600 ms.
The face stimuli was superimposed on the fixation cross for a random duration of 800 to 1,000 ms.
Inter stimulus interval of 1,700 ms comprised a central white circle.

Two types of stimulation pattern:

- Immediate: The image was presented consecutively
- Long: The two images were presented with 5-15 intervening stimuli

For the purposes of our analysis, we treat these two stimulation patterns of stimuli together.
To maintain attention, subjects were asked to judge the symmetry of the image and respond with a keypress.

### Acquisition details

- Sampling frequency : 1100 Hz
- Stimulation triggers: The trigger channel is STI101 with the following event code
- Famous faces: 5 (first), 6 (immediate), and 7 (long)
- Unfamiliar faces: 13 (first), 14 (immediate), and 15 (long)
- Scrambled faces: 17 (first), 18 (immediate), and 19 (long)
- Sensors
  - 102 magnetometers
  - 204 planar gradiometers
  - 70 electrodes recorded with a nose reference (Easycap conforming to extended 10-20% system)
  - Two sets of bipolar electrodes were used to measure vertical (left eye; EEG062) and horizontal
  - electro-oculograms (EEG061). Another set was used to measure ECG (EEG063)
- A fixed 34 ms delay exists between the appearance of a trigger in the trigger channel STI101 and the appearance of the stimulus on the screen
