---
title: FieldTrip Workshop in Exeter, UK
parent: FieldTrip courses and workshops
category: workshop
---

# FieldTrip Workshop in Exeter, UK

- Workshop leaders: Eelke Spaak and Linda Drijvers
- When: 6-7 June 2017
- Where: University of Exeter

We will keep this page up to date and post new information here when available.

## Schedule

#### Day 1 (Tuesday 6 June 2017)

- 8:45 - 9:00 Registration, with coffee/tea
- 9:00 - 9:15 Introduction
- 9:15 - 10:15 Lecture 1: Overview of the FieldTrip toolbox and event-related averaging [slides](https://www.dropbox.com/s/m0zgsq05a0orwzr/1_intro_and_preprocessing_Linda.pptx?dl=0)
- 10:15 - 10:30 Coffee break
- 10:30 - 12:30 Hands-on 1: [Preprocessing EEG data and event-related potentials](/tutorial/preprocessing_erp)
  - If time permits, have a look at [Event-related averaging and MEG planar gradient](/tutorial/eventrelatedaveraging) but only the first half (stop when you get to the planar gradient).
- 12:30 - 13:30 Lunch
- 13:30 - 14:30 Lecture 2: Fundamentals of neuronal oscillations and synchrony [slides](https://www.dropbox.com/s/iou7x06h0xff5jh/2_frequency_oscillations_Eelke.pptx?dl=0)
- 14:30 - 14:45 Tea break
- 14:45 - 16:45 Hands-on 2: [Time-frequency analysis of power](/tutorial/timefrequencyanalysis)
- 16:45 - 17:15 Wrap-up / Q&A session
- 19:00 Dinner

#### Day 2 (Wednesday 7 June 2017)

- 9:00 - 10:00 Lecture 3: Statistical inference using non-parametric permutation techniques [slides](https://www.dropbox.com/s/ah8kp2tejegza6u/3.%20cluster%20statistics%20%28Eelke%29.pptx?dl=0)
- 10:00 - 10:15 Coffee break
- 10:15 - 12:15 Hands-on 3: Parametric and non-parametric statistics in FieldTrip
  - There are several options here. You can choose a somewhat ['gentle' introduction tutorial](/tutorial/eventrelatedstatistics), and follow that by, or start immediately with, either or both of the more in-depth tutorials:
    - [Cluster-based permutation tests on event-related fields](/tutorial/cluster_permutation_timelock) and/or
    - [Cluster-based permutation tests on time-frequency data](/tutorial/cluster_permutation_freq)
- 12:15 - 13:00 Lunch
- 13:00 - 14:00 Lecture 4: Connectivity analysis of electrophysiological data [slides](https://www.dropbox.com/s/0ckwxqk856ra6q3/4.%20connectivity%20analysis%20%28Eelke%29.pptx?dl=0)
- 14:00 - 15:45 Hands-on 4: [Analysis of sensor- and source-level connectivity](/tutorial/connectivity)
- 15:45 - 16:00 Tea break
- 16:00 - 17:30 FieldTrip playground: work on your own data
- 17:30 - 18:00 Wrap-up / Q&A session

Further reading on connectivity and its pitfalls (Bastos and Schoffelen, 2016): <http://journal.frontiersin.org/article/10.3389/fnsys.2015.00175/full>

## Tutorial preparation

All the code (correct FieldTrip version) and data for the tutorials are already downloaded on your workshop computer (thus no need to install FieldTrip, nor to download the data when the tutorial indicates this).

- Change directory to the location of the FieldTrip package (here: C:\\workshop-exeter). Note the subfolders present.
- Add the FieldTrip folder to the pat

  addpath('C:/workshop-exeter/fieldtrip');

Note: **do not** add the folder recursively, i.e., do not use addpath(genpath('C:/workshop-exeter/fieldtrip')).

- Run 'ft_defaults' in Matlab.
- Then change directory to the one specifically holding the data for the particular tutorial, e.g., the first is preprocessing_erp.
- Confirm that FT has been successfully added to your path, for example by typing 'which ft_preprocessing' in Matlab; the correct path should be displayed.
