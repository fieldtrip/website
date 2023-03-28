---
title: Creating a FEM volume conduction model of the head for source-reconstruction of EEG data
tags: [tutorial, eeg, source, headmodel, mri, plotting, meg-language]
---

# Creating a FEM volume conduction model of the head for source-reconstruction of EEG data

## Introduction

This tutorial demonstrates how to construct a Finite Element Method (FEM) volume conduction model of the head, also known as head model, based on an individual subject's anatomical MRI. For didactic resons we will use the anatomical MRI corresponding to the data that was also analyzed in other tutorials. The anatomical MRI data is included in the [Subject01.zip](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip) MEG dataset.

In reality we did _not_ record EEG data for this subject, nor do we have recorded electrode positions. To demonstrate the EEG volume conduction model, we will use [template](/template/electrode) electrodes. The template electrodes are not aligned with the individual MRI and head model, hence we will conclude with the alignment of the electrodes.

This tutorial will **not** show how to perform the source reconstruction itself. If you are interested in source reconstruction methods, you can go to the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and to the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

We have another tutorial that demonstrates how to make a [Boundary Element Method (BEM) headmodel for EEG](/tutorial/headmodel_eeg_bem). Furthermore, if you are interested in MEG head models, we recommend that you go to the corresponding [MEG tutorial](/tutorial/headmodel_meg).

