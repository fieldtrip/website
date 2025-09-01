---
title: FieldTrip workshop in Barcelona
---

The workshop is hosted by the Sociedad Española de Psicofisiología y Neurociencia cognitiva y afectiva (SEPNECA).

{% include image src="/assets/img/workshop/barcelona/campus_mundet.jpg" width="250" %}

#### Where

In the Aula Master of the Llevant Building, at the Campus Mundet, near the Faculty of Psychology ([google maps](https://www.google.nl/maps/place/Edifici+Llevant,+08035+Barcelona,+Spanje/@41.4386094,2.1445684,18z/data=!3m1!4b1!4m5!1m2!2m1!1scampus+in+de+buurt+van+Mundet,+Barcelona,+Spanje!3m1!1s0x12a497e1d3cabe79/0x4383b1771095ab74)).

#### When

July 9th ­‐ 10th 2015

#### Who

Diego Lozano-Soldevilla and Robert Oostenveld will be lecturing and tutoring. Josep Marco-Pallares is the host and local organiser.

## Program

### Thursday July 9th

Session I

- 9:00 – 9:30 Registration, coffee, opening remarks
- 9:30 – 10:30 Lecture: An introduction to the MEG and the FieldTrip toolbox
- 10:30 – 10:45 Coffee Break
- 10:45 – 12:30 Hands-on: [Getting started with event-related fields](/tutorial/sensor/eventrelatedaveraging)

- 12:30 – 13:45 Lunch

  Session II

- 13:45 – 14:45 Lecture: Fundamentals of neuronal oscillations and synchrony
- 14:45 – 15:00 Coffee Break
- 15:00 – 17:00 Hands-on: [Time-frequency analysis of power](/tutorial/sensor/timefrequencyanalysis)
- 17:00 – 17:30 Wrap-up-the-day: “Ask the experts” session

- 21:00 – ... Social get-together

### Friday July 10th

Session III

- 9:00 – 10:00 Lecture: Forward and inverse models
- 10:00 – 10:15 Coffee break
- 10:15 – 12:00 Hands-on: [Identifying oscillatory sources using beamformers](/tutorial/source/beamformer)
- 12:00 – 13:15 Lunch

Session IV

- 13:15 – 14:15 Lecture: Non-parametric statistical techniques
- 14:15 – 14:30 Coffee break
- 14:30 – 16:30 Hands-on: [Cluster-based permutation tests: intro](/tutorial/stats/cluster_permutation_timelock) and [Cluster-based permutation tests: advanced](/tutorial/stats/cluster_permutation_freq)
- 16:30 – 17:00 Wrap-up-the-day: “Ask the experts” session.

- Handing in of evaluation forms
- Handing out certificates

## Getting started with the hands-on sessions

For the hands-on sessions you have to start MATLAB. To ensure that everything runs smooth, we will work with a clean and well-tested version of FieldTrip that is distributed on a USB stick, rather than the version you might already have installed. (If you have a FieldTrip version dating from sometime in the last few weeks, that should be fine.) Importantly, the tutorial data does not have to be downloaded but will also be distributed on the USB stick.

1.  Copy the complete contents of the USB stick to your computer.
2.  Unzip the fieldtrip-xxxxxxxx.zip file.
3.  Put Subject01.zip in a directory called 'tutorial'.

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

The `restoredefaultpath` command clears your path, keeping only the
official MATLAB toolboxes. The `addpath(pwd)` statement adds the
present working directory, i.e. the directory containing the fieldtrip
main functions. The `ft_defaults` command ensures that all required
subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial
