---
title: FieldTrip workshop in Göttingen in 2014
---

# FieldTrip workshop in Göttingen in 2014

## Where

Room 2.122
Georg-Elias-Müller-Institut für Psychologie
Gosslerstrasse 14
D-37073 Göttingen

## When

February 8-9, 2014

## Who

Lilla Magyari and Nietzsche Lam

The local organizers are Danai Theodosopoulou and Carsten Schmidt

## Course program

_Saturday 8th February_

### Session I

- 10:00 - 10:15 Registration, welcome, opening remarks
- 10:15 - 11:15 Lecture: An introduction to the MEG/EEG and the FieldTrip toolbox
- 11:15 - 11:30 Coffee Break
- 11:30 - 13:30 Hands-on: Initiation to FieldTrip & getting started with EEG data (preprocessing, ERP)
- 13:30 - 14:45 Lunch

### Session II

- 14:45 - 15:45 Lecture: Fundamentals of neuronal oscillations and synchrony
- 15:45 - 16:00 Coffee Break
- 16:00 - 18:00 Hands-on: Time-frequency analysis of power
- 18:00 - 18:30 Wrap-up-the-day and Summary

_Sunday 9th February_

### Session III

- 9:00 - 10:15 Lecture: Non-parametric permutation techniques
- 10:15 - 10:30 Coffee break
- 10:30 - 12:30 Hands-on: Statistical Analyses
- 12:30 - 13:45 Lunch

### Session IV

- 13:45 - 14:45 Lecture: Source reconstruction in FieldTrip
- 14:45 - 15:00 Coffee break
- 15:00 - 17:00 FieldTrip Playground (bring your own data)
- 17:00 - 17:30 Wrap-up-the-day and Summary

## Installing FieldTrip and preparing for the hands-on sessions

For the hands-on sessions you have to start MATLAB. To ensure that
everything runs smooth, we will work with a clean and well-tested
version of FieldTrip that is distributed on a USB stick, rather than the older version you might already have installed. Furthermore, the tutorial data will also be distributed on the USB stick.

If you want to download it in advance, please go to <https://download.fieldtriptoolbox.org/> and get

- fieldtrip-20130906.zip
- Subject01.zip
- all files in the tutorial/eventrelatedaveraging directory

{% include markup/danger %}
Depending on the unzip program you are using (e.g., Winrar), the name of the zip file might also appear as directory, resulting in path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the FieldTrip directory in a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the MATLAB command window

    restoredefaultpath
    cd path_to_directory/fieldtrip-xxxxxxxx
    addpath(pwd)
    ft_defaults

{% include markup/danger %}
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
