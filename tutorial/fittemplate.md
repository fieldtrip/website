---
title: Individualizing a template volume conduction to on the basis of surface information
tags: [tutorial, head model]
---

# Individualizing a template volume conduction to on the basis of surface information

## Introduction

This tutorial demonstrates how to construct an individualized template volume conduction model on the basis of a surface scan.

This tutorial does not cover how to do the source estimation itself.

###  Background

The quality of EEG source estimates depends on accurate volume conduction models and sensor positions. The volume conduction model comprises a description of the geometry, of the conductivities and of a computational approach for solving Poisson’s equations. 

The current golden standard is to measure the head geometry with an MRI and on the basis of that to create a volume conduction model. However, this data is not always available.

## Procedure

In this section we describe the procedure to acquire electrode positions with a 3D-Scanner
*  First we have to record the data using the 3D-Scanner;
*  then we will read the surface me with **[ft_read_headshape](/reference/ft_read_headshape)**
*  we convert the units of the mesh **[ft_convert_units](/reference/ft_convert_units)**
*  we localise the fiducials on the head surface **[ft_electrodeplacement](/reference/ft_electrodeplacement)**
*  we realign the mesh on the bases of the fiducials to ctf-coordiantes **[ft_meshrealign](/reference/ft_meshrealign)**
*  now we are able to localise the electrode locations **[ft_electrodeplacement](/reference/ft_electrodeplacement)**
*  finally we assign the electrode labels

### Download

For this the tutorial we will use [this](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/epilepsy) dataset. More information on this dataset can be found [here](/tutorial/epilepsy/).



### Loading and coregistering data

Before starting with FieldTrip, it is important that you set up your [MATLAB path](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path) properly.

	cd PATH_TO_FIELDTRIP
	ft_defaults

Then you can load the data head shape measured with the Polhemus and a template volume conduction model.

	filename = 'case1/ctf_data/case1.pos'
	polhemus = ft_read_headshape(filename);
  template = ft_read_vol('standard_bem.mat');
	disp(polhemus)
	   pos: [390×3 double]
	   fid: [1×1 struct]
	   unit: 'cm'
	disp(template)
     bnd: [1×3 struct]
     cond: [0.3300 0.0041 0.3300]
     mat: [3000×3000 double]
     type: 'dipoli'
     unit: 'mm'

Before fitting the template we want to have consistent units. Therefore, we convert the Polhemus units into mm.

	polhemus = ft_convert_units(polhemus,'mm');

We visualize the template and the Polhemus together, and see that they are not coregistered.

	ft_plot_mesh(polhemus)
	ft_plot_mesh(template.bnd(1))
	alpha 0.5

{% include image src="/assets/img/tutorial/fittemplate/Polhemus_template_plot.png" width="400" %}
*Figure 1: Polhemus and skin compartment of the template plotted together*

As a next step we will coregister them.

	cfg                         = [];
	cfg.template.headshape      = polhemus;
	cfg.individual.headmodel    = template;
	cfg.checksize               = inf;
	cfg                         = ft_interactiverealign(cfg);
	template                    = ft_transform_vol(cfg.m,template);

{% include image src="/assets/img/tutorial/fittemplate/Coregistration.pngg" %}
*Figures 2: Coregistration procedure*


Before we fit the template to the head surface measurement based on the Polhemus, we have to prepare the template. First we have to remove details before fitting.


## Summary and further reading

In this tutorial we learned how to individualize a volume conduction model.

For further reading suggest to read to about [BEM](/tutorial/headmodel_eeg_bem) or [FEM](/tutorial/headmodel_eeg_fem).

-----
This tutorial was last tested on 02-04-2019 by Simon Homölle on Windows 10, Matlab 2018a.
