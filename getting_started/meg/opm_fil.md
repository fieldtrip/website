---
title: Getting started with OPM data recorded at the FIL
category: getting_started
tags: [dataformat, meg, opm, fil]
redirect_from:
    - /getting_started/opm_fil/
---

# Getting started with OPM data recorded at the FIL

Optically Pumped Magnetometers offer an exiting opportunity to advance the recording of MEG data. This page provides a short summary on how to get started with processing OPM MEG data that was recorded at the FIL in London. This documentation is largely based on the [OPM GitHub repository](https://github.com/tierneytim/OPM) of Tim Tierney which is geared towards processing the data in SPM.

{% include markup/skyblue %}
On GitHub you can also find the [neurofractal/analyse_OPMEG](https://github.com/neurofractal/analyse_OPMEG) repository, which contains a bunch of scripts and functions to analyse OPM data using the FieldTrip toolbox.
{% include markup/end %}

This is how the test dataset looks like. It consists of multiple files, that are largely organized to [BIDS](https://bids-specification.readthedocs.io/en/stable/). The data was recorded during median nerve stimulation of the left wrist, the sensors were placed over the right hemisphere.

    channelsfile  = 'testData/channels.tsv';
    coordsysfile  = 'testData/coordsystem.json';
    datafile      = 'testData/meg.bin';
    headerfile    = 'testData/meg.json';
    positionsfile = 'testData/positions.tsv';

    mrifile       = 'testData/T1w.nii';
    cortexfile    = 'testData/testCustom.gii';

Note that the data and headerinformation is scattered over multiple files, similar to BrainVision (vhdr,vmrk,eeg) and other formats. In FieldTrip we use cfg.dataset to indicate such a collection; in this case cfg.dataset can either refer to the headerfile or to the datafile.

## Time series data

You can read the header and data using the low-level functions like this

    hdr = ft_read_header(datafile, 'headerformat', 'opm_fil');
    dat = ft_read_data(datafile, 'headerformat', 'opm_fil', 'dataformat', 'opm_fil');
    event = ft_read_event(datafile, 'headerformat', 'opm_fil', 'eventformat', 'opm_fil');

This uses the `opm_fil` function in fieldtrip/fileio/private. Since the file format is not automatically detected, you have to specify it explicitly.

You can also process the data in the usual way using **[ft_preprocessing](/reference/ft_preprocessing)** or visualize it with **[ft_databrowser](/reference/ft_databrowser)**. The following returns the data in a continuous representation.

    cfg = [];
    cfg.headerformat = 'opm_fil';
    cfg.dataformat = 'opm_fil';
    cfg.eventformat = 'opm_fil';
    cfg.dataset = datafile;
    data = ft_preprocessing(cfg);

## Triggers and events

The data contains a trigger channel that is sampled at the same speed as all other channels. Events are detected and returned using **[ft_read_event](/reference/fileio/ft_read_event)** as usual, and you can use **[ft_definetrial](/reference/ft_definetrial)** to define trials.

    cfg = [];
    cfg.headerformat = 'opm_fil';
    cfg.dataformat = 'opm_fil';
    cfg.eventformat = 'opm_fil';
    cfg.dataset = datafile;
    cfg.trialdef.eventtype = '?';
    ft_definetrial(cfg); % let us look at the event types and values

    cfg.trialdef.eventtype = 'TRIG1';
    cfg.trialdef.eventvalue = 16;
    cfg.trialdef.prestim = 0.1;
    cfg.trialdef.poststim = 0.3;
    cfg = ft_definetrial(cfg);

    cfg.demean = 'yes';
    cfg.baselinewindow = [-inf 0];
    data = ft_preprocessing(cfg);

## Visualizing using a template layout

Following removal of bad trials, we can compute an averaged ERP.

    cfg = [];
    cfg.method = 'summary';
    data_clean = ft_rejectvisual(cfg, data);

    cfg = [];
    timelock = ft_timelockanalysis(cfg, data_clean);

And plot this using a schematic layout of the channels.

    cfg = [];
    cfg.layout = 'ordered';
    cfg.channel = 1:17;
    ft_multiplotER(cfg, timelock);

{% include image src="/assets/img/getting_started/opm_fil/figure1.png" width="500" %}

This does not follow the position of the channels over the head, but simply puts them in a regular grid. There are multiple options for this; it is explained in more detail in the [layout tutorial](/tutorial/layout/#creating-a-schematic-ieeg-layout).

## Spatial position and orientation of sensors

To represent the ERFs on the position of the channels relative to the head, we need to know the positions of the OPM sensors. These are represented in the grad structure. Note that although it is called "grad", it actually contains magnetometer positions and orientations.

    grad = timelock.grad;

    figure
    ft_plot_sens(grad, 'label', 'label');
    ft_plot_axes(grad);

{% include image src="/assets/img/getting_started/opm_fil/figure2.png" width="500" %}

Plotting the positions together with the axes makes clear that the x, y, and z-axis are not specified properly. That is because the coordinate system in which the positions is expressed is not recognized. We can specify this using

    grad = ft_determine_coordsys(grad);

which is an interactive function. You have to provide the following answers:

    % What is the anatomical label for the positive X-axis [r, l, a, p, s, i]? r
    % What is the anatomical label for the positive Y-axis [r, l, a, p, s, i]? a
    % What is the anatomical label for the positive Z-axis [r, l, a, p, s, i]? s
    % Is the origin of the coordinate system at the a(nterior commissure), i(nterauricular), n(ot a landmark)? n

which results in the coordinate system being updated to RAS. This means that the x goes to the Right, the y goes to Anterior, and the z goes to superior. See also [this FAQ](/faq/coordsys) on coordinate systems.

We could in principle now continue with further coregistration, using either one (or a combination) of these

1.  coregister the OPM sensor positions to anatomical landmarks on the head
2.  coregister the OPM positions to an anatomical MRI
3.  coregister an anatomical MRI to the OPM positions
4.  coregister the OPM sensor positions and the anatomical MRI to anatomical landmarks on the head

## Visualizing using a recording specific layout

Now that the coordinate system is well defined, we can make a better layout that represents the channels relative to their location on the head.

Since it is not a whole head MEG array, but a small array with limited coverage, it is recommended not to make a whole-head pancake plot of it, as the coverage would be rather small. Instead we can use an orthographic projection from the upper-right side of the subject to get a good view on the sensor array. This is also explained in the [layout tutorial](/tutorial/layout/#creating-a-layout-from-sensor-positions) where an example is presented for a view of the MEG helmet from the left and from the right.

    cfg = [];
    cfg.grad = grad;
    cfg.projection = 'orthographic';
    cfg.viewpoint = 'topright';
    cfg.outline = 'no';
    layout = ft_prepare_layout(cfg);

    figure
    ft_plot_layout(layout);

{% include image src="/assets/img/getting_started/opm_fil/figure3.png" width="500" %}

    cfg = [];
    cfg.layout = layout;
    cfg.channel = 1:17;
    ft_multiplotER(cfg, timelock);

{% include image src="/assets/img/getting_started/opm_fil/figure4.png" width="500" %}

## OPM specific signal processing and denoising

The OPM sensors have different noise characteristics. It is important to deal with the noise, to filter the data and to use e.g., reference channels to remove environmental interference. However, that falls outside the scope of this tutorial. The [OPM GitHub repository](https://github.com/tierneytim/OPM) of Tim Tierney provides SPM code to do that.
