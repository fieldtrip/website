---
title: How to create a head model if you do not have an individual MRI
tags: [example, source]
---

# How to create a head model if you do not have an individual MRI

## Introduction

A volume conduction model of the head is required for source reconstruction. Ideally you base the
headmodel on the individual's anatomical MRI, but that is not always available. In the case of EEG you can use a template head model and fit your measured electrodes (or template electrodes) on the scalp of the template model. For MEG you cannot simply use a template head model, since the distance between the head and the (fixed) MEG sensors depends on the head size.

In this example we will show two ways on how to create an individual head model on the basis of surface
data acquired with the Polhemus. Both methods determine the translation, rotation and scaling of the
template head model to fit the Polhemus head shape, but the second method applies a more detailed spatial scaling.

## Download

Both approaches will be demonstrated using the same dataset, which you can find on the
[ftp server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/epilepsy). More
information on this dataset can be found [here](/tutorial/epilepsy/).

## Loading the data

Before starting with FieldTrip, it is important that you set up your
[MATLAB path](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path) properly.

You can load the head shape measured during the MEG recording with the Polhemus and a
template volume conduction model. We have to ensure that they have consistent units, hence
we will convert the units into mm.

    polhemus = ft_read_headshape('epilepsy/case1/ctf_data/case1.pos');
    polhemus = ft_convert_units(polhemus,'mm');

    template = ft_read_vol('standard_bem.mat');
    template = ft_convert_units(template,'mm');

## Coregistration

In the next step we coregister the template head model with the Polhemus head shape to ensure that they are expressed consistently in the MEG coordinate system (i.e. relative to the same origin and with the axes pointing in the same direction). The coregistration consists of a rotation and translation.

    cfg = [];
    cfg.template.headshape      = polhemus;
    cfg.checksize               = inf;
    cfg.individual.headmodel    = template;
    cfg                         = ft_interactiverealign(cfg);
    template                    = ft_transform_geometry(cfg.m, template);

## Removing unshared details between Polhemus and the template

To create the individualized head model it is important that the scalp
surface of the template head model only contains features that are also in the Polhemus head
shape, and vice versa. We can use **[ft_defacemesh](/reference/ft_defacemesh)** to remove some features.

So first we visualise both meshes:

    ft_plot_mesh(template.bnd);  
    ft_plot_mesh(polhemus);  

{% include image src="/assets/img/example/fittemplate/template_surface_polhemus_surface_plot.png" %}

As the template model and the Polhemus measurement have exclusive features, we will now remove these  

    defaced_template = template.bnd(1);  

    cfg              = [];
    cfg.translate    = [-40 0 -50];
    cfg.scale        = [200 200 200];
    cfg.rotate       = [0 0 0];
    defaced_template =  ft_defacemesh(cfg, defaced_template);

    cfg              = [];
    cfg.translate    = [-40 0 -50];
    cfg.scale        = [200 200 200];
    cfg.rotate       = [0 0 0];
    defaced_polhemus =  ft_defacemesh(cfg, polhemus);

Now we have another look at the surfaces

    ft_plot_mesh(defaced_template);  
    ft_plot_mesh(defaced_polhemus);  

{% include image src="/assets/img/example/fittemplate/defaced_template_surface_polhemus_surface_plot.png" %}


## Determining and applying of the transformation

### Method 1: On the basis of spheres fitted to the head shapes

For the first approach we will fit a sphere to the three fiducials and we will fit another sphere to the template head model. On the basis of difference of the center and scaling between the two spheres we can derive a transformation containing information of the translation and the global scaling.

Fit a sphere to the MRI template

    cfg=[];
    cfg.method='singlesphere';
    template_sphere = ft_prepare_headmodel(cfg, defaced_template);

Fit a sphere to the polhemus headshape

    cfg=[];
    cfg.method = 'singlesphere';
    polhemus_sphere = ft_prepare_headmodel(cfg, defaced_polhemus);

Determine the global scaling and translation

    scale = polhemus_sphere.r/template_sphere.r;

    T2 = [1 0 0 template_sphere.o(1);
          0 1 0 template_sphere.o(2);
          0 0 1 template_sphere.o(3);
          0 0 0 1                ];

    T1 = [1 0 0 -template_sphere.o(1);
          0 1 0 -template_sphere.o(2);
          0 0 1 -template_sphere.o(3);
          0 0 0 1                 ];

    S  = [scale 0 0 0;
          0 scale 0 0;
          0 0 scale 0;
          0 0 0 1 ];

    transformation = T1*S*T2;

Apply the transformation to the template head model

    template_sphere = ft_transform_geometry(transformation, template)

### Method 2: On the basis of the full head surface

This requires an external toolbox, which can be downloaded [here](https://sites.google.com/site/myronenko/research/cpd)

With this method we apply an affine transformation to the template head model to fit the
whole Polhemus head shape.  This not only applies a translation and rotation, but also a
scaling in the different directions and some skewing.

We will now use the template scalp and the Polhemus head shape to determine the
affine transformation.

    cfg              = [];
    cfg.headshape    = polhemus;
    cfg.template     = defaced_template.bnd(1);
    cfg.method       = 'fittemplate';
    template_surface = ft_prepare_mesh(cfg, template.bnd);

## Preparing the head models

Now that we have have the surfaces of the full template model (not only the scalp) transformed to fit the Polhemus measurement, we can recompute the volume conduction model

    cfg = [];
    cfg.method = 'openmeeg';
    headmodel_sphere = ft_prepare_headmodel(cfg, template_sphere);

    cfg = [];
    cfg.method = 'openmeeg';
    headmodel_surface = ft_prepare_headmodel(cfg, template_surface);    
