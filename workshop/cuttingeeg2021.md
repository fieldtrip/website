---
title: FieldTrip tutorial at CuttingEEG 2021 in Aix-en-Provence
tags: [cuttingeeg2021]
---

# FieldTrip tutorial at CuttingEEG 2021 in Aix-en-Provence

- Who: Jan-Mathijs Schoffelen and Robert Oostenveld
- When: 4 October 2021
- Where: Le Cube Université Aix-Marseille (AMU)
- See <https://cuttingeeg2021.org> for more details

_We will keep this page up to date and post new information here when available._

## Introduction and preparatory remarks

In this hands-on session we will go over preprocessing and time-frequency analysis, and specifically look at how your selection of data segments, rereferencing, filtering and handling of artifacts can be optimized to get the best time-frequency estimates of the EEG and MEG activity. If you are entirely new to time-frequency analysis in general, we recommend you to watch one of our [youtube lectures](<https://youtu.be/dHTuzMsjVJA>) in advance.

## The data used in this tutorial

To be decided, the data will be shared on <https://zenodo.org/communities/cuttingeeg>.

## Getting started with the hands-on session

To ensure that everything runs smoothly, please download and unzip a recent version of FieldTrip from <https://github.com/fieldtrip/fieldtrip/releases>. We made some last minute changes for a smooth user experience so you should pick a copy that is as young as (or younger than) 20210927. To get going, you need to start MATLAB. Then, you need to issue the following commands:

    restoredefaultpath
    cd <your_fieldtrip_location>
    addpath(pwd)
    ft_defaults

The `<your_fieldtrip_location>` is the directory in which all the code is after you have unzipped the downloaded folder. 

{% include markup/danger %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed. See also this [frequently asked question](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path).
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check that you are in the correct directory.

After installing FieldTrip to your path, you need to change into the hands-on specific directory, containing the data that is necessary to run the hands-on session.

The actual tutorial can be found on <https://www.fieldtriptoolbox.org/workshop/cuttingeeg2021/tutorial_freq/>
