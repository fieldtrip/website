---
title: FieldTrip workshop in Hamburg in 2013
---

# FieldTrip workshop in Hamburg in 2013

## When

Wednesday 11 to Friday 13 September 2013.

## Where

Dept. of Neurophysiology and Pathophysiology
University Medical Center Hamburg-Eppendorf
Martinistrasse 52, D - 20246 Hamburg, Germany

N55,Campus Lehre,room 210/11

## Program

### Wednesday 11 September (day 1)

- Lecture 1: Introduction into FieldTrip - Laura
- Coffee break
- Lecture 2: Generation and propagation of signals - Guido
- Lunch break
- Hands-on 1: [data preprocessing and artifact detection](/tutorial/eventrelatedaveraging) (data provided, see below)
- Tea break
- Hands-on 2: processing own data, event-related potentials (own data)
- Wrap-up of the day

_The first hands-on can be skipped by people that already have been using FieldTrip. It is meant to get everyone at the same level and to make sure that everyone is comfortable with processing their own data._

### Thursday 12 September (day 2)

- Lecture 3: Frequency analysis - Jan-Mathijs
- Coffee break
- Hands-on 3: [Frequency and time-frequency analysis](/tutorial/timefrequencyanalysis) (own data)
- Lunch break
- Lecture 4: Inverse modeling of EEG and MEG - Robert
- Tea break
- Hands-on 4: [Beamforming](/tutorial/beamformer) and [Minimum-norm estimation](/tutorial/minimumnormestimate) (own data, bring the MRI)
- Wrap-up of the day

_We will use the online tutorials on the website, but in principle you will be working on your own data._

### Friday 13 September (day 3)

- Lecture 5: Connectivity analysis - Jan-Mathijs
- Coffee break
- Hands-on 5: Connectivity and network analysis
- Lunch break
- Lecture: Non-parametric statistics
- Tea break
- Hands-on: Experimental design and statistics
- Wrap-up of the day

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
