---
title: Creating a volume conduction model of the head for source reconstruction of MEG data
parent: Source reconstruction
grand_parent: Tutorials
category: tutorial
tags: [source, meg, headmodel, mri, plotting, meg-language]
redirect_from:
    - /tutorial/headmodel_meg/
---

# Creating a volume conduction model of the head for source reconstruction of MEG data

## Introduction

This tutorial describes how to construct a volume conduction model of the head (head model) based on an individual subject's MRI. We will use the anatomical images that belong to the same subject whose data were analyzed in the [Preprocessing - Segmenting and reading trial-based EEG and MEG data](/tutorial/preprocessing) and the [Event-related averaging and MEG planar gradient](/tutorial/eventrelatedaveraging) tutorials. The corresponding anatomical MRI data is available from the [download server](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip).

The volume conduction model of the head that will be constructed here is specific to the computation and source reconstruction of MEG data. Different strategies can be used for the construction of head models. The processing pipeline of the tutorial is an example which we think is the most appropriate for the tutorial-dataset.

This tutorial will **not** show how to perform the source reconstruction itself. If you are interested in source reconstruction methods, you can go to the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and to the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

{% include markup/green %}
The volume conduction model created here is MEG specific and cannot be used for EEG source reconstruction. If you are interested in EEG source reconstruction methods, you can go to the corresponding [EEG tutorial](/tutorial/headmodel_eeg).
{% include markup/end %}

## Background

{% include /shared/tutorial/sourcelocalization_background.md %}

This tutorial is focusing on how to build the **volume conduction model for the head**.

{% include /shared/tutorial/headmodel_background.md %}

In this specific tutorial we will use a semi-realistic head model developed by Nolte (2003) that assumes a realistic information about the interface between the brain and the skull. This outer brain surface will be extracted from the anatomical MRI images of the subject. First, we will use anatomical MRI of the subject to extract the brain surface from the anatomical images, which is termed **segmentation**. Note that the segmentation procedure is quite time consuming. Following the segmentation of the anatomical images, a description of the surface using vertices and triangles is constructed. Finally, the single-shell head model will be computed.

{% include markup/skyblue %}
If an anatomical MRI is not available for your MEG subject, you can consider to use a template MRI or a template head model that is located in the FieldTrip template directory. If you do not have an MRI, but if you do have a measurement of the scalp surface (e.g., with a Polhemus tracker), you can use a local spheres volume conduction model. If you do not want to (or cannot) use any realistic information about the brain-surface or the head-shape, you can resort to the single sphere volume conduction model.
{% include markup/end %}

## Procedure

We will create a head model based on the anatomical mri of the [tutorial data set](/tutorial/meg_language) which is available [here](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip). The pipeline is depicted in Figure 2.

- First, we will read the anatomical data with **[ft_read_mri](/reference/fileio/ft_read_mri)**;
- then we segment the anatomical information into different tissue types with **[ft_volumesegment](/reference/ft_volumesegment)**;
- and create the headmodel with **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**.
- Finally, we will check the geometry of the head model by plotting it with **[ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)**.

{% include image src="/assets/img/tutorial/headmodel_meg/figure1.png" width="250" %}

_Figure 2. Pipeline of creating and visualizing a head model_

### Reading in the anatomical data

Before starting to use FieldTrip, it is important that you set up your MATLAB path properly. You can read about how to set up your MATLAB path [here](/faq/installation).

    cd <path_to_fieldtrip>
    ft_defaults

Then, you can read in the mri data.

    mri = ft_read_mri('Subject01.mri');

    disp(mri)
              dim: [256 256 256]
          anatomy: [256x256x256 int16]
              hdr: [1x1 struct]
        transform: [4x4 double]
             unit: 'mm'
         coordsys: 'ctf'

The structure of your mri variable contains the following field

