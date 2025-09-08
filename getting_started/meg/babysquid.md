---
title: Getting started with BabySQUID data
tags: [dataformat, babysquid, meg]
category: getting_started
redirect_from:
    - /getting_started/babysquid/
---

## Introduction

The BabySQUID is a series of MEG systems for infants and young children that is developed by [Tristan Technologies](http://tristantech.com/babysquid).

- [BabySQUID Artemis123](http://tristantech.com/artemis123babysquid), see also this [paper](http://journal.frontiersin.org/article/10.3389/fnhum.2014.00099/abstract)
- [BabySQUID MAGView](http://tristantech.com/meg-system-magview)
- [BabySQUID 74-channel system](http://www.tristantech.com/pdf/babySQUID_v1.1.pdf)

## Background

The BabySQUID systems record the data in the fif file format, which is the same format used in the Neuromag/Elekta/MEGIN systems. Consequently the same low-level reading functions can be used and the data can be directly imported into FieldTrip. Certain functionalities in FieldTrip depend on the type of sensors and their arrangements, and therefore we use the **[ft_senstype](/reference/forward/ft_senstype)** helper function to distinguish the different acquisition systems.

To analyze your BabySQUID MEG data in FieldTrip, you would usually start by calling high-level functions such as **[ft_definetrial](/reference/ft_definetrial)** or **[ft_preprocessing](/reference/ft_preprocessing)** (see the [tutorial documentation](/tutorial)). These functions read the raw MEG data by calling low-level functions. The header, data and events are in the fif file, which you specify as

    cfg.dataset = 'filename.fif';

To get started with reading your BabySQUID MEG data into FieldTrip, it might be a good check to call the low-level reading functions directly, i.e. to check that **[ft_read_header](/reference/fileio/ft_read_header)** and **[ft_read_event](/reference/fileio/ft_read_event)** return the expected representation of the data.

The events in the BabySQUID files might not always be detected properly if they are represented as an noisy analog trigger channel. In that case you might have to write your own trialfun (see **[ft_definetrial](/reference/ft_definetrial)**).
