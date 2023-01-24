---
title: Creating a BEM volume conduction model of the head for source-reconstruction of EEG data
tags: [tutorial, eeg, source, headmodel, mri, plotting, meg-language]
---

# Creating a BEM volume conduction model of the head for source-reconstruction of EEG data

## Introduction

In this tutorial you can find information about how to construct a Boundary Element Method (BEM) volume conduction model of the head, also known as head model, based on an individual subject's anatomical MRI. For didactic resons we will use the anatomical MRI corresponding to the data that was also analyzed in other tutorials. The anatomical MRI data is included in the [Subject01.zip](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip) MEG dataset.

In reality we did _not_ record EEG data for this subject. To demonstrate the EEG volume conduction model, we will "cheat" and use an EEG dataset from another recording in which we did not have an anatomical MRI. Although this results in a bit of a Frankenstein dataset, it does allows us to demonstrate how to build an EEG head model and how to align the electrodes.

This tutorial will **not** show how to perform the source reconstruction itself. If you are interested in source reconstruction methods, you can go to the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and to the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

Furthermore, if you are interested in MEG head models, you can go to the corresponding [MEG tutorial](/tutorial/headmodel_meg).

## Background

{% include /shared/tutorial/sourcelocalization_background.md %}

This tutorial is focusing on how to build the **volume conduction model for the head**, which is also known as the **head model**.

{% include /shared/tutorial/headmodel_background.md %}

{% include markup/info %}
If you do not have an MRI for your subject, you can consider to use a template MRI or a template head model that is located in the FieldTrip `template` directory. See [here](/template/headmodel) for more info.

If you do not have an MRI but do have a measurement of the scalp surface and/or of the electrodes (e.g., with a Polhemus tracker), you can also fit a concentric spheres model to the scalp and/or electrodes. However, we recommend to use a realistic template head model and fit the measured electrodes to the template head model rather than the other way around.
{% include markup/end %}

## Procedure

Here, we will work towards a volume conduction model of the head based on the boundary element method (BEM). The BEM makes use of the realistic shjape of the  interfaces (the boundaries) between the skin, skull and brain surfaces. The outline is that we will classify each of the voxels in an anatomical MRI as one of the known tissue types; this is termed **segmentation**. Following the segmentation, we construct a triangulated mesh that describes each surface. Finally, the BEM model will be computed.

The anatomical MRI of the [tutorial data set](/tutorial/meg_language) is available [here](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip). Although we did not record EEG in this particular language study, we will nevertheless use it as example MRI to make an BEM volume conduction model for EEG.

-   we read the anatomical data with **[ft_read_mri](/reference/fileio/ft_read_mri)**
-   if needed, we use **[ft_volumerealign](/reference/ft_volumerealign)** to align the MRI with the desired coordinate system
-   if needed, we use **[ft_volumereslice](/reference/ft_volumereslice)** to ensure that the voxels are isotropic
-   we segment the anatomical information into different tissue types with **[ft_volumesegment](/reference/ft_volumesegment)**
-   we triangulate the boundaries between the tissues with **[ft_prepare_mesh](/reference/ft_prepare_mesh)**
-   we create the headmodel with **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**

Throughout the process we use **[ft_sourceplot](/reference/ft_sourceplot)**, **[ft_plot_mesh](/reference/plotting/ft_plot_mesh)** and **[ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)** to check that each of the steps was executed correctly.

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure1.png" %}

_Figure 2. Pipeline for creating a BEM model_

### Reading in the anatomical data

Before starting with FieldTrip, it is important that you set up your [MATLAB path](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path) properly.

    cd <path_to_fieldtrip>
    ft_defaults

Then, you can read in the anatomical MRI data.

    mri = ft_read_mri('Subject01.mri');

    disp(mri)
              dim: [256 256 256]
          anatomy: [256x256x256 int16]
              hdr: [1x1 struct]
        transform: [4x4 double]
         coordsys: 'ctf'

The structure of the `mri` variable contains the following fields:

-   `dim` gives information on the size (i.e. the number of voxels) of the anatomical volume into each direction
-   `anatomy` is a matrix (with the size and number of dimensions specified in `dim`) that contains the anatomical information
-   `hdr` contains the detailled header information from the original file, it contents vary, depending on the file format
-   `transform` is a homogenous [transformation matrix](/faq/homogenous) that allows expressing the voxel positions (in the field `anatomy`) in a certain coordinate system
-   `coordsys` specifies the coordinate system

