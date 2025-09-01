---
title: ECoG/sEEG FieldTrip bootcamp at UC Davis
tags: [davis2019]
---

We're hosting the first ECoG/sEEG FieldTrip bootcamp at the UC Davis
Medical Center (Sacramento, California) on March 20-22. The workshop
will consist of lectures and hands-on sessions covering the methods
implemented in FieldTrip. Speakers include Robert Oostenveld (Donders
Institute), Arjen Stolk (UC Berkeley, Donders), Bob Knight (UC Berkeley),
and Fady Girgis (UC Davis). For more information, including how to register, please
visit the [bootcamp website](https://saez.faculty.ucdavis.edu/fieldtrip-bootcamp/).

EEG/MEG data for the hands-on sessions are available [here](https://download.fieldtriptoolbox.org/workshop/davis2019/).

iEEG data for the hands-on sessions are available [here](https://doi.org/10.5281/zenodo.1201559).

## Planning for the playground session

Please share some details on your data for planning the playground session via [this form](https://goo.gl/forms/7OThPe2b6oWp00D63).

Please see the [playground notes](https://docs.google.com/document/d/1bvzi8gv1WUHME41Rw2e5vofUy7s0NNY5cEb-4Vm2nNE/edit?usp=sharing) with  pointers to relevant documentation and functions. This page can be updated as we go along with the playground session.

## Wednesday March 20th 2019

### Session I

- 8:15 – 9:00 Registration, welcome and coffee
- 9:00 – 9:15 Welcome and opening remarks (Ignacio Saez)
- 9:15 – 10:15 Lecture I: Introduction to the FieldTrip Toolbox (Robert Oostenveld)
- 10:15 – 10:30 Coffee break
- 10:30 – 12:30 Hands-on I: [Trial selection](/tutorial/preproc/preprocessing) & [Preprocessing](/tutorial/sensor/preprocessing_erp)

### Session II

- 13:45 – 14:45 Lecture II: Clinical aspects of intracranial recordings (Fady Girgis)
- 14:45 – 15:45 Lecture III: Fundamentals of neuronal oscillations and synchrony (Arjen Stolk)
- 15:45 – 16:00 Coffee break
- 16:00 – 18:00 Hands-on II: [Time-frequency analysis](/tutorial/sensor/timefrequencyanalysis)
- 18:00 – 18:30 Wrap-up-the-day and Summary

## Thursday March 21st 2019

### Session III

- 9:00 – 10:15 Lecture IV: [Anatomical reconstruction of intracranial data (Arjen Stolk)](https://youtu.be/NdIqUSPPAeM)
- 10:15 – 10:30 Coffee break
- 10:30 – 12:30 Hands-on III: [Analysis of human ECoG and SEEG](/tutorial/intracranial/human_ecog)

### Session IV

- 13:45 – 14:45 Lecture V: Insights into Human Cognition from Intracranial Recordings (Robert T. Knight)
- 14:45 – 15:45 Lecture VI: Connectivity analysis (Robert Oostenveld)
- 15:45 – 16:00 Coffee break
- 16:00 – 17:00 Hands-on IV: [Coherence analysis](/tutorial/connectivity/coherence)
- 17:00 – 18:30 Lecture VII: Statistical testing/methods (Robert Oostenveld & Arjen Stolk)

## Friday March 22nd 2019

### Session V

- 9:00 – 10:15 FieldTrip Playground (bring your own data)
- 10:15 – 10:30 Coffee break
- 10:30 – 12:30 FieldTrip Playground (bring your own data)
- 12:30 - 13:45 Wrap-up-the-day and Closing remarks

## Getting started with the hands-on sessions

To ensure that everything runs smooth, please use a recent version of FieldTrip. To get going, you need to start MATLAB. Then, you need to issue the following command

    restoredefaultpath
    cd C:\your_fieldtrip_location
    addpath(pwd)
    ft_defaults

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed. See also this [frequently asked question](/faq/matlab/installation).
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check that you are in the correct directory.

After installing FieldTrip to your path, you need to change into the hands-on specific directory, containing the data that is necessary to run the specific hands-on session.
