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

Unlike SQUID systems, which have standard coregistration procedures, OPMs don't have a single standard. In this tutorial, we coregister the OPMs with the MRI using an optical 3D scanner which captures the participant’s facial features along with the OPM helmet ([Zetter et al., 2019](https://www.nature.com/articles/s41598-019-41763-4)).


This tutorial combines the FieldTrip tutorials on [preprocessing of Optically Pumped Magnetometer (OPM) data](tutorial/preprocessing_opm/) and [coregistration of Optically Pumped Magnetometer (OPM) data](tutorial/coregistration_opm/). It does not cover follow-up analyses (like source reconstruction) which in principle should not differ from the SQUID follow-up analyses, or alternative coregistration methods which are covered in the tutorial on [coregistration of Optically Pumped Magnetometer (OPM) data](tutorial/coregistration_opm/).

## Background


In this tutorial we will use recordings made with 32 OPM sensors placed in an adult-sized “smart” helmet with a total of 144 slots. This helmet is called “smart” as each slot allows the sensor to slide in until it touches the head surface, regardless of the head size and shape. To limit head movements we mounted the helmet on a wooden plate.

To acquire a measurement for each of the 144 helmet slots, we divided the experiment into six runs while maintaining the participant's head in a fixed position. We kept 9 sensors around the participant’s head fixed for all the recordings. The remaining 23 sensors were moved to different helmet slots in each run to cover the whole scalp as homogeneously as possible.

### The dataset used in this tutorial
The data for this tutorial was recorded with a 32-sensor FieldLine HEDscan v3 system with a so-called smart helmet. Each OPM sensor has one channel that measures the normal component of the magnetic field. 

