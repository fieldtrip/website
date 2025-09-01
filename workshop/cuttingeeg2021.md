---
title: FieldTrip tutorial at CuttingEEG 2021 in Aix-en-Provence
tags: [cuttingeeg2021]
---

- Who: Jan-Mathijs Schoffelen and Robert Oostenveld
- When: 4 October 2021
- Where: Le Cube Université Aix-Marseille (AMU) and screen sharing on zoom 889 8100 0507.
- See <https://cuttingeeg2021.org> for more details

_We will keep this page up to date and post new information here when available._

## Introduction and preparatory remarks

In this hands-on we will do a tutorial on [time-frequency analysis on short and long timescales](/workshop/cuttingeeg2021/tutorial_freq). The tutorial covers preprocessing and time-frequency analysis, and we will specifically look at how your selection of data segments, rereferencing, filtering and handling of artifacts can be optimized to get the best time-frequency estimates of the EEG and MEG activity.

If you are new to time-frequency analysis in general, we recommend you to watch the lecture on the [fundamentals of neuronal oscillations](https://youtu.be/dHTuzMsjVJA) in advance. If you are entirely new to FieldTrip, please watch the [introduction lecture](https://youtu.be/7B4rDZYwQLM). An overview of all lectures is available [here](/video).

## The data used in this tutorial

We will be using the [eeg-language](/tag/eeg-language) dataset that has been converted to BIDS. The data is available from our [download server](https://download.fieldtriptoolbox.org/workshop/cuttingeeg2021/) and is alternatively available from <https://zenodo.org/communities/cuttingeeg>.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5531370.svg)](https://doi.org/10.5281/zenodo.5531370)

The conversion of the 5 pilot subjects' EEG data to BIDS is fully documented on [this page](/workshop/cuttingeeg2021/bids_language). You don't have to run that code, but you can use it as inspiration for organizing your own data in the [BIDS format](/example/other/bids), or use it to convert the full dataset that is available from the [archive of the MPI for Psycholinguistics](https://hdl.handle.net/1839/00-0000-0000-001B-860D-8).

The "minimal" dataset (~260MB) contains one subject and is enough to run the tutorial. The "pilot" dataset (~1.7GB) contains all 5 subjects used for the pilot analysis in the original paper; you can use that if you want to explore other subjects with this tutorial.

## Getting started with the hands-on session

{% include markup/red %}
Please download and unzip a recent version of FieldTrip from <https://github.com/fieldtrip/fieldtrip/releases>. We will be using some cutting edge features in FieldTrip, so you should download and install release [20210928](https://github.com/fieldtrip/fieldtrip/releases/tag/20210928) or later.
{% include markup/end %}

To get going, you need to start MATLAB. Then, you need to issue the following commands:

    restoredefaultpath
    cd <your_fieldtrip_location>
    addpath(pwd)
    ft_defaults

The `<your_fieldtrip_location>` is the directory in which all the code is after you have unzipped the downloaded folder.

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the `startup.m` file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed. See also this [frequently asked question](/faq/matlab/installation).
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check that you are in the correct directory.

After installing FieldTrip to your path, you need to change into the hands-on specific directory, containing the data that is necessary to run the hands-on session.
