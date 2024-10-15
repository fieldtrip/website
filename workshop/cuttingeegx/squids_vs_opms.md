---
title: SQUIDs versus OPMs
tags: [cuttingeegx]
---

# SQUIDs versus OPMs

## Introduction

Traditional MEG systems use superconducting quantum interference devices (SQUIDs), which require expensive cryogenic cooling with liquid helium and involve placing the sensors 1.5-2 cm from the scalp. Optically pumped magnetometers (OPMs), a new generation of MEG, eliminate the need for cryogenic cooling, allowing sensors to be placed closer to the scalp. OPMs are small individual sensors that allow the researcher to choose where to place them over the head. These sensors are held in place by 3D-printed helmets, which can be customized for each subject.

Even though, both SQUID and OPM system detect the brain's magnetic fields, their data analysis steps differ a bit. In this tutorial we explore the differences in preprocessing and coregistration between the two systems.

OPMs are flexible in their placement allowing for new recording strategies. These new recording strategies lead to new data analysis strategies. For example, in this tutorial we use a small number of OPMs (32 sensors) and do sequential recordings in which we position them over different places over the scalp.

OPMs are magnetometers, as their name suggests. Magnetometers are more sensitive to environmental noise than gradiometers, which most SQUID systems have. Several data analysis algorithms to remove environmental noise have been proposed (see [Seymour et al (2022)](https://www.sciencedirect.com/science/article/pii/S1053811921011058?via%3Dihub) for more details). In this tutorial, we apply homogeneous field correction (HFC). HFC works better with a large number of sensors (more than 32).

Unlike SQUID systems, which have standard coregistration procedures, OPMs don't have a single standard. In this tutorial, we coregister the OPMs with the MRI using an optical 3D scanner which captures the participant’s facial features along with the OPM helmet (Zetter et al., 2019).


This tutorial does not cover follow-up analyses (like source reconstruction) which in principle should not differ from the SQUID follow-up analyses, or alternative coregistration methods which are covered in the tutorial on [coregistration of Optically Pumped Magnetometer (OPM) data](tutorial/coregistration_opm/).

## Background


In this tutorial we will use recordings made with 32 OPM sensors  placed in an adult-sized “smart” helmet with a total of 144 slots. Each slot allows the sensor to move along a single axial direction. That way, the sensor can slide in its slot until it touches the head surface, regardless of the head size and shape. To limit head movements we mounted the helmet on a wooden plate.

To acquire a measurement for each of the 144 helmet slots, we divided the experiment into six sequential recordings while maintaining the participant's head in a fixed position. We kept 9 sensors around the participant’s head fixed for each recordings. Since the OPM sensors touched the participant’s head and the helmet was mounted, these 9 sensors were able to keep the participant's head fixed throughout the experiment. In each recording we moved the remaining 23 sensors to fill every helmet slot.

### The dataset used in this tutorial
The data for this tutorial was recorded with a 32-sensor FieldLine HEDscan v3 system with a so-called smart helmet. Each OPM sensor has one channel that measures the normal component of the magnetic field. 

We perform an experiment with left median nerve stimulation on a single participant using both the SQUID and the OPM system. We expect the activity to be modelled 20 ms post-stimulation with a dipole located at the right Primary Somatosensory (S1) area (Andersen & Dalal, 2021; Boto et al., 2017; Buchner et al., 1994)). 

The dataset can be downloaded from our download server.

## Procedure 
In this tutorial for the SQUIDs we will take the following steps:
- Define trials and read the data using **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)**
- Removing artifacts using **[ft_rejectvisual](/reference/ft_rejectvisual)**
- Compute the averaged ERFs using **[ft_timelockanalysis](/reference/ft_timelockanalysis)**
- Visualize the results for all the channels with **[ft_multiplotER](/reference/ft_multiplotER)**
- Plot the 2D sensor topography for a specified latency with **[ft_topoplotER](/reference/ft_topoplotER)**
- Coregister MRI with SQUIDs using **[ft_volumerealign](/reference/ft_volumerealign)**
- Plot the 3D sensor topography for a specified latency with **[ft_plot_topo3d](/reference/plotting/ft_plot_topo3d)**

For the OPMs we will take the following steps:
- Define trials and read the data using **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)**
- Removing artifacts using **[ft_denoise_hfc](/reference/ft_denoise_hfc)** and **[ft_rejectvisual](/reference/ft_rejectvisual)**
- Compute the averaged ERFs using **[ft_timelockanalysis](/reference/ft_timelockanalysis)**
- Renaming duplicate channels
- Concatenate the data over the six recordings using **[ft_appendtimelock](/reference/ft_appendtimelock)**
- Add NaNs to the missing channels
- Visualize the results for all the channels with **[ft_multiplotER](/reference/ft_multiplotER)**
- Plot the 2D sensor topography for a specified latency with **[ft_topoplotER](/reference/ft_topoplotER)**
- Coregister MRI with OPMs using an optical 3D scanner. For this several functions are used: **[ft_volumerealign](/reference/ft_volumerealign)**, **[ft_read_headshape](/reference/fileio/ft_read_headshape)**, **[ft_meshrealign](/reference/ft_meshrealign)**, **[ft_defacemesh](/reference/ft_defacemesh)**, and **[ft_transform_geometry](/reference/utilities/ft_transform_geometry)**.
- Append sensors from the six recordings using **[ft_appendsens](/reference/ft_appendsens)**
- Plot the 3D sensor topography for a specified latency with **[ft_plot_topo3d](/reference/plotting/ft_plot_topo3d)**

