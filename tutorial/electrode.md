---
title: Localizing electrodes using a 3D-scanner
tags: [tutorial, source, electrode]
---

# Localizing electrodes using a 3D-scanner

## Introduction

This tutorial demonstrates how to construct an electrode model based on a single subject's 3D-scan. This electrode model can be used for creating a [BEM](/tutorial/headmodel_eeg_bem) or [FEM](/tutorial/headmodel_eeg_fem) volume conduction model.

This tutorial does not cover how to create a 2-D channel layout for plotting, nor how to do the source estimation itself.

###  Background

The quality of EEG source estimates depends on accurate volume conduction models and sensor positions. The volume conduction model comprises a description of the geometry, of the conductivities and of a computational approach for solving Poisson’s equations. 

The current golden standard is to measure the head geometry with an MRI and sensor positions with a Polhemus. Measuring the sensor positions with the Polhemus on specific groups can be challenging or even impossible.

In this tutorial we want to focus on creating a electrode  based on 3D surface scan of a human head. The 3D-scan device we are using in this tutorial is a [http://structure.io](http://structure.io) device. However, other devices are also feasible as long as the 3D-scan output is written in a FieldTrip supported [data format](/faq/dataformat).

{% include markup/info %}
This youtube video shows the procedure that is explained in this tutorial

{% include youtube id="d6FZlZTf-Hg" %}
{% include markup/end %}

## Procedure

In this section we describe the procedure to acquire electrode positions with a 3D-Scanner
*  First we have to record the data using the 3D-Scanner;
*  then we will read the surface me with **[ft_read_headshape](/reference/ft_read_headshape)**
*  we convert the units of the mesh **[ft_convert_units](/reference/ft_convert_units)**
*  we localise the fiducials on the head surface **[ft_electrodeplacement](/reference/ft_electrodeplacement)**
*  we realign the mesh on the bases of the fiducials to ctf-coordiantes **[ft_meshrealign](/reference/ft_meshrealign)**
*  now we are able to localise the electrode locations **[ft_electrodeplacement](/reference/ft_electrodeplacement)**
*  finally we assign the electrode labels

### Recording data

For recording with the structure.io we use [Scanner - Structure Sensor Sample](https://itunes.apple.com/us/app/scanner-structure-sensor-sample/id891169722?mt=8). This software allows use to capture our subjects head surface by just walking around the subject. [Here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/electrode/3D-Scan.zip ) you can download the example we used in this tutorial.

### Loading and coregistering data

Before starting with FieldTrip, it is important that you set up your [MATLAB path](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path) properly.

	cd PATH_TO_FIELDTRIP
	ft_defaults

Then you can load the data (this might take a moment)

	head_surface = ft_read_headshape('Model/Model.obj')
	disp(head_surface)
	      pos: [553494x3 double]
	      tri: [800000x3 double]
	     unit: 'm'
	    color: [553494x3 uint8]

We convert the units to mm.

	head_surface = ft_convert_units(head_surface,'mm');

We visualise the mesh surface

	ft_plot_mesh(head_surface)

{% include image src="/assets/img/tutorial/electrode/structure_headsurface.jpg" width="400" %}
*Figure 1: Mesh recorded with 3D-scanner*

In the next step we will transform our mesh into the ctf-coordinates. For this we have to specify the nasion (NAS), left preauricular (LPA) and right preauricular (RPA) points.

	cfg = [];
	cfg.method = 'headshape';
	fiducials = ft_electrodeplacement(cfg,head_surface);

With having specified the fiducials we are now able to coregister our head surface to the ctf-coordinates. To easier identify the locations of the fiducials you can also mark the locations on your subject with a coloured pen.

{% include image src="/assets/img/tutorial/electrode/structure_nas.png" %}
{% include image src="/assets/img/tutorial/electrode/structure_left.png" %}
{% include image src="/assets/img/tutorial/electrode/structure_right.png" %}
*Figures: Location of the fiducials*

	cfg = [];
	cfg.method = 'fiducial';
	cfg. coordsys = 'ctf';
	cfg.fiducial.nas    = fiducials.elecpos(1,:); %position of NAS
	cfg.fiducial.lpa    = fiducials.elecpos(2,:); %position of LPA
	cfg.fiducial.rpa    = fiducials.elecpos(3,:); %position of RPA
	head_surface = ft_meshrealign(cfg,head_surface);

Again we visualise the head surface, but we also plot the axes along with it.

	ft_plot_axes(head_surface)
	ft_plot_mesh(head_surface)

{% include image src="/assets/img/tutorial/electrode/structure_realigned.jpg" width="100" %}--0)
*Figure: Realigned head surface*

### Identify electrode locations

The previous made sure that our head model is now in the right coordinate system. This allows us now to identify the electrode locations. With our scanner the texture mapping quality is not fitting the actual structural data, so for identifying the electrode locations we remove the texture mapping.

To localise the electrode we use the crates that are visible on the surface.

	cfg = [];
	cfg.method = 'headshape';
	elec = ft_electrodeplacement(cfg,head_surface);

{% include image src="/assets/img/tutorial/electrode/structure_electrodeplacement.png" width="500" %}
*Figure: Identifying electrode locations*

### Assign electrode labels

Now we need to assign the correct labels. We used the [M10](http://www.easycap.de/e/electrodes/13_M10.htm) arrangement.

As [ft_electrodeplacement](/reference/ft_electrodeplacement) uses the the labelling scheme '1','2',... and so on we need to assign the correct labels the reference, ground and the anatomical landmarks NAS,LPA and RPA.

	elec.label(61:65) = { ...
	    'GND'
	    'REF'
	    'NAS'
	    'LPA'
	    'RPA'  
	};

### Visualize the electrodes in 3D

A final visualisation showing the electrodes on the color surface mesh of the subject.

	ft_plot_mesh(head_surface)
	ft_plot_sens(elec)

{% include image src="/assets/img/tutorial/electrode/structure_electrode_head_surface.png" width="300" %}

*Figure: Head surface with localised electrodes*

### Moving electrodes inward

The electrode location are now digitised on the outer surface of the cap. In the figures you can see the plastic ring in which you plug in the electrodes. This means we digitised the surface of the ring and not the contact between electrode and skin surface. We can correct for this mismatch by moving the electrode inward according to their normals.

	cfg = [];
	cfg.method = 'moveinward'; %'moveinward' moves electrodes inward along their normals
	cfg.moveinward = 12;     %cfg.moveinward     = number, the distance that the electrode should be moved
	                           %inward (negative numbers result in an outward move)
	cfg.elec = 'elec';
	elec = ft_electroderealign(cfg);

## Summary and further reading

In this tutorial we learned how to process a head surface created by a 3D-Scan. Furthermore we learned how to identify electrode locations to create a electrode model which can be used for volume conduction modelling.

For further reading suggest to read  about [coordinate systems](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined). This will help you understand the different coordinate systems you can use for co-registration.

As electrode models are part of volume conduction modelling we also suggest to investigate the tutorials about [BEM](/tutorial/headmodel_eeg_bem) or [FEM](/tutorial/headmodel_eeg_fem).
