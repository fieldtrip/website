---
title: Creating a FEM volume conduction model of the head for source-reconstruction of EEG data
tags: [tutorial, eeg, source, headmodel, mri, plot, meg-language]
---

# Creating a FEM volume conduction model of the head for source-reconstruction of EEG data

## Introduction

This tutorial demonstrates how to construct a volume conduction model of the head based on a single subject's MRI. We will use the anatomical images that belong to the same subject whose data was analyzed in other tutorials. The anatomical MRI data is available from the [FieldTrip ftp server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip). Here, an EEG specific FEM model will be shown. In reality, we do not have corresponding EEG data for the subject we will use in this tutorial, rather we will use a template EEG electrode set to demonstrate how to build a FEM model for EEG and how to align the electrodes to anatomical data.

This tutorial will **not** show how to perform the source reconstruction itself. If you are interested in source reconstruction methods, you can go to the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and to the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

Furthermore, elsewhere on this website you can find also information [about MEG headmodels](/tutorial/headmodel_meg) and about other [EEG headmodels](/tutorial/headmodel_eeg).

We want to note that the FEM modelling works only on MATLAB versions 2011 and above.

{% include markup/warning %}
The SimBio software is described in detail [here](https://www.mrt.uni-jena.de/simbio/index.php/Main_Page#Welcome). The integration with FieldTrip is described in the reference below. Please cite this reference if you use the FieldTrip-SimBio pipeline in your research.

Vorwerk, J., Oostenveld, R., Piastra, M.C., Magyari, L., & Wolters, C. H. **The FieldTrip‐SimBio pipeline for EEG forward solutions.** BioMed Eng OnLine (2018) 17:37. [DOI: 10.1186/s12938-018-0463-y](https://doi.org/10.1186/s12938-018-0463-y).
{% include markup/end %}

## Background

{% include /shared/tutorial/sourcelocalization_background.md %}

This tutorial is focusing on how to build the **FEM volume conduction model for the head**.

{% include /shared/tutorial/headmodel_background.md %}

{% include markup/info %}
If an anatomical MRI is not available for your EEG subject, you can consider to use a template MRI or a template head model that is located in the FieldTrip template directory. If you do not have an MRI, but if you do have a measurement of the scalp surface (e.g. with a Polhemus tracker), you can use concentric spheres volume conduction model. If you do not want to (or cannot) use any realistic information about the brain-surface or the head-shape, you can resort to the single sphere volume conduction model.
{% include markup/end %}

## Procedure

Here, we will work towards a volume conduction model of the head based on the finite element method (FEM). The FEM model assumes realistic information where the skin, skull, csf, gray and white matter is in the head. First, we will use an anatomical MRI to extract these tissue. This procedure is termed **segmentation**. Following the segmentation, a geometrical description of the head will be created using hexahedrons. Finally, the FEM model will be computed.

The anatomical mri of the [tutorial data set](/tutorial/meg_language) is available [here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/hedmodel_fem2.png" width="200" %}

_Figure 2. Pipeline for creating a FEM model_

- First, we will read the anatomical data with **[ft_read_mri](/reference/ft_read_mri)**;
- then we reslice the anatomical data with **[ft_volumereslice](/reference/ft_volumereslice)**;
- segment the anatomical information into different tissue types with **[ft_volumesegment](/reference/ft_volumesegment)**;
- create a geometrical description of the head (mesh) with **[ft_prepare_mesh](/reference/ft_prepare_mesh)**;
- create the headmodel with **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**;
- and visualize the geometry of the head by **[ft_plot_mesh](/reference/ft_plot_mesh)**

## Reading in the anatomical data

Before starting with FieldTrip, it is important that you set up your [matlab path](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path) properly.

    cd PATH_TO_FIELDTRIP
    ft_defaults

Then, you can read in the mri data.

    mri = ft_read_mri('Subject01.mri');

    disp(mri)
              dim: [256 256 256]
          anatomy: [256x256x256 int16]
              hdr: [1x1 struct]
        transform: [4x4 double]
         coordsys: 'ctf'

The structure of your mri variable contains the following field

- **dim**: This field gives information on the size (i.e. the number of voxels) of the anatomical volume into each direction.
- **anatomy**: This is a matrix (with the size and number of dimensions specified in **dim**) that contains the anatomical information represented by numbers.
- **hdr**: Header information of the anatomical images.
- **transform**: A homogenous [transformation matrix](/faq/how_change_mri_orientation_size_fov) that aligns the anatomical data (in field **anatomy**) to a certain coordinate system.
- **coordsys**: The description of the coordinate system which the anatomical data is aligned to.

You can see that the **coordsys** field of anatomical data that we read in is already aligned to the [ctf coordinate system](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined#details_of_the_ctf_coordinate_system).

## Align MRI to the head coordinate system

When you prepare a head model for EEG, the head model should be in the same coordinate system as the electrodes. It is not relevant in which coordinate system the geometrical information is defined, until all are [aligned](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions). For this, you can do two thing

- either you need to align the anatomical MRI (before the segmentation) into the same coordinate system in which the electrodes will be expressed. For example, if you want to align the anatomical MRI to the ctf coordinate system, it can be aligned with using the **[ft_volumerealign](/reference/ft_volumerealign)** function. For this alignment, you will need to align your MRI to the fiducial points (LPA, RPA and nasion). The output of any later processing step (segmentation, mesh, headmodel) will be expressed in the same coordinate system as your anatomical mri. And then, you can also align the electrodes to the same points.

- or you can also align later your electrodes interactively or manually to an existing head model.

The anatomical MRI that we use in this tutorial is already aligned to the CTF head coordinate system](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined#details_of_the_ctf_coordinate_system). We also have information (see later) how the EEG electrodes are positioned relative to the fiducials. Therefore, there is no reason to align the anatomical MRI to any other coordinate system.

It is also possible to read in anatomical MRI data in [other formats](/faq/dataformat), which are defined in [a different coordinate system](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined). When you read in your own anatomical data, it may does not give information on the coordinate system in which the anatomical data is expressed and/or maybe there is no transformation matrix specified. In this case, you can check the coordinate-system with the **[ft_determine_coordsys](/reference/ft_determine_coordsys)** function.

## Reslice the volume

In the next step of this tutorial, we will segment the anatomical MRI. Segmentation works properly when the voxels of the anatomical images are homogenous (i.e. the size of the voxel is the same into each direction). If you do not have homogenous voxels (or you are not sure of), you can use the **[ft_volumereslice](/reference/ft_volumereslice)** function on the anatomical data before segmentation. Read more about re-slicing [here](/faq/how_change_mri_orientation_size_fov).

    cfg     = [];
    cfg.dim = mri.dim;
    mri     = ft_volumereslice(cfg,mri);

{% include markup/info %}
Reslicing will apply the coordinate transformation on your anatomical data. (While **[ft_volumerealign](/reference/ft_volumerealign)** does not change the anatomical data, but it adjusts the transformation matrix of the data, **[ft_volumereslice](/reference/ft_volumereslice)** will change the anatomical data, i.e. it will arrange data in field **anatomy** according to the coordinate system.) Do not use this function if later you need to recover the original orientation of the voxels.
{% include markup/end %}

We check if the resolution and the dimensions were well specified, and the reslicement did not cause any loss in the anatomical information (i.e. if all parts of the head are present in the resliced images).

    cfg=[];
    ft_sourceplot(cfg,mri);

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/mri_noreslice.png" width="250" %}
{% include image src="/assets/img/tutorial/headmodel_eeg_fem/mri.png" width="250" %}

_Figure 3. Mri plotted before reslicement (left) and after reslicement (right)_

## Segmentation

In this step, the voxels of the anatomical MRI are segmented (i.e. separated) into the five different tissue types: scalp, skull, csf (cerebro-spinal fluid), gray and white matter. These latest three tissues belong to the brain. The function **[ft_volumesegment](/reference/ft_volumesegment)** will produce the required output. You can read more about how the tissue-types are represented in the output of this function in this [FAQ](/faq/how_is_the_segmentation_defined). The segmentation should contain a binary representation of 5 tissue types which do not overlap.

{% include markup/warning %}
Note that the segmentation is quite time consuming (~15mins) and if you want you can load the result and skip ahead to the next step. You can download the segmented MRI of this tutorial data from the from the [ftp server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/headmodel_fem/segmentedmri.mat) (segmentedmri.mat).
{% include markup/end %}

    cfg           = [];
    cfg.output    = {'gray','white','csf','skull','scalp'};
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

The segmentedmri data structure is similar to the mri data structure, but contains the new field

- **unit** : unit of the head coordinate system
- **cfg** : configuration information of the function which created segmentedmri
- **gray** : binary representation of the gray matter
- **white**: binary representation of the white matter
- **csf** : binary representation of the csf (cerebro-spinal fluid)
- **skull**: binary representation of the skull
- **scalp**: binary representation of the scalp

The segmentation does not change the coordinate system, nor the size of the volume. You can see this in the first three fields (dim, transform and coordsys) which are the same as the corresponding fields of the input mri data structure. But now, the field **transform** aligns the matrix in fields **skull**, **scalp**... etc. to the coordinate system defined in the **coordsys** field.

The function **[ft_sourceplot](/reference/ft_sourceplot)** can be used to plot the segmented tissues. In order, to see all tissues in one image, **[ft_datatype_segmentation](/reference/ft_datatype_segmentation)** can convert the segmentation structure to an [indexed representation](/faq/how_is_the_segmentation_defined). Each tissue-types will be shown by a different color in the image.

    seg_i = ft_datatype_segmentation(segmentedmri,'segmentationstyle','indexed');

    cfg              = [];
    cfg.funparameter = 'seg';
    cfg.funcolormap  = lines(6); % distinct color per tissue
    cfg.location     = 'center';
    cfg.atlas        = seg_i;    % the segmentation can also be used as atlas
    ft_sourceplot(cfg, seg_i);

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/5tissues_segmentation.png" width="450" %}

_Figure 4. Binary representations of scalp, skull tissues, gray and white matter, csf _

## Mesh

In this step, a geometrical description of the head is created by the **[ft_prepare_mesh](/reference/ft_prepare_mesh)** function. The output of this function is a hexahedral mesh (i.e. the points of the mesh are connected in such way that they create hexahedrons). Each hexahedron is assigned to one of the five tissue-types.
In order to improve the geometrical properties of the mesh (i. e. its approximation of the head shape), a node-shift approach can be applied which shifts boundary vertices in the direction of those hexahedrons that represent the minority around it(see figure. The magnitude of the shift is controlled by a shift parameter which can range from 0 (no shift) to 0.49(maximum shift). However, choosing the shift parameter too large can result in degenerated hexahedrons. For starters we recommend a shift parameter of 0.3.
{% include image src="/assets/img/tutorial/headmodel_eeg_fem/slide_mesh_detailed.png" width="300" %}
{% include image src="/assets/img/tutorial/headmodel_eeg_fem/slide_mesh_ns_detailed.png" width="300" %}

_Figure 5._
Comparison of an unshifted mesh(upper) and shifted mesh(lower). Visualization done with ParaView.

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

At the moment FieldTrip only supports hexahedrons for FEM modelling.

## Head model

Gray and white matter, csf, skull and skin has been differentiated in the geometrical description of the head. Now, we will create the volume conduction model. We will specify method 'simbio' in the cfg.method field of **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**. This methods also requires to specify the conductivities for each tissue-types.
The vol can also be downloaded here [ftp server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/headmodel_fem/vol.mat).

    cfg        = [];
    cfg.method ='simbio';
    cfg.conductivity = [0.33 0.14 1.79 0.01 0.43];   % order follows mesh.tissyelabel
    vol        = ft_prepare_headmodel(cfg, mesh);

    save vol vol

    disp(vol)
                pos: [4354427x3 double]
                hex: [4253761x8 double]
             tissue: [4253761x1 double]
               cond: [0.33 0.14 1.79 0.01 0.43]
        tissuelabel: {'gray'  'white'  'csf'  'skull'  'scalp'}
              stiff: [4354427x4354427 double]
               type: 'simbio'
               unit: 'mm'
                cfg: [1x1 struct]

The vol data structure contains the same information in the **pos** (**pnt** in mesh), **hex**, **tissue** and **tissulabel** fields than the mesh we created earlier. And it has also new field

- **cond**: conductivity of each tissue-type (in order of tissuelabel)
- **stiff**: matrix
- **type**: describes the method that was used to create the headmodel.
- **unit**: the unit of measurement of the geometrical data in the pos field
- **cfg**: configuration of the function that was used to create vol

Note that the unit of measurement used in the geometrical description of vol is in 'mm'. The EEG sensors should be also defined in 'mm'. The units of all type of geometrical information should be the same when a leadfield is computed for source-reconstruction.

## Visualization

The hexahedral mesh is a geometrical description of the head. It is built up from hexahedrons. For visualization, it is possible to use the **[ft_plot_mesh](/reference/ft_plot_mesh)** function which is generally used for plotting any type of meshes in FieldTrip. Because of the large number of points in a mesh, it is advised to use the 'surfaceonly' option. In this case, the function will plot hexagonal surfaces of those hexahedrons which create the outside surface of the head.

    ft_plot_mesh(mesh, 'surfaceonly', 'yes');

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/fem_mesh.png" width="600" %}

_Figure 6._ Plot of the FEM mesh

Alternatively, you can write the mesh into another format with **[ft_write_headshape](/reference/ft_write_headshape)** and use an external (free) software [ParaView](http://www.paraview.org/) or [MeshLab](http://www.meshlab.org) for visualization.

## Align the electrodes

The head model is now expressed in the same head coordinates as the anatomical mri (i.e. in the [CTF coordinate system](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined#details_of_the_ctf_coordinate_system)). Consequently, we need to express the electrode positions in the same coordinate system. First, we plot the outermost layer of the head model together with the electrodes to check if the alignment is necessary.

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
    ft_plot_mesh(mesh,'surfaceonly','yes','vertexcolor','none','edgecolor','none','facecolor',[0.5 0.5 0.5],'face alpha',0.7)
    camlight

    ft_plot_sens(elec,'style', 'sr');

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/fem_mesh_misaligned_electrodes.png" width="500" %}

_Figure 7._ FEM mesh surface plotted with electrode-positions (not aligned).

The figure shows that the channels are not aligned with the surface of the head. In FieldTrip, electrode and channel positions are [differentiated](/faq/how_are_electrodes_magnetometers_or_gradiometers_described), but
the positions of the channels and electrodes should be the same for the alignment. Therefore, we will use electrodes and channels interchangeably.

The electrodes can be aligned in two way

- if there are anatomical landmarks which positions are known in the anatomical mri and also relative to the electrodes, we can automatically align the electrode positions with a few lines of script or

- if the exact position of anatomical landmarks are not known relative to the electrodes, we visualize the surface of the head and the electrodes on the same image, and we transform, rotate and scale the electrodes until they fit to the head surface according to our visual judgement.

Now, we will show how to do the alignment in both way

### Automatic alignment

First, we will align the electrodes automatically to the anatomical landmarks (to the fiducials: nasion, [left and right Pre-Auricular points](/faq/how_are_the_lpa_and_rpa_points_defined)) of the anatomical mri. The head model was created from the same mri, therefore the electrodes will also be aligned to the head-model.

For the automatic alignment, we need three informatio

- electrode positions
- position of fiducial landmarks relative to the electrodes
- position of fiducial landmarks in the anatomical mri

In the template set of electrodes, the first three labels are: 'Nz', 'LPA' and 'RPA'. These labels show that the first three rows of the **elec.chanpos** field defines the position of the nasion, left and right PA (the landmarks of the CTF ) in _"electrode" coordinates_. We can use this information for the automatic alignment. But we also need to know the position of the same points in the anatomical mri. We use an anatomical mri which has been already aligned to these points, therefore we can find these coordinates in the header information.

    disp(mri.hdr.fiducial.mri)
        nas: [87 60 116]
        lpa: [29 145 155]
        rpa: [144 142 158]

{% include markup/warning %}
If you do not have the position of the anatomical landmarks in your volume, you can use the **[ft_volumerealign](/reference/ft_volumerealign)** function to get those positions.
{% include markup/end %}

First, we convert the fiducial positions from voxel into CTF headcoordinate system using the [transformation matrix](/faq/what_is_the_plotting_convention_for_anatomical_mris) and the **[ft_warp_apply](/reference/ft_warp_apply)** function.

    nas = mri.hdr.fiducial.mri.nas;
    lpa = mri.hdr.fiducial.mri.lpa;
    rpa = mri.hdr.fiducial.mri.rpa;

    vox2head = mri.transform;

    nas = ft_warp_apply(vox2head, nas, 'homogenous');
    lpa = ft_warp_apply(vox2head, lpa, 'homogenous');
    rpa = ft_warp_apply(vox2head, rpa, 'homogenous');

Then, we determine the translation and rotation that is needed to get the position of the fiducials in the electrode structure (defined with labels 'Nz', 'LPA', 'RPA') to their counterparts in the CTF head coordinate system that we acquired from the anatomical mri (nas, lpa, rpa).

    % create a structure similar to a template set of electrodes
    fid.chanpos       = [nas; lpa; rpa];       % CTF head coordinates of fiducials
    fid.label         = {'Nz','LPA','RPA'};    % use the same labels as those in elec
    fid.unit          = 'mm';                  % use the same units as those in mri

    % alignment
    cfg               = [];
    cfg.method        = 'fiducial';
    cfg.elec          = elec;                  % the electrodes we want to align
    cfg.template      = fid;                   % the template we want to align to
    cfg.fiducial      = {'Nz', 'LPA', 'RPA'};  % labels of fiducials in fid and in elec
    elec_aligned      = ft_electroderealign(cfg);

We can check the alignment by plotting together the scalp surface with the electrodes.

    figure;
    hold on;
    ft_plot_mesh(mesh,'surfaceonly','yes','vertexcolor','none','edgecolor','none','facecolor',[0.5 0.5 0.5],'face alpha',0.5)
    camlight
    ft_plot_sens(elec_aligned,'style','sr');

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/fem_mesh_misaligned_electrodes_corrected.png" width="500" %}

_Figure 8. Electrodes plotted together with the head surface after automatic alignement._

The alignment is much better, but not perfect. Some of the electrodes are below the head surface in the front, while the electrodes in the back do not fit tightly to the head. The remaining misalignment is due to the use of different conventions to [define the fiducials](/faq/how_are_the_lpa_and_rpa_points_defined). We can improve the alignment of the electrodes interactively.

### Interactive alignment

    cfg          = [];
    cfg.method   = 'interactive';
    cfg.elec     = elec_aligned;
    cfg.headshape = vol;
    elec_aligned = ft_electroderealign(cfg);

    save elec_aligned elec_aligned;

Here, we only need to use translation. We can shift about 15 mm along the x-axis and -10 mm along the y-axis. Note that in the CTF head coordinate system the x-axis is towards the nose.

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/fem_mesh_misaligned_electrodes_manually_corrected.png" width="500" %}

_Figure 9. Aligned electrodes plotted together with the head surface_

## Headmodel interpolation

## Exercise 1

{% include markup/info %}
Create a head model with method 'concentricspheres' that you fit on scalp, skull and brain surfaces, i.e. using the already made mesh.

Plot the head model in the same figure with the brain surface and scalp. Check the help of **[ft_plot_vol](/reference/ft_plot_vol)** for further options of the visualization (e.g. color, transparency) which help to see the spheres and the brain surface together.

What is the difference between this head model and the FEM?
{% include markup/end %}

## Exercise 2

{% include markup/info %}
In exercise 1, you created a head model with method 'concentricspheres'. How is its geometrical description defined? What is the difference between the geometrical description of the concentric spheres model and BEM model?
{% include markup/end %}

## Summary and further reading

In this tutorial, it was explained how to build a volume conduction model of the head using a single subject anatomical mri and a finite element method (FEM).

You can read more about specific source-reconstruction methods in the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and in the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

Here are the related FAQs:

{% include seealso tag1="faq" tag2="headmodel" tag3="eeg" %}

and the related examples:

{% include seealso tag1="example" tag2="headmodel" tag3="eeg" %}
