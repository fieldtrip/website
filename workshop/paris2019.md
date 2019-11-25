---
title: Practical MEEG workshop at ICM in Paris
tags: [paris2019]
---

# Practical MEEG workshop at ICM in Paris

PracticalMEEG aims at providing an intensive several–days training to MEG and EEG analysts. It will provide its attendees with the ability to create a full analysis pipeline with exemplar (or their own) data in one or several of three leading software dedicated to MEG and EEG analysis (Brainstorm, FieldTrip and MNE-python). More details can be found on <http://practicalmeeg2019.org>.

## Where

[ICM Institute for Brain and Spinal Cord](https://goo.gl/maps/B8vuqTo3tcagXFsM8)
Hôpital Pitié Salpêtrière
47 Boulevard de l'Hôpital
75013 Paris, France

## When

3-5 December 2019.

## Who

Maximilien Chaumon is the local organizer.

Robert Oostenveld and Jan-Mathijs Schoffelen will come from the Donders to lecture and tutor, assisted by Stephen Whitmarsh (who is a former Dondarian), and various other people from the MNE and BrainStorm teams.

# Program and training material

Please visit the <http://practicalmeeg2019.org>. website for more information.

All hands on sessions will be using the same [dataset](/workshop/meg-uk-2015/dataset).

## Schedule

#### Day 1 (Tuesday December 3, 2019)

- 08:30 – 09:00 Registration, with coffee/tea + Welcome & intro
- 09:00 – 10:30 Lecture 1: Data organization (Robert) and initial data processing(Alex)
- 10:30 – 12:30 Hands-on 1a: [From raw to ERPs using FieldTrip](/workshop/paris2019/handson_raw2erp)
- 10:30 – 12:30 Hands-on 1b: [From raw to ERPs using Brainstorm](https://neuroimage.usc.edu/brainstorm/WorkshopParis2019)
- 10:30 – 12:30 Hands-on 1c: From raw to ERPs using MNE python


- 12:30 – 13:30 Lunch

- 13:30 – 15:00 Lecture 2: Sensor level analysis (JM)
- 15:00 – 17:00 Hands-on 2a: [Sensor level analysis using Fieldtrip](/workshop/paris2019/handson_sensoranalysis)
- 15:00 – 17:00 Hands-on 2b: [Sensor level analysis using Brainstorm](https://neuroimage.usc.edu/brainstorm/WorkshopParis2019)
- 15:00 – 17:00 Hands-on 2c: Sensor level analysis using MNE python
- 17:00 – 17:30 Wrap-up / Q&A session

#### Day 2 (Wednesday December 4, 2019)

- 09:00 – 10:30 Lecture 3: Source estimation 1 (Alex & François)
- 10:30 – 12:30 Hands-on 3a: [Creating head and source models using Fieldtrip](/workshop/paris2019/handson_anatomy)
- 10:30 – 12:30 Hands-on 3b: [Creating head and source models using Brainstorm](https://neuroimage.usc.edu/brainstorm/WorkshopParis2019)
- 10:30 – 12:30 Hands-on 3c: Creating head and source models using MNE python

- 12:30 – 13:30 Lunch

- 13:30 – 15:00 Lecture 4: Source estimation 2 (Denis)
- 15:00 – 17:00 Hands-on 4a: [Single and distributed sources using Fieldtrip](/workshop/paris2019/handson_sourceanalysis)
- 15:00 – 17:00 Hands-on 4b: [Single and distributed sources using Brainstorm](https://neuroimage.usc.edu/brainstorm/WorkshopParis2019)
- 15:00 – 17:00 Hands-on 4c: Single and distributed sources using MNE python
- 17:00 – 17:30 Wrap-up / Q&A session

#### Day 3 (Thursday December 5, 2019)

- 09:00 – 10:30 Lecture 5: Group level analysis (Robert)
- 10:30 – 12:30 Hands-on 5a: [Group level analysis using Fieldtrip](/workshop/paris2019/handson_groupanalysis)
- 10:30 – 12:30 Hands-on 5b: [Group level analysis using Brainstorm](https://neuroimage.usc.edu/brainstorm/WorkshopParis2019)
- 10:30 – 12:30 Hands-on 5c: Group level analysis using MNE python

- 12:30 – 13:30 Lunch

- 13:30 – 15:00 Lecture 6: Miscellaneous topics
- 15:00 – 17:00 Hands-on 2: Playground and final try out
- 17:00 – 17:30 Wrap-up / Q&A session

## Tutorial preparation

{% include markup/info %}
For this workshop, we have created a set of dedicated tutorials, and fixed some small bugs in FieldTrip in order to get everything to run smoothly. Therefore, you should have a really recent version of the code, otherwise the tutorials will not run through without errors. Specifically, you need to have the code not 'older' than November 25, 2019.
{% include markup/end %}

In order to use Fieldtrip, the toolbox needs to be added to the matlab path. To achieve this, do the following:

- Change directory to the location of the FieldTrip package. Note the subfolders present.
- Add the FieldTrip folder to the path

    addpath('where_is_fieldtrip');

(Note: **do not** add the folder recursively; i.e. do not use addpath(genpath()))

- Run 'ft_defaults' in MATLAB.
- Confirm that FT has been successfully added to your path, for example by typing 'which ft_preprocessing' in Matlab; the correct path should be displayed.
