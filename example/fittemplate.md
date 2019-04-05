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

## Determining and applying of the transformation

### Method 1: On the basis of spheres fitted to the head shapes

For the first approach we will fit a sphere to the head surface measured with the Polhemus and another sphere to the template head model. On the basis of difference of the center and scaling between the two spheres we can derive a transformation containing information of the translation and the global scaling.

Fit a sphere to the MRI template

    cfg             = [];
    cfg.method      = 'singlesphere';
    template_sphere = ft_prepare_headmodel(cfg, template);

Fit a sphere to the Polhemus headshape

    cf              = [];
    cfg.method      = 'singlesphere';
    polhemus_sphere = ft_prepare_headmodel(cfg, polhemus);

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

    template_t_sphere = ft_transform_geometry(transformation, template);

### Method 2: On the basis of fiducials

With this method we describe a scaling method if we only have the fiducials recorded with the Polhemus.

First we have to localise the fiducials on the template models.

    cfg                = [];
    cfg.method         = 'headshape';
    fiducials          = ft_electrode_placement(cfg, template.bnd);

{% include image src="\assets\img\example\fittemplate\electrodeplacement.png" %}  

Fit a sphere to the MRI template

    cfg             = [];
    cfg.method      = 'singlesphere';
    template_sphere = ft_prepare_headmodel(cfg, fiducials);

Unfortunately for this data set we need to a bit of noise to the fiducials . Otherwise,
the algorithm determining the sphere will not work correctly.

    polhemus.fid.pos = polhemus.fid.pos+randn(3,3)/100     

Fit a sphere to the fiducials, (For this example this radius should be 73.4mm, if not please repeat the previous step)

    cfg              = [];
    cfg.method      = 'singlesphere';
    polhemus_sphere = ft_prepare_headmodel(cfg, polhemus.fid);

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

    template_fiducials = ft_transform_geometry(transformation, template);

### Method 3: On the basis of the full head surface

This requires an external toolbox, which can be downloaded [here](https://sites.google.com/site/myronenko/research/cpd)

With this method we apply an affine transformation to the template head model to fit the
whole Polhemus head shape.  This not only applies a translation and rotation, but also a
scaling in the different directions and some skewing.

To create the individualized head model with this method it is important that the scalp
surface of the template head model only contains features that are also in the Polhemus head
shape, and vice versa. We can use **[ft_defacemesh](/reference/ft_defacemesh)** to remove some features.

So first we visualise both meshes:

    ft_plot_mesh(template.bnd);  
    ft_plot_mesh(polhemus);  

{% include image src="/assets/img/example/fittemplate/template_surface_polhemus_surface_plot.png" %}

As the template model and the Polhemus measurement have exclusive features. The Polhemus measurement digitized facial details and part of the upper headsurface, it did not measure the head surface on the side and lower part of the back of the head. So we will now remove these from the template.

    defaced_template      = template.bnd(1);
    defaced_template.unit = template.unit

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

We will now use the template scalp and the Polhemus head shape to determine the
affine transformation.

    cfg              = [];
    cfg.headshape    = defaced_polhemus;
    cfg.template     = defaced_template;
    cfg.method       = 'fittemplate';
    template_surface = ft_prepare_mesh(cfg, template.bnd);

## Preparing the head models

Now that we have have the surfaces of the full template model (not only the scalp) transformed to fit the Polhemus measurement, we can recompute the volume conduction model

### Openmeeg

First we will create the volume conduction models using Openmeeg

    cfg              = [];
    cfg.conductivity = [0.33 0.0042 0.33];
    cfg.method       = 'openmeeg';
    headmodel_sphere = ft_prepare_headmodel(cfg, template_t_sphere.bnd);

    ft_plot_mesh(headmodel_sphere.bnd(1))
    ft_plot_mesh(polhemus)

{% include image src="\assets\img\example\fittemplate\headmodel_sphere_polhemus.png" %}

    cfg               = [];
    cfg.conductivity  = [0.33 0.0042 0.33];
    cfg.method        = 'openmeeg';
    headmodel_fiducials = ft_prepare_headmodel(cfg, template_fiducials);    

    ft_plot_mesh(headmodel_sphere.bnd(1))
    ft_plot_mesh(polhemus)

{% include image src="\assets\img\example\fittemplate\headmodel_fiducials_polhemus.png" %}

    cfg               = [];
    cfg.conductivity  = [0.33 0.0042 0.33];
    cfg.method        = 'openmeeg';
    headmodel_surface = ft_prepare_headmodel(cfg, template_surface);    

    ft_plot_mesh(headmodel_sphere.bnd(1))
    ft_plot_mesh(polhemus)

{% include image src="\assets\img\example\fittemplate\headmodel_surface_polhemus.png" %}

### Taking the inner shell for a single shell model

Another option is to create a single shell model. As we have scaled all 3 compartments of the template head model, we can create a single shell of the innermost boundary, which represents the brain compartment.

    cfg                          = [];
    cfg.method                   = 'singlesphere';
    headmodel_singleshell_sphere = ft_prepare_headmodel(cfg, template_t_sphere.bnd(3));

    cfg                          = [];
    cfg.method                   = 'singlesphere';
    headmodel_singleshell_sphere = ft_prepare_headmodel(cfg, template_fiducials.bnd(3));

    cfg                          = [];
    cfg.method                   = 'singlesphere';
    headmodel_singleshell_sphere = ft_prepare_headmodel(cfg, template_surface(3));
