---
title: Creating a head model, when there is no MRI
tags: [example]
---

# Creating a head model, when there is no MRI

## Introduction

Creating a head model is crucial for source reconstruction. The typical way is to
base the headmodel on the individual's anatomical MRI. However, this data is not always available.
In this example we will show two ways on how to create an individual head model on the basis of surface
data acquired with the Polhemus.

Both methods share the same approach by applying a spatial transformation on the template head model. However, the derivation of the transformation is different.

## Download

For both approaches we will use the same dataset, which can be found
[here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/epilepsy)
dataset. More information on this dataset can be found
[here](/tutorial/epilepsy/).
Also we need an external toolbox which can be downloaded [here](https://sites.google.com/site/myronenko/research/cpd)

## Loading the data

Before starting with FieldTrip, it is important that you set up your
[MATLAB path](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path) properly.

Then you can load the data head shape measured with the Polhemus and a
template volume conduction model. Also we will convert the units into mm
by now.

    polhemus = ft_read_headshape(filename);
    polhemus = ft_convert_units(polhemus,'mm');

    template = ft_read_vol('standard_bem.mat');
    template = ft_convert_units(template,'mm');

## Coregistration

In the next step we coregister both meshes with each other. Coregistration ensures that bot datasets are expressed in the same coordinate system. This already serves as an initial rotation and translation of the data and ensures, that the next steps are more robust.


    cfg = [];
    cfg.template.headshape      = polhemus;
    cfg.checksize               = inf;
    cfg.individual.headmodel    = template;
    cfg                         = ft_interactiverealign(cfg);
    template                    = ft_transform_geometry(cfg.m,template);

## Determining and applying of the transformation

### Method 1: On the basis of fiducials

For the first approach we will fit a sphere to the three fiducials and we will fit another sphere to the template head model. On the basis of difference of the center and scaling between the two spheres we can derive a transformation containing information of the translation and the global scaling.

For this approach we will need determine the fiducials to Fiducials

    nas = polhemus.elecpos
    lpa = polhemus.elecpos
    rpa = polhemus.elecpos

Fit a sphere to the MRI template

    cfg=[];
    cfg.method='singlesphere';
    scalp_sphere = ft_prepare_headmodel(cfg, template.bnd(1));

Fit a sphere to the fiducials

    cfg=[];
    cfg.method = 'singlesphere';
    headshape_sphere = ft_prepare_headmodel(cfg, fiducials);

Determine the global scaling and translation

    scale = headshape_sphere.r/scalp_sphere.r;

    T2 = [1 0 0 scalp_sphere.o(1);
          0 1 0 scalp_sphere.o(2);
          0 0 1 scalp_sphere.o(3);
          0 0 0 1                ];

    T1 = [1 0 0 -scalp_sphere.o(1);
          0 1 0 -scalp_sphere.o(2);
          0 0 1 -scalp_sphere.o(3);
          0 0 0 1                 ];

    S  = [scale 0 0 0;
          0 scale 0 0;
          0 0 scale 0;
          0 0 0 1 ];

    transformation = T1*S*T2;

Appyling the transformation to the template

    template_fiducial = ft_transform_geometry(transformation, template)


### Method 2: On the basis of the head surface

With this method we make full use of the head surface. In this approach we match the template head model to fit the whole polhemus measurement and not only the three fiducials. This allows us to compute an affine transformation (transformation, with translation, rotation, scaling and skewing)

For creating the individualized mesh it is important that the head
surface of template only contains features that are also in the head
surface measurement of the Polhemus. Therefore, we use ft_defacemesh to remove the undesired features.

    defaced_template                = template;
    cfg                             = [];
    defaced_template.bnd(1).unit    = 'mm';
    defaced                         =  ft_defacemesh(cfg,defaced_template.bnd(1));

    defaced_template.bnd(1).pos = defaced.pos;
    defaced_template.bnd(1).tri = defaced.tri;

We will now use the surface information of the template model and the
Polhemus measurement to create an individualised version mesh of the template mesh.

    cfg              = [];
    cfg.headshape    = polhemus;
    cfg.template     = defaced_template.bnd(1);
    cfg.method       = 'fittemplate';
    template_surface = ft_prepare_mesh(cfg, template.bnd);

## Creating volume conduction model

Now we have derived two geometrical description. This allows to create the head models

    cfg = [];
    cfg.method = 'bemcp';
    headmodel_fiducial = ft_prepare_headmodel(cfg, template_fiducial);

    cfg = [];
    cfg.method = 'bemcp';
    headmodel_surface = ft_prepare_headmodel(cfg, template_surface);

## Discussion

We introduced two different ways to create individualized head models, when no anatomical MRI is available. One uses three fiducials, while the other uses the whole head surface. Using the fiducials requires a minimal investment of digitizing three locations on the head surface. In using the whole head surface we can obtain a more realistic description of the individual head model, but this requires more lab time than the other approach.
