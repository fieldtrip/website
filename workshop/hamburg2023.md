---
title: FieldTrip workshop in Hamburg in 2023
---

# FieldTrip workshop in Hamburg 2023

The research training group [Emotional Learning and Memory](https://www.grk2753.uni-hamburg.de/) GRK/RTG 2753 organizes a FieldTrip workshop at the University of Hamburg, Germany.

## Where

The workshop will take place at the Department of Cognitive Psychology, University of Hamburg Von-Melle-Park 5.

## Who

Tzvetan Popov with local organizers.

## When

From 8 to 10 November 2023.

## Program

### Day 1 - 8.11.2023

**Session I**

- **09:00 – 09:15** Registration and welcome
- **09:15 – 10:15** Lecture: Introduction to EEG and the FieldTrip Toolbox
- **10:15 – 10:30** Coffee break
- **10:30 – 12:30** Hands-on: [Initiation to FieldTrip; Analyzing EEG data (event-related potentials)](https://www.notion.so/9b48e6f48d824aa488b7cea8084a827c?pvs=21)

**Session II**

- **12:30 – 13:30** Lunch
- **13:30 – 14:30** Lecture: Fundamentals of neuronal oscillations and synchrony

### Day 2- 9.11.2023

**Session III**

- **9:00 – 10:45** Hands-on: [Time-frequency Analysis of Power](https://www.notion.so/9b48e6f48d824aa488b7cea8084a827c?pvs=21)
- **10:45 – 11:00** Coffee break
- **11:00 – 12:30** Lecture: Non-parametric permutation techniques
- **12:30 – 13:30** Lunch

**Session IV**

- **13:30 – 14:45** Hands-On: [Statistical Analyses](https://www.notion.so/9b48e6f48d824aa488b7cea8084a827c?pvs=21)
- **14:45 – 15:00** Coffee break
- **15:00 – 16:30** Hands-On: [Statistical Analyses- MVPA and decoding](https://www.notion.so/9b48e6f48d824aa488b7cea8084a827c?pvs=21)
- **16:30 – 17:00** Wrap-up-the-day and Summary

### Day 3 - 10.11.2023

**Session V**

- **9:00 – 10:30** Lecture: Source reconstruction in FieldTrip
- **10:30 – 10:45** Coffee break
- **10:45 – 12:30** Hands-on: [Source Reconstruction on oscillatory data (beamformer)](https://www.notion.so/9b48e6f48d824aa488b7cea8084a827c?pvs=21)
- **12:30 – 13:30** Lunch

**Session VI**

- **13:30 – 15:30** FieldTrip Playground (bring your own data)
- **15:30 – 15:45** Coffee break
- **15:45 – 16:30** FieldTrip Playground continued
- **16:30 – 17:00** Wrap-up-the-day and Closing remarks

## Getting started with the hands-on sessions

For the hands-on sessions you have to start MATLAB. Make sure you
have downloaded the hands-on data prior to the start of the workshop as
it is quite a large download. A recent version of FieldTrip can be
downloaded [here](https://www.fieldtriptoolbox.org/download/), and the
tutorial data can be downloaded here.

Depending on the unzip program you are using (e.g., Winrar), the
name of the zip file might also appear as directory, resulting in
path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the
FieldTrip directory in a FieldTrip directory. Please fix that by moving
all files one level up.

After copying all files to your computer and unzipping then, you
start MATLAB. To ensure that the right version of FieldTrip is used, and
 not another version (such as the one included in SPM or EEGLAB), you
type in the MATLAB command window

```matlab
restoredefaultpath
cd path_to_directory/fieldtrip-xxxxxxxx
addpath(pwd)
ft_defaults
```

Please do NOT use the graphical path management tool from MATLAB.
In this hands-on session we’ll manage the path from the command line,
but in general you are much better off using a startup.m file than the
path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories
 will be added automatically when needed, but only when needed.

The `restoredefaultpath` command clears your path, keeping only the
official MATLAB toolboxes. The `addpath(pwd)` statement adds the
present working directory, i.e. the directory containing the fieldtrip
main functions. The `ft_defaults` command ensures that all required
subdirectories are added to the path.

If you get the error “can’t find the command ft_defaults” you should
check the present working directory.

After installing FieldTrip to your path, you change into the data directory

```matlab
cd path_to_directory/data
```
