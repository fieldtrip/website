---
title: FieldTrip Workshop in Guangzhou, China
---

- Who: Diego Lozano-Soldevilla
- When: August 23rd-25th 2016
- Where: South China Normal University, Guangzhou

REGISTRATION CLOSED: NO PLACES AVAILABLE

## Program

### Tuesday August 23rd

- Session I

  - 9:45 Registration, coffee, opening remarks
  - 10:05 – 11:00 Lecture: Introduction to EEG (vs MEG) and the FieldTrip toolbox
  - 11:00 – 11:15 Coffee Break
  - 11:15 – 12:45 Hands-on: Preprocessing EEG and event-related averaging, design your own sensory ECoG electrode montage
    - <https://www.fieldtriptoolbox.org/tutorial/preprocessing_erp>
    - <https://www.fieldtriptoolbox.org/tutorial/layout>
  - 12:45 – 13:45 Lunch

- Session II

  - 13:45 – 14:45 Lecture: Fundamentals of neuronal oscillations and synchrony
  - 14:45 – 15:00 Coffee Break
  - 15:00 – 16:45 Hands-on: Time-frequency analysis of power
    - <https://www.fieldtriptoolbox.org/tutorial/timefrequencyanalysis>
  - 16:45 – 17:30 Wrap-up-the-day: “Ask the experts” session

- dinner (not included, i.e. on own costs)

### Wednesday August 24th

- Session III

  - 10:00 – 11:00 Lecture: Connectivity analysis on sensor data
  - 11:00 – 11:15 Coffee break
  - 11:15 – 13:00 Hands-on: Connectivity analysis on sensor data
    - <https://www.fieldtriptoolbox.org/tutorial/connectivity>
  - 13:00 – 14:00 Lunch

- Session IV
  - 14:00 – 15:15 Lecture: Non-parametric randomization techniques
  - 15:15 – 15:30 Coffee break
  - 15:30 – 17:15 Hands-on: Parametric and non-parametric statistics on sensor data
    - <https://www.fieldtriptoolbox.org/tutorial/eventrelatedstatistics>
    - <https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_freq>
  - 17:15 – 18:00 Wrap-up-the-day: “Ask the experts” session

### Thursday August 25th

- Session V
  - 10:00 – 13:00 FieldTrip playground: bring your own data
    - <https://www.fieldtriptoolbox.org/tutorial/monkey_ecog>
  - Wrap up of the workshop

## Installing FieldTrip and Tutorial preparation

For the hands-on sessions you have to start MATLAB. To ensure that everything runs smooth, we will work with a clean and well-tested version of FieldTrip that you can download [here](https://download.fieldtriptoolbox.org/fieldtrip-20160818.zip). Importantly, the tutorial data does not have to be
downloaded but we strongly recommend to download before the workshop by clicking at this [link](https://www.dropbox.com/s/0sqv44taxhjbsqk/data_tutorials.rar?dl=0).

1.  Copy the complete contents of the USB stick to your computer.
2.  Unzip the fieldtrip-20160818.zip file.
3.  Put all the data files in a directory called 'tutorial' (or something else you'll remember).

{% include markup/red %}
Depending on the unzip program you are using (e.g., Winrar), the name of the zip file might also appear as directory, resulting in path_to_directory/fieldtrip-20160818/fieldtrip-20160818, i.e. the FieldTrip directory inside a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the MATLAB command window

    restoredefaultpath
    cd path_to_directory/fieldtrip-20160818
    addpath(pwd)
    ft_defaults

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed.
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial
