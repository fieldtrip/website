---
title: FieldTrip Workshop in London, UK
parent: FieldTrip courses and workshops
category: workshop
---

# FieldTrip Workshop in London, UK

- Workshop leaders: Eelke Spaak and Johanna Zumer
- When: 3-5 March 2016
- Where: King's College, IoP

We will keep this page up to date and post new information here when available.

## Schedule

#### Day 1 (Thursday 3 March, 2016)

- 15:00 - 15:30 Registration, with coffee/tea
- 15:30 - 16:00 Introduction ([slides](https://dl.dropboxusercontent.com/u/4023322/kcl-london-slides/0_overview_Eelke.pptx))
- 16:00 - 17:00 Lecture 1: Overview of the FieldTrip toolbox and event-related averaging ([slides](https://dl.dropboxusercontent.com/u/4023322/kcl-london-slides/1_Intro_preprocessingEEG_Johanna_KCLondon.pptx))

- Evening Pub? (at own expense)

#### Day 2 (Friday 4 March, 2016)

- 9:00 - 11:00 Hands-on 1: [Preprocessing EEG data and event-related potentials](/tutorial/preprocessing_erp)
  - If you finish early, feel free to look at [Event-related averaging and MEG planar gradient](/tutorial/eventrelatedaveraging) but only the first half (stop when you get to the planar gradient)
- 11:00 - 11:30 Coffee break
- 11:30 - 12:30 Lecture 2: Fundamentals of neuronal oscillations and synchrony ([slides](https://dl.dropboxusercontent.com/u/4023322/kcl-london-slides/2_frequency_oscillations_johanna_KCLondon.pptx))
- 12:30 - 13:30 Lunch
- 13:30 - 15:30 Hands-on 2: [Time-frequency analysis of power](/tutorial/timefrequencyanalysis)
  - Note: read through the Preprocessing section, but do not execute the code, as you have been given only dataFIC.mat, which is the output of preprocessing
- 15:30 - 16:00 Tea break
- 16:00 - 17:00 Lecture 3: Statistical inference using non-parametric permutation techniques ([slides](https://dl.dropboxusercontent.com/u/4023322/kcl-london-slides/3.%20cluster%20statistics%20%28Eelke%29.pptx))
- 17:00 - 17:30 wrap-up / Q&A
- 18:30 Dinner (at own expense)

#### Day 3 (Saturday 5 March, 2016)

- 9:00 - 11:00 Hands-on 3: [Parametric and non-parametric statistics on event-related fields](/tutorial/eventrelatedstatistics)

  - If you finish the above early and time permits (or you want to do something more in-depth immediately; feel free!), you may want to try either
    - [Cluster-based permutation tests on event-related fields](/tutorial/cluster_permutation_timelock) and/or
    - [Cluster-based permutation tests on time-frequency data](/tutorial/cluster_permutation_freq)

- 11:00 - 11:30 Coffee break

- 11:30 - 12:30 Lecture 4: Connectivity analysis of electrophysiological data ([slides](https://dl.dropboxusercontent.com/u/4023322/kcl-london-slides/4.%20connectivity%20analysis%20%28Eelke%29.pptx))

- 12:30 - 13:15 Lunch
- 13:15 - 15:15 Hands-on 4: [Analysis of sensor- and source-level connectivity](/tutorial/connectivity)
- 15:15 - 15:30 Tea break
- 15:30 - 17:30 FieldTrip playground: work on your own data
- 17:30 - 18:00 wrap-up / Q&A

Further reading on connectivity and its pitfalls (Bastos and Schoffelen, 2016): <http://journal.frontiersin.org/article/10.3389/fnsys.2015.00175/full>

## Tutorial preparation

All the code (correct FieldTrip version) and data for the tutorials are already downloaded on your workshop computer (thus no need to install FieldTrip, nor to download the data when the tutorial indicates this).

- Change directory to the location of the FieldTrip package (here: M:\kcl-london). Note the subfolders present.
- Add the FieldTrip folder to the path

  addpath('M:\kcl-london\fieldtrip-20151216');

Note: **do not** add the folder recursively, i.e., do not use addpath(genpath('M:\kcl-london\fieldtrip-20151216')).

- Run 'ft_defaults' in MATLAB.
- Then change directory to the one specifically holding the data for the particular tutorial, e.g., the first is preprocessing_erp.
- Confirm that FT has been successfully added to your path, for example by typing 'which ft_preprocessing' in Matlab; the correct path should be displayed.