{% include markup/warning %}
The FEM method described here is based on the SimBio software, which is described in detail [here](https://www.mrt.uni-jena.de/simbio/index.php/Main_Page#Welcome). The integration with FieldTrip is described in the paper below. Please cite this paper if you use the FieldTrip-SimBio pipeline in your research.

Vorwerk, J., Oostenveld, R., Piastra, M.C., Magyari, L., & Wolters, C. H. **The FieldTrip‐SimBio pipeline for EEG forward solutions.** BioMed Eng OnLine (2018). {% include badge doi="10.1186/s12938-018-0463-y" %}
{% include markup/end %}

## Background

{% include /shared/tutorial/sourcelocalization_background.md %}

This tutorial is focusing on how to build the **FEM volume conduction model for the head**, which is also known as the **head model**.

{% include /shared/tutorial/headmodel_background.md %}

{% include markup/info %}
If you do not have an MRI for your subject, you can consider to use a template MRI or a template head model that is located in the FieldTrip `template` directory. See [here](/template/headmodel) for more info.

If you do not have an MRI, but do have a measurement of the scalp surface and/or of the electrodes (e.g., with a Polhemus tracker), you could also fit a concentric spheres model to the scalp and/or electrodes. However, we recommend to use a realistic template head model and fit the measured electrodes to the template head model rather than the other way around.
{% include markup/end %}

## Procedure

Here, we will work towards a volume conduction model of the head based on the Finite Element Method (FEM). The FEM assumes realistic geometrical information about the head, including the skin, skull, csf, gray, and white matter. It can include more tissue types, and in contrast tp the BEM, the geometry of each tissue type can be arbitrary complex.

The procedure  starts with classifying each of the voxels in the anatomical MRI as one of the tissue types that we want to model; this is termed **segmentation**. Following the segmentation, we construct a tetrahedral or hexahedral mesh that describe the different tissue types. Finally, the FEM model will be computed using the conductivities of the corresponding tissue types.

The anatomical MRI of the [tutorial data set](/tutorial/meg_language) is available [here](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip). Although we did not record EEG in this study, we will nevertheless use it as example MRI to make an BEM volume conduction model for EEG.

-   we read the anatomical data with **[ft_read_mri](/reference/fileio/ft_read_mri)**
-   if needed, we use **[ft_volumerealign](/reference/ft_volumerealign)** to align the MRI with the desired coordinate system
-   if needed, we use **[ft_volumereslice](/reference/ft_volumereslice)** to flip the volume so that it points up
-   we segment the anatomical information into different tissue types with **[ft_volumesegment](/reference/ft_volumesegment)**
-   we make a mesh that describes all tissue types with **[ft_prepare_mesh](/reference/ft_prepare_mesh)**
-   we create the headmodel with **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**

Throughout the process we use **[ft_sourceplot](/reference/ft_sourceplot)**, **[ft_plot_mesh](/reference/plotting/ft_plot_mesh)** and **[ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)** to check that each of the steps was executed correctly.

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure1.png" width="400" %}

_Figure; Pipeline for creating a FEM model_

{% include /shared/tutorial/headmodel_read_align.md %}

#### Exercise 1

{% include markup/info %}
Check that the homogenous transformation matrix in `mri_realigned` is the same as the one in `mri`. If so, that means that each voxel is at exactly the same position. If you misspecify the voxel indices of the fiducials or anatomical landmarks, they will be different.
{% include markup/end %}

## Reslicing

A common issue with anatomical MRI data is that it is plotted [upside down](/faq/my_mri_is_upside_down_is_this_a_problem). This is not neccessarily a problem for the FEM model that we will make, as we know the position of each MRI voxel relative to the coordinate system, but it is a bit inconvenient in the plottting of MRI slices and quality control later in the pipeline.

The **[ft_volumereslice](/reference/ft_volumereslice)** function can be used to flip the volume such that the 1st dimension of the three-dimensional `mri.anatomy` array corresponds approximately with the x-axis of the coordinate system, that the 2nd dimension corresponds approximately to the y-axis, and the 3rd dimension to the z-axis.

Note that the axes of the coordinate system in general will not be exactly aligned with the orientation and direction of the slices of the MRI during acquisition.  You can also use **[ft_volumereslice](/reference/ft_volumereslice)** to properly reslice your anatomical MRI; in that case it will be interpolated onto a regular and isotropic grid in which the volume is alignbed with the axes and the size of the voxel is identical in each direction. This is recommended when you use morphological image operations such as [imerode](https://www.mathworks.com/help/images/ref/imerode.html) and [imdilate](https://www.mathworks.com/help/images/ref/imdilate.html), which is common for constructing the segmentation that underlies the triangulated surfaces for the boundary element method (BEM).

The following flips the volume such that the anatomical volume approximately aligns with the axes

    cfg = [];
    cfg.method = 'flip';
    mri_resliced = ft_volumereslice(cfg, mri_realigned);

If you would want to align it exactly with the axes and/or make the voxels isotropic, you could use the 'linear' method in **[ft_volumereslice](/reference/ft_volumereslice)**.

Following the reslicing, the MRI should be shown with the correct side up, the field-of-view should be symmetric from left to right. If you move along the first axis, you should see that the first voxel index `i` increase _and_ that the `x` position increases (idem for `j/y` and `k/z`).

    cfg = [];
    cfg.method = 'ortho';
    ft_sourceplot(cfg, mri_resliced)
    
{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figureX.png" width="600" %}

_Figure; The MRI after assigning the desired coordinate system and reslicing_

YOu should check that all parts of the head are present in the resliced images, including the nose, back of the head and the top of the head. If not, you need to redo the reslicing with a slightly modified vield of view.

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure2.png" width="250" %}
{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure3.png" width="250" %}

_Figure 3. MRI plotted before (left) and after reslicing (right)_

## Segmentation

In this step, the voxels of the anatomical MRI are segmented or classified using **[ft_volumesegment](/reference/ft_volumesegment)** into the three different tissue types: scalp, skull, csf (cerebro-spinal fluid), gray and white matter. You can read more about how the tissue-types are represented in the output of this function in this [FAQ](/faq/how_is_the_segmentation_defined). The resulting segmentation should be a binary representation of the 5 tissue types without overlap, i.e., each voxel belongs to exactly one tissue type.

{% include markup/warning %}
Note that the segmentation is quite time consuming (~15mins) and if you want you can load the result and skip ahead to the next step. You can download the segmented MRI of this tutorial data from the [download server](https://download.fieldtriptoolbox.org/tutorial/headmodel_eeg_fem/).
{% include markup/end %}

    cfg           = [];
    cfg.output    = {'gray', 'white', 'csf', 'skull', 'scalp'};
    segmentedmri  = ft_volumesegment(cfg, mri);
    
    save segmentedmri segmentedmri

     disp(segmentedmri)
               dim: [256 256 256]
         transform: [4x4 double]
          coordsys: 'ctf'
              unit: 'mm'
              gray: [256x256x256 logical]
             white: [256x256x256 logical]
               csf: [256x256x256 logical]
             skull: [256x256x256 logical]
             scalp: [256x256x256 logical]
               cfg: [1x1 struct]

The segmentedmri data structure is similar to the mri data structure, but contains the new fields:

-   `gray`: binary representation of the grey matter, note the difference between [UK and US spelling](https://www.merriam-webster.com/words-at-play/gray-vs-grey-usage-difference)
-   `white`: binary representation of the white matter
-   `csf`: binary representation of the CSF
-   `skull`: binary representation of the skull
-   `scalp`: binary representation of the scalp

The segmentation does not change the coordinate system, nor the size of the voxels or volume. You can see this in the first three fields (`dim`, `transform` and `coordsys`) which are the same as the corresponding fields in the MRI. The field `transform` aligns the 3D array in `gray`,, `white`, `csf`, `skull` and `scalp` to the coordinate system defined in the `coordsys` field, just like it did for the `anatomy` field in the anatomical MRI. It is good practice to check at this point in a figure, whether the segmented compartments look as expected.

{% include markup/warning %}
Occasionally, the quality of the anatomical image is not sufficient to provide a good segmentation out-of-the-box. This for example happens if there are large spatial inhomogeneities in the MRI that are caused by the anatomical MRI being acquired while the subject was wearing an EEG cap. The **[ft_volumebiascorrect](/reference/ft_volumebiascorrect)** function allows correcting for these inhomogeneities. The **[ft_defacevolume](/reference/ft_defacevolume)** function can be used to erase parts of the MRI where there should be no signal, for example artifacts outside the head.

For more information, you can consult this [frequently asked question](/faq/why_does_my_eegheadmodel_look_funny).
{% include markup/end %}

{%
  ##############################################################
  # I made it up to here in revising the tutorial
  # The figures still need to be updated
  ##############################################################
%}

The function **[ft_sourceplot](/reference/ft_sourceplot)** can be used to plot the segmented tissues. In order, to see all tissues in one image, **[ft_datatype_segmentation](/reference/utilities/ft_datatype_segmentation)** can convert the segmentation structure to an [indexed representation](/faq/how_is_the_segmentation_defined). Each tissue-types will be shown by a different color in the image.

    seg_i = ft_datatype_segmentation(segmentedmri, 'segmentationstyle', 'indexed');

    cfg              = [];
    cfg.funparameter = 'seg';
    cfg.funcolormap  = lines(6); % distinct color per tissue
    cfg.location     = 'center';
    cfg.atlas        = seg_i;    % the segmentation can also be used as atlas
    ft_sourceplot(cfg, seg_i);

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure4.png" width="450" %}

_Figure 4. Binary representations of scalp, skull tissues, gray and white matter, csf_

## Mesh

In this step, a geometrical description of the head is created by the **[ft_prepare_mesh](/reference/ft_prepare_mesh)** function. The output of this function is a hexahedral mesh (i.e., the points of the mesh are connected in such way that they create hexahedrons). Each hexahedron is assigned to one of the five tissue-types.

To improve the geometrical properties of the mesh (i.e., its approximation of the head shape), a node-shift approach can be applied which shifts boundary vertices in the direction of those hexahedrons that represent the minority around it (see figure). The magnitude of the shift is controlled by a shift parameter which can range from 0 (no shift) to 0.49 (maximum shift). However, choosing the shift parameter too large can result in degenerated hexahedrons. For starters we recommend a shift parameter of 0.3.

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure5.png" width="300" %}
{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure6.png" width="300" %}

_Figure 5. Comparison of an unshifted mesh(upper) and shifted mesh(lower). Visualization done with ParaView._

    cfg        = [];
    cfg.shift  = 0.3;
    cfg.method = 'hexahedral';
    mesh = ft_prepare_mesh(cfg,segmentedmri);

    disp(mesh)
                pnt: [4354427x3 double]
                hex: [4253761x8 double]
             tissue: [4253761x1 double]
        tissuelabel: {'gray'  'white'  'csf'  'skull'  'scalp'}
               unit: 'mm'

The mesh contains the following field

- **pos** : The position of the vertices.
- **hex** : Each row defines 8 corners of a hexahedron (row numbers of the **pnt** field).
- **unit**: Units in which the vertices are expressed.
- **tissue**: Each hexahedron (in **hex**) is indexed with a value from 1...N. These values represent the tissue-types and are assigned to each type according to the order in **tissuelabel**.
- **tissuelabel**: Names of tissue-types.

At the moment FieldTrip only supports hexahedrons for FEM modeling.

## Head model

Gray and white matter, csf, skull and skin has been differentiated in the geometrical description of the head. Now, we will create the volume conduction model. We will specify `cfg.method='simbio'` in **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**. This methods also requires to specify the conductivities for each tissue-types. The headmodel can also be downloaded from our [download server](https://download.fieldtriptoolbox.org/tutorial/headmodel_eeg_fem/).

    cfg        = [];
    cfg.method ='simbio';
    cfg.conductivity = [0.33 0.14 1.79 0.01 0.43];   % the order follows mesh.tissuelabel
    headmodel  = ft_prepare_headmodel(cfg, mesh);

    disp(headmodel)
                pos: [4354427x3 double]
                hex: [4253761x8 double]
             tissue: [4253761x1 double]
               cond: [0.33 0.14 1.79 0.01 0.43]
        tissuelabel: {'gray'  'white'  'csf'  'skull'  'scalp'}
              stiff: [4354427x4354427 double]
               type: 'simbio'
               unit: 'mm'
                cfg: [1x1 struct]

The headmodel data structure contains the same information in the **pos** (**pnt** in mesh), **hex**, **tissue** and **tissulabel** fields than the mesh we created earlier. And it has also new fields:

- **cond**: conductivity of each tissue-type (in order of tissuelabel)
- **stiff**: matrix
- **type**: describes the method that was used to create the headmodel.
- **unit**: the unit of measurement of the geometrical data in the pos field
- **cfg**: configuration of the function that was used to create vol

Note that the unit of measurement used in the geometrical description of headmodel is in 'mm'. The EEG sensors should be also defined in 'mm'. The units of all type of geometrical information should be the same when a leadfield is computed for source-reconstruction.

## Visualization

The hexahedral mesh is a geometrical description of the head. It is built up from hexahedrons. For visualization, it is possible to use the **[ft_plot_mesh](/reference/plotting/ft_plot_mesh)** function which is generally used for plotting any type of meshes in FieldTrip. Because of the large number of points in a mesh, it is advised to use the 'surfaceonly' option. In this case, the function will plot hexagonal surfaces of those hexahedrons which create the outside surface of the head.

    ft_plot_mesh(mesh, 'surfaceonly', 'yes');

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure7.png" width="600" %}

_Figure 6. Plot of the FEM mesh_

Alternatively, you can write the mesh into another format with **[ft_write_headshape](/reference/fileio/ft_write_headshape)** and use an external (free) software [ParaView](http://www.paraview.org) or [MeshLab](http://www.meshlab.org) for visualization.

## Align the electrodes

The head model is now expressed in the same head coordinates as the anatomical mri (i.e., in the [CTF coordinate system](/faq/coordsys#details_of_the_ctf_coordinate_system)). Consequently, we need to express the electrode positions in the same coordinate system. First, we plot the outermost layer of the head model together with the electrodes to check if the alignment is necessary.

Since for this subject we have an MRI, but no EEG electrodes, we will use a template EEG electrode set which you can find in the fieldtrip/template/electrode/standard_1020.elc file.

    % you may need to specify the full path to the file
    elec = ft_read_sens('standard_1020.elc');

    disp(elec)
        chanpos: [97x3 double]
        elecpos: [97x3 double]
          label: {97x1 cell}
           type: 'eeg1010'
           unit: 'mm'

are described in the **chanpos** and **elecpos** field. The **label** field contains the name of the channels.

    figure
    hold on
    ft_plot_mesh(mesh, 'surfaceonly', 'yes', 'vertexcolor', 'none', 'edgecolor', 'none', 'facecolor', [0.5 0.5 0.5], 'face alpha', 0.7)
    camlight

    ft_plot_sens(elec);

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure8.png" width="500" %}

_Figure 7. FEM mesh surface plotted with electrode-positions (not aligned)._

The figure shows that the channels are not aligned with the surface of the head. In FieldTrip, electrode and channel positions are [differentiated](/faq/how_are_electrodes_magnetometers_or_gradiometers_described), but
the positions of the channels and electrodes should be the same for the alignment. Therefore, we will use electrodes and channels interchangeably.

The electrodes can be aligned in two ways

- if there are anatomical landmarks which positions are known in the anatomical mri and also relative to the electrodes, we can automatically align the electrode positions with a few lines of script or

- if the exact position of anatomical landmarks are not known relative to the electrodes, we visualize the surface of the head and the electrodes on the same image, and we transform, rotate and scale the electrodes until they fit to the head surface according to our visual judgement.

Now, we will show how to do the alignment in both ways

### Automatic alignment

First, we will align the electrodes automatically to the anatomical landmarks (to the fiducials: nasion, [left and right Pre-Auricular points](/faq/how_are_the_lpa_and_rpa_points_defined)) of the anatomical mri. The head model was created from the same mri, therefore the electrodes will also be aligned to the head-model.

For the automatic alignment, we need to know the following:

- electrode positions
- position of fiducial landmarks relative to the electrodes
- position of fiducial landmarks in the anatomical mri

In the template set of electrodes, the first three labels are: 'Nz', 'LPA' and 'RPA'. These labels show that the first three rows of the **elec.chanpos** field defines the position of the nasion, left and right PA (the landmarks of the CTF ) in _"electrode" coordinates_. We can use this information for the automatic alignment. But we also need to know the position of the same points in the anatomical mri. We use an anatomical mri which has been already aligned to these points, therefore we can find these coordinates in the header information.

    disp(mri_orig.hdr.fiducial.mri)
        nas: [87 60 116]
        lpa: [29 145 155]
        rpa: [144 142 158]

{% include markup/warning %}
If you do not have the position of the anatomical landmarks in your volume, you can use the **[ft_sourceplot](/reference/ft_sourceplot)** function to get those positions.
{% include markup/end %}

First, we convert the fiducial positions from voxel into CTF headcoordinate system using the [transformation matrix](/faq/what_is_the_plotting_convention_for_anatomical_mris) and the **[ft_warp_apply](/reference/utilities/ft_warp_apply)** function.

    nas = mri_orig.hdr.fiducial.mri.nas;
    lpa = mri_orig.hdr.fiducial.mri.lpa;
    rpa = mri_orig.hdr.fiducial.mri.rpa;

    vox2head = mri_orig.transform;

    nas = ft_warp_apply(vox2head, nas, 'homogenous');
    lpa = ft_warp_apply(vox2head, lpa, 'homogenous');
    rpa = ft_warp_apply(vox2head, rpa, 'homogenous');

Then, we determine the translation and rotation that is needed to get the position of the fiducials ()'Nz', 'LPA', 'RPA') in the electrode structure to their counterparts ('nas', 'lpa', 'rpa') in the CTF head coordinate system that we obtained from the anatomical MRI.

    % create a structure similar to a template set of electrodes
    fid.pos           = [nas; lpa; rpa];       % CTF head coordinates of fiducials
    fid.label         = {'Nz', 'LPA', 'RPA'};  % use the same labels as those in elec
    fid.unit          = 'mm';                  % use the same units as those in mri

    % alignment
    cfg               = [];
    cfg.method        = 'fiducial';
    cfg.elec          = elec;                  % the electrodes we want to align
    cfg.template      = fid;                   % the template we want to align to
    cfg.fiducial      = {'Nz', 'LPA', 'RPA'};  % labels of fiducials in fid and in elec
    elec_aligned      = ft_electroderealign(cfg);

We can check the alignment by plotting together the scalp surface with the electrodes.

    figure
    hold on
    ft_plot_mesh(mesh, 'surfaceonly', 'yes', 'vertexcolor', 'none', 'edgecolor', 'none', 'facecolor', [0.5 0.5 0.5], 'facealpha', 0.5)
    camlight
    ft_plot_sens(elec_aligned);

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure9.png" width="500" %}

_Figure 8. Electrodes plotted together with the head surface after automatic alignement._

The alignment is much better, but not perfect. Some of the electrodes are below the head surface in the front, while the electrodes in the back do not fit tightly to the head. The remaining misalignment is due to the use of different conventions to [define the fiducials](/faq/how_are_the_lpa_and_rpa_points_defined). We can improve the alignment of the electrodes interactively.

### Interactive alignment

    cfg          = [];
    cfg.method   = 'interactive';
    cfg.elec     = elec_aligned;
    cfg.headshape = headmodel;
    elec_aligned = ft_electroderealign(cfg);

    save elec_aligned elec_aligned;

Here, we only need to use translation. We can shift about 15 mm along the x-axis and -10 mm along the y-axis. Note that in the CTF head coordinate system the x-axis is towards the nose.

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure10.png" width="500" %}

_Figure 9. Aligned electrodes plotted together with the head surface_

## Exercise 1

{% include markup/info %}
Create a head model with method `concentricspheres` that you fit on scalp, skull and brain surfaces, i.e., using the already constructed mesh.

Plot the head model in the same figure with the brain surface and scalp. Check the help of **[ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)** for visualization options (e.g., color, transparency) which help to see the spheres and the brain surface together.

What is the difference between this head model and the FEM?
{% include markup/end %}

## Exercise 2

{% include markup/info %}
In exercise 1, you created a head model with method `concentricspheres`. How is its geometrical description defined? What is the difference between the geometrical description of the concentric spheres model and BEM model?
{% include markup/end %}

## Summary and suggested further reading

This tutorial explained how to build a volume conduction model of the head using a single subject anatomical MRI and a finite element method (FEM).

You can read more about specific source-reconstruction methods in the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and in the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

Here are the related FAQs:

{% include seealso tag1="faq" tag2="headmodel" tag3="eeg" %}

and the related examples:

{% include seealso tag1="example" tag2="headmodel" tag3="eeg" %}
