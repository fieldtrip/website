---
title: Getting started with BESA data
tags: [dataformat, besa]
category: getting_started
redirect_from:
    - /getting_started/besa/
---

A lot of valuable information can be found on the [BESA wiki](http://wiki.besa.de/). Please add your information and experiences here if you're using BESA data.

## Background

BESA is a commercial software package for EEG and MEG data analysis (see <http://www.besa.de>). One of BESA's strong points is source analysis, in particular concerning dipole modeling. By including prior anatomical or functional knowledge as constraints on the source model, it is possible to make robust estimations of relatively complex source configurations. This is further facilitated by the easy to use GUI. Computation can be done using a number of pre-defined head models that can be extended to individual head models (FEM) when using the extension package BESA MRI or adapting your FEM to BESA standards. BESA's source analysis methods also include some beamformers.

FieldTrip has very extensive support for advanced frequency and time-frequency analysis of EEG and MEG data. The main approach for source analysis that is currently implemented in FieldTrip uses various beamformer methods in the time, but especially in the frequency domain. In that respect, it differs a little bit from BESA. However, a large difference between BESA and FieldTrip is that the latter also includes support for advanced statistical analysis of channel and source level data.

One might wish to combine BESA's capacities and convenience in spatiotemporal dipole modeling with FieldTrip's strength on advanced frequency estimates and statistical analysis on the channel and source level. This tutorial describes how you can read in channel and source level data that has been analyzed in BESA, and how you can enhance your analysis of that data in FieldTrip.

## Reading in data files from BESA

BESA has its own file formats for storing various aspects of the data. Most of the files contain the data in plain ASCII format and it is relatively easy to read in their contents into MATLAB or any other program. You can use a normal text editing program like Microsoft Wordpad to have a look at the content and format of the files.

FieldTrip directly supports the following BESA file format

- `.avr` contains an averaged ERP/ERF
- `.mul` contains an averaged ERP/ERF stored in a multiplexed format
- `.elp` contains electrode labels-
- `.sfp` contains electrode labels and positions
- `.pdg` contains the settings of an analysis paradigm
- `.tfc` contains a time-frequency representation of power or coherence
- `.dat` contains multiple source beamformer output on a regular 3D grid

It is possible to use the low-level functions in FieldTrip to read in the BESA data into MATLAB, but it is preferred to use the high-level **[besa2fieldtrip](/reference/besa2fieldtrip)** function. That function will read the data and format it into a structure that is compatible with FieldTrip. Depending of the content of the file, the data will be formatted to appear similar to the output of one of the FieldTrip function

- `.avr` converted to ft_timelockanalysis
- `.mul` converted to ft_timelockanalysis
- `.tfc` converted to ft_freqanalysis

For example, you can read in event-related potentials using

    timelock = besa2fieldtrip('filename.avr');

or a time-frequency estimate of power using

    freq = besa2fieldtrip('filename.tfc');

## BESA MATLAB toolbox

For some of the file formats, there happen to be two low-level conversion functions importers. FieldTrip comes with the low-level functions of itself, but there is also a BESA toolbox written by Karsten Hochstatter. The preferred method for using **[besa2fieldtrip](/reference/besa2fieldtrip)** is to download the BESA toolbox and to add it to your MATLAB path. The conversion function will automatically detect and use it when available on your path.

The BESA toolbox is maintained by [BESA](http://www.besa.de) and included in the FieldTrip release in `fieldtrip/external/besa`.

## Electrode information

BESA electrode files can also be read into MATLAB, using the **[ft_read_sens](/reference/fileio/ft_read_sens)** function. They do not directly correspond to a core FieldTrip data structure, but you can add the electrode information to any FieldTrip data structure according to this:

    data = besa2fieldtrip('yourbesafile.avr');
    data.elec = ft_read_sens('yourelectrodes.sfp');

## Reading .dat files with source reconstructions

Because BESA `.dat` files do not include mask information, the resulting data structure will not have the `.inside` field assigned correctly, which will lead to errors in subsequent analyses. Consequently these fields much be set for each subject. The following code is an example of how to develop a reasonable mask and apply it to all subjects (it masks out only those coordinates with a value of 0 for all subjects

    files=dir(['yoursubjectdirectory' filesep '.dat']);
    inside=[];
    for k=1:length(files)
      src(k)=besa2fieldtrip(files(k).name);
      in=find(src(k).avg.pow);
      inside(end+1:end+length(in))=in;
    end

    inside=unique(inside);
    outside=1:length(src(1).pos);
    outside(inside)=[];

    for k=1:length(files)
      src(k).outside=outside;
      src(k).inside=inside;
    end

## Continuous data in the .besa format

The `.besa` format contains continuous (unprocessed) data, including header and event details.

Events can also be stored in a data channel appended to the brain data channels. For instance, a photodiode transducer attached to a stimulus presentation screen may convert screen light into current. This way, changes in light are captured as an analog signal in that data channel and can be used to synchronize timing of the experiment with the brain recording. When the name or the channel index of the event channel is known, it becomes feasible to use that channel for reading data segments or trials of interest into the MATLAB work environment using FieldTrip. The most straightforward approach is to create a trial function (as invoked with cfg.trialfun) that reads in the event channel and performs some form of thresholding on the signal in that channel to determine the events of interest. We provide an example pipeline below.

    % define trials
    cfg            = [];
    cfg.dataset    = 'dataset.besa';
    cfg.trialfun   = 'trialfun_ttl';
    cfg            = ft_definetrial(cfg);

where `trialfun_ttl` is your own MATLAB function for conditional selection of data segments or trials of interest. See [this page](/example/preproc/trialfun) for the actual `trialfun_ttl` example function.

    % read and preprocess the data
    cfg.continuous = 'yes';
    cfg.channel    = 'all';
    data           = ft_preprocessing(cfg);

Note that filtering, rereferencing, etcetera can be performed at the preprocessing stage. Type 'help ft_preprocessing' to get an overview of the possibilities. Now that the raw data is in the MATLAB environment it becomes possible, as shown below, to use ft_databrowser to browse through the raw segmented data. See also [this page](/tutorial/preproc/visual_artifact_rejection) for a number of strategies on how to inspect and clean up the data from artifacts.

    % visually inspect the data
    cfg            = [];
    cfg.viewmode   = 'vertical';
    ft_databrowser(cfg, data);

## See also

{% include seealso tag="besa" %}
