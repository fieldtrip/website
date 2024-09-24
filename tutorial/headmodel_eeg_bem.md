---
title: Creating a BEM volume conduction model of the head for source reconstruction of EEG data
category: tutorial
tags: [eeg, source, headmodel, mri, plotting, meg-language]
---

# Creating a BEM volume conduction model of the head for source reconstruction of EEG data

## Introduction

This tutorial demonstrates how to construct a Boundary Element Method (BEM) volume conduction model of the head, also known as head model, based on an individual subject's anatomical MRI. For didactic reasons we will use the anatomical MRI corresponding to the data that was also analyzed in other tutorials. The original anatomical MRI data, along with the (intermediate) results of this tutorial, can be downloaded from [out download server](https://download.fieldtriptoolbox.org/tutorial/headmodel_eeg_bem/).

In reality we did _not_ record EEG data for this subject, nor do we have recorded electrode positions. To demonstrate the EEG volume conduction model, we will use [template](/template/electrode) electrodes. The template electrodes are not aligned with the individual MRI and head model, hence towards the end we will demonstrate how to align the template electrodes with the model.

This tutorial will **not** show how to perform the source reconstruction itself. If you are interested in source reconstruction methods, you can go to the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and to the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

We have another tutorial that demonstrates how to make a [Finite Element Method (FEM) headmodel for EEG](/tutorial/headmodel_eeg_fem). Furthermore, if you are interested in MEG head models, we recommend that you go to the corresponding [MEG tutorial](/tutorial/headmodel_meg).

## Background

{% include /shared/tutorial/sourcelocalization_background.md %}

This tutorial is focusing on how to build the **BEM volume conduction model for the head**, which is also known as the **head model**.

{% include /shared/tutorial/headmodel_background.md %}

{% include markup/skyblue %}
If you do not have an MRI for your subject, you can consider to use a template MRI or a template head model that is located in the FieldTrip `template` directory. See [here](/template/headmodel) for more info.

If you do not have an MRI, but do have a measurement of the scalp surface and/or of the electrodes (e.g., with a Polhemus tracker), you could also fit a concentric spheres model to the scalp and/or electrodes. However, we recommend to use a realistic template head model and fit the measured electrodes to the template head model rather than the other way around.
{% include markup/end %}

## Procedure

Here, we will work towards a boundary element method (BEM) volume conduction model of the head. The BEM makes use of the realistic shape of the  interfaces (the boundaries) between the skin, skull and brain surfaces. The procedure  starts with classifying each of the voxels in the anatomical MRI as one of the tissue types that we want to model; this is termed **segmentation**. Following the segmentation, we construct triangulated meshes that describe the boundaries. Finally, the BEM model will be computed using the conductivities of the corresponding tissue types.

The anatomical MRI of the [tutorial data set](/tutorial/meg_language) is available [here](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip). Although we did not record EEG in this study, we will nevertheless use it as example MRI to make an BEM volume conduction model for EEG.

-   we read the anatomical data with **[ft_read_mri](/reference/fileio/ft_read_mri)**
-   if needed, we use **[ft_volumerealign](/reference/ft_volumerealign)** to align the MRI with the desired coordinate system
-   if needed, we use **[ft_volumereslice](/reference/ft_volumereslice)** to ensure that the voxels are isotropic
-   we segment the anatomical information into different tissue types with **[ft_volumesegment](/reference/ft_volumesegment)**
-   we triangulate the boundaries between the tissues with **[ft_prepare_mesh](/reference/ft_prepare_mesh)**
-   we create the headmodel with **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**

Throughout the process we use **[ft_sourceplot](/reference/ft_sourceplot)**, **[ft_plot_mesh](/reference/plotting/ft_plot_mesh)** and **[ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)** to check that each of the steps was executed correctly.

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure1.png" width="400" %}

_Figure; Pipeline for creating a BEM model_

{% include /shared/tutorial/headmodel_read_align.md %}

#### Exercise 1

{% include markup/skyblue %}
Check that the homogenous transformation matrix in `mri_realigned` is the same as the one in `mri`. If so, that means that each voxel is at exactly the same position. If you misspecify the voxel indices of the fiducials or anatomical landmarks, they will be different.
{% include markup/end %}

### Reslicing

