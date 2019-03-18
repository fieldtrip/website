---
title: Specifying the channel layout for plotting
tags: [tutorial, plot, eeg, meg, ecog, layout]
---

# Specifying the channel layout for plotting

The 2-D channel layout is a representation of the channel positions, together with the outline of the head or other anatomical features, that allows data to be plotted in a topographically consistent manner on a 2-D computer screen (or piece of paper). The 2-D channel layout is _not an exact representation_ of the channel positions, just a projection for the purpose of visualization.

## Introduction to layout files (.lay files)

FieldTrip can use layout files that gives you exact control of the 2-D position of the sensors for topoplotting, and of the per-channel local coordinate axes for the multiplotting. These layout files are ascii file with the extension .lay, or MATLAB files containing a variable with the name "lay". In general, FieldTrip prefers .mat-files because of more flexible outlines of the headshape. For .lay files a standard headshape is drawn around the normalized channel positions. Here is a small snippet of an ASCII layout file:

    1  -0.308949  0.951110  0.750000  0.450000  Fp1
    2   0.000121  1.000000  0.750000  0.450000  Fpz
    3   0.309064  0.951004  0.750000  0.450000  Fp2
    4  -0.808816  0.587705  0.750000  0.450000  F7
    5  -0.411232  0.519845  0.750000  0.450000  F3
    6   0.000257  0.499920  0.750000  0.450000  Fz
    7   0.410919  0.519568  0.750000  0.450000  F4
    8   0.809069  0.587789  0.750000  0.450000  F8
    ...

The format of the layout file is described in more detail in this [frequently asked question](/faq/what_is_the_format_of_the_layout_file_which_is_used_for_plotting).

## Template layout files

The **[template layout files](/template/layout)** included in FieldTrip are based on the sensor specifications as obtained from the manufacturer website or manual. Please also check the corresponding **[getting started section](/getting_started)** section that describes your system.

## Making a layout for MEG sensors

Since MEG sensors are in generally fixed in a rigid helmet that is placed in a dewar, it is not common to make MEG layouts for individual subjects. Instead, most people will simply use one of the **[template layout files](/template/layout)**.

For future OPM based MEG systems it is more likely that MEG sensor layouts will differ from one subject to another subject. Constructing 2-D layouts for OPM based systems can be done similar to the way that they are constructed for EEG systems. If you have the 3-D description of the MEG sensors, you can also specify that as `cfg.grad` into **[ft_prepare_layout](/reference/ft_prepare_layout)** to make a 3-D layout.

## Making a layout for EEG electrodes

The **[ft_prepare_layout](/reference/ft_prepare_layout)** function can be used to make a layout for your specific EEG cap. This can be especially convenient if you have a nice (bitmap) image with the electrode arrangement, like this:

{% include image src="/assets/img/tutorial/layout/easycap_m10_equidistant61chan.gif" %}

This image is for the equidistant M10 electrodecap arrangement and taken from the [Easycap](http://www.easycap.de) website. You can specify cfg.image in **[ft_prepare_layout](/reference/ft_prepare_layout)** and subsequently click on the location of each electrode. After specifying each electrode location, you'll be asked to specify the outlines of the head (i.e. the circle around the head, the nose and ears and optionally some lines representing other important landmarks) and to specify the mask for the topographic interpolation.

    cfg = [];
    cfg.image = 'easycap_m10_equidistant61chan.gif';
    layout_m10 = ft_prepare_layout(cfg);

## Making a layout for EGoG electrodes

The placement of ECoG electrodes always differs from one patient to the next patient. It is common that the neurosurgeon makes a sketch (on paper) of the electrode placement in relation to anatomical landmarks such as the central sulcus. Sometimes a photo is taken, such as this one that was copied from [Dalal et al. in Journal of Neuroscience Methods 174 (2008) 106–115)](http://www.ncbi.nlm.nih.gov/pubmed/18657573).

{% include image src="/assets/img/tutorial/layout/dalal_ecog.png" width="450" %}

As in the EEG case, you can specify cfg.image in **[ft_prepare_layout](/reference/ft_prepare_layout)** and subsequently click on the location of each electrode. Instead of specifying the complete outline of the head as we usually do in EEG (as a circle), you may want to identify other important landmarks such as the major sulci and the outline of the trepanation. You can also specify the mask for the topographic interpolation. If you have a large trepanation with multiple smaller grids, you probably want to make a mask for the topographic interpolation around each grid, to avoid the ECoG potential from being interpolated in between the grids where no actual electrodes were placed.

    cfg = [];
    cfg.image = 'dalal_ecog.png';
    layout_ecog = ft_prepare_layout(cfg);

{% include image src="/assets/img/tutorial/layout/dalal_ecog.png" width="400" %}

After creating the layout, you should manually assign the correct name of the channel labels in the lay.label cell-array. Furthermore, you probably should place the SCALE and COMNT locations at a convenient place in the figure and modify the width and height of the boxes used for multiplotting. You can use **[ft_layoutplot](/reference/ft_layoutplot)** for a visual inspection of the complete layout

    cfg = [];
    cfg.layout = layout_ecog;   % this is the layout structure that you created before
    ft_layoutplot(cfg);

{% include image src="/assets/img/tutorial/layout/fig2.png" width="400" %}

or including the original image as black-and-white background like this

    cfg = [];
    cfg.image  = 'dalal_ecog.png';    % use the photo as background
    cfg.layout = layout_ecog;         % this is the layout structure that you created before
    ft_layoutplot(cfg);

{% include image src="/assets/img/tutorial/layout/fig3.png" width="400" %}

Once you are happy with the result, you can save it to a MATLAB file like this:

    save layout_ecog.mat layout_ecog

The MATLAB file can subsequently be specified as cfg.layout='layout_ecog.mat' whenever you need a layout for plotting. Alternatively, you can specify the layout like `cfg.layout=layout_ecog`.

The advantage of the MATLAB file over the ASCII file, is that the MATLAB file can also contain a user-specified outline of the head and user-specified mask, whereas for the ASCII layout file the same circle with nose and ears will be used.

### Functions that require a layout configuration

Layouts are an essential functionality for all 2-D plotting functions in FieldTrip. See below for an overview of functions that require you to specify a layout.

- **[ft_multiplotER](/reference/ft_multiplotER)**
- **[ft_multiplotTFR](/reference/ft_multiplotTFR)**
- **[ft_topoplotER](/reference/ft_topoplotER)**
- **[ft_topoplotTFR](/reference/ft_topoplotTFR)**
- **[ft_movieplotER](/reference/ft_movieplotER)**
- **[ft_movieplotTFR](/reference/ft_movieplotTFR)**
- **[ft_databrowser](/reference/ft_databrowser)**
- **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)**
- **[ft_neighbourplot](/reference/ft_neighbourplot)**
- **[ft_layoutplot](/reference/ft_layoutplot)**
