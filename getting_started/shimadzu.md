---
title: Getting started with Shimadzu NIRS data
category: getting_started
tags: [dataformat, nirs, shimadzu]
---

# Getting started with Shimadzu NIRS data

FieldTrip does not offer direct support for the Shimadzu NIRS data, but you can make use of a work-around using the [Homer2](https://www.nitrc.org/projects/homer2) toolbox and a conversion script that is shared on [NITRC](https://www.nitrc.org).

## Converting Shimadzu files to .nirs files

A MATLAB script to convert the near-infrared spectroscopy data recorded by Shimadzu system(s) to a `.nirs` file format for use for use with Homer2 can be obtained at <https://www.nitrc.org/projects/shimadzu2nirs>. Created by Sahar Jahani.

The `.nirs` file format that results from the conversion is directly supported in FieldTrip. It might be that you need to use the [Homer2](https://www.nitrc.org/projects/homer2) toolbox to construct the sensor definition (i.e. the SD structure),

Note that the `.nirs` file is a MATLAB file in disguise, you can read it with

    nirs = load(filename, '-mat');
    
and you can save it back to disk with
    
    save(filename, 'nirs', -struct');    

However, for reading and preprocessing the data in FieldTrip you would normally not use this low-level approach to access the data, but rather **[ft_preprocessing](/reference/ft_preprocessing)** and **[ft_definetrial](/reference/ft_definetrial)** as explained in the [general tutorials](/tutorial).