We perform a left median nerve stimulation experiment on a single participant in both the SQUID and the OPM system. We expect to find a dipole 20 ms post-stimulation in the right primary somatosensory (S1) area ([Andersen & Dalal, 2021](https://pubmed.ncbi.nlm.nih.gov/34089874/); [Buchner et al., 1994](https://link.springer.com/article/10.1007/BF01211175)). 

The dataset can be downloaded from our [download-server](https://download.fieldtriptoolbox.org/workshop/cuttingeegx).

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
### Preprocessing & trial definition

We begin by loading the SQUID data and defining trials. In the experiment, the inter-trial interval ranged from 800-1200 ms. We select a 200 ms prestimulus and 400 ms poststimulus window. We then select trials where left median nerve stimulation occurred (trigger code = 1).

```
cfg                     = [];
cfg.dataset             = 'M:\Documents\cuttingeegx-workshop\data\squid\subj001ses002_3031000.01_20231208_01.ds';
cfg.trialdef.eventtype  = 'UPPT001';
cfg.trialdef.eventvalue = [1]; % select stimulation trials only (which are ~85 % of all the trials)
cfg.trialdef.prestim    = 0.2; % ISI varied from 0.8 to 1.2 sec
cfg.trialdef.poststim   = 0.4;
cfg                     = ft_definetrial(cfg);

cfg.demean         = 'yes';  
cfg.baselinewindow = [-Inf 0]; 
cfg.continuous     = 'yes'; % without that I get the error: 'requested data segment extends over a discontinuous trial boundary'. I guess I need cfg.continuous since 'subj001ses002_3031000.01_20231208_01.ds' is initially a continuous recording and I do not want to lose the ITI during preprocessing.
data_stim          = ft_preprocessing(cfg);

save data_stim data_stim
```

### Removing artifacts

The summary method in **[ft_rejectvisual](/reference/ft_rejectvisual)** allows to manually remove trials and/or channels that have high variance. 

```
load data_stim data_stim

cfg             = [];
cfg.method      = 'summary';
data_stim_clean = ft_rejectvisual(cfg,data_stim);

save data_stim_clean data_stim_clean
```

### Compute ERFs

We start by removing trials that have higher variance than 8e-25 Tesla-squared, then assess the channels. Removing trials also reduces channel variance, so no need to reject any channels. We then calculate the ERFs: 

```
load data_stim_clean data_stim_clean

cfg     = [];
avg_stim = ft_timelockanalysis(cfg, data_stim_clean);

save avg_stim avg_stim
```
### Visualisation

We plot the activity from all the sensors.

```
load avg_stim avg_stim

% find the time window of the activity
cfg = [];
cfg.layout = 'CTF275_helmet';
ft_multiplotER(cfg, avg_stim); % use interactive
```

We are now going to use the interactive feature of **[ft_multiplotER](/reference/ft_multiplotER)** to find our activity of interest. We select the sensors that are on top of the right primary somatosensory area since that is where we expect our activity to be localised. We see a negative peak around 20 ms (more specifically 35-50 ms) post-stimulation. We can select this time window to see the topography. The dipolar pattern the right primary somatosensory area is now visible. We can also plot this dipolar pattern with **[ft_topoplotER](/reference/ft_topoplotER)**.

```
% plot the activity at [0.035 0.050]
cfg = [];
cfg.xlim = [0.035 0.050];
cfg.layout = 'CTF275_helmet';
ft_topoplotER(cfg, avg_stim); 

print -dpng figures/cuttingeegx_topo_squid.png
```

### Coregister the anatomical MRI to the SQUID coordinate system

We read the MRI, SQUID channels and the Polhemus headshape in memory. I recommend converting all quantities to SI units to ensure consistent units throughout your pipeline.

```
mri    = ft_read_mri('M:\Documents\cuttingeegx-workshop\data\dicoms\00001_1.3.12.2.1107.5.2.19.45416.2022110716263882460203497.IMA');
ctf275 = ft_read_sens('M:\Documents\cuttingeegx-workshop\data\squid\subj001ses002_3031000.01_20231208_01.ds', 'senstype', 'meg');
shape  = ft_read_headshape('M:\Documents\cuttingeegx-workshop\data\squid\subj001ses001ses002.pos');

mri = ft_convert_units(mri, 'm');
ctf275 = ft_convert_units(ctf275, 'm');
shape  = ft_convert_units(shape, 'm');

save mri mri
save ctf275 ctf275
save shape shape
```

We coregister the MRI with the SQUIDs by converting the MRI coordinate system to match that of the SQUIDs. In other words, we ensure that the three fiducials (nasion, LPA and RPA) defining the MRI coordinate system are aligned to the same three fiducials defining the SQUID coordinate system.

```
load shape shape
load ctf275 ctf275

% assign the 'ctf' coordinate system to the MRI 
cfg          = [];
cfg.method   = 'interactive';
cfg.coordsys = 'ctf';
mri_realigned1 = ft_volumerealign(cfg, mri);

save mri_realigned1 mri_realigned1
```


To refine the coregistration, we can also coregister the Polhemus head shape with the skin surface that is extracted from the previously aligned MRI. Now not only the fiducials but also other skin surface points acquired with the Polhemus are used for the alignment.

```
load mri_realigned1 mri_realigned1

cfg = [];
cfg.method = 'headshape';
cfg.headshape.headshape = shape;
mri_realigned2 = ft_volumerealign(cfg, mri_realigned1); 

% check 
cfg = [];
cfg.method = 'headshape';
cfg.headshape.headshape = shape;
cfg.headshape.icp = 'no';
ft_volumerealign(cfg, mri_realigned2); % takes too long

save mri_realigned2 mri_realigned2
```


### 3D sensor topography
Let's plot the sensor topography in 3D using **[ft_plot_topo3d](/reference/plotting/ft_plot_topo3d)**. This will help us visualize where the sensors are positioned relative to the head. To make this clearer, we'll also display the scalp and brain surfaces.

First, we'll prepare the surface mesh of the scalp and brain:

```
load mri_realigned2 mri_realigned2

cfg                = [];
cfg.output         = {'brain', 'scalp'};
mri_segmented          = ft_volumesegment(cfg, mri_realigned2);

cfg                = [];
cfg.tissue         = {'brain'};
mesh_brain         = ft_prepare_mesh(cfg, mri_segmented);

cfg                = [];
cfg.tissue         = {'scalp'};
mesh_scalp         = ft_prepare_mesh(cfg, mri_segmented);

save mesh_brain mesh_brain
save mesh_scalp mesh_scalp
```
Now, we'll plot the 3D sensor topography for the time window [0.035, 0.050] seconds, along with the brain and scalp:

```
sampling_rate = 1200; % in Hz
prestim = 0.2;

I1 = (prestim+0.035)*sampling_rate; 
I2 = (prestim+0.050)*sampling_rate;

selected_avg = mean(avg_stim.avg(:, I1:I2), 2);

figure;
ft_plot_mesh(mesh_scalp, 'facealpha', 0.5, 'facecolor', 'skin', 'edgecolor', 'none', 'edgecolor', 'skin' )
hold on
ft_plot_mesh(mesh_brain, 'facecolor', 'brain', 'edgecolor', 'none');
hold on
ft_plot_topo3d(pos275,selected_avg, 'facealpha', 0.9)
camlight
view([360 0])


print -dpng M:\Documents\cuttingeegx-workshop\code\figures\squid\cuttingeegx_topo3d_squid.png
```

The SQUID sensors are located 1.5-2.0 cm from the scalp, resulting in a less focal sensor topography.

## OPM
### Preprocessing
HFC is a method for denoising MEG data based on a spatially homogeneous model of the background magnetic field across the OPM array. This method has previously been used successfully for reducing magnetic interference in OPM magnetometers (see Supplementary Material Fig. A3; Hill et al., 2022; Mellor et al., 2023; Seymour et al., 2022) that are more sensitive to the environmental noise than the SQUID gradiometers. 

### Coregistration
