---
title: Specifying the channel layout for plotting
layout: default
tags: [tutorial, plot, eeg, meg, ecog, layout]
---

# Table of contents
{:.no_toc}

* this is a markdown unordered list which will be replaced with the ToC, excluding the "Contents header" from above
{:toc}

# Specifying the channel layout for plotting

## Introduction to layout files (.lay files)

FieldTrip can use layout files that gives you exact control of the 2-D position of the sensors for topoplotting, and of the per-channel local coordinate axes for the multiplotting. These layout files are ascii file with the extention .lay, or MATLAB files containing a variable with the name "lay". In general, FieldTrip prefers .mat-files because of more flexible outlines of the headshape. For .lay files a standard headshape is drawn around the normalized channel positions. Here is a small snippet of an ascii layout fil

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

## Standard layout files included in FieldTrip

The **[standard layout files](/template/layout)** included in FieldTrip are based on the sensor specifications as obtained from the manufacturer website or manual. If an image of the sensor positions is available on the manufacturer website, a copy of it is located in the fieldtrip/template/layout directory. For standard layout files that are included in FieldTrip, please check the corresponding **[getting started section](/getting_started)** corresponding of your system.

## Using the ft_prepare_layout function to make a layout

The **[ft_prepare_layout](/reference/ft_prepare_layout)** function can be used to make a custom layout. This can be especially convenient if you have a nice bitmap image for the channel arrangement, like this

{% include image src="/static/img/tutorial/layout/easycap_m10_equidistant61chan.gif" %}

for the Easycap M10 electrodecap arrangement (see http://www.easycap.de/easycap/e/electrodes/13_M10.htm) for full details), or like this

{% include image src="/static/img/tutorial/layout/dalal_ecog.png" width="450" %}

for an ECoG electrode arrangement (this example photo is taken from [Dalal et al. in Journal of Neuroscience Methods 174 (2008) 106–115)](http://www.ncbi.nlm.nih.gov/pubmed/18657573).

You can specify cfg.image in **[ft_prepare_layout](/reference/ft_prepare_layout)** and subsequently click on the location of each electrode. After specifying each electrode location, you'll be asked to specify the outlines of the head (i.e. the circle around the head, the nose and ears and optionally some lines representing other important landmarks) and to specify the mask for the topographic interpolation.

    cfg = [];
    cfg.image = 'dalal_ecog.png';
    lay = ft_prepare_layout(cfg);

{% include image src="/static/img/tutorial/layout/fig1.png" width="400" %}

After creating the layout, you should manually assign the correct name of the channel labels in the lay.label cell-array. Furthermore, you probably should place the SCALE and COMNT locations at a convenient place in the figure and modify the width and height of the boxes used for multiplotting. You can use **[ft_layoutplot](/reference/ft_layoutplot)** for a visual inspection of the complete layout

    cfg = [];
    cfg.layout = lay;   % this is the layout structure that you created with ft_prepare_layout
    ft_layoutplot(cfg);

{% include image src="/static/img/tutorial/layout/fig2.png" width="400" %}

or including the original image as black-and-white background like this

    cfg = [];
    cfg.image  = 'dalal_ecog.png';    % use the photo as background
    cfg.layout = lay;                 % this is the layout structure that you created with ft_prepare_layout
    ft_layoutplot(cfg);

{% include image src="/static/img/tutorial/layout/fig3.png" width="400" %}

Once you are happy with the result, you can save it to a MATLAB fil

    save dalal_ecog.mat lay         % save the layout in the variable "lay" to a MATLAB file

The MATLAB file can subsequently be specified as cfg.layout='dalal_ecog.mat' whenever you need a layout for plotting. Alternatively, you can specify the layout like cfg.layout=lay.

The advantage of the MATLAB file over the ascii file, is that the MATLAB file can also contain a user-specified outline of the head and user-specified mask, whereas for the ascii layout file always the same circle with nose and ears will be used.

### Functions that require a layout configuration

Layouts are an essential element in FieldTrip, and many FieldTrip functions rely that the user specifies a layout in his configuration (cfg.layout). See below for an overview of such function

*  **[ft_prepare_layout](/reference/ft_prepare_layout)**
*  **[ft_layoutplot](/reference/ft_layoutplot)**
*  **[ft_multiplotTFR](/reference/ft_multiplotTFR)**
*  **[ft_multiplotER](/reference/ft_multiplotER)**
*  **[ft_topoplotTFR](/reference/ft_topoplotTFR)**
*  **[ft_topoplotER](/reference/ft_topoplotER)**
*  **[ft_databrowser](/reference/ft_databrowser)**
*  **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)**
*  **[ft_neighbourplot](/reference/ft_neighbourplot)**
