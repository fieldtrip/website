---
title: Workshop on analyzing intracranial data - spikes and fields
---

# Workshop on analyzing intracranial data: spikes and fields

## Where

York University, Toronto, Canada.

## When

Saturday 9 March 2013 up to Monday 11 March 2013.

## Who

Thilo Womelsdorf is the host and local organizer. Robert Oostenveld (Donders, Nijmegen, NL) and Martin Vinck (SILS, Amsterdam, NL) are the main tutors.

## Program

### Saturday

- morning

  - 1h lecture - Introduction to FieldTrip and LFP/EEG analysis (Robert Oostenveld)
  - 2h handson <https://www.fieldtriptoolbox.org/tutorial/eventrelatedaveraging>

- afternoon

  - 1h lecture - Spike, and Spike-LFP Analysis (Martin Vinck)
  - 1h handson <https://www.fieldtriptoolbox.org/tutorial/spike>
  - 1h people work on own data with ERFs and/or spikes

- evening - special interest lectures on decoding methods
  - Use of entropy and mutual information measures for neuroscience applications (Martin)
  - A hands-on introduction to Bayesian decoding of multiple spike train data (Matthijs van der Meer; e-mail to get the data)
  - open discussion

### Sunday

- morning

  - 1h lecture - Frequency analysis of power and coherence (Robert)
  - 2h handson <https://www.fieldtriptoolbox.org/tutorial/timefrequencyanalysis>

- afternoon

  - 1h lecture - Connectivity analysis (Martin)
  - 1h handson <https://www.fieldtriptoolbox.org/tutorial/spikefield>
  - 1h handson <https://www.fieldtriptoolbox.org/tutorial/connectivity>

- evening
  - short project presentations from participants

### Monday

- morning
  - 1h lecture - Randomization and Cluster statistics (Robert)
  - 2h people work on own data on laptops

## Preparing for the hands-on sessions

Please copy the data and the FieldTrip version that we will use from <http://storage.aml.yorku.ca>. This will take some time.

For the hands-on sessions you have to start MATLAB. To ensure that
everything runs smooth, we will work with a **clean and well-tested**
version of FieldTrip that is distributed on the workstations and on a USB stick. You should **not** work with an old version you might already have installed in the past. Furthermore, the tutorial data **does not have to be downloaded** but will also be distributed on the workstations and on a USB stick.

If you work on your own laptop you need the USB stick:

1.  Copy the complete content from the USB stick to your computer
2.  Unzip the fieldtrip-xxxxxxxx.zip file.
3.  Unzip the Subject01.zip file, you should place the contents in the tutorial directory.

{% include markup/danger %}
Depending on the unzip program you are using (e.g., Winrar), the name of the zip file might also appear as directory, resulting in path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the FieldTrip directory in a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the **MATLAB command window**

    restoredefaultpath
    cd path_to_directory/fieldtrip-xxxxxxxx
    ls
    addpath(pwd)
    ft_defaults

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes.

The ls statement shows the list of files in the present directory, and you can visually check that the contents are correct and for example not in another subfolder. You should see a long list of ft_xxx.m functions.

The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

{% include markup/danger %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, but only when needed.
{% include markup/end %}

After installing FieldTrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial

In general the tutorials start by reading the raw data from "Subject01.ds", which is a data directory. You should **not** go into the Subject01.ds directory, but stay at the level of the tutorial directory. If a specific tutorial instructs you to load data (and if you want the skip the step just prior to that because of time limitations), you should go into the tutorial data directory.
