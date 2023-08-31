---
title: Creating a FEM volume conduction model of the head for source reconstruction of EEG data
tags: [tutorial, eeg, source, headmodel, mri, plotting, paraview, seg3d, meg-language]
---

# Creating a FEM volume conduction model of the head for source reconstruction of EEG data

## Introduction

This tutorial demonstrates how to construct a Finite Element Method (FEM) volume conduction model of the head, also known as head model, based on an individual subject's anatomical MRI. For didactic reasons we will use the anatomical MRI corresponding to the data that was also analyzed in other tutorials. The original anatomical MRI data, along with the (intermediate) results of this tutorial, can be downloaded from [out download server](https://download.fieldtriptoolbox.org/tutorial/headmodel_eeg_fem/).

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

### Reslicing

A common issue with anatomical MRI data is that it is plotted [upside down](/faq/my_mri_is_upside_down_is_this_a_problem). This is not necessarily a problem for the FEM model that we will make, as we know the position of each MRI voxel relative to the coordinate system, but it is a bit inconvenient in the plotting of MRI slices and quality control later in the pipeline.

The **[ft_volumereslice](/reference/ft_volumereslice)** function can be used to flip the volume such that the 1st dimension of the three-dimensional `mri.anatomy` array corresponds approximately with the x-axis of the coordinate system, that the 2nd dimension corresponds approximately to the y-axis, and the 3rd dimension to the z-axis.

