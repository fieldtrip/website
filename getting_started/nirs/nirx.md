---
title: Getting started with NIRx NIRS data
category: getting_started
tags: [dataformat, nirs, nirx]
redirect_from:
    - /getting_started/nirx/
---

FieldTrip does not offer direct support for the NIRx NIRS data yet, but you can make use of a work-around using the [Homer2](https://www.nitrc.org/projects/homer2) toolbox and a conversion script that is shared on [NITRC](https://www.nitrc.org).

{% include markup/skyblue %}
We are working on implementing direct support for the NIRx file formats. To keep track of developments, please check [this GitHub issue](https://github.com/fieldtrip/fieldtrip/issues/1528).  
{% include markup/end %}

## Converting NIRx files to .nirs files

A MATLAB script which takes near-infrared spectroscopy data recorded by NIRx system(s) and converts it to a `.nirs` file format for use with for use with Homer2 can be obtained at <http://www.nitrc.org/projects/nirx2nirs>. Created by Rob Cooper.

The `.nirs` file format that results from the conversion is directly supported in FieldTrip. It might be that you need to use the [Homer2](https://www.nitrc.org/projects/homer2) toolbox to construct the sensor definition (i.e. the SD structure),

Note that the `.nirs` file is a MATLAB file in disguise, you can read it with

    nirs = load(filename, '-mat');
    
and you can save it back to disk with
    
    save(filename, 'nirs', -struct');    

However, for reading and preprocessing the data in FieldTrip you would normally not use this low-level approach to access the data, but rather **[ft_preprocessing](/reference/ft_preprocessing)** and **[ft_definetrial](/reference/ft_definetrial)** as explained in the [general tutorials](/tutorial).
