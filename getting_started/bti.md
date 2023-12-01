---
title: Getting started with BTi/4D data
tags: [dataformat, 4d, bti, meg]
---

# Getting started with BTi/4D data

{% include markup/success %}
The company based in San Diego (CA, USA) making these MEG systems was initially called BTi and later renamed to 4D-Neuroimaging. The company is not operational any more, although its MEG systems are still being used in various labs over the world.    
{% include markup/end %}

## Introduction

The recommended way of working with BTi/4D data is to work on the raw data files directly. The code for reading header information from the raw files is based on Eugene Kronberg's "msi2matlab" tools, and have been further developed by Gavin Paterson and Jan-Mathijs Schoffelen, at CCNi.

Alternatively, you can work with BTi/4D data using intermediate ASCII files (.m4d and .xyz), created with "pdf2set", which is a c-program linked to the BTi/4D libraries. This "pdf2set" program should be available to all BTi/4D users.

All the required BTi/4D reading functions for MATLAB are supplied with the FieldTrip toolbox.

This page explains how to get started reading and using each of the file types in FieldTrip.

## Background

MEG datasets obtained from a BTi/4D MEG-system are usually stored in a directory structure which looks like this:

    /basepath/subjid/scanname/sessionname/runname/

Within each runname/-directory is a bunch of files which do not have uniquely identifiable names, this is important to keep in mind when a given dataset consists of multiple runs per subject, or when you analyze multiple subjects.
Each runname/-directory usually contains the following file

1.  hs_file, containing a list of coordinates in 3D-space, describing the participant's headshape.
2.  config, containing system specific information regarding the acquisition parameters etc
3.  one or more data files, the name(s) of which depend on the acquisition parameters used (see below)

FieldTrip knows how to deal with raw, i.e. unprocessed, data files. Data files which have been obtained using BTi/4D software (such as averaging, digital weight computation etc) can probably not be handled by FieldTrip.

## Set the path

To get started, you should add the FieldTrip main directory to your path, and execute the **[ft_defaults](/reference/ft_defaults)** function, which sets the defaults and configures up the minimal required path settings. See also this [frequently asked question](/faq/installation).

    addpath <path_to_fieldtrip>
    ft_defaults

## Reading MEG data

### Organization of the files

The BTi/4D software organizes all files in a nested directory structure, managing the subject, scan/experiment, session and run, with at the lowest level the actual data files. The files containing the various bits of information do not have file extensions to distinguish them, the full filename instead is required to interpret which file is which. A BTi/4D dataset directory at the lowest level (a "run") might contain something like this

| filename | content of the file                                                                 |
| -------- | ----------------------------------------------------------------------------------- |
| 0        | EEG/MEG recording (channel X time data)                                             |
| 1        | MEG short recording to determine head position                                      |
| 2        | MEG short recording to determine head position                                      |
| config   | system specification and acquisition parameters                                     |
| exp0     | redundant information about the experiment                                          |
| exp1     | redundant information about the experiment                                          |
| exp2     | redundant information about the experiment                                          |
| hs_file  | digitized head-shape coordinates (x-, y-, z-points)                                 |
| pdf.txt  | ASCII file with a description of the alternative file names of the data (see below) |

Depending on how the dataset is exported the actual data files are just named 0, 1, 2, ..., (as above) but could also be called something like:

| c,rfDC          |
| --------------- |
| e,rfhp1.0Hz     |
| hc,rfDC         |
| e,rfhp1.0Hz,COH |

The letter(s) before the first comma refer to the recording mode: e for epoched data, c for continuously recorded data, or hc for continuously recorded data with the coils in continuous headmotiontracking mode. The rfXXXX part refers to the hardware filter settings, rfDC meaning no filtering at all, and rfhp1.0Hz means that a 1.0 Hz cutoff high pass filter was applied prior to the digitization of the data.
COH (or COH1) refer to the short recording to obtain the positions of the Coils On Head.

### Organization of the directories

The BTi/4D software also uses a directory structure to organize the data in line with its patient/subject database. The directory structure looks like

    p0/s0/n0/r0
    p0/s1/n0/r0
    p0/s2/n0/r0
    p0/s2/n0/r1
    p0/s2/n0/r2
    p0/s2/n0/r3
    p0/s3/n0/r0
    p0/s4/n0/r0
    p0/s4/n0/r1

where the numbers (here 0, 1, 2, ...) can be different.