Note that the axes of the coordinate system in general will not be exactly aligned with the orientation and direction of the slices of the MRI during acquisition.  You can also use **[ft_volumereslice](/reference/ft_volumereslice)** to properly reslice your anatomical MRI; in that case it will be interpolated onto a regular and isotropic grid in which the volume is aligned with the axes and the size of the voxel is identical in each direction. This is recommended when you use morphological image operations such as [imerode](https://www.mathworks.com/help/images/ref/imerode.html) and [imdilate](https://www.mathworks.com/help/images/ref/imdilate.html), which is common for constructing the segmentation that underlies the triangulated surfaces for the boundary element method (BEM).

The following flips the volume such that the anatomical volume approximately aligns with the axes

    cfg = [];
    cfg.method = 'flip';
    mri_resliced = ft_volumereslice(cfg, mri_realigned);

    save mri_resliced mri_resliced

If you would want to align it exactly with the axes and/or make the voxels isotropic, you could use the 'linear' method in **[ft_volumereslice](/reference/ft_volumereslice)**.

Following the reslicing, the MRI should be shown with the correct side up, the field-of-view should be symmetric from left to right. If you move along the first axis, you should see that the first voxel index `i` increase _and_ that the `x` position increases (idem for `j/y` and `k/z`).

    cfg = [];
    cfg.method = 'ortho';
    ft_sourceplot(cfg, mri_resliced)

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure2.png" width="600" %}

_Figure; The MRI after assigning the desired coordinate system and reslicing_

You should check that all parts of the head are present in the resliced images, including the nose, back of the head and the top of the head. If not, you need to redo the reslicing with a slightly modified vield of view.

### Segmentation

In this step, the voxels of the anatomical MRI are segmented or classified using **[ft_volumesegment](/reference/ft_volumesegment)** into the three different tissue types: scalp, skull, csf (cerebro-spinal fluid), gray and white matter. You can read more about how the tissue-types are represented in the output of this function in this [FAQ](/faq/how_is_the_segmentation_defined). The resulting segmentation should be a binary representation of the 5 tissue types without overlap, i.e., each voxel belongs to exactly one tissue type.

{% include markup/warning %}
Note that the segmentation is quite time consuming (~15mins) and if you want you can load the result and skip ahead to the next step. You can download the segmented MRI of this tutorial data from the [download server](https://download.fieldtriptoolbox.org/tutorial/headmodel_eeg_fem/).
{% include markup/end %}

    cfg           = [];
    cfg.output    = {'gray', 'white', 'csf', 'skull', 'scalp'};
    segmentedmri  = ft_volumesegment(cfg, mri_resliced);

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

The function **[ft_sourceplot](/reference/ft_sourceplot)** can be used to plot the segmented tissues. To see all tissues in one image, we use **[ft_datatype_segmentation](/reference/utilities/ft_datatype_segmentation)** to convert the segmentation structure to an [indexed representation](/faq/how_is_the_segmentation_defined). Each tissue type has a different value and will be shown by a different color.

    % convert from probabilistic/binary into indexed representation
    segmentedmri_indexed = ft_datatype_segmentation(segmentedmri, 'segmentationstyle', 'indexed');

    % also add the anatomical mri
    segmentedmri_indexed.anatomy = mri_resliced.anatomy;

    cfg              = [];
    cfg.anaparameter = 'anatomy';
    cfg.funparameter = 'tissue';
    cfg.funcolormap  = lines(6);              % distinct color per tissue + background
    cfg.atlas        = segmentedmri_indexed;  % this is just like an anatomical atlas, see https://www.fieldtriptoolbox.org/template/atlas/
    cfg.location     = 'center';
    ft_sourceplot(cfg, segmentedmri_indexed);

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure3.png" width="600" %}

_Figure. Binary representations of gray matter, white matter, csf, skull, and scalp_

### Meshing

The next step is to create a geometrical description of the head by the **[ft_prepare_mesh](/reference/ft_prepare_mesh)** function. At the moment FieldTrip-SIMBIO only supports hexahedra. The hexahedral mesh elements consist of 8 vertices at the corners that are connected like cubes. Each hexahedron is assigned to one of the five tissue-types.

To improve how the mesh approximates the head shape, a node-shift can be applied. This shifts vertices at the boundaries in the direction of those hexahedra that represent the minority around it (see figure). The magnitude of the shift is controlled by a shift parameter which can range from 0 (no shift) to 0.3.

    cfg        = [];
    cfg.shift  = 0.3;
    cfg.method = 'hexahedral';
    mesh = ft_prepare_mesh(cfg, segmentedmri);

    save mesh mesh

    disp(mesh)
                pos: [2372249x3 double]
                hex: [2301983x8 double]
             tissue: [2301983x1 double]
        tissuelabel: {'csf'  'gray'  'scalp'  'skull'  'white'}
               unit: 'mm'
           coordsys: 'ctf'
                cfg: [1x1 struct]

The mesh contains the following field

- **pos** : The position of the vertices.
- **hex** : Each row defines 8 corners of a hexahedron (row numbers of the **pnt** field).
- **unit**: Units in which the vertices are expressed.
- **tissue**: Each hexahedron (in **hex**) is indexed with a value from 1...N. These values represent the tissue-types and are assigned to each type according to the order in **tissuelabel**.
- **tissuelabel**: Names of tissue-types.

You can plot the anatomical MRI, the segmentation and the hexahedral mesh together in one figure. Note that you will have to zoom in quite a bit to see the individual hexahedral elements, as there are so many.

    cfg = [];
    cfg.funparameter = 'tissue';
    cfg.anaparameter = 'anatomy';
    cfg.atlas = segmentedmri_indexed; % this is just like an anatomical atlas, see https://www.fieldtriptoolbox.org/template/atlas/
    cfg.funcolormap = lines(6);
    cfg.method = 'ortho';
    cfg.intersectmesh = mesh;
    ft_sourceplot(cfg, segmentedmri_indexed)

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure4.png" width="600" %}
{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure5.png" width="600" %}

_Figure. Comparison of a shifted mesh (upper) and unshifted mesh (lower)._

The visualization can also be done using [Seg3D](/getting_started/seg3d) or [ParaView](/getting_started/paraview). With Seg3D you can make modifications to the segmentation.

### Compute the FEM head model

Now that gray matter, white matter, csf, skull and skin has been modeled as a mesh, we will create the volume conduction model. We will specify `cfg.method='simbio'` in **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**. This methods also requires to specify the conductivities for each tissue-types. The headmodel can also be downloaded from our [download server](https://download.fieldtriptoolbox.org/tutorial/headmodel_eeg_fem/).

    cfg        = [];
    cfg.method = 'simbio';
    cfg.conductivity = [1.79 0.33 0.43 0.01 0.14];   % the order follows mesh.tissuelabel, which is 'csf', 'gray', 'scalp', 'skull', 'white'
    headmodel  = ft_prepare_headmodel(cfg, mesh);

    save headmodel headmodel

    disp(headmodel)
                pos: [2372249x3 double]
                hex: [2301983x8 double]
             tissue: [2301983x1 double]
               cond: [1.79 0.33 0.43 0.01 0.14]
        tissuelabel: {'csf'  'gray'  'scalp'  'skull'  'white'}
              stiff: [2372249x2372249 double]
               type: 'simbio'
               unit: 'mm'
                cfg: [1x1 struct]

The headmodel data structure contains the same information in the **pos**, **hex**, **tissue** and **tissulabel** fields than the mesh we created earlier. And it has also new fields:

- **cond**: conductivity of each tissue-type (in order of tissuelabel)
- **stiff**: matrix
- **type**: describes the method that was used to create the headmodel.

Note that the unit of measurement used in the geometrical description of headmodel is in 'mm'. The EEG sensors should be also defined in 'mm'. The units of all type of geometrical information should be the same when a leadfield is computed for source reconstruction.

### Visualization

The hexahedral mesh is a geometrical description of the head. It is built up from hexahedra. For visualization, it is possible to use the **[ft_plot_mesh](/reference/plotting/ft_plot_mesh)** function which is generally used for plotting any type of meshes in FieldTrip. Because of the large number of points in a mesh, it is advised to use the 'surfaceonly' option. In this case, the function will plot hexagonal surfaces of those hexahedra which create the outside surface of the head.

    ft_plot_mesh(mesh, 'edgecolor','none', 'facecolor', 'skin', 'facealpha', 0.7);
    ft_plot_axes(mesh)
    alpha 1
    material default
    camlight

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure6.png" width="600" %}

_Figure. Plot of the FEM mesh_

This only shows the outside of the scalp. To see the other tissues, you can split the mesh into the different tissue types and make one mesh for each.

    % make a copy for each tissue type
    % after splitting we don't need the tissue and tissuelabel any more
    mesh_csf   = rmfield(mesh, {'tissue', 'tissuelabel'});
    mesh_gray  = rmfield(mesh, {'tissue', 'tissuelabel'});
    mesh_scalp = rmfield(mesh, {'tissue', 'tissuelabel'});
    mesh_skull = rmfield(mesh, {'tissue', 'tissuelabel'});
    mesh_white = rmfield(mesh, {'tissue', 'tissuelabel'});

    % only keep the hexahedra for the corresponding tissue type
    mesh_csf.hex   = mesh.hex(mesh.tissue==1,:);
    mesh_gray.hex  = mesh.hex(mesh.tissue==2,:);
    mesh_scalp.hex = mesh.hex(mesh.tissue==3,:);
    mesh_skull.hex = mesh.hex(mesh.tissue==4,:);
    mesh_white.hex = mesh.hex(mesh.tissue==5,:);

Alternatively, you can write the mesh to a file on disk with **[ft_write_headshape](/reference/fileio/ft_write_headshape)** and use [ParaView](/getting_started/paraview) for visualization.

### Align EEG electrodes

The procedure to align the electrodes is basically the same as for a BEM head model which you can read in much more detail [here](/tutorial/headmodel_eeg_bem). Very shortly: you can do the following to align it to the FEM mesh.

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

    cfg = [];
    cfg.method = 'interactive';
    cfg.headshape = mesh; % we can specify the hexahedral FEM mesh as the headshape
    elec_realigned = ft_electroderealign(cfg, elec)

    save elec_realigned elec_realigned

Since rotations and translations do not "commute", i.e. the order in which you execute the rotation matters, it can be confusing to specify all rotations and translations in one go. Instead, you can use the "apply" button to do the transformations stepwise.

In this situation we need

- rotate -90 around z; apply
- translate 35 along x and 35 along z; apply
- scale 0.98 along x, 0.90 along y, and 0.80 along z; apply
- translate 25 along z; apply
- rotate 11 degrees around y, translate -5 along x; apply
- quit

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure7.png" width="600" %}

_Figure; Use the GUI to align the electrodes._

Using a final plot that includes the electrode labels, we can check that it all matches.

    figure
    ft_plot_headmodel(headmodel, 'facecolor', 'skin', 'facealpha', 0.7);
    hold on
    ft_plot_sens(elec_realigned, 'elecshape', 'sphere', 'label', 'on');
    camlight

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure8.png" width="600" %}

_Figure; Realigned electrodes plotted together with the scalp surface._

This electrode structure can be used later when the leadfield is computed with **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)** and **[ft_sourceanalysis](/reference/ft_sourceanalysis)**, or with **[ft_dipolefitting](/reference/ft_dipolefitting)**. During the computation of the leadfield, the electrodes will be projected exactly onto the scalp surface, so don't worry if the fit is not yet 100% perfect.

### Construct source model

With single-shell and BEM volume conduction models you can place the dipoles of the source model anywhere in the brain compartment. With more detailed FEM models, you want the dipoles only in the grey matter. Furthermore, the FEM computations will be more accurate if the dipoles are placed at the centroids of the volume elements.

The following starts with a 8 mm regular grid. The dipole positions are subsequently moved to the nearest centroid.

    cfg = [];
    cfg.method = 'basedonresolution';
    cfg.resolution = 8; % in mm
    cfg.unit = 'mm';
    cfg.headmodel = mesh;
    cfg.headmodel.type = 'simbio';
    cfg.movetocentroids = 'yes';
    sourcemodel = ft_prepare_sourcemodel(cfg)

    save sourcemodel sourcemodel

We can plot the complete sourcemodel and compare it to only the sources inside the grey matter. This makes use of the MATLAB [linkprop](https://nl.mathworks.com/help/matlab/ref/linkprop.html) command to keep the two subplots in sync.

    figure
    ax1 = subplot(1,2,1); ft_plot_mesh(sourcemodel); ft_plot_axes(sourcemodel)
    ax2 = subplot(1,2,2); ft_plot_mesh(sourcemodel.pos(sourcemodel.inside,:))

    hlink = linkprop([ax1, ax2], {'CameraPosition', 'CameraUpVector', 'xLim', 'YLim', 'ZLim'});
    rotate3d on

{% include image src="/assets/img/tutorial/headmodel_eeg_fem/figure9.png" width="600" %}

_Figure; All source positions (left) and those inside the grey matter (right)._

There are many dipoles at positions where we will not compute the leadfields anyway, such as the skull and lower parts of the head. We can prune the sourcemodel and select only the dipoles inside grey matter.

    sourcemodel.pos    = sourcemodel.pos(sourcemodel.inside,:)
    sourcemodel.tissue = sourcemodel.tissue(sourcemodel.inside,:); % also update the tissue indices
    sourcemodel.inside = sourcemodel.inside(sourcemodel.inside,:); % and update the inside vector itself

The construction of the sourcemodel above takes quite some time as many dipoles need to be compared with many centroids. We can speed it up by starting with a smaller regular grid of dipoles by explicitly specifying the initial regular grid. This requires knowing the (approximate) boundaries of the brain.

    cfg = [];
    cfg.method = 'basedongrid';
    cfg.xgrid = -80:8:120;  % specified in multiples of 8, so that [0 0 0] is part of the grid
    cfg.ygrid = -80:8:80;
    cfg.zgrid = -24:8:120;
    cfg.unit = 'mm';
    cfg.headmodel = mesh;
    cfg.headmodel.type = 'simbio';
    cfg.movetocentroids = 'yes';
    sourcemodel = ft_prepare_sourcemodel(cfg)

## Summary and suggested further reading

This tutorial explained how to build a volume conduction model of the head using a single subject anatomical MRI and a finite element method (FEM) using the FieldTrip-SIMBIO pipeline.

You can read more about specific source reconstruction methods in the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and in the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

Here are the related FAQs:

{% include seealso tag1="faq" tag2="headmodel" tag3="eeg" %}

and the related examples:

{% include seealso tag1="example" tag2="headmodel" tag3="eeg" %}
