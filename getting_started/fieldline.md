---
title: Getting started with FieldLine OPM data
tags: [dataformat, meg, fieldline]
---

# Getting started with FieldLine OPM data

[FieldLine](https://fieldlineinc.com/) is a company located in Boulder, Colorado that develops OPM sensors and complete OPM-based MEG systems. The data from their current systems is stored in the \*.fif format, which is developed and still used by [Neuromag/Elekta/Megin](/getting_started/neuromag). The \*.fif file format is already supported by FieldTrip, which means that no special functions are needed for reading the data.

There are a number of differences though, which are relevant in processing FieldLine data. One difference is how events or triggers are detected and represented. Another difference is in the procedure used to record the position of the OPM sensors relative to the head, which is relevant in the coregistration procedure between MEG and MRI.

## Reading and processing triggers


## Coregistration with anatomical MRI
