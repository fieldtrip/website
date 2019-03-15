---
title: ECoG/sEEG FieldTrip bootcamp at UC Davis
tags: [davis2019]
---

# ECoG/sEEG FieldTrip bootcamp at UC Davis

We're hosting the first ECoG/sEEG FieldTrip bootcamp at the UC Davis
Medical Center (Sacramento, California) on March 20-22. The workshop
will consist of lectures and hands-on sessions covering the methods
implemented in FieldTrip. Speakers include Robert Oostenveld (Donders
Institute), Bob Knight (UC Berkeley), and Arjen Stolk (UC Berkeley,
Donders). For more information, including how to register, please
visit the [bootcamp website](https://saez.faculty.ucdavis.edu/fieldtrip-bootcamp/).

EEG/MEG data for the hands-on sessions are available [here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/workshop/davis2019/).

iEEG data for the hands-on sessions are available [here](https://doi.org/10.5281/zenodo.1201559).

## Wednesday March 20th 2019

### Session I

- 9:00 – 9:15 Registration, welcome, and coffee
- 9:15 – 10:15 Lecture I: Introduction to the FieldTrip Toolbox (Robert Oostenveld)
- 10:15 – 10:30 Coffee break
- 10:30 – 12:30 Hands-on I: [Trial selection](/tutorial/preprocessing) & [Preprocessing](/tutorial/preprocessing_erp)

### Session II

- 13:45 – 14:45 Lecture II: Clinical aspects of intracranial recordings (Fady Girgis)
- 14:45 – 15:45 Lecture III: Fundamentals of neuronal oscillations and synchrony (Arjen Stolk)
- 15:45 – 16:00 Coffee break
- 16:00 – 18:00 Hands-on II: [Time-frequency analysis](/tutorial/timefrequencyanalysis)
- 18:00 – 18:30 Wrap-up-the-day and Summary

## Thursday March 21st 2019

### Session III

- 9:00 – 10:15 Lecture III: Anatomical reconstruction of intracranial data (Arjen Stolk)
- 10:15 – 10:30 Coffee break
- 10:30 – 12:30 Hands-on III: [Analysis of human ECoG and SEEG](/tutorial/human_ecog)

### Session IV

- 13:45 – 14:45 Lecture IV: Insights into Human Cognition from Intracranial Recordings (Robert T. Knight)
- 14:45 – 15:45 Lecture V: Connectivity analysis (Robert Oostenveld)
- 15:45 – 16:00 Coffee break
- 16:00 – 17:00 Hands-on IV: [Coherence analysis](/tutorial/coherence)
- 17:00 – 18:30 Lecture VI: Statistical testing/methods (Robert Oostenveld & Arjen Stolk)

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

{% include markup/danger %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed. See also this [frequently asked question](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path).
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check that you are in the correct directory.

After installing FieldTrip to your path, you need to change into the hands-on specific directory, containing the data that is necessary to run the specific hands-on session.