- **dim**: This field gives information on the size (i.e. the number of voxels) of the anatomical volume into each direction.
- **anatomy**: This is a matrix (with the size and number of dimensions specified in **dim**) that contains the anatomical information represented by numbers.
- **hdr**: Header information of the anatomical images.
- **transform**: A transformation matrix that aligns the anatomical data (in field **anatomy**) to a certain coordinate system.
- **coordsys**: The description of the coordinate system which the anatomical data is aligned to.

You can see that the **coordsys** field of anatomical data that we read in is already aligned to the [ctf coordinate system](/faq/coordsys#details_of_the_ctf_coordinate_system). This can be done using the CTF specific MRIConverter and MRIViewer software as outlined [here](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions) or using the **[ft_volumerealign](/reference/ft_volumerealign)** function.

{% include markup/skyblue %}
It is also possible to read in anatomical MRI data in [other formats](/faq/dataformat), which are defined in [a different coordinate system](/faq/coordsys). If your anatomical MRI is not aligned to the ctf coordinate system, it can be [aligned](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions) using **[ft_volumerealign](/reference/ft_volumerealign)** function. For this, you will need to align your MRI to the [fiducial
points](/faq/how_are_the_lpa_and_rpa_points_defined).

When you read in your own anatomical data, it may not give information on the coordinate system in which the anatomical data is expressed and/or maybe there is no [transformation matrix](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions) specified. In this case, you can check the coordinate-system with the **[ft_determine_coordsys](/reference/utilities/ft_determine_coordsys)** function.
{% include markup/end %}

### Segmentation

In this step, the voxels of the anatomical MRI are segmented (i.e. separated) into [different tissue types](/faq/how_is_the_segmentation_defined) . By default, the gray matter, white matter and the cerebro-spinal fluid (csf) compartments are differentiated. Based on these compartments a so called brainmask is created, which is a binary mask of the content inside the skull. All voxels that are inside the skull (i.e. the complete brain) are represented by 1, all other voxels by 0. The function **[ft_volumesegment](/reference/ft_volumesegment)** will produce the required output.

{% include markup/yellow %}
Note that the segmentation is quite time consuming and if you want you can load the result and skip ahead to the next step. You can download the segmented MRI of this tutorial data from the [download server](https://download.fieldtriptoolbox.org/tutorial/headmodel_meg/segmentedmri.mat) (segmentedmri.mat).
{% include markup/end %}

    cfg           = [];
    cfg.output    = 'brain';
    segmentedmri  = ft_volumesegment(cfg, mri);

    save segmentedmri segmentedmri

    disp(segmentedmri)
            dim: [256 256 256]
        transform: [4x4 double]
         coordsys: 'ctf'
             unit: 'mm'
            brain: [256x256x256 logical]
              cfg: [1x1 struct]

The segmentedmri data structure contains the following field

- **dim**

- **transform**

- **coordsys**

- **unit**: unit of measurement of the voxels

- **brain**: binary brainmask

- **cfg**: configuration information of the function which created segmentedmri

The segmentation does not change the coordinate system, nor the size of the volume. You can see this in the first three fields (dim, transform and coordsys) which are the same as the corresponding fields of the input mri data structure. But now, the field **transform** aligns the matrix in field **brain** (which contains the brainmask) to the coordinate system defined in the **coordsys** field.

Alternatively, you can also leave out the definition of the cfg.output. In this case, the function will output the default segmentation that are the probabilistic values of the gray, white and csf compartments. In this case, the brain mask will be automatically created in the next step by the ft_prepare_headmodel function. For further information on the different segmentation options, read the help of **[ft_volumesegment](/reference/ft_volumesegment)**.

### Head model

Once the brain mask is segmented out of the anatomical MRI, a surface description of the brain is constructed and the volume conduction model . We will specify method 'singleshell' to build the head model in the cfg.method field using **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**.

    cfg = [];
    cfg.method='singleshell';
    vol = ft_prepare_headmodel(cfg, segmentedmri);

    save vol vol

    disp(vol)
         bnd: [1x1 struct]
        type: 'singleshell'
        unit: 'mm'
         cfg: [1x1 struct]

The vol data structure contains the following field

- **bnd**: contains the geometrical description of the head model.

- **type**: describes the method that was used to create the headmodel.

- **unit**: the unit of measurement of the geometrical data in the bnd field

- **cfg**: configuration of the function that was used to create vol

The **bnd** field describes a surface with vertices and triangles (in the **bnd.pnt** and **bnd.tri** fields) as the geometrical description of the volume conductor.

{% include markup/skyblue %}
This tutorial does not intend to make a elaborative comparison of the different volume conduction models, nor to discuss their relative merits.

The method used in this tutorial is based on [Nolte G. (2003) The magnetic lead field theorem in the quasi-static approximation and its use for magnetoencephalography forward calculation in realistic volume conductors](http://www.ncbi.nlm.nih.gov/pubmed/14680264). We recommend this method for most general MEG situations.

The paper [Lalancette M, Quraan M, Cheyne D. (2011) Evaluation of multiple-sphere head models for MEG source localization](http://www.ncbi.nlm.nih.gov/pubmed/21828900) discusses another popular method for MEG forward modeling, which is based on fitting local spheres to the surface. This alternative method can be used by specifying 'localspheres' as method in **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**.

Alternatively, you can also create and use a multiple-layered head model with Openmeeg. For this you can follow the procedure described in the tutorial for [creating a volume conduction model for EEG data](/tutorial/headmodel_eeg_bem#head_model)
{% include markup/end %}

### Visualization

The head model contains the brain-skull boundary as the geometrical description of the head. You can visualize this using the following code. First, we will plot the sensors (MEG channels) with the **[ft_plot_sens](/reference/plotting/ft_plot_sens)** function. Second, we will plot the head model with **[ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)** in the same figure with the sensors. In order to plot also the location of the MEG channels, we read in the location of the channels using the .ds file from the tutorial data and the **[ft_read_sens](/reference/fileio/ft_read_sens)** function. The [Subject01.zip](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip) MEG dataset includes the MEG data and the anatomical MRI. The units of the headmodel are defined in 'mm', while the units of the sensors are in 'cm'. When we plot the headmodel together with the sensors, they need to have the same units. Therefore, the units of the headmodel will be converted to 'cm' with the **[ft_convert_units](/reference/forward/ft_convert_units)** function.

    vol = ft_convert_units(vol, 'cm');
    sens = ft_read_sens('Subject01.ds', 'senstype', 'meg');

    figure
    ft_plot_sens(sens, 'style', '*b');

    hold on
    ft_plot_headmodel(vol);

{% include image src="/assets/img/tutorial/headmodel_meg/figure2.png" width="300" %}

_Figure 3. The geometry of the volume conduction model of the head using method "singleshell"_

When the figure is plotted, you can look at the figure from different views using the curved arrow in the MATLAB figure menu. Note that there are 4 channels hovering above the normal channels; those are the MEG reference channels that can be used for environmental noise suppression.

### Exercise 1

{% include markup/skyblue %}
Create a head model with method 'singlesphere' that you fit on the inside brain surface, i.e. using the output of the already made segmentation.

Plot both head models in the same figure, check the help of **[ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)** for further options of the visualization (e.g., color, transparency) which help to see the two head models together.

What is the difference between the head models?
{% include markup/end %}

### Exercise 2

{% include markup/skyblue %}
In exercise 1, you created a head model with method 'singlesphere'. How is its geometrical description defined? What is the difference between the fields of the single sphere and single-shell model which contain the geometrical description?
{% include markup/end %}

## Summary and further reading

In this tutorial, it was explained how to build a volume conduction model of the head using a single subject anatomical mri and the single shell method developed by Nolte (2003). In the exercises, we compared the head model to a single sphere that was fitted on the inside brain surface.

You can read more about specific source reconstruction methods in the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and in the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

### See also these frequently asked questions

{% include seealso category="faq" tag1="headmodel" tag2="meg" %}

### See also these examples

{% include seealso category="example" tag1="headmodel" tag2="meg" %}
