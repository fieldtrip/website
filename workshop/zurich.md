---
title: FieldTrip workshop in Zürich
---

- Where: Department of Psychology, University Zürich
- When: 24-26 February, 2014
- Who: Eelke Spaak and Jörn Horschig, the local organizers are Maj-Britt Niemi and Alexandra Buender

### Installing FieldTrip and Tutorial preparation

For the hands-on sessions you have to start MATLAB. To ensure that everything runs smooth, we will work with a clean and well-tested version of FieldTrip that is distributed on a USB stick, rather than the version you might already have installed. (If you have a FieldTrip version dating from sometime in the last few weeks, that should be fine.) Importantly, the tutorial data does not have to be downloaded but will also be distributed on the USB stick.

1.  Copy the complete contents of the USB stick to your computer.
2.  Unzip the fieldtrip-xxxxxxxx.zip file.
3.  Put all the data files in a directory called 'tutorial' (or something else you'll remember).

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

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed.
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial

### Program

#### Monday

- morning

  - 1h intro lecture [ppt](https://db.tt/wNf4lyNH)
  - 2h hands-on <https://www.fieldtriptoolbox.org/tutorial/eventrelatedaveraging>

- afternoon

  - 1h oscillations lecture [ppt](https://db.tt/IRxD9rDb)
  - 2h handson <https://www.fieldtriptoolbox.org/tutorial/timefrequencyanalysis>

- evening
  - pub

#### Tuesday

- morning

  - 1h beamforming lecture [ppt](https://db.tt/kR4N2pSp)
  - 2h hands on <https://www.fieldtriptoolbox.org/tutorial/beamformer>

- afternoon

  - 1h nonparametric statistics lecture [ppt](https://db.tt/x9E0jmDG)
  - 1h hands on <https://www.fieldtriptoolbox.org/tutorial/eventrelatedstatistics>
  - 1h hands on <https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_freq>

- evening
  - dinner <http://goo.gl/maps/IM6yX>

#### Wednesday

- morning
  - 3h playground (working on own data), [ft_trialfun_brainvision_segmented](https://db.tt/rn7mS2Lu)
