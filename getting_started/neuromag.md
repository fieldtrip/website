---
title: Getting started with Neuromag/Elekta/Megin data
tags: [dataformat, neuromag, elekta, megin, meg]
---

# Getting started with Neuromag/Elekta/Megin data

{% include markup/green %}
The company based in Helsinki (Finland) making these MEG systems started as Neuromag, and later was acquired by Elekta, a much larger Swedish company. Since 2018 it operates under the name Megin and now is part of [Croton Healthcare](https://crotonhealthcare.com) (which also happens to be the parent company of York Instruments). We usually refer to these systems as "Neuromag" systems.
{% include markup/end %}

## Introduction

All Neuromag data is stored in .fif files, where the files can contain different data objects. The following data objects can be read and used in FieldTrip: MEG data, EEG data, gradiometer positions, single sphere models, BEM models (using the MEG-CALC toolbox). FieldTrip reads Neuromag fif files using low-level MATLAB functions from the MNE-matlab toolbox, originally written by Matti Hämäläinen, see [MNE software](https://mne.tools/stable/overview/matlab.html). This will work on any platform, as it is based on open source m-files, which can be downloaded from [github](https://github.com/mne-tools/mne-matlab). The "fieldtrip/external/mne" folder contains those functions as well.

Alternative support for Neuromag data is implemented by calling the mex files from [Kimmo Uutela's MEG-PD toolbox](https://kimmouutela.yolasite.com/meg-pd.php). The files in the MEG-PD toolbox are not included with FieldTrip, but you can download them
(works on Linux only). Extract the toolbox and put it on your MATLAB path, or copy the files into the "fieldtrip/fileio/private" directory. This is used if you select the file format as "neuromag_fif".

Note that the MEG-PD toolbox will only function on 32-bit machines, and requires either a Linux or HP-UX system to run. As the mex files are compiled code, it is not possible to modify these to run on 64-bit machines (which are becoming increasingly common), at present.

## Set the path

To get started, you need to add the paths where the FieldTrip and MNE toolboxes can be found. You should add the FieldTrip main directory to your path, and execute the **[ft_defaults](/reference/ft_defaults)** function, which sets the defaults and configures up the minimal required path settings. See also this [frequently asked question](/faq/installation).

    addpath <path_to_fieldtrip>
    ft_defaults

## Reading MEG data

The first step is to see if you can read in the data using both the toolboxes by typing the following in the command window:

    >> hdr = ft_read_header(filename); % your fif-filename
    >> hdr

    hdr =

            label: {317x1 cell}
           nChans: 317
               Fs: 1000
             grad: [1x1 struct]
             unit: {1x317 cell}
         nSamples: 396000
      nSamplesPre: 0
          nTrials: 1
             orig: [1x1 struct]

The header contains a lot of information about the measurement parameters. In this example 317 channels were recorded, the sampling frequency was a 1000 Hz and in the field hdr.grad you can find information about the sensor-locations, for example. The field 'hdr.orig' contains all the original header information.

    >> dat = ft_read_data(filename);
    >> size(dat)

    ans =

           317      396000

The variable 'dat' contains all the data for 317 channels for all samples. This is a recording of 396 seconds sampled at 1000 Hz.

When this works you are sure that FieldTrip can handle your dataset and you can start to analyze your data as described [here](/tutorial/introduction).

## Special issues

- If you have STI001 up to STI008, the TTL values (single bits) in those channels will be combined into an event of type 'Trigger' with an integer value between 0 and 255.
- Reading .fif mri-data with FieldTrip and making a single shell headmodel (example script can be found [here](/example/neuromag_aligned2mni)).
- The default behavior of ft_read_event is that it assumes that event values below 5 are noise. However, in the new systems (Elekta Neuromag VectorView or Triux (306 channels both) this is seldom the case.

## Frequently Asked Questions

### Can I do source reconstruction with combined planar and magnetometer channels?

Yes, by specifying `cfg.coilaccuracy=1` or 2 during ft_preprocessing

### Can I do source reconstruction with combined MEG and EEG channels?

Almost.

### How can I visualize planar gradient data?

After combining, but also by pulling them apart in side-by-side layouts.

### How can I do stats with clustering on data from the planar gradiometers?

After combining, or using some smart (still to be defined) neighbourhood definition.

### Can I do stats with clustering on combined planar and data?

Yes, using two (non-neighbouring) concatenated neighbourhood definitions.

### Can I combine multiple runs of an experiment (over multiple files)?

Yes, by using ft_appenddata...but see next question.

### How can I deal with rank-deficient maxfiltered data from multiple datasets/runs?

After combining data from separate runs using ft_appenddata, you can run PCA using ft_componentanalysis followed by ft_rejectcomponent such that the rank of your covariance matrix is a number less than 64.

### Should I use or avoid using MaxFilter?

It depends on several factors, including the level of noise in your recording, the presence of artefacts from outside the helmet and large amounts of head movement. Optimising source-localisation for Maxfiltered data is still under development. N.B. If you used Internal Active Shielding (IAS), running Maxfilter prior to processing in FieldTrip is obligatory.