You can see that in the data we just read in the `coordsys` specifies that it is already aligned to the [CTF coordinate system](/faq/coordsys#details-of-the-ctf-coordinate-system).

### Align the MRI to the head coordinate system

The EEG head model needs to be expressed in the same coordinate system as the electrodes and the source model. It is not really relevant which specific coordinate system is used, as long as all are consistently [aligned](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions).

As the very first step, we recommend to use **[ft_volumerealign](/reference/ft_volumerealign)** to align the anatomical MRI to the coordinate system that you want to use in your source reconstruction. If you want to align the anatomical MRI to the CTF coordinate system, you need to specify the anatomical landmarks (LPA, RPA and nasion) and the MRI will be translated and rotated such that the axes of the coordinate systems pass thorugh these landmarks.

The output of any later processing step on the MRI (reslicing, segmentation, mesh, headmodel) will consequently be expressed in the same coordinate system as the anatomical MRI.  Once the anatomical processing on the basis of the MRI is done, you can align the electrodes to the same anatomical landmarks and/or you can fit the electrodes interactively on the scalp surface of your head model.

In this specific case the anatomical MRI is already aligned to the CTF coordinate system; you can check this yourself with **[ft_determine_coordsys](/reference/utilities/ft_determine_coordsys)**. Therefore, we do not need to align the anatomical MRI to any other convention.

{% include markup/info %}
It is also possible to read in anatomical MRI data in [other formats](/faq/dataformat), which are defined in [a different coordinate system](/faq/coordsys). When you read in your own anatomical data, it may does not give information on the coordinate system in which the anatomical data is expressed and/or maybe there is no transformation matrix specified. In this case, you can check the coordinate-system with the **[ft_determine_coordsys](/reference/utilities/ft_determine_coordsys)** function.
{% include markup/end %}

### Reslicing

The segmentation of the anatomical MRI works best if the voxels are isotropic, i.e., if the size of the voxel is identical in each direction. If you do not have isotropic voxels, or you are not sure, you can use the **[ft_volumereslice](/reference/ft_volumereslice)** function to interpolate the anatomical MRI onto isotropic voxels. You can read more about reslicing in this [frequently asked question](/faq/how_change_mri_orientation_size_fov).

An advantage of reslicing is that it also aligns the voxels with the axes of the coordinate system, thereby avoiding it being plotted [upside down](/faq/my_mri_is_upside_down_is_this_a_problem) later in the pipeline.

### Segmentation

In this step, the voxels of the anatomical MRI are segmented or classified using **[ft_volumesegment](/reference/ft_volumesegment)** into the three different tissue types: scalp, skull and brain. You can read more about how the tissue-types are represented in the output of this function in this [FAQ](/faq/how_is_the_segmentation_defined).

{% include markup/info %}
The segmentation is quite time consuming (~15mins). For the purpose of this tutorial you can skip this and load the result and move on to the next step. You can download the result from our [download server](https://download.fieldtriptoolbox.org/tutorial/headmodel_eeg_bem/).
{% include markup/end %}

    cfg           = [];
    cfg.output    = {'brain', 'skull', 'scalp'};
    segmentedmri  = ft_volumesegment(cfg, mri);

    save segmentedmri segmentedmri

    disp(segmentedmri)
            dim: [256 256 256]
        transform: [4x4 double]
         coordsys: 'ctf'
             unit: 'mm'
            brain: [256x256x256 logical]
            skull: [256x256x256 logical]
            scalp: [256x256x256 logical]
              cfg: [1x1 struct]

The `segmentedmri` data structure is similar to the `mri` data structure, but contains the additional fields

-   `brain`: binary representation of the brain
-   `skull`: binary representation of the skull
-   `scalp`: binary representation of the scalp

The segmentation does not change the coordinate system, nor the size of the volume. You can see this in the first three fields (`dim`, `transform` and `coordsys`) which are the same as the corresponding fields in the MRI. But now, the field `transform` aligns the matrix in field `brain`, `skull` and `scalp` to the coordinate system defined in the `coordsys` field. It is good practice to check at this point in a figure, whether the segmented compartments look as expected.

{% include markup/warning %}
Occasionally, the quality of the anatomical image is not sufficient to provide a good segmentation out-of-the-box. This for example happens if there are large spatial inhomogeneities in the MRI that are caused by the anatomical MRI being acquired while the subject was wearing an EEG cap. The **[ft_volumebiascorrect](/reference/ft_volumebiascorrect)** function allows correcting for these inhomogeneities. For more information, you can consult this [frequently asked question](/faq/why_does_my_eegheadmodel_look_funny).
{% include markup/end %}

### Construct meshes for the boundaries

In this step, triangulated surface meshes are created at the borders of the different tissue-types using **[ft_prepare_mesh](/reference/ft_prepare_mesh)**. The output consists of surfaces represented by points or vertices that are connected in triangles. The tissues from which the surfaces are created have to be specified and also the number of vertices for each tissue.

    cfg = [];
    cfg.tissue      = {'brain','skull','scalp'};
    cfg.numvertices = [3000 2000 1000];
    mesh = ft_prepare_mesh(cfg,segmentedmri);

    save mesh mesh

     disp(mesh(1))
         pnt: [3000x3 double]
         tri: [5996x3 double]
        unit: 'mm'

The mesh structure contains the following field

-   `pos` represents the (x,y,z) coordinate of alll vertices of the surface.
-   `tri` each row defines the indices (the row numbers) of three vertices that form a triangle
-   `unit` describes the units in which the points are expressed

The mesh is a structure array with the geometry of three surfaces. The first represents the boundaty between the brain and the inside of the skull, the second the outside surface of the skull, and the third represents the boundary between the scalp and the air.

### Head model

The scalp, skull and brain mask have already been segmented and surface descriptions of the boundaries have been constructed. Now, we will use **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** to create the actual volume conduction model.

Here we will specify the 'dipoli' method, but there are [other methods](/faq/what_kind_of_volume_conduction_models_are_implemented) to build a BEM model. Some of these methods are not supported on all platforms (windows/macos/linux), some of them are more accurate, and some of them do not come pre-packaged and are more hassle to install. If 'dipoli' does not work for you, you can try 'openmeeg' or 'bemcp'. To skip this step and continue with the tutorial, you can also download the result from our [download server](https://download.fieldtriptoolbox.org/tutorial/headmodel_eeg_bem/).

    % Create a volume conduction model
    cfg        = [];
    cfg.method = 'dipoli'; % You can also specify 'openmeeg', 'bemcp', or another method
    headmodel  = ft_prepare_headmodel(cfg, bnd);

    save headmodel headmodel

    disp(headmodel)
         bnd: [1x3 struct]
        cond: [0.3300 0.0041 0.3300]
         mat: [6000x6000 double]
        type: 'dipoli'
        unit: 'mm'
         cfg: [1x1 struct]

The headmodel data structure contains the following fields:

-   `bnd` contains the geometrical description of the head model.
-   `cond` conductivity of each surface
-   `mat` matrix
-   `type` describes the method that was used to create the headmodel.
-   `unit` the unit of measurement of the geometrical data in the bnd field

The `bnd` field is the same as the mesh that we created in the previous step. The head model also contains a conductivity value for each compartment and a matrix used for the volume conduction model. Note that, as the unit of measurement for the head model is 'mm', the EEG sensors should be also defined in 'mm'.

{% include markup/danger %}
The order in which different tissue types are represented in the output of **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** may depend on the volume conduction model you are using. Make sure to double-check which tissue type is represented where in headmodel.bnd.
{% include markup/end %}

### Visualization

The headmodel contains three structures in the `bnd` field. These are the geometrical descriptions of the scalp, skull and brain surfaces. First, we will plot each of the surfaces using the **[ft_plot_mesh](/reference/plotting/ft_plot_mesh)** function. Then, all surfaces will be plot together on the same figure.

    figure
    ft_plot_mesh(headmodel.bnd(3),'facecolor','none'); % scalp
    figure
    ft_plot_mesh(headmodel.bnd(2),'facecolor','none'); % skull
    figure
    ft_plot_mesh(headmodel.bnd(1),'facecolor','none'); %b rain

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure2.png" %}
{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure3.png" %}
{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure4.png" %}

_Figure 3. The geometry of the volume conduction model using BEM ('dipoli'): scalp (left), skull (middle) and brain (right)_

    ft_plot_mesh(headmodel.bnd(1), 'facecolor',[0.2 0.2 0.2], 'facealpha', 0.3, 'edgecolor', [1 1 1], 'edgealpha', 0.05);
    hold on
    ft_plot_mesh(headmodel.bnd(2),'edgecolor','none','facealpha',0.4);
    hold on
    ft_plot_mesh(headmodel.bnd(3),'edgecolor','none','facecolor',[0.4 0.6 0.4]);

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure5.png" width="350" %}

_Figure 4. The geometry of the volume conduction model. All surfaces (scalp:gray,skull:white,brain:green) plotted together_

You can look at the figure from different 3D view poiunts using the curved arrow in the MATLAB figure menu.

### Align the electrodes

The head model is expressed in head coordinates of the anatomical MRI (ctf [coordinate system](/faq/coordsys)). We need to define the electrode positions in the same head coordinate system. First, we plot the outermost layer of the head model (scalp) together with the electrodes to check if the alignment is necessary. We use a template set of electrodes which you can find in the FieldTrip/template/electrode/standard_1020.elc file.

    % you may need to specify the full path to the file
    elec = ft_read_sens('standard_1020.elc');

    disp(elec)
        chanpos: [97x3 double]
        elecpos: [97x3 double]
          label: {97x1 cell}
           type: 'ext1020'
           unit: 'mm'

The electrode positions are described in the `elecpos` field. The `label` field contains the name of the electrodes.

    % load volume conduction model
    load headmodel
    figure
    % plot the scalp surface from the head model
    ft_plot_mesh(headmodel.bnd(1), 'edgecolor','none','facealpha',0.8,'facecolor',[0.6 0.6 0.8]);
    hold on
    % electrodes
    ft_plot_sens(elec,'style', 'sk');

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure6.png" width="300" %}

_Figure 5._

The figure shows that the electrodes are not aligned with the scalp surface.

The electrodes can be aligned in two ways, which we will demonstrate below:

-   if there are anatomical landmarks which positions are known in the anatomical MRI and also relative to the electrodes, we can automatically align the electrode positions with a few lines of script or
-   if the exact position of anatomical landmarks are not known relative to the electrodes, we visualize the surface of the head and the electrodes on the same image, and we transform, rotate and scale the electrodes until they fit to the head surface according to our visual judgement.

#### Automatic alignment

First, we will align the electrodes automatically to the anatomical landmarks of the anatomical MRI. The head model was created from the same mri, therefore the electrodes will also be aligned to the head-model.

For the automatic alignment, we need three pieces of informatio

-   electrode positions
-   position of fiducial landmarks relative to the electrodes
-   position of fiducial landmarks in the anatomical MRI

In the template set of electrodes, the first three labels are: 'Nz', 'LPA' and 'RPA'. These labels show that the first three rows of the `elec.chanpos` field defines the position of the nasion, left and right PA (the landmarks of the CTF ) in _"electrode" coordinates_. We can use this information for the automatic alignment. But we also need to know the position of the same points in the anatomical MRI. We use an anatomical MRI which has been already aligned to these points, therefore we can find these coordinates in the header information.

    mri = ft_read_mri('Subject01.mri');

    disp(mri.hdr.fiducial.mri)
        nas: [87 60 116]
        lpa: [29 145 155]
        rpa: [144 142 158]

{% include markup/warning %}
If you do not have the position of the anatomical landmarks in your volume, you can use the **[ft_volumerealign](/reference/ft_volumerealign)** function to get those positions.
{% include markup/end %}

First, we get these positions in the CTF coordinate system using the transformation matrix of the mri and the ft_warp_apply function.

    nas = mri.hdr.fiducial.mri.nas;
    lpa = mri.hdr.fiducial.mri.lpa;
    rpa = mri.hdr.fiducial.mri.rpa;

    transm = mri.transform;

    nas = ft_warp_apply(transm,nas, 'homogenous');
    lpa = ft_warp_apply(transm,lpa, 'homogenous');
    rpa = ft_warp_apply(transm,rpa, 'homogenous');

Then, we align the position of the fiducials in the electrode structure (defined with labels 'Nz', 'LPA', 'RPA') to their ctf-coordinates that we acquired from the anatomical MRI (nas, lpa, rpa).

    % create a structure similar to a template set of electrodes
    fid.elecpos       = [nas; lpa; rpa];       % ctf-coordinates of fiducials
    fid.label         = {'Nz','LPA','RPA'};    % same labels as in elec
    fid.unit          = 'mm';                  % same units as mri

    % alignment
    cfg               = [];
    cfg.method        = 'fiducial';
    cfg.target        = fid;                   % see above
    cfg.elec          = elec;
    cfg.fiducial      = {'Nz', 'LPA', 'RPA'};  % labels of fiducials in fid and in elec
    elec_aligned      = ft_electroderealign(cfg);

    save elec_aligned elec_aligned;

We can check the alignment by plotting together the scalp surface with the electrodes.

    figure
    ft_plot_sens(elec_aligned,'style','sk');
    hold on
    ft_plot_mesh(headmodel.bnd(1),'facealpha', 0.85, 'edgecolor', 'none', 'facecolor', [0.65 0.65 0.65]); %scalp

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure7.png" width="350" %}

_Figure 6. Electrodes plotted together with the scalp surface._

{% include markup/warning %}
Some of the electrodes are below the skin in the front, while the electrodes in the back do not fit tightly to the head. This happened because there are [different conventions to define the fiducials](/faq/how_are_the_lpa_and_rpa_points_defined).

The anatomical MRI is expressed in CTF coordinates with the fiducials for the left and right ear [aligned with the ear canal](/faq/how_can_i_convert_an_anatomical_mri_from_dicom_into_ctf_format) according to DCCN conventions.

The description of the electrodes includes the position of the left and right pre-auriciular point proper, i.e., the point of the posterior root of the zygomatic arch lying immediately in front of the upper end of the tragus.
{% include markup/end %}

One way to fix the misalignment is to provide the location of consistent fiducial locations. In this case it could be implemented by specifying the LPA and RPA point in the anatomical MRI shifted approximately 20 mm more anterior.

In the subsequent section however, we try to improve the alignment of the electrodes interactively.

#### Interactive alignment

    cfg           = [];
    cfg.method    = 'interactive';
    cfg.elec      = elec_aligned;
    cfg.headshape = headmodel.bnd(1);
    elec_aligned  = ft_electroderealign(cfg);

Here, we only need to use translation. We can shift the x axis with a few mm (12). This will move the electrodes more towards the front of the head. (Note: the positive x is towards the nasion in the ctf ccordinate system.) The electrodes fit better to the head surface after the translation.

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure8.png" width="350" %}

_Figure 7. Aligned electrodes plotted together with the scalp surface_

This electrode structure can be used later when the leadfield is computed during source-reconstruction. During the computation of the leadfield, the electrodes will be projected onto the scalp surface.

### Exercise 1

{% include markup/info %}
Create a head model with method 'concentricspheres' that you fit on scalp, skull and brain surfaces, i.e. using the already made mesh.

Plot the head model in the same figure including the brain, skull and scalp. Check the help of **[ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)** for further options of the visualization (e.g., color, transparency) which help to see the spheres together with the actual surfaces in the mesh that results from the segmentation.

What is the difference between the spherical and the BEM model?
{% include markup/end %}

### Exercise 2

{% include markup/info %}
In exercise 1, you created a head model with method 'concentricspheres'. How is its geometrical description defined? What is the difference between the geometrical description of the concentric spheres model and BEM model?
{% include markup/end %}

## Summary and further reading

In this tutorial, it was explained how to build a volume conduction model of the head using a single subject anatomical MRI and the boundary element method (BEM) developed by Oostendorp and van Oosterom (1989). In the exercises, we compared the BEM model to a concentric spheres model that was fitted on the scalp, skull and brain surfaces.

You can read more about specific source-reconstruction methods in the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and in the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

Here are the related FAQs:

{% include seealso tag1="faq" tag2="headmodel" tag3="eeg" %}

and the related examples:

{% include seealso tag1="example" tag2="headmodel" tag3="eeg" %}
