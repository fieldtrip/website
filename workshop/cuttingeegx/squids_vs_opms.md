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


This tutorial does not cover follow-up analyses (like source reconstruction) which in principle should not differ from the SQUID follow-up analyses, other denoising techniques (a separate FieldTrip tutorial is in progress), or alternative coregistration methods, that are covered in the tutorial on [Coregistration of Optically Pumped Magnetometer (OPM) data](tutorial/coregistration_opm/).

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


## SQUID
### Preprocessing
### Coregistration


## OPM
### Preprocessing
HFC is a method for denoising MEG data based on a spatially homogeneous model of the background magnetic field across the OPM array. This method has previously been used successfully for reducing magnetic interference in OPM magnetometers (see Supplementary Material Fig. A3; Hill et al., 2022; Mellor et al., 2023; Seymour et al., 2022) that are more sensitive to the environmental noise than the SQUID gradiometers. 

### Coregistration
