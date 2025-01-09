---
title: Workshop on FieldTrip, nonparametric statistics and connectivity
parent: FieldTrip courses and workshops
category: workshop
---

## Workshop on FieldTrip, nonparametric statistics and connectivity

### Where

Eberhard-Karls-University of Tübingen, Graduate Training Center of Neuroscience, Tübingen, Germany.

### When

Wednesday February 27 2013 up to Friday March 1 2013.

### Who

Paolo Belardinelli is the host and local organizer. Eelke Spaak and Jörn Horschig (Donders, Nijmegen, NL) are the main tutors. Paolo Belardinelli and Erick Ortiz will support the workshop.

### Installing FieldTrip and Tutorial preparation

For the hands-on sessions you have to start MATLAB. To ensure that
everything runs smooth, we will work with a clean and well-tested
version of FieldTrip that is distributed on a USB stcik, rather than the version you might already
have installed. Furthermore, the tutorial data does not have to be
downloaded but will also be distributed on the USB stick.

1.  Copy the complete Tübingen directory from the USB stick to your computer
2.  Unzip the fieldtrip-xxxxxxxx.zip file.
3.  Unzip the "data.zip" and "spm atlas.zip" file, you should place the contents in the tutorial directory.

{% include markup/red %}
Depending on the unzip program you are using (e.g., Winrar), the name of the zip file might also appear as directory, resulting in path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the FieldTrip directory in a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the MATLAB command window

    restoredefaultpath
    cd path_to_directory/fieldtrip-xxxxxxxx
    addpath(pwd)
    ft_defaults

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, but only when needed.
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial

### Tentative program

#### Wednesday

- morning

  - 1h intro lecture
  - 2h handson <https://www.fieldtriptoolbox.org/tutorial/sensor_analysis>

- afternoon

  - 1h beamforming lecture
  - 2h handson <https://www.fieldtriptoolbox.org/tutorial/beamformingextended>

- evening
  - dinner

#### Thursday

- morning

  - 1h connectivity lecture
  - 2h hands on <https://www.fieldtriptoolbox.org/tutorial/connectivityextended>

- afternoon

  - 1h nonparametric statistics lecture
  - 1h hands on <https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock>
  - 1h hands on <https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_freq>

- evening
  - pub?

#### Friday

- morning
  - 3h playground (working on own data)