The segmentation of the anatomical MRI into brain, skull and scalp works best if the voxels are isotropic, i.e., if the size of the voxel is identical in each direction. If you do not have isotropic voxels, or you are not sure, you can use the **[ft_volumereslice](/reference/ft_volumereslice)** function to interpolate the anatomical MRI onto isotropic voxels. You can read more about reslicing in this [frequently asked question](/faq/how_change_mri_orientation_size_fov).

An advantage of reslicing is that it also aligns the voxels with the axes of the coordinate system, thereby avoiding it being plotted [upside down](/faq/my_mri_is_upside_down_is_this_a_problem) later in the pipeline.

    cfg = [];
    cfg.method = 'linear';
    mri_resliced = ft_volumereslice(cfg, mri_realigned);

    save mri_resliced mri_resliced

Following the reslicing, the MRI should be shown with the correct side up, the field-of-view should be symmetric from left to right. If you move along the first axis, you should see that the first voxel index `i` increase _and_ that the `x` position increases (idem for `j/y` and `k/z`).

    cfg = [];
    cfg.method = 'ortho';
    ft_sourceplot(cfg, mri_resliced)

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure4.png" width="600" %}

_Figure; The MRI after assigning the desired coordinate system and reslicing_

### Segmentation

In this step, the voxels of the anatomical MRI are segmented or classified using **[ft_volumesegment](/reference/ft_volumesegment)** into the three different tissue types: scalp, skull and brain. You can read more about how the tissue-types are represented in the output of this function in this [FAQ](/faq/how_is_the_segmentation_defined).

