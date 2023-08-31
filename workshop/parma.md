---
title: FieldTrip workshop in Parma
---

# FieldTrip workshop in Parma

#### Where

Dipartimento di Neuroscienze - Sezione di Fisiologia, Universitá degli Studi di Parm
Via Volturno 39, Parma, Italia

#### When

April 28-30 2014

#### Who

Diego Lozano-Soldevilla and Arjen Stolk will be lecturing and tutoring.
Sebo Uithol is the host and local organizer

## Tentative Program

#### Monday April 28

- Session I

  - 9:45 Registration, coffee, opening remarks
  - 10:05 - 11:00 Lecture: An introduction to the MEG and the FieldTrip toolbox
  - 11:00 - 11:15 Coffee Break
  - 11:15 - 12:45 Hands-on: Getting started with event-related fields
    - <https://www.fieldtriptoolbox.org/tutorial/eventrelatedaveraging>
  - 12:45 - 13:45 Lunch

- Session II
  - 13:45 - 14:45 Lecture: Fundamentals of neuronal oscillations and synchrony
  - 14:45 - 15:00 Coffee Break
  - 15:00 - 16:45 Hands-on: Time-frequency analysis of power
    - <https://www.fieldtriptoolbox.org/tutorial/timefrequencyanalysis>
  - 16:45 - 17:30 Wrap-up-the-day: Ask the experts session

#### Tuesday April 29

- Session III

  - 10:00 - 11:00 Lecture: Beamformer techniques for source reconstruction
  - 11:00 - 11:15 Coffee break
  - 11:15 - 13:00 Hands-on: Identifying oscillatory sources using beamformer techniques
    - <https://www.fieldtriptoolbox.org/tutorial/beamformer>
  - 13:00 - 14:00 Lunch

- Session IV

  - 14:00 - 15:15 Lecture: Non-parametric randomization techniques
  - 15:15 - 15:30 Coffee break
  - 15:30 - 17:15 Hands-on: Parametric and non-parametric statistics on event-related fields
    - <https://www.fieldtriptoolbox.org/tutorial/eventrelatedstatistics>
    - <https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_freq>
  - 17:15 - 18:00 Wrap-up-the-day: Ask the experts session

  - 20:00 Workshop Dinner @ ???

#### Wednesday April 30

- Session V
  - 10:00 - 13:00 FieldTrip playground

## Installing FieldTrip and Tutorial preparation

For the hands-on sessions you have to start MATLAB. To ensure that
everything runs smooth, we will work with a clean and well-tested
version of FieldTrip that is distributed on a USB stick, rather than the version you might already
have installed. (If you have a FieldTrip version dating from sometime in the last few weeks, that should be fine.) Importantly, the tutorial data does not have to be
downloaded but will also be distributed on the USB stick.

1.  Copy the complete contents of the USB stick to your computer.
2.  Unzip the fieldtrip-xxxxxxxx.zip file.
3.  Put all the data files in a directory called 'tutorial' (or something else you'll remember).

{% include markup/danger %}
Depending on the unzip program you are using (e.g., Winrar), the name of the zip file might also appear as directory, resulting in path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the FieldTrip directory in a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the MATLAB command window

    restoredefaultpath
    cd path_to_directory/fieldtrip-xxxxxxxx
    addpath(pwd)
    ft_defaults

{% include markup/danger %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed.
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial
