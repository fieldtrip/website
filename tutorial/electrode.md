---
title: Localizing electrodes using a 3D-scanner
tags: [tutorial, source, electrode, fiducial, coordinate]
---

# Localizing electrodes using a 3D-scanner

## Introduction

This tutorial demonstrates how to construct an electrode model based on a single subject's 3D-scan. This electrode model can be used in combination with a [BEM](/tutorial/headmodel_eeg_bem) or [FEM](/tutorial/headmodel_eeg_fem) volume conduction model for source reconstruction.

This tutorial does not cover how to create a 2-D channel layout for plotting, nor how to do the source estimation itself.

{% include markup/yellow %}
Please cite the following paper when using this implementation for localizing electrodes with the Structure Sensor 3D-scanner.

Homölle S, Oostenveld R. [Using a structured-light 3D scanner to improve EEG source modeling with more accurate electrode positions.](https://doi.org/10.1016/j.jneumeth.2019.108378) J Neurosci Methods (2019).
{% include markup/end %}

### Background

The quality of EEG source estimates depends on the accuracy of the volume conduction models and of the sensor positions. The volume conduction model comprises a description of the geometry, of the conductivities and of a computational approach for solving Poisson's equations. The current golden standard is to measure the head geometry with an MRI and the EEG electrode positions with a [Polhemus](https://polhemus.com) electromagnetic digitizer. However, the Polhemus device is expensive and measuring the sensor positions with the Polhemus is time consuming, which can make it challenging or even impossible on specific subject groups.

In this tutorial we demonstrate the localization of EEG electrodes based on 3D-scan of a subject's head. The specific device we are using is the [structure sensor](http://structure.io) by Occipital. However, other 3D scanning devices would also work, as long as you can read the output of the 3D-scanner into MATLAB.

{% include markup/skyblue %}
This youtube video shows the procedure that is explained in this tutorial

{% include youtube id="d6FZlZTf-Hg" %}
{% include markup/end %}

## Procedure

In this section we describe the procedure to acquire electrode positions with a 3D-Scanner

- First we have to record the data using the 3D-scanner
- then we will read the surface me with **[ft_read_headshape](/reference/fileio/ft_read_headshape)**
- we convert the units of the mesh **[ft_convert_units](/reference/forward/ft_convert_units)**
- we localise the fiducials on the head surface **[ft_electrodeplacement](/reference/ft_electrodeplacement)**
- we realign the mesh on the bases of the fiducials to ctf-coordiantes **[ft_meshrealign](/reference/ft_meshrealign)**
- now we are able to localise the electrode locations **[ft_electrodeplacement](/reference/ft_electrodeplacement)**
- finally we assign the electrode labels

### Recording data

The structure sensor is attached to an iPad mini. We use the [Scanner - Structure Sensor Sample](https://itunes.apple.com/us/app/scanner-structure-sensor-sample/id891169722?mt=8) application on the iPad which is available from the Apple Store. This application allows us to capture our subjects head surface by just walking around the subject.

[Here](https://download.fieldtriptoolbox.org/tutorial/electrode/3D-Scan.zip) you can download the result of the 3D-scan that we will use in this tutorial. Note that the Structure Sensor data comprises three files that should be kept together: an `.obj` file with the geometry, a `.jpg` file with the color photo texture mapping, and an `.mtl` file that maps between the geometry and the colors. If the `.mtl` and `.jpg` file are missing, there is no color information for the mesh.

Before starting with FieldTrip, it is important that you set up your [MATLAB path](/faq/installation) properly.

    cd <path_to_fieldtrip>
    ft_defaults

### Loading the data and coregistration

We start with loading the Structure Sensor file into memory. This also reads the `.mtl` and `.jpg` file and performs the [texture mapping](https://en.wikipedia.org/wiki/Texture_mapping) of the color photo onto the triangulated surface mesh.

    headshape = ft_read_headshape('Model/Model.obj')

    disp(headshape)
          pos: [177642x3 double]
          tri: [200000x3 double]
        color: [177642x3 double]
         unit: 'm'

We convert the units to mm

    headshape = ft_convert_units(headshape, 'mm');

and visualize the mesh surface

    ft_plot_headshape(headshape)

{% include image src="/assets/img/tutorial/electrode/figure1.png" width="600" %}
_Figure: Head shape as recorded with the Structure Sensor 3D-scanner_

The head is shown upside down and rotated by about 45 degrees. We can use **[ft_meshrealign](/reference/ft_meshrealign)** to put it upright with the vertex along the z-axis and to have the nose point along the x- or y-axis. This is not strictly required, but it will facilitate the 3D rotation during the coregistration.

    cfg = [];
    cfg.method = 'interactive';
    headshape = ft_meshrealign(cfg, headshape);

{% include image src="/assets/img/tutorial/electrode/figure2.png" width="600" %}
_Figure: ft_meshrealign graphical user interface_

We suggest that you set the alpha level (the transparency) to 1.0. You can use the standard MATLAB 3D plotting options to rotate the 3D view. Rotate the view such that the positive z-axis is pointing to the top of the figure.

{% include markup/skyblue %}
As subsequent 3D rotations, translations and scalings are not [commutative](https://en.wikipedia.org/wiki/Commutative_property), the order matters. Whenever you click "apply", the specified rotations, translations and scaling is applied to the mesh and you can start again without having to think about the interaction between the operations.
{% include markup/end %}

The first rotation to be applied to the mesh is -90 degrees around the x-axis. Click "apply". The second rotation is 55 degrees around the z-axis. Click "apply" and "quit".

To check, you can plot it again.

    ft_plot_headshape(headshape, 'axes', true) % plot it together with the axes

After this step, the nose points approximately along the x-axis and the vertex along the z-axis. Note however that the y-axis crosses at the posterior part of the ears, not passing through any specific anatomical landmarks, so although it is upright, it is not yet in a well-defined [coordinate system](/faq/coordsys).

In the next step we will transform the mesh into [CTF coordinates](/faq/coordsys). For this we have to specify the nasion (NAS), left preauricular (LPA) and right preauricular (RPA) points.

    cfg = [];
    cfg.method = 'headshape';
    cfg.channel = {'nas', 'lpa', 'rpa'};
    fiducials = ft_electrodeplacement(cfg, headshape);

{% include image src="/assets/img/tutorial/electrode/figure3.png" width="600" %}
_Figure: ft_electrodeplacement graphical user interface_

Immediately after starting **[ft_electrodeplacement](/reference/ft_electrodeplacement)** it will show a figure and print in the command window that "The coordinate system is not specified. Do you want to change the anatomical labels for the axes [Y, n]?". We know that the mesh is not yet expressed in a well-defined coordinate system; that is precisely what we are working towards. Hence you can type "n" for "no" and continue with the specification of the anatomical landmarks in the as-of-now unknown coordinate system.

This video at [178 seconds](https://youtu.be/d6FZlZTf-Hg?t=178) demonstrates how to select anatomical landmarks, although it shows an older version of **[ft_electrodeplacement](/reference/ft_electrodeplacement)**. The 3-D figure rotation changed with MATLAB 2019 and in recent FieldTrip versions the GUI shows a list of electrode (or anatomical landmark) labels. You first select the anatomical landmark by clicking on the mesh, then select the corresponding label "nas" for the first anatomical landmark on the bridge of the nose. Then you enable 3D rotate, rotate the head to the left or right, disable 3D rotate, and repeat the click on the mesh and selection of the corresponding label. After assigning all three labels tro a position on the mesh, you can close the qindow or press "q".

The LPA and RPA landmarks correspond to the point where the jaw bone attaches to the upper skull. These points are best identified by palpating (i.e., feeling with your fingertips) while the participant opens and closes their jaw. To facilitate the offline identification in the 3D-scan, you can mark the locations of the LPA and RPA on your participant by pasting a small piece of tape in front of the ear and marking the LPA and RPA with a felt-tip marker. After the 3D scan, you can pull the piece of tape off again before proceeding with the EEG recording.

Now that we have the position of the fiducials relative to the original coordinate system of the head surface, we are able to coregister our head surface such that the fiducial positions are along the axes (according to the CTF coordinates).

    cfg = [];
    cfg.method        = 'fiducial';
    cfg.coordsys      = 'ctf';
    cfg.fiducial.nas  = fiducials.elecpos(1,:); %position of NAS
    cfg.fiducial.lpa  = fiducials.elecpos(2,:); %position of LPA
    cfg.fiducial.rpa  = fiducials.elecpos(3,:); %position of RPA
    headshape = ft_meshrealign(cfg, headshape);

Again we visualize the head surface, including the axes of the coordinate system. You can check that the positive and negative y-axes go through the preauricular points.

    ft_plot_mesh(headshape, 'axes', true)

{% include image src="/assets/img/tutorial/electrode/figure4.png" width="600" %}
_Figure: Realigned head surface in CTF coordinates_

### Identify electrode locations

The previous step ensured that our head surface is in the coordinate system in which we want the electrode positions to be defined. We continue with identifying the electrode locations. With the structure sensor 3D-scanner, the texture mapping (i.e., the photo) is not fitting the structural data (i.e. the geometry), so for identifying the electrode locations we ignore the texture mapping and just rely on the bumps corresponding to the electrodes.

    cfg = [];
    cfg.method = 'headshape';
    % optionally you can specify the list of electrode names
    % cfg.channel = {'1'	'2'	'3'	'4'	'5'	'6'	'7'	'8'	'9'	'10'	'11'	'12'	'13'	'14'	'15'	'16'	'17'	'18'	'19'	'20'	'21'	'22'	'23'	'24'	'25'	'26'	'27'	'28'	'29'	'30'	'31'	'32'	'33'	'34'	'35'	'36'	'37'	'38'	'39'	'40'	'41'	'42'	'43'	'44'	'45'	'46'	'47'	'48'	'49'	'50'	'51'	'52'	'53'	'54'	'55'	'56'	'57'	'58'	'59'	'60', 'REF', 'GND', 'nas', 'lpa', 'rpa'};
    elec = ft_electrodeplacement(cfg, headshape);

{% include image src="/assets/img/tutorial/electrode/figure5.png" width="600" %}
_Figure: ft_electrodeplacement graphical user interface_

To keep track of which electrode (and which name) goes with which position, it helps to have a separate window open with a schematic representation of the electrode positions. Here we use the [template layout](/template/layout/#easycapm10---equidistant-61-channel-arrangement) figure for the Easycap M10.

### Assign electrode labels

If you did not specify the electrode labels as `cfg.channel` in the previous step, you still will have to assign the labels to all electrodes.

In the specific case here, we used an electrode cap from [Easycap](https://www.easycap.de) that has the electrodes in the [M10](http://www.easycap.de/e/electrodes/13_M10.htm) arrangement. The call to **[ft_electrodeplacement](/reference/ft_electrodeplacement)** by default returns default electrode labels as '1','2',... and so on, which also would have been correct for the first 60 electrodes.

To assign the correct electrode labels to the last 5 positions that we clicked for the reference, the ground and the anatomical landmarks (NAS, LPA and RPA), we use the following piece of MATLAB code:

    elec.label(61:65) = { ...
        'REF'
        'GND'
        'nas'
        'lpa'
        'rpa'
    };

### Visualize the electrodes in 3D

A final visualization shows the electrodes on the colored surface mesh of the subject.

    ft_plot_headshape(headshape)
    ft_plot_sens(elec, 'label', 'on', 'fontsize', 15, 'elecshape', 'disc', 'elecsize', 10)

{% include image src="/assets/img/tutorial/electrode/figure6.png" width="600" %}
_Figure: Head surface with localized electrodes_

### Moving electrodes inward

The electrode location are now digitized on the outer surface of the scanned surface. In the figures you can see the plastic ring in which the electrodes are plugged. However, the contact with the skin is realized by injecting electrode gel. We can correct for the mismatch between outer surface of the electrode holder and the skin surface by moving the electrode locations inward according to their normals. Usig the following code, we are moving inward by 6 mm.

    cfg = [];
    cfg.method     = 'moveinward';
    cfg.moveinward = 6;
    cfg.elec       = elec;
    elec = ft_electroderealign(cfg);

## Summary and further reading

In this tutorial we demonstrated how to extract electrode positions from a 3D scanned head surface. The resulting electrode model can be used for volume conduction model, or in the construction of a [2D layout](/tutorial/layout) for data visualization.

We suggest you read the frequently asked question about [coordinate systems](/faq/coordsys) to understand the different coordinate systems in which data can be expressed. Since electrode models are often used in source reconstruction, we also suggest you to read the tutorials about [BEM](/tutorial/headmodel_eeg_bem) and [FEM](/tutorial/headmodel_eeg_fem) volume conduction models.

Frequently asked questions that relate to electrodes are:

{% include seealso tag1="electrode" tag2="faq" %}