{% include markup/skyblue %}
The segmentation is quite time consuming (~15 minutes). For the purpose of this tutorial you can skip this and load the result and move on to the next step. You can download the result from our [download server](https://download.fieldtriptoolbox.org/tutorial/headmodel_eeg_bem/).
{% include markup/end %}

    cfg           = [];
    cfg.output    = {'brain', 'skull', 'scalp'};
    segmentedmri  = ft_volumesegment(cfg, mri_resliced);

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

The `segmentedmri` data structure is similar to the `mri` data structure, but contains the additional fields:

-   `brain`: binary representation of the brain
-   `skull`: binary representation of the skull
-   `scalp`: binary representation of the scalp

The segmentation does not change the coordinate system, nor the size of the voxels or volume. You can see this in the first three fields (`dim`, `transform` and `coordsys`) which are the same as the corresponding fields in the MRI. The field `transform` aligns the 3D array in `brain`, `skull` and `scalp` to the coordinate system defined in the `coordsys` field, just like it did for the `anatomy` field in the anatomical MRI. It is good practice to check at this point in a figure, whether the segmented compartments look as expected.

{% include markup/yellow %}
Occasionally, the quality of the anatomical image is not sufficient to provide a good segmentation out-of-the-box. This for example happens if there are large spatial inhomogeneities in the MRI that are caused by the anatomical MRI being acquired while the subject was wearing an EEG cap. The **[ft_volumebiascorrect](/reference/ft_volumebiascorrect)** function allows correcting for these inhomogeneities. The **[ft_defacevolume](/reference/ft_defacevolume)** function can be used to erase parts of the MRI where there should be no signal, for example artifacts outside the head.

For more information, you can consult this [frequently asked question](/faq/why_does_my_eegheadmodel_look_funny).
{% include markup/end %}

The first thing to check is whether the segmented volumes have a reasonable size. The brain compartment should be about 1300-1600 ml, and the skull compartment about 400-500 ml when using `cfg.spmmethod='old'` which results in the "inflated brain" as skull compartment (see figure below). The volume of the scalp compartment can be arbitrarily large, as it extends to the neck.

    ft_checkdata(segmentedmri, 'feedback', 'yes') % display some information about the segmentation

    the input is segmented volume data with dimensions [256 256 256]
    voxel size along 1st dimension (i) : 1.000000 mm
    voxel size along 2nd dimension (j) : 1.000000 mm
    voxel size along 3rd dimension (k) : 1.000000 mm
    volume per voxel                   : 1.000000 mm^3
    the volume of each of the segmented compartments is
    brain           :     1573 ml (  9.37 %)
    scalp           :     2229 ml ( 13.29 %)
    skull           :      452 ml (  2.69 %)
    total segmented :     4254 ml ( 25.35 %)
    total volume    :    16777 ml (100.00 %)

We can change the segmentation from the probabilistic (or in this case Boolean) representation into an indexed representation; this represents the tissue types by successive integers, which we can plot together color-codes in a single image.

    segmentedmri_indexed = ft_checkdata(segmentedmri, 'segmentationstyle', 'indexed')

    disp(segmentedmri_indexed)
              dim: [256 256 256]
        transform: [4x4 double]
         coordsys: 'ctf'
             unit: 'mm'
              cfg: [1x1 struct]
           tissue: [256x256x256 double]
      tissuelabel: {'scalp'  'skull'  'brain'}

After adding the anatomical data to the segmentation, we can plot them together. By specifying our own colormap, we can be sure that the tissue types have clearly distinguishable colors.

    segmentedmri_indexed.anatomy = mri_resliced.anatomy;

    cfg = [];
    cfg.method = 'ortho';
    cfg.anaparameter = 'anatomy';
    cfg.funparameter = 'tissue';
    cfg.funcolormap = [
      0 0 0
      1 0 0
      0 1 0
      0 0 1
      ];
    ft_sourceplot(cfg, segmentedmri_indexed)

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure5.png" width="600" %}

_Figure; The segmented MRI plotted on top of the anatomy_

When visualizing the volume, we should check that the skull and scalp compartment have a consistent thickness, and that both the skull and scalp are neither too thin, nor too thick anywhere. The meshes that we construct in the next step need to be non-intersecting; a very thin layer in the segmentation requires a very fine mesh to prevent it from touching another mesh.

### Construct meshes for the boundaries

In this step, triangulated surface meshes are created at the borders between the different tissue types using **[ft_prepare_mesh](/reference/ft_prepare_mesh)**. The output consists of surfaces represented by points or vertices that are connected in triangles. The tissues from which the surfaces are created have to be specified and also the number of vertices for each tissue. Since the potential changes the most rapidly on the outside of the brain (or inside of the skull), we want that surface to be the most detailed. The potential does not change rapidly over the scalp, so that can remain relatively coarse. It is common to use the ratio 3/2/1 for the scalp/skull/brain.

    cfg = [];
    cfg.tissue      = {'brain', 'skull', 'scalp'};
    cfg.numvertices = [3000 2000 1000];
    mesh = ft_prepare_mesh(cfg, segmentedmri);

    save mesh mesh

     disp(mesh(1))
         pos: [3000x3 double]
         tri: [5996x3 double]
        unit: 'mm'
    coordsys: 'ctf'

The mesh structure is an array with three surfaces. Each surface contains the (x,y,z) positions of all vertices in `pos` and the triangulation in `tri`, in which each row defines the indices (the row numbers) of three vertices that form a triangle. The first surface represents the boundary between the brain and the inside of the skull, the second the outside surface of the skull, and the third represents the boundary between the scalp and the air.

### Visualization

The meshes can be plotted individually using **[ft_plot_mesh](/reference/plotting/ft_plot_mesh)**.

    figure
    ft_plot_mesh(mesh(1), 'facecolor', 'none'); % brain
    view([0 -1 0]); % from the right side

    figure
    ft_plot_mesh(mesh(2), 'facecolor', 'none'); % skull
    view([0 -1 0]); % from the right side

    figure
    ft_plot_mesh(mesh(3), 'facecolor', 'none'); % scalp
    view([0 -1 0]); % from the right side

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure6.png" width="350" %}
{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure7.png" width="350" %}
{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure8.png" width="350" %}

_Figure; The geometry of the BEM surface meshes: brain (top), skull (middle) and scalp (bottom)_

Using the curved arrow in the MATLAB figure menu or the [rotate3d](https://www.mathworks.com/help/matlab/ref/matlab.graphics.interaction.internal.rotate3d.html) or [view](https://nl.mathworks.com/help/matlab/ref/view.html) commands, you can turn and look at it from different view points.

You can make more life-like images by changing the color, adding lights and/or changing the reflective parameters of the 3D model. Besides the default skin tone, you can also explicitly use 'skin_light',' skin_medium_light', 'skin_medium', 'skin_medium_dark', or 'skin_dark'.

    figure
    ft_plot_mesh(mesh(3), 'facecolor', 'skin')
    camlight

    % using another skin tone and better lighting
    figure
    ft_plot_mesh(mesh(3), 'facecolor', 'skin_dark')
    lighting gouraud  % default is flat
    material dull     % ranges from dull, default, shiny, metal
    light(gca, 'Position', [+1  0  0])
    light(gca, 'Position', [-1  0  0])
    light(gca, 'Position', [ 0 +1  0])
    light(gca, 'Position', [ 0 -1  0])
    light(gca, 'Position', [ 0  0 +1])
    light(gca, 'Position', [ 0  0 -1])

Since the potential does not change that rapidly on the scalp, it is sufficient for the volume conduction model to have a relatively coarse scalp triangulation. However, if you want to make better quality figures, you might want to make a mesh of the scalp with many more vertices; this is something we will do further down when aligning the electrodes.

We can also plot the surfaces together in the same figure. This allows us to see how the meshes relate spatially to each other.

    figure
    ft_plot_mesh(mesh(1), 'facecolor','r', 'facealpha', 1.0, 'edgecolor', 'k', 'edgealpha', 1);
    hold on
    ft_plot_mesh(mesh(2), 'facecolor','g', 'facealpha', 0.4, 'edgecolor', 'k', 'edgealpha', 0.1);
    hold on
    ft_plot_mesh(mesh(3), 'facecolor','b', 'facealpha', 0.4, 'edgecolor', 'k', 'edgealpha', 0.1);

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure9.png" width="600" %}

_Figure; The geometry of the BEM surface meshes: all surfaces plotted together_

### Head model

Now that the scalp, skull and brain have been segmented and surface descriptions have been constructed for each, we will use **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** to create the actual volume conduction model.

Here we will specify the 'dipoli' method, but there are [other methods](/faq/what_kind_of_volume_conduction_models_are_implemented) to build a BEM model. Some of these methods are not supported on all platforms (Windows/macOS/Linux), some of them are more accurate, and some of them do not come pre-packaged and are more of a hassle to install. If 'dipoli' does not work for you, you can try 'openmeeg' or 'bemcp'. To skip this step and continue with the tutorial, you can also download the result from our [download server](https://download.fieldtriptoolbox.org/tutorial/headmodel_eeg_bem/).

    % Create a volume conduction model
    cfg        = [];
    cfg.method = 'dipoli'; % You can also specify 'openmeeg', 'bemcp', or another method
    headmodel  = ft_prepare_headmodel(cfg, mesh);

    save headmodel_dipoli headmodel

    disp(headmodel)
         bnd: [1x3 struct]
        cond: [0.3300 0.0041 0.3300]
         mat: [6000x6000 double]
        type: 'dipoli'
    coordsys: 'ctf'
        unit: 'mm'
         cfg: [1x1 struct]

The headmodel data structure contains the following fields:

-   `bnd` contains the geometrical description of each boundary
-   `cond` conductivity of each compartment
-   `mat` the BEM "system" matrix that relates the potention of each of the 3000+2000+1000 vertices to each other vertex
-   `type` describes the method that was used to create the headmodel

The `bnd` field is the same as the mesh that we created in the previous step. The head model also contains a conductivity value for each compartment and a matrix used for the volume conduction model. Note that, as the unit of measurement for the head model is 'mm' and the coordsys is 'ctf', the EEG sensors should be also defined in 'mm' and the CTF coordinate system.

{% include markup/red %}
The order in which the different boundaries and tissue types are represented in the output of **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** may depend on the BEM method you are using.
{% include markup/end %}

### Align the electrodes to the head model

There are many EEG manufacturers and almost as many EEG electrode placement systems. Here we will read an extended version of the 10-20 system from the `fieldtrip/template` directory.

    % you may need to specify the full path to the file
    elec = ft_read_sens('standard_1020.elc');

    disp(elec)
        chanpos: [97x3 double]
       chantype: {97x1 cell}
       chanunit: {97x1 cell}
        elecpos: [97x3 double]
          label: {97x1 cell}
           type: 'eeg1010'
           unit: 'mm'

The electrode positions are described in the `elecpos` field and the `label` field contains the name of the electrodes. See this [frequently asked question](/faq/how_are_electrodes_magnetometers_or_gradiometers_described) for more details.

The head model is expressed in the same units and coordinates as the anatomical MRI, in this case the CTF [coordinate system](/faq/coordsys)). Therefore, the electrode positions need to be specified accordingly. We can do a first check with

    elec = ft_determine_coordsys(elec)

    Do you want to change the anatomical labels for the axes [Y, n]? y
    What is the anatomical label for the positive X-axis [r, l, a, p, s, i]? r
    What is the anatomical label for the positive Y-axis [r, l, a, p, s, i]? a
    What is the anatomical label for the positive Z-axis [r, l, a, p, s, i]? s
    Is the origin of the coordinate system at the a(nterior commissure), i(nterauricular), s(scanner origin), n(ot a landmark)? n

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure10.png" width="600" %}

_Figure; Determine the coordinate system in which the original electrodes are expressed_

We cannot see what the origin of the coordinate system is aligned to. It is definitely _not_ interauricular, as none of the axes passes (approximately) through the ears. By answering the questions, we can establish that the electrodes are in a RAS coordinate system with the first positive x axis pointing to Right, the second positive y axis to Anterior and the third positive z axis to Superior.

{% include markup/green %}
The specific template electrode set that we are using here is in fact coregistered with the MNI coordinate system. It is documented in more detail [here](/template/electrode/) and the corresponding template BEM headmodel is documented [here](/template/headmodel/#standard_bemmat).
{% include markup/end %}

#### Manual alignment of the template electrodes

To align the template electrodes with the head model, we can take the scalp surface that we constructed earlier. However, that is (for computational reasons) relatively coarse. We can also make a new scalp surface description with more detail. If we align the electrodes with that, they will also be aligned with the lower resolution head model.

    cfg = [];
    cfg.tissue      = 'scalp';
    cfg.numvertices = 10000;
    scalp = ft_prepare_mesh(cfg, segmentedmri);

    save scalp scalp

We can plot the electrode positions together with the

    figure
    ft_plot_mesh(scalp, 'edgecolor','none', 'facecolor', 'skin', 'facealpha', 0.6);
    hold on
    ft_plot_sens(elec, 'elecshape', 'sphere', 'label', 'on');

    % put some lights around the whole scene, but not too bright
    material dull
    light(gca, 'Position', [+1  0  0], 'Color', [1 1 1]/2)
    light(gca, 'Position', [-1  0  0], 'Color', [1 1 1]/2)
    light(gca, 'Position', [ 0 +1  0], 'Color', [1 1 1]/2)
    light(gca, 'Position', [ 0 -1  0], 'Color', [1 1 1]/2)
    light(gca, 'Position', [ 0  0 +1], 'Color', [1 1 1]/2)
    light(gca, 'Position', [ 0  0 -1], 'Color', [1 1 1]/2)

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure11.png" width="600" %}

_Figure; Template electrodes are not yet aligned with the scalp surface._

It is quite clear that the electrodes are not aligned with the scalp surface, they are rotated by 90 degrees, shifted (aka translated), and also appear to have the incorrect overall scale.

We can use **[ft_electroderealign](/reference/ft_electroderealign)** for interactive alignment

    cfg            = [];
    cfg.method     = 'interactive';
    cfg.elec       = elec;
    cfg.headshape  = scalp;
    elec_realigned = ft_electroderealign(cfg);

    save elec_realigned elec_realigned

Since rotations and translations do not "commute", i.e. the order in which you execute the rotation matters, it can be confusing to specify all rotations and translations in one go. Instead, you can use the "apply" button to do the transformations stepwise.

In this situation we need

- rotate -90 around z; apply
- translate 35 along x and 35 along z; apply
- scale 0.98 along x, 0.90 along y, and 0.80 along z; apply
- translate 25 along z; apply
- rotate 11 degrees around y, translate -5 along x; apply
- quit

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure12.png" width="600" %}

_Figure; Use the GUI to align the electrodes_

    figure
    ft_plot_mesh(scalp, 'edgecolor','none', 'facecolor', 'skin', 'facealpha', 0.7);
    hold on
    ft_plot_sens(elec_realigned, 'elecshape', 'sphere', 'label', 'on');
    camlight

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure13.png" width="600" %}

_Figure; Realigned electrodes plotted together with the scalp surface_

This electrode structure can be used later when the leadfield is computed with **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)** and **[ft_sourceanalysis](/reference/ft_sourceanalysis)**, or with **[ft_dipolefitting](/reference/ft_dipolefitting)**. During the computation of the leadfield, the electrodes will be projected exactly onto the scalp surface, so don't worry if the fit is not yet 100% perfect.

#### Automatic placement based on the anatomical landmarks

When working with EEG recorded from electrodes placed according to the 10-20 system, we can also use **[ft_electrodeplacement](/reference/ft_electrodeplacement)** to determine the electrodes. For that we first need to determine the anatomical landmarks, which are sometimes - incorrectly - referred to as fiducials.

We can use either the scalp surface to click on them:

    cfg = [];
    cfg.method = 'headshape';
    cfg.channel = {'nas', 'ini', 'lpa', 'rpa'};
    fiducials = ft_electrodeplacement(cfg, scalp);

Or we can use the anatomical MRI to identify them

    cfg = [];
    cfg.method = 'volume';
    cfg.channel = {'nas', 'ini', 'lpa', 'rpa'};
    fiducials = ft_electrodeplacement(cfg, mri_resliced);

    save fiducials fiducials

The headshape method is easiest for the pre-auricular points, as you can recognize the whole shape of the ears. The volume method is the easiest for the nasion, and by far the most accurate for the inion.

    disp(fiducials.elecpos)
      113.5789   -1.3870   -0.8349
      -74.8196    1.5368   34.6337
       20.4483   67.4268    3.3728
       16.4416  -70.3234    2.5651
    disp(fiducials.label)
      4x1 cell array
        {'nas'}
        {'ini'}
        {'lpa'}
        {'rpa'}

After having identified the anatomical landmarks, we can

    cfg           = [];
    cfg.method    = '1020';
    cfg.fiducial.nas = fiducials.elecpos(1,:);
    cfg.fiducial.ini = fiducials.elecpos(2,:);
    cfg.fiducial.lpa = fiducials.elecpos(3,:);
    cfg.fiducial.rpa = fiducials.elecpos(4,:);
    elec_placed = ft_electrodeplacement(cfg, scalp);

    save elec_placed elec_placed

Again we can plot the electrodes together with the head surface.

    figure
    ft_plot_mesh(scalp, 'edgecolor','none', 'facecolor', 'skin', 'facealpha', 1.0);
    hold on
    ft_plot_sens(elec_placed, 'elecshape', 'disc', 'label', 'on');
    camlight

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure14.png" width="600" %}

_Figure; High-density 1020 electrodes placed according to the anatomical landmarks on the scalp_

You can also plot the realigned template electrodes with the ones from the automatic 1020 placement scheme.

    figure
    ft_plot_sens(elec_realigned, 'elecshape', 'sphere', 'label', 'on', 'facecolor', 'r', 'fontcolor', 'r');
    ft_plot_sens(elec_placed, 'elecshape', 'sphere', 'label', 'on', 'facecolor', 'b', 'fontcolor', 'b');

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure15.png" width="600" %}

_Figure; Comparing the aligned template positions (red) and the automatically placed 1020 positions ((blue)_

### Exercise 2

{% include markup/skyblue %}
Create a head model with method 'concentricspheres' that you fit on scalp, skull and brain surfaces, i.e. using the already made mesh.

Plot the head model using **[ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)**. You can use `facealpha` for the transparency, this helps to see the spheres together.

What is the difference between the spherical and the BEM model?

Note that the scalp is unrealistically thick compared to the skull; this is because we fitted it to the whole head surface, all the way up to the neck. The lower part of the head - as well as the lower part of the brain and skull - are not very spherical. Therefore it is recommended to remove them from the meshes prior to fitting the spheres. You can use **[ft_defacemesh](/reference/ft_defacemesh)** to remove part of the meshes, usually the face, but here you would use it to remove the bottom half of the scalp, skull and brain surfaces.

{% include markup/end %}

### Exercise 3

{% include markup/skyblue %}
In exercise 2, you created a head model with method 'concentricspheres'. How is its geometrical description defined? What is the difference between the geometrical description of the concentric spheres model and BEM model?
{% include markup/end %}

## Summary and further reading

This tutorial explained how to build a volume conduction model of the head using a single subject anatomical MRI and the boundary element method (BEM) developed by Oostendorp and van Oosterom (1989). In the exercises, we also compared the BEM model to a concentric spheres model that was fitted on the scalp, skull and brain surfaces.

You can read more about specific source reconstruction methods in the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and in the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

### See also these frequently asked questions

{% include seealso category="faq" tag1="headmodel" tag2="eeg" %}

### See also these examples

{% include seealso category="example" tag1="headmodel" tag2="eeg" %}
