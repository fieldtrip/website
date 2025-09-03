---
title: FieldTrip Workshop in Tübingen, Germany
---

- Workshop leaders: Britta Westner and Tzvetan Popov
- When: 13-14 October 2016
- Where: University of Tübingen, Germany

We will keep this page up to date and post new information here when available.

## Schedule

### Day 1 (Thursday 13 October, 2016)

- 09:00 - 09:30 Registration, welcome and coffee
- 09:30 - 10:45 Lecture 1: Fundamentals of neuronal oscillations and synchrony (**Britta Westner**)
- 11:00 - 12:45 Hands-on 1:
  - [Time-frequency analysis of power](/tutorial/sensor/timefrequencyanalysis)
- 12:45 - 13:00 Lunch
- 13:30 - 15:00 Lecture 2: Statistics using non-parametric randomization techniques (**Tzvetan Popov**)
- 15:00 - 15:15 Coffee Break
- 15:15 - 16:15 Hands-on 2:

  - [Cluster-based permutation tests on event-related fields](/tutorial/stats/cluster_permutation_timelock) and/or
  - [Cluster-based permutation tests on time-frequency data](/tutorial/stats/cluster_permutation_freq)

- 16:30 - 17:00 Wrap-up-the-day: special topics, general questions and answers
- 19:00 - 21:30 Dinner: **tba** (not included in registration)

### Day 2 (Friday 14 October, 2016)

- 9:00 - 10:30 Lecture 3: Source reconstruction using beamformers (**Britta Westner**)
- 10:30 - 10:45 Coffee break
- 10:35 - 12:15 Hands-on 3:
  - [Identifying oscillatory sources using beamformers ](/tutorial/source/beamformer)
- 12:15 - 13:00 Lunch
- 13:00 - 14:30 Hands-on 4:
  - [Source level statistics within the permutation framework](/workshop/aarhus2015/beamformingerf#meg_plotting_sources_of_response_related_evoked_field_using_statistical_threshold)
- 14:30 - 14:45 Coffee break
- 14:45 - 17:00 FieldTrip playground (bring your own data!)
- 17:00 - 17:30 Wrap up the event, questions and answers!

## Tutorial preparation

To prepare for the hands-on sessions, you should watch the following online videos prior to the workshop. Note that these lectures are about one hour each, which means that you should **plan ahead and take your time** to go through them. It is your own responsibility to come well-prepared. Starting one day in advance will not cut it!

- [MEG instrumentation (video)](https://www.youtube.com/watch?v=15Qs4fuPpes)
- [FieldTrip intro (video and hands-on)](/tutorial/intro/introduction)

## Installing FieldTrip and Tutorial preparation

For the hands-on sessions you have to start MATLAB. To ensure that
everything runs smooth, we will work with a clean and well-tested
version of fieldtrip. The tutorial data together with the FieldTrip version can be downloaded [here](https://depot.uni-konstanz.de/cgi-bin/exchange.pl?g=s38xv3f76w)).

1.  Unzip the FieldTrip-Tutorial-Tübingen.zip file.
2.  Unzip the fieldtrip-master.zip file.
3.  Put all the data files in a directory called 'tutorial' (or something else you'll remember).

{% include markup/red %}
Depending on the unzip program you are using (e.g., Winrar), the name of the zip file might also appear as directory, resulting in path_to_directory/fieldtrip-master/fieldtrip-master, i.e. the FieldTrip directory in a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the MATLAB command window

    restoredefaultpath
    cd path_to_directory/fieldtrip-master
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