## Practicalities - Taken from Donders Toolkit 2024

This will be an in-person event with no possibilities for hybrid or online attendance.

### Wifi access

If you need wifi access and you don't have a eduroam account through your institution, it is possible to get a visitor access. This needs to be renewed each day. Please follow the instructions on [this intranet page](https://intranet.donders.ru.nl/index.php?id=eva).

### Test your installation in advance

For the hands-on sessions we assume that you will work on your own laptop computer. To have a smooth experience - and to avoid having to spend precious debugging time during the hands-on sessions - we recommend that you [test your MATLAB and FieldTrip installation in advance](/workshop/toolkit2024/test_installation), and download the data that we will need during the hands-on sessions. Before running this test, we recommend that you prepare your laptop as per the instructions in the next section, which explains in some more detail what needs to be downloaded in advance, as well as how you can easily obtain (and install) a copy of FieldTrip on your computer.

## Getting started with the hands-on sessions

For the hands-on sessions we assume that you have a computer with a relatively recent version of MATLAB installed (preferably < 5 years old, >= 2019a/b).

To ensure that everything runs smoothly, we recommend that you set up your computer with a clean and well-tested version of FieldTrip, and download the data that are needed for the hands-on sessions in advance.

{% include markup/red %}
You can either 'click around' using web browsers and/or explorer windows to grab the data that are needed, or instead (less work, at least if it works) execute the MATLAB code below.
{% include markup/end %}

To get a recent copy of FieldTrip, you can follow this [link](https://github.com/fieldtrip/fieldtrip/releases/tag/20240417), download the zip-file, and unzip it at a convenient location on your laptop's hard drive. Alternatively, you could do the following in the MATLAB command window. 

```
% create a folder that will contain the code and the data, and change directory
mkdir('toolkit2024');
cd('toolkit2024');

% download and unzip fieldtrip into the newly created folder
url_fieldtrip = 'https://github.com/fieldtrip/fieldtrip/archive/refs/tags/20240417.zip';
unzip(url_fieldtrip);
```

Upon completion of this step, the folder structure should look something like this: 

```bash
fieldtrip-20240417/
|-- bin
|-- compat
|-- connectivity
|-- contrib
|-- external
|-- fileio
|-- forward
|-- inverse
|-- plotting
|-- preproc
|-- private
|-- qsub
|-- realtime
|-- specest
|-- src
|-- statfun
|-- template
|-- test
|-- trialfun
`-- utilities
```

{% include markup/red %}
If you have downloaded and unzipped by hand, it could be that there's an 'extra folder layer' in your directory structure. We recommend that you remove this extra layer, i.e. move all content one level up.
{% include markup/end %}

Next, we proceed with downloading the relevant data. The data that are used in the hands-on sessions, are stored on the FieldTrip [download-server](https://download.fieldtriptoolbox.org/tutorial/). The tutorial documentation contains links to the relevant files, but it is easier to pre-install (and if needed to unzip) the data. To this end, you can use the recipe below. Please ensure that your present working directory is the ```toolkit2024``` folder, which you created in the previous step.

```
% create a folder (within toolkit2024) that will contain the data, to keep a clean structure
mkdir('data');
cd('data');

% create a folder and download the SQUID and OPM dataset
mkdir('opm_vs_squid');
cd('opm_vs_squid');
url_tutorial = 'https://download.fieldtriptoolbox.org/tutorial/opm_vs_squid';
fnames = {''};
for k = 1:numel(fnames)
  websave(fnames{k}, fullfile(url_tutorial, fnames{k}));
end
cd('../../');
```
At this stage, you ideally have a directory structure that looks like the following one:
```bash
.
|-- data
|   `-- opm_vs_squid
`-- fieldtrip-20240417
    |-- bin
    |-- compat
    |-- connectivity
    |-- contrib
    |-- external
    |-- fileio
    |-- forward
    |-- inverse
    |-- plotting
    |-- preproc
    |-- private
    |-- qsub
    |-- realtime
    |-- specest
    |-- src
    |-- statfun
    |-- template
    |-- test
    |-- trialfun
    `-- utilities
```
So, if you from now on - that is for the duration of the toolkit - *ALWAYS* execute the following steps after starting a fresh MATLAB session, you should be all good to go:

```
% change into the 'toolkit2024' folder and then do the following
restoredefaultpath
addpath('fieldtrip-20240417');
addpath(genpath('data'));
ft_defaults;
```

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath` statement adds the `fieldtrip-20240417` directory, i.e. the directory containing the FieldTrip main functions. The other `addpath` statement tells MATLAB where to find the relevant data, and the `ft_defaults` command ensures that all of FieldTrip's required subdirectories are added to the path.

{% include markup/red %}
In general, please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using a startup.m file than the path GUI. You can find more information about startup files in the MATLAB documentation.

Furthermore, please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/installation).
{% include markup/end %}

## SQUID
### Preprocessing

### Coregistration


## OPM
### Preprocessing
HFC is a method for denoising MEG data based on a spatially homogeneous model of the background magnetic field across the OPM array. This method has previously been used successfully for reducing magnetic interference in OPM magnetometers (see Supplementary Material Fig. A3; Hill et al., 2022; Mellor et al., 2023; Seymour et al., 2022) that are more sensitive to the environmental noise than the SQUID gradiometers. 

### Coregistration
