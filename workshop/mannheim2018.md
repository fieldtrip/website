---
title: FieldTrip Workshop in Mannheim
---

# FieldTrip workshop in Mannheim

The Central Institute of Mental Health (CIMH) in Mannheim Germany will be hosting a FieldTrip Course on MEG Analysis with Tzvetan Popov and Gianpaolo Dimarchi from 10 to 12 of December 2018.

### Where

[ZI Mannheim](https://www.zi-mannheim.de/en.html)
Central Institute for Mental Health
J 5
68159 Mannheim
Germany

{% include image src="/assets/img/workshop/mannheim2018/zi-logo.png" width="304" link="https://www.zi-mannheim.de/en.html" %}

### When

Mon 10 Dec- Wed 12 Dec, 2018.

### Who

Tzvetan Popov and Gianpaolo Dimarchi.

## Program

### Monday 10 December 2018

Session I

- **10:00 - 10:15** Registration, welcome and coffee
- **10:15 - 11:15** Lecture: Introduction to MEG and the FieldTrip Toolbox _Tzvetan Popov_
- **11:15 - 11:30** Coffee break
- **11:30 - 13:30** Hands-on: Initiation to FieldTrip; Analyzing MEG data (event-related fields)

Session II

- **13:30 - 14:45** Lunch
- **14:45 - 15:45** Lecture: Fundamentals of neuronal oscillations and synchrony _Tzvetan Popov_
- **15:45 - 16:00** Coffee break
- **16:00 - 18:00** Hands-on: Time-frequency Analysis of Power
- **18:00 - 18:30** Wrap-up-the-day and Summary

### Tuesday 11 December 2018

Session III

- **9:00 - 10:15** Lecture: Non-parametric permutation techniques _Tzvetan Popov_
- **10:15- 10:30** Coffee break
- **10:30- 12:30** Hands-On: Statistical Analyses
- **12:30- 13:45** Lunch

Session IV

- **13:45 - 14:45** Lecture: Source reconstruction in FieldTrip _Tzvetan Popov_
- **14:45 - 15:00** Coffee break
- **15:00 - 17:00** Hands-on: Source Reconstruction on Oscillatory data (beamformer)
- **17:00 - 17:30** Wrap-up-the-day and Summary
- **19:00 - 23:00** Social Event

### Wednesday 12 December 2018

Session V

- **9:00 - 10:15** FieldTrip Playground (bring your own data) _Tzvetan Popov and Gianpaolo Dimarchi_
- **10:15- 10:30** Coffee break
- **10:30- 12:30** FieldTrip Playground (bring your own data)
- **12:30- 13:45** Wrap-up-the-day and Closing remarks

## Getting started with the hands-on sessions

For the hands-on sessions you have to start MATLAB. Make sure you have downloaded the hands-on data prior to the start of the workshop as it is quite a large download. All the required data and a recent version of FieldTrip can be downloaded [here](https://download.fieldtriptoolbox.org/workshop/mannheim2018/).

{% include markup/red %}
Depending on the unzip program you are using (e.g., Winrar), the name of the zip file might also appear as directory, resulting in path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the FieldTrip directory in a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the MATLAB command window

    restoredefaultpath
    cd path_to_directory/fieldtrip-xxxxxxxx
    addpath(pwd)
    ft_defaults

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using a startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, but only when needed.
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the
official MATLAB toolboxes. The `addpath(pwd)` statement adds the
present working directory, i.e. the directory containing the fieldtrip
main functions. The `ft_defaults` command ensures that all required
subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the data directory

    cd path_to_directory/data
