---
title: MEG/EEG analysis and FieldTrip Workshop in Oxford, UK
tags: [oxford2019]
---

# MEG/EEG analysis and FieldTrip Workshop in Oxford, UK

- Workshop leaders: Eelke Spaak and Nadine Dijkstra
- Local organizer: Jasper Hajonides van der Meulen
- When: 6-8 May 2019
- Where: Department of Experimental Psychology, Anna Watts building, Jericho, Oxford


## Schedule

#### Day 1 (Monday 6 May, 2019)

- 08:45 – 09:00 Registration, with coffee/tea
- 09:00 – 09:15 Introduction
- 09:15 – 10:15 Lecture 1: Overview of the FieldTrip toolbox and neuronal oscillations
- 10:15 – 10:30 Coffee break
- 10:30 – 12:30 Hands-on 1: [Reading in data and performing sensor-level ERF and TFR analyses](/workshop/oxford2019/sensor_analysis_plusminus)

- 12:30 – 13:30 Lunch

- 13:30 – 14:30 Lecture 2: Statistical inference using non-parametric permutation techniques
- 14:30 – 14:45 Tea break
- 14:45 – 16:45 Hands-on 2: [Cluster-based permutation tests on event-related fields](/tutorial/stats/cluster_permutation_timelock)
- 16:45 – 17:15 Wrap-up / Q&A session


#### Day 2 (Tuesday 7 May, 2019)

- 09:00 – 10:00 Lecture 3: Beamformer techniques for source reconstruction
- 10:00 – 10:15 Coffee break
- 10:15 – 12:15 Hands-on 3: [Source reconstruction of induced oscillatory activity and/or  corticomuscular coherence](/tutorial/source/beamformingextended)

- 12:15 – 13:15 Lunch

- 13:15 – 13:45 Decoding neural representations through space and time (Michael Wolff)
- 13:45 – 14:15 Temporally-Unconstrained Decoding Analysis (Cameron Higgins)
- 14:15 – 14:45 Empirical Mode Decomposition for time-frequency analysis (Andrew Quinn)
- 14:45 – 15:00 Tea break
- 15:00 – 17:00 Hands-on 4: Getting started with cutting-edge stuff
- 17:00 – 17:30 Wrap-up / Q&A session

- 19:00 Dinner, location TBA

#### Day 3 (Wednesday 8 May, 2019)

- 09:00 – 12:30 FieldTrip/advanced analysis playground

## Tutorial preparation

All the code (correct FieldTrip version) and data for the tutorials are already downloaded on your workshop computer (thus no need to install FieldTrip, nor to download the data when the tutorial indicates this).

- Change directory to the location of the FieldTrip package. Note the subfolders present.
- Add the FieldTrip folder to the path

    addpath('path_to_fieldtrip');

Note: **do not** add the folder recursively, i.e., do not use `addpath(genpath('path_to_fieldtrip'))`.

- Run 'ft_defaults' in MATLAB.
- Then change directory to the one specifically holding the data for the particular tutorial, e.g., the first is sensor_analysis_plusminus.
- Confirm that FT has been successfully added to your path, for example by typing 'which ft_preprocessing' in Matlab; the correct path should be displayed.
