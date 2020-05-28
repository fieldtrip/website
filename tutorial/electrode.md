---
title: Localizing electrodes using a 3D-scanner
tags: [tutorial, source, electrode]
---

# Localizing electrodes using a 3D-scanner

## Introduction

This tutorial demonstrates how to construct an electrode model based on a single subject's 3D-scan. This electrode model can be used in combination with a [BEM](/tutorial/headmodel_eeg_bem) or [FEM](/tutorial/headmodel_eeg_fem) volume conduction model for source reconstruction.

This tutorial does not cover how to create a 2-D channel layout for plotting, nor how to do the source estimation itself.

{% include markup/warning %}
Please cite this paper when using our implementation for localizing electrodes with the Structure Sensor 3D-scanner.

Homölle S, Oostenveld R. [Using a structured-light 3D scanner to improve EEG source modeling with more accurate electrode positions.](https://doi.org/10.1016/j.jneumeth.2019.108378) J Neurosci Methods. 2019 Oct 1;326:108378.
{% include markup/end %}

### Background

The quality of EEG source estimates depends on the accuracy of the volume conduction models and of the sensor positions. The volume conduction model comprises a description of the geometry, of the conductivities and of a computational approach for solving Poisson's equations. The current golden standard is to measure the head geometry with an MRI and the EEG electrode positions with a [Polhemus](https://polhemus.com) electromagnetic digitizer. However, the Polhemus device is expensive and measuring the sensor positions with the Polhemus is time consuming, which can make it challenging or even impossible on specific subject groups.

In this tutorial we demonstrate the localization of EEG electrodes based on 3D-scan of a subject's head. The specific device we are using is the [structure sensor](http://structure.io) by Occipital. However, other 3D scanning devices would also work, as long as you can read the output of the 3D-scanner into MATLAB.

{% include markup/info %}
This youtube video shows the procedure that is explained in this tutorial

{% include youtube id="d6FZlZTf-Hg" %}
{% include markup/end %}

## Procedure

In this section we describe the procedure to acquire electrode positions with a 3D-Scanner

- First we have to record the data using the 3D-scanner
- then we will read the surface me with **[ft_read_headshape](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_headshape.m)**
- we convert the units of the mesh **[ft_convert_units](https://github.com/fieldtrip/fieldtrip/blob/release/ft_convert_units.m)**
- we localise the fiducials on the head surface **[ft_electrodeplacement](https://github.com/fieldtrip/fieldtrip/blob/release/ft_electrodeplacement.m)**
- we realign the mesh on the bases of the fiducials to ctf-coordiantes **[ft_meshrealign](https://github.com/fieldtrip/fieldtrip/blob/release/ft_meshrealign.m)**
- now we are able to localise the electrode locations **[ft_electrodeplacement](https://github.com/fieldtrip/fieldtrip/blob/release/ft_electrodeplacement.m)**
- finally we assign the electrode labels

### Recording data

The structure sensor is attached to an iPad mini. We use the [Scanner - Structure Sensor Sample](https://itunes.apple.com/us/app/scanner-structure-sensor-sample/id891169722?mt=8) application on the iPad which is available from the Apple Store. This application allows us to capture our subjects head surface by just walking around the subject. [Here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/electrode/3D-Scan.zip) you can download the result of the 3D-scan that we will use in this tutorial.

### Loading and coregistering data

Before starting with FieldTrip, it is important that you set up your [MATLAB path](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path) properly.

    cd PATH_TO_FIELDTRIP
    ft_defaults

Then you can load the data (this might take some time)

    head_surface = ft_read_headshape('Model/Model.obj')
    disp(head_surface)

          pos: [553494x3 double]
          tri: [800000x3 double]
         unit: 'm'
        color: [553494x3 uint8]

We convert the units to mm.

    head_surface = ft_convert_units(head_surface, 'mm');

We visualize the mesh surface

    ft_plot_mesh(head_surface)

{% include image src="/assets/img/tutorial/electrode/structure_headsurface.jpg" width="400" %}

_Figure 1: Mesh recorded with 3D-scanner_

In the next step we will transform our mesh into [CTF coordinates](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/). For this we have to specify the nasion (NAS), left preauricular (LPA) and right preauricular (RPA) points.

    cfg = [];
    cfg.method = 'headshape';
    fiducials = ft_electrodeplacement(cfg, head_surface);

Now that we have the position of the fiducials relative to the original coordinate system of the head surface, we are able to coregister our head surface such that the fiducial positions are along the axes (according to the CTF coordinates). To facilitate the identification of the fiducials in the 3D-scan, you can also mark the locations on your subject with a coloured pen.

{% include image src="/assets/img/tutorial/electrode/structure_nas.png" %}
{% include image src="/assets/img/tutorial/electrode/structure_left.png" %}
{% include image src="/assets/img/tutorial/electrode/structure_right.png" %}

_Figures: Location of the fiducials_

    cfg = [];
    cfg.method        = 'fiducial';
    cfg.coordsys      = 'ctf';
    cfg.fiducial.nas  = fiducials.elecpos(1,:); %position of NAS
    cfg.fiducial.lpa  = fiducials.elecpos(2,:); %position of LPA
    cfg.fiducial.rpa  = fiducials.elecpos(3,:); %position of RPA
    head_surface = ft_meshrealign(cfg, head_surface);

Again we visualize the head surface, and now we also plot the axes of the coordinate system along with it.

    ft_plot_axes(head_surface)
    ft_plot_mesh(head_surface)

{% include image src="/assets/img/tutorial/electrode/structure_realigned.jpg" width="300" %}

_Figure: Realigned head surface_

### Identify electrode locations

The previous step ensured that our head surface is in the coordinate system in which we want the electrode positions to be defined. We continue with identifying the electrode locations. With the structure sensor 3D-scanner, the texture mapping (i.e. the photo) is not fitting the structural data (i.e. the geometry), so for identifying the electrode locations we ignore the texture mapping and just rely on the bumps corresponding to the electrodes.

    cfg = [];
    cfg.method = 'headshape';
    elec = ft_electrodeplacement(cfg, head_surface);

{% include image src="/assets/img/tutorial/electrode/structure_electrodeplacement.png" width="500" %}

_Figure: Identifying electrode locations_

### Assign electrode labels

The next step is to assign the labels to all electrodes. In the specific case, we used an electrode cap from [Easycap](https://www.easycap.de) that has the electrodes in the [M10](http://www.easycap.de/e/electrodes/13_M10.htm) arrangement.

The call to **[ft_electrodeplacement](https://github.com/fieldtrip/fieldtrip/blob/release/ft_electrodeplacement.m)** returns default electrode labels as '1','2',... and so on, which is correct for the first 60 electrodes. To assign the correct labels to the reference, ground and to the anatomical landmarks (NAS, LPA and RPA), we use the following piece of MATLAB code:

    elec.label(61:65) = { ...
        'GND'
        'REF'
        'NAS'
        'LPA'
        'RPA'
    };

### Visualize the electrodes in 3D

A final visualization shows the electrodes on the colored surface mesh of the subject.

    ft_plot_mesh(head_surface)
    ft_plot_sens(elec)

{% include image src="/assets/img/tutorial/electrode/structure_electrode_head_surface.png" width="300" %}

_Figure: Head surface with localized electrodes_

### Moving electrodes inward

The electrode location are now digitized on the outer surface of the scanned surface. In the figures you can see the plastic ring in which the electrodes are plugged. However, the contact with the skin is realized by injecting electrode gel. We can correct for the mismatch between outer surface of the electrode holder and the skin surface by moving the electrode locations inward according to their normals. Usig the following code, we are moving inward by 12 mm.

    cfg = [];
    cfg.method     = 'moveinward';
    cfg.moveinward = 12;
    cfg.elec       = elec;
    elec = ft_electroderealign(cfg);

## Summary and further reading

In this tutorial we demonstrated how to extract electrode positions from a 3D scanned head surface. The resulting electrode model can be used for volume conduction model, or in the construction of a [2D layout](/tutorial/layout/) for data visualization.

We suggest you read the frequently asked question about [coordinate systems](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined) to understand the different coordinate systemsin which data can be expressed. Since electrode models are often used in source reconstruction, we also suggest you to read the tutorials about [BEM](/tutorial/headmodel_eeg_bem) and [FEM](/tutorial/headmodel_eeg_fem) volume conduction models.

Frequently asked questions that relate to electrodes are:

{% include seealso tag1="electrode" tag2="faq" %}
