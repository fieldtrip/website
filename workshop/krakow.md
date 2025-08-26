---
title: FieldTrip workshop in Krakow, Poland
---

# FieldTrip workshop in Krakow, Poland

## Using the tutorial data and the FieldTrip version provided

For the hands-on sessions you have to start MATLAB. To ensure that
everything runs smooth, we will work with a **clean and well-tested**
version of FieldTrip that is distributed on a USB stcik, rather than the version you might already
have installed. Furthermore, the tutorial data **does not have to be
downloaded** but will also be distributed on the USB stick.

1.  Copy the complete Krakow directory from the USB stick to your computer
2.  Unzip the fieldtrip-xxxxxxxx.zip file.
3.  Unzip the Subject01.zip file, you should place the contents in the tutorial directory.

{% include markup/red %}
Depending on the unzip program you are using (e.g., Winrar), the name of the zip file might also appear as directory, resulting in path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the FieldTrip directory in a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the **MATLAB command window**

    restoredefaultpath
    cd path_to_directory/fieldtrip-xxxxxxxx
    ls
    addpath(pwd)
    ft_defaults

The `restoredefaultpath` command clears your path, keeping only the
official MATLAB toolboxes.

The ls statement shows the list of files in the present directory, and you can visually check that the contents are correct and for example not in another subfolder. You should see a long list of ft_xxx.m functions.

The `addpath(pwd)` statement adds the
present working directory, i.e. the directory containing the fieldtrip
main functions. The `ft_defaults` command ensures that all required
subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, but only when needed.
{% include markup/end %}

After installing FieldTrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial

In general the tutorials start by reading the raw data from
"Subject01.ds", which is a data directory. You should not go into
the Subject01.ds directory, but stay at the level of the tutorial
directory. If a specific tutorial instructs you to load data (and
if you want the skip the step just prior to that because of time
limitations), you should go into the respective tutorial subdirectory,
i.e. tutorial/eventreltedaveraging.

## Krakow specific information

The tutorials that we will use during this toolkit are

**Tuesday morning:** Please begin with [event-related averaging](/tutorial/eventrelatedaveraging) going up to and including the axial gradiometer section only. It is helpful to read [The data set used in this tutorial](/tutorial/meg_language) prior to running the tutorial. When you reach the section on planar gradiometer, switch then to this EEG example: [EEG data: reading-in trials and pre-processing](/tutorial/preprocessing_erp). For this EEG example, you will also need the BrainVision data provided on the USB sticks.

**Tuesday afternoon:** [Time-frequency analysis using Hanning window, multitapers and wavelets](/tutorial/timefrequencyanalysis)

**Wednesday morning:** [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer)

**Wednesday afternoon:** [Multivariate analysis of electrophysiological data](/tutorial/multivariateanalysis)

**Thursday, FieldTrip Playground:** If you are stuck with any .bdf specific questions, you might gain insight from the [getting started with BioSemi](/getting_started/biosemi) documentation page.