| directory level | explanation                                                       |
| --------------- | ----------------------------------------------------------------- |
| pN              | subject level                                                     |
| sN              | scan level, this usually corresponds to the experimental protocol |
| nN              | session level, this usually is identified by the date and time    |
| rN              | run level                                                         |

### Read header

The **[ft_read_header](/reference/fileio/ft_read_header)** function reads header information and represents it in a common data-independent format. It takes the name of the data file as input. Header information with respect to a particular data file is stored in two places: the run-specific config-file, and the data file itself. The low-level reading function read_4d_hdr reads the header information from the specified data file and then tries to read the corresponding config file which should be stored in the same directory.

To read the header from one of your datasets, use

    hdr = ft_read_header('c,rfDC')

when your current directory is where the data can be seen, or

    hdr = ft_read_header('/basepath/subjid/scanname/sessionname/runname/c,rfDC')

{% include markup/danger %}
Make sure that the run config file is in the same directory as the data-file, otherwise the relevant header information cannot be extracted.
{% include markup/end %}

### Digital balancing weights

Typically, a set of (analog and a set of) digital balancing weights are applied to the data upon acquisition. The digital balancing weights are present in the header information (this is the case for 248-channel systems; we are still working out how to do this for the older 148-channel systems). This information is stored in the field hdr.grad. The tra-matrix (grad.tra) represents in each row the linear combination of measurement coils contributing to the corresponding channel. The coils are defined to have a position and an orientation (grad.coilpos and grad.coilori), and the channels are identified through the label (grad.label). The rightmost part of the tra-matrix usually contains the balancing coefficients. As a whole, the tra-matrix contains crucial information that is needed for the correct computation of the leadfields, which are used for forward and inverse modeling.

### Read data

### Preprocessing

The BTi/4D neuroimaging software contains functionality to compute and apply a set of balancing weights, based on the magnetic field measurements by a set of reference coils, located far away from the brain. The idea is that these coils mainly pick up environmental noise. By subtracting a weighted combination of the reference coil measurements from the coils that pick up the brain activity, one potentially achieves a reduction in the noise (this is typically low frequency noise, so it is most relevant when analyzing event-related fields). The set of weights can be computed using linear regression. The command-line programs provide by BTi/4D are called 'cfw' and 'afw', and operate on a whole data set at once. FieldTrip contains an implementation of the same algorithm, which moreover allows for more flexibility than the BTi/4D implementation. For example, one can use a subset of the data for the weight computation, and/or preprocess the reference coil data (amplifying particular features) prior to weight computation. The FieldTrip function that achieves the weight computation/balancing is **[ft_denoise_pca](/reference/ft_denoise_pca)**

### MEG-system specific issues

1.  The order of the channels as they appear in the data file is not nicely ordered compared to how the channels are arranged on the helmet. This should not be a problem because FieldTrip works with the channel labels and does not make assumptions on a particular ordering of the channels. Yet, it is important to keep in mind that at some places in the code there is no explicit check on the matching of the channel order. This can for example be problematic when using precomputed leadfields for inverse modeling. Leadfields can be computed by **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)**, where you can provide a list of channels for which the leadfield has to be computed. The order (and number) of the channels specified in this list has to be the same as the order and number of channels in the data you are later going to use for your inverse modeling.
2.  Typically, before each recording, you have to specify a set of analog and digital weights which will be applied to the data before they are stored on disk. This means that the data as they are stored on disk represent so-called 'synthetic gradients' rather than the magnetic field (or gradient) picked up at a particular coil (pair of coils) location. Namely, the data on each channel is the magnetic field picked up by the coil corresponding to that channel _minus_ a linear combination of the fields picked up by a set of reference coils. This linear combination is different for each channel and is specified by a weight table. The analog weights are applied prior to digitization, and therefore cannot be 'undone'. The digital weights can be 'undone', or one can recompute the weights using a different set of reference channels, or a different stretch of data. Importantly, since the data usually essentially consist of synthetic gradient data, the digital weight table should be incorporated into the gradiometer-structure's balancing matrix, for a correct computation of the forward model. As of yet, this only works for data acquired with the Magnes 3600 system (and is tested with the Glaswegian 248-magnetometer system).

{% include markup/danger %}
Application of the balancing for 148-channel systems is still disabled, because the header information is not explicit with respect to the channel order of the digital weights.
{% include markup/end %}
