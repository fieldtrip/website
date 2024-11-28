---
title: What is the format of the layout file which is used for plotting?
category: faq
tags: [layout, plotting]
redirect_from:
    - /faq/what_is_the_format_of_the_layout_file_which_is_used_for_plotting/
---

# What is the format of the layout file which is used for plotting?

The layout file is a plain ASCII file with the extention .lay. It gives you exact control of the 2-D position of the channels for topoplotting, and of the per-channel local coordinate axes for the multiplotting. The 2-D positions of the channels can be expressed in an arbitrary coordinate system. Once read in, they will be shifted and scaled such that they fit within a prespecified x- and y-range ([-0.45 0.45] a.u.). After shifting and scaling, a circle representing the head with nose and ears will be added. This circle has a center (0,0) and radius 0.5 (a.u.).

Here is a small snippet of an EEG layout fil

    1  -0.308949  0.951110  0.750000  0.450000  Fp1
    2   0.000121  1.000000  0.750000  0.450000  Fpz
    3   0.309064  0.951004  0.750000  0.450000  Fp2
    4  -0.808816  0.587705  0.750000  0.450000  F7
    5  -0.411232  0.519845  0.750000  0.450000  F3
    6   0.000257  0.499920  0.750000  0.450000  Fz
    7   0.410919  0.519568  0.750000  0.450000  F4
    8   0.809069  0.587789  0.750000  0.450000  F8
    ...

The 1st column is the channel number in the layout file, it is not used any more by the plotting functions, but should be present in the layout file.
The 2nd and 3rd are the X-position and Y-position.
The 4th and 5th column specify the width and height
The 6th column is a string with the channel label.

The width and height are used for the subplot that will be made in **[ft_multiplotER](/reference/ft_multiplotER)** and **[ft_multiplotTFR](/reference/ft_multiplotTFR)**. The width and height represent 80 and 60% of the smallest 2D channel distance respectively. The channels in the data are matched case sensitive to the channels in the layout. There are two additional labels, SCALE and COMNT, which specify the location and size of the comment and scale.

Instead of constructing an ASCII layout file, you can also specify one of the supported electrode or gradiometer files (e.g., Polhemus file, or CTF .res4 header file). The **[ft_prepare_layout](/reference/ft_prepare_layout)** function will read the 3-D sensor positions from the file and will projected these to a 2-D plane. Furthermore, if no layout file is specified, but if electrodes or gradiometers are present in the data, the **[ft_prepare_layout](/reference/ft_prepare_layout)** function will use those to create a 2-D layout on the fly.

Alternative to the ASCII layout file, you can also use a MATLAB layout file. It should be a .mat file containing a single variable with the name "lay". The lay variable should be a structure with

`<code>`lay =
pos: [153x2 double]
width: [153x1 double]
height: [153x1 double]
label: {153x1 cell}
outline: {[101x2 double][3x2 double] [10x2 double][10x2 double]}
mask: {[101x2 double]}
`</code>`

This structure describes the position of each channel, the width and height of the box for **[ft_multiplotER](/reference/ft_multiplotER)** and **[ft_multiplotTFR](/reference/ft_multiplotTFR)**, and the label. Furthermore, it optionally can contain the outline and the mask.

The optional outline in the layout defines the black lines that are drawn on top of the color-coded interpolated values. In this case it contains four line segments: a circle that represents the outline of the head (101x2), a triangle (3x2) that represents the nose and two other shapes (10x2) that represent both ears. These outlines just contain the 2-D points that should be connected with a black line. The default is to use a head-shaped outline, but especially for ECoG data it makes sense to use the sulcal pattern as outline.

The optional mask in the layout defines the region over which **[ft_topoplotER](/reference/ft_topoplotER)** and **[ft_topoplotTFR](/reference/ft_topoplotTFR)** should interpolate the values. Usually the values should be interpolated over the whole head, and in this example it therefore corresponds to the first outline that is a circle representing the head. For ECoG data the mask should represent the area of the cortex that is covered by the electrode grid. If the recording was done with multiple electrode grids that are spaced, i.e. such that the topographical values should not be interpolated between the separate grids, you can specify one mask for each grid.

See the [layout](/tutorial/layout) tutorial for more information.
