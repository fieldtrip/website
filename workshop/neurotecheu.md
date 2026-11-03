---
title: NeurotechEU hackathon - wearable neurotechnology with fNIRS and EEG 
tags: [neurotecheu, eeg-audodd, realtime, unicorn, eegsynth, lsl]
---

Radboud University collaborates with several other European universities in [NeurotechEU](https://theneurotech.eu) to train the future generation of researchers, innovators, and entrepreneurs that will implement the potential of neurotechnology into a reality for European society and beyond.

Wearable neurotechnology is increasingly used in neuroscience, rehabilitation, human factors research, neuro-ergonomics and brain-computer interfaces. Among the most widely adopted wearable methods are Electroencephalography (EEG) and Functional Near-Infrared Spectroscopy (fNIRS).

In this hackathon, you will work in a group to design new applications for these techniques. You will also receive lectures that introduce both techniques from physiological principles to practical application. You will learn how brain activity can be measured through electrical and haemodynamic signals and how the two modalities. Working in interdisciplinary teams, students are challenged to answer a practical question and design a new application using wearable neurotechnology and to demonstrate, through experimentation and data analysis, how EEG, fNIRS, or a combination of both could provide a meaningful solution.

- When: Thursday & Friday, 29 & 30 October 2026 - online
- When: Friday-Wednesday, 6-11 November 2026 - in-person

See the [event posting](https://www.ru.nl/en/about-us/events/neurotecheu-hackathonwearable-neurotechnology-fnirs-and-eeg) on the Radboud University website for more details.

This page provides links to the documentation, datasets, and software for the parts presented by Robert Oostenveld.

## Offline EEG processing

**Friday 30 Oct, 11:45-13:00**

In this hands-on workshop participants will learn how to do offline processing of EEG data. We will start with a short presentation on EEG biophysics and experimental lab setups, followed by a demonstration of importing the data in MATLAB or Python, quality assurance, bad channel and segment removal, re-referencing, filtering, ICA cleaning, event detection, segmenting, and estimation of event-related responses and/or oscillatory activity. Participants will learn the characteristics of raw EEG signals, recognize and deal with common artifacts, and extract interpretable brain signals.

- [Slides](https://download.fieldtriptoolbox.org/workshop/neurotecheu/slides/EEG_data_processing-offline.pdf)
- [Hands-on instructions](/workshop/neurotecheu/offline)

## Real-time EEG processing

**Saturday 7 Nov, 9:00-10:30**

In this hands-on workshop participants will learn how to set up EEG equipment, stream data, and do real-time analysis of EEG data with the aim to make a closed-loop application. We will start with some slides explaining the requirements of real-time processing, including delays and jitter, and strategies for implementing a processing pipeline and feedback loop.

- [Slides](https://download.fieldtriptoolbox.org/workshop/neurotecheu/slides/EEG_data_processing-realtime.pdf)
- [Hands-on instructions](/workshop/neurotecheu/realtime)
