---
title: FieldTrip workshop in Kiel, Germany
---

# FieldTrip workshop in Kiel, Germany

We will keep this page up to date and post new information here when available.

- Instructor: Cristiano Micheli
- When: 25-27 April 2016
- Where: Kiel, Germany

#### Monday April 25th

- Session I

  - 10:00 – 11:00 Lecture: Beamformer techniques for source reconstruction
  - 11:00 – 11:15 Coffee break
  - 11:15 – 13:00 Hands-on: Identifying oscillatory sources using beamformer techniques
    _ <https://www.fieldtriptoolbox.org/tutorial/headmodel_eeg_bem>
    _ <https://www.fieldtriptoolbox.org/tutorial/beamformer>
  - 13:00 – 14:00 Lunch

- Session II

  - 14:00 – 15:15 Lecture: Non-parametric randomization techniques
  - 15:15 – 15:30 Coffee break
  - 15:30 – 17:15 Hands-on: Parametric and non-parametric statistics on event-related fields
    _ <https://www.fieldtriptoolbox.org/tutorial/eventrelatedstatistics>
    _ <https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_freq>
  - 17:15 – 18:00 Wrap-up-the-day: “Ask the expert” session

- Evening : ... social activity

#### Tuesday April 26th

- Session III

  - 10:00 – 11:00 Lecture: Connectivity analysis
  - 11:00 – 11:15 Coffee break
  - 11:15 – 13:00 Hands-on: Analysis of sensor- and source-level connectivity \* <https://www.fieldtriptoolbox.org/tutorial/connectivityextended>
  - 13:00 – 14:00 Lunch

- Session IV

  - 14:00 – 15:15 Hands-on: Virtual sensors' connectivity \* <https://www.fieldtriptoolbox.org/workshop/meg-uk-2015/fieldtrip-beamformer-demo>
  - 15:15 – 15:30 Coffee break
  - 15:30 – 17:15 Hands-on: Whole brain network and connectivity analysis \* <https://www.fieldtriptoolbox.org/tutorial/networkanalysis>
  - 17:15 – 18:00 Wrap-up-the-day: “Ask the expert” session

  - Evening : ... social activity

#### Wednesday April 27th

- Session V
  - 10:00 – 13:00 FieldTrip playground

## Getting started with the hands-on sessions

For the hands-on sessions you have to start MATLAB. To ensure that everything runs smooth, we will work with a clean and well-tested version of FieldTrip that we have installed on all computers and that we will bring on on a USB stick. Importantly, the tutorial data does not have to be downloaded but will also be distributed on the computers and available on the USB stick.

If you work on your own lapto

1.  Copy the complete contents of the USB stick to your computer.
2.  Unzip the fieldtrip-xxxxxxxx.zip file.
3.  Put Subject01.zip in a directory called 'tutorial'.

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

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/installation)).
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the
official MATLAB toolboxes. The `addpath(pwd)` statement adds the
present working directory, i.e. the directory containing the fieldtrip
main functions. The `ft_defaults` command ensures that all required
subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial
