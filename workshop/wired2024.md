---
title: FieldTrip tutorial at WIRED 2024 in Paris
tags: [wired2024]
---

Robert Oostenveld and [Marie-Constance Corsi](https://marieconstance-corsi.netlify.app) will present a hands-on tutorial at the [Workshop on Intracranial Recordings in humans, Epilepsy, DBS](https://wired-icm.org) (WIRED) at ICM in Paris from 13th to  15th of March 2024. The FieldTrip tutorial will happen in the afternoon of Wednesday 13 March.

To attend the hands-on tutorials, participants will have to register [here](https://wired-icm.org/registration/) and bring their own laptops with MATLAB installed.

## Program

We will look at the **Anatomical workflow** and the **Functional workflow** of the tutorial on the [Analysis of human ECoG and sEEG recordings](/tutorial/intracranial/human_ecog). This comprises section 2, 3, and 4 in the outline of the [Advances in human intracranial electroencephalography research, guidelines and good practices](https://doi.org/10.1016/j.neuroimage.2022.119438) paper. Section 5 on statistics and section 6 on perspectives are obviously also relevant and we will take some time to discuss these.

## How to prepare

### Get an overview of FieldTrip

Please take a quick look at the [FieldTrip reference paper](https://doi.org/10.1155/2011/156869) if you have not done so already. If you have an hour or so, you can watch this [introductory lecture](https://www.youtube.com/watch?v=7B4rDZYwQLM). Note that more recorded lectures are available as [video](/video).

### Read up on intracranial analyses

Have a look at the recent paper [Advances in human intracranial electroencephalography research, guidelines and good practices](https://doi.org/10.1016/j.neuroimage.2022.119438). It is quite a long and detailed paper, so you may not be able to read it in a single session.

### Make sure you have a recent version of MATLAB

We develop FieldTrip to be compatible with MATLAB versions up to 5 years old. Please note that we may not always be running the latest MATLAB version ourselves, so sometimes it can happen that your brand-new MATLAB release causes some issues that we have not encountered and fixed yet.

### Download and install a recent FieldTrip version

{% include markup/skyblue %}
Please download and unzip a recent version of FieldTrip from <https://github.com/fieldtrip/fieldtrip/releases> and download the tutorial data.
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

After installing FieldTrip to your path, you change to the location where the tutorial data can be found and you create a new m-file in your editor.

    cd <your_tutorial_data_location>
    edit tutorial_script.m % this file does not yet exist

### Allow execution of mex files on macOS

The FieldTrip toolbox comes with a bunch of [mex files](https://en.wikipedia.org/wiki/MEX_file). These contain compiled code that is linked at run time. If you are working on macOS, chances are that your security settings do not allow the execution of unsigned code. This [FAQ](/faq/matlab/mex_osx) explains how to add an exception to run the mex files.

### Prepare and bring your questions

You may be working on your own intracranial EEG (SEEG or ECoG) research project. Please think about questions that you have on the processing of your data, especially conceptual questions on the analysis, or regarding the analysis strategy. We will address these questions plenary so that other attendees can also learn from them. We may not have enough time to go into detail on technical questions.
