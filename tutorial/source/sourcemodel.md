---
title: Creating a source model for source reconstruction of MEG or EEG data
parent: Source reconstruction
grand_parent: Tutorials
category: tutorial
tags: [source, meg, sourcemodel, mri, plotting, meg-language]
redirect_from:
    - /tutorial/sourcemodel/
---

# Creating a source model for source reconstruction of MEG or EEG data

## Introduction

In this tutorial you can find information about how to construct a source model that can be used for source reconstruction of EEG or MEG data. The source model describes a set of positions (and possibly orientations) of equivalent current dipoles that are taken into consideration when doing the source reconstruction. Note that not all source reconstruction methods require an explicit definition of a source model. Note also, that by and large source models should have the same specifications, irrespective of whether you are reconstructing EEG or MEG data. In this tutorial we will demonstrate how to use subject-specific anatomical data to create different types of source models. Which source model is most appropriate depends on the source reconstruction algorithm used, the additional analysis steps you have in mind, and on your own preferences. The anatomical MRI data is available from the [download server](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip).

This tutorial will **not** show how to perform the source reconstruction itself. If you are interested in source reconstruction methods, you can go to the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and to the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

## Background

Depending of the source reconstruction algorithm you want to use, you have to a priori specify a model that describes the locations of the sources (and sometimes the orientation) that you want to take into account. Specifically, this pertains to distributed source modeling approaches (e.g., Minimum Norm Estimation procedures), and for scanning approaches (e.g., beamformers). Dipolefitting approaches in general do not require an a priori source model (apart from when you want to use the option 'gridsearch').
In general, one could construct a source model that defines positions of dipoles on a 3-dimensional grid (this is sometimes referred to as a volumetric source model), or on a 2-dimensional surface (typically the cortical sheet).

## Procedure

We will describe a few different ways to create a source model based on the anatomical mri of the [tutorial data set](/tutorial/meg_language) which is available [here](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip). Some of these procedures can be done entirely using high-level FieldTrip functions. Other procedures require the use of external software, in particular FreeSurfer, and Connectome-workbench.

- Construction of a source model based on a regular 3-dimensional grid of dipole positions.
- Construction of a source model based on a surface description of the cortical sheet.
- Performing group analysis on 3-dimensional source-reconstructed data.
- Performing group analysis on cortical sheet-based source-reconstructed data.

## Construction of a source model based on a regular 3-dimensional grid of dipole positions

Content is coming soon!

## Construction of a source model based on a surface description of the cortical sheet

### Preprocessing of the anatomical MRI, reslicing and coregistration

The anatomical preprocessing is done in MATLAB with FieldTrip. The goal of this step is to create a file with a T1w anatomical image that can be used for the creation of two 'geometric objects': a volume conduction model of the head (not covered in this tutorial), and a cortical sheet based source model. Moreover, this image will be used to create coregistration information to the different coordinate systems involved. One annoying thing to be aware of, and to think about in advance, is the fact that typically different parts of the pipeline assume (or require) different conventions of coordinate systems. Specifically, geometric information (sensor locations) in MEG/EEG (MEEG) data is typically expressed in a coordinate system that is defined based on external anatomical landmarks, whereas software used for processing of structural data usually requires coordinates to be expressed according to brain-anatomy related landmarks, such as the anterior and posterior commissures. More information about coordinate systems can be found at the [frequently asked question about coordinate systems](/faq/coordsys). To make a long story short, for now it suffices to know that you're safe if you know how to convert back and forth between the different relevant coordinate systems. The least error-prone and most convenient way to do this, is to create a well-defined reference anatomical image, which will be created with the following steps

- read the anatomical images into MATLAB with **[ft_read_mri](/reference/fileio/ft_read_mri)**.
- ensure that the coordinate system of the mri is defined according to the M/EEG device's coordinate system, which can be checked with **[ft_determine_coordsys](/reference/utilities/ft_determine_coordsys)** and imposed with **[ft_volumerealign](/reference/ft_volumerealign)**.
- optionally reslice the volume with **[ft_volumereslice](/reference/ft_volumereslice)** in order to have a uniform thickness for each slice, and to have the axes of the coordinate system lined up with the 'voxel axes'.
- save the coregistration matrix that defines the transformation from voxels to the M/EEG coordinate system, and the MEEG-aligned volume (the latter to be used for headmodel creation).
- coregister the same volumetric image to an acpc-based coordinate system, which allows the anatomical image to serve as in input image to FreeSurfer's automatic surface extraction pipeline.
- save the acpc-aligned anatomy in FreeSurfer compatible format, using **[ft_volumewrite](/reference/ft_volumewrite)**. This anatomical image will serve as starting point for the creation of the cortical sheet based source model.

Thus, the input of the preprocessing is the anatomical MRI. The output is two anatomical images, as well as a set of transformation matrices.

#### 0. Preamble

For this part of the tutorial you need a working copy of FreeSurfer (the below was written for version 6.0, but likely also works for higher versions), and of [Connectome-workbench](https://www.humanconnectome.org/software/connectome-workbench).

#### 1. Preparation of the anatomical MRI: read in MRI data

    mripath     = <directory-where-the-inputimage-is-located-and-where-the-output-will-be-stored>;
    subjectname = 'Subject01';
    mri         = ft_read_mri(fullfile(mripath,sprintf('%s.mri',subjectname)));

#### 2. Preparation of the anatomical MRI: impose coordinate system according to the M/EEG coordinates

In this example, we are using an MRI which has been processed to contain a transformation matrix that corresponds to the CTF convention. Thus, the coordinate system coincides with the coordinates in which the MEG sensors are expressed, and a coincidence between coordinate systems is a prerequisite for a meaningful source reconstruction. Often, however, the anatomical image is expressed in an arbitrary coordinate system, and it needs to be coregistered to the MEEG-based coordinate system.

To find out about the coordinate system of your mri, you can use the following function to check it.

    mri = ft_determine_coordsys(mri, 'interactive', 'yes');

If it worked well, you will see the coordinate system specified in the mri structure in the mri.coordsys field. If 'coordsys' is not 'ctf' (in this example), or according to the mnemonic that is used to designate the coordinate system in which the M/EEG sensors/electrodes are expressed, you will need to align your mri, e.g., using anatomical landmarks (typically nasion, and left/right pre-auricular points) with the **[ft_volumerealign](/reference/ft_volumerealign)** function. The mnemonic 'ctf' for the coordsys is used to indicate the coordinate system used here. Ft_volumerealign does not change the anatomical data, instead it creates a transformation matrix that aligns the anatomical data to the intended coordinate system. Note that the following step can be skipped for the example MRI image used here.

    cfg          = [];
    cfg.method   = 'interactive';
    cfg.coordsys = 'ctf';
    mri          = ft_volumerealign(cfg, mri);

#### 3. Incorporate headshape information (optional)

If you have additionally used the Polhemus to record the headshape and the location of the head localizer coils, you can use these to refine the alignment between the MEG and MRI data. For this you can use **[ft_read_headshape](/reference/fileio/ft_read_headshape)** and **[ft_volumerealign](/reference/ft_volumerealign)** with method 'headshape' to either automatically or interactively rotate, scale and translate the MRI until it matches the recorded headshape best. In this example it does not add additional information beyond the MRI, since the headshape was not recorded but obtained from the anatomical MRI (post-coregistration) using the CTF MRIViewer software. The output will contain an updated transformation matrix.

    headshape = ft_read_headshape('Subject01.shape');

    % first align to headshape automatically
    cfg                       = [];
    cfg.method                = 'headshape';
    cfg.headshape.headshape   = headshape;
    cfg.headshape.icp         = 'yes';
    cfg.headshape.interactive = 'no';
    mri                       = ft_volumerealign(cfg, mri);

    % second call, but this time interactive to check result and potentially perform manual correction.
    cfg.headshape.interactive = 'yes';
    mri                       = ft_volumerealign(cfg, mri);

{% include markup/red %}
Note that it really only makes sense to take additional head shape information into account if it is congruent with the data acquisition. If you record information about the head shape in relation to the head localizer coils (fiducials) on LPA/RPA and on nasion, you should make sure to use the same fiducial locations as those used during the MEG session.
{% include markup/end %}


#### 4. Preparation of the anatomical MRI: reslicing

This step reslices the anatomical volume in a way that voxels will be isotropic. We use 1 mm resolution and we specify the dimension as 256X256X256, because this is the format which FreeSurfer works with. Note that this will also affect the transformation matrix, which is why we save it to file only after the reslicing.

    cfg            = [];
    cfg.resolution = 1;
    cfg.dim        = [256 256 256];
    mri            = ft_volumereslice(cfg, mri);

For later use, we also save the transformation matrix.

  transform_vox2ctf = mri.transform;
  save(fullfile(mripath,sprintf('%s_transform_vox2ctf',subjectname)), 'transform_vox2ctf');


#### 5. Preparation of the anatomical MRI: save to disk

    % save the resliced anatomy in a FreeSurfer compatible format
    cfg             = [];
    cfg.filename    = fullfile(mripath,sprintf('%sctf.mgz',subjectname));
    cfg.filetype    = 'mgz';
    cfg.parameter   = 'anatomy';
    ft_volumewrite(cfg, mri);

{% include markup/red %}
Importantly, the mgz-filetype is not fully supported on Windows platforms. Reading **and** writing can be done on Linux and Mac platforms. When you are processing the anatomical information on one of these platforms it is OK to save as mgz (and useful too, because it compresses the files and uses less diskspace as a consequence). These files cannot be saved on a Windows PC (although reading is possible). If you use MATLAB on Windows, you can save the volume as a nifti file using cfg.filetype = 'nifti'. Subsequently, if needed, you can convert it to mgz using [mri_convert](http://surfer.nmr.mgh.harvard.edu/fswiki/mri_convert) with FreeSurfer. Note, however, that as far as the writer of this tutorial knows, FreeSurfer itself does not run on Windows.
{% include markup/end %}

#### 6. Preparation of the anatomical MRI: coregister to coordinate system according to the 'acpc' convention

In order for the freesurfer pipeline to work, the anatomical image needs to be also be coregistered to the 'acpc' coordinate system, otherwise freesurfer does not know where to start. 'acpc' stands for anterior commissure and posterior commissure, and refers to the origin of the coordinate system, as well as the line that defines the posterior-anterior (Y) axis of the coordinate system. It is a RAS-based coordinate system.

    cfg          = [];
    cfg.method   = 'interactive';
    cfg.coordsys = 'acpc';
    mri          = ft_volumerealign(cfg, mri);

For later use, we save the transformation matrix. Combined with the transformation matrix saved earlier, we can now toggle back and forth between the acpc-based coordinates, and the ctf-based coordinates.

    transform_vox2acpc = mri.transform;
    save(fullfile(mripath,sprintf('%s_transform_vox2acpc',subjectname)), 'transform_vox2acpc');

Also save the acpc-coregistered anatomical image, this file will be the input file for the freesurfer processing pipeline:

    cfg          = [];
    cfg.filename = fullfile(mripath,sprintf('%s.mgz',subjectname));
    cfg.filetype = 'mgz';
    cfg.parameter = 'anatomy';
    ft_volumewrite(cfg, mri);

The MATLAB-based preparation of the anatomical data is now finished. We created two .mgz files, one that can be used for the creation of a cortical sheet-based source model (Subject01.mgz), and one that can be used for the creation of a volume conduction model of the head (Subject01ctf.mgz). Moreover, 2 coregistration matrices have been constructed that enable switching between coordinate systems.

### Creation of cortical sheet with FreeSurfer and resampling with Connectome workbench

#### Source model: Introduction

We will use FreeSurfer to create a source model that is based on a description of the cortical sheet. Essentially, we will construct a triangulated cortical mesh, ideally consisting of a number of approximately equally sized triangles that form a topological sphere for each of the cerebral hemispheres. FreeSurfer generates meshes with > 100000 vertices per hemisphere, which is too much for a workable M/EEG source reconstruction. Therefore, we use Connectome workbench to downsample the triangulated meshes. This step serves the purpose of retaining a topologically correct description of the surface, and keeping the variance in triangle size low. In contrast, MATLAB's reducepatch function breaks the topology and leads to a bigger variance in triangle size. A convenient byproduct of the proposed Connectome workbench-based processing is that the resulting cortical meshes are surface-registered to a common template, which allows for direct comparison of dipole locations with the same index across subjects.

The creation process of the source-space can be divided into 3 stages:

1.  Volumetric and surface-based processing in FreeSurfer.
2.  Creation of the mesh using Connectome workbench.
3.  Coregistration of the source model to the MEEG-based coordinate system with FieldTrip.

The volumetric and surface based processing typically take a long time (on the order of 10 hours). These steps will run automatically, and most of the time don't require user intervention. Sometimes, however, the automatic procedure fails, which requires inspection of the logs and/or inspection of the files created by FreeSurfer. In our experience, the most likely causes are a mismatch of input coordinate system (which can be resolved by checking and fixing the MATLAB-based coregistration steps), or an otherwise suboptimal white matter segmentation, or skullstripping. This is mostly due to slabs of dura being attached to the white matter volumes. This needs to be corrected manually. Please refer to the FreeSurfer documentation for more information. In practice this would mean that parts of the FreeSurfer pipeline needs to be redone after correction of the relevant volumes.

The input of the creation process of the meshes is the acpc-coregistered mgz file that was created previously. The output is the source model that is a MATLAB structure called 'sourcemodel' in this tutorial.

The exact specifics of how to run FreeSurfer and Connectome workbench may depend on your local computing infrastructure. The code below has been tested to work for users that work with the compute cluster at the Centre for Cognitive Neuroimaging of the Donders Institute in Nijmegen.

#### 1. Source model: Volumetric and surface-based processing in FreeSurfer

FreeSurfer's anatomical processing pipeline consists of a series of automated steps, which essentially consist of:

1.  processing steps on a volumetric anatomical MRI (image intensity normalization, co-registration with Talairach space, skull stripping, automatic segmentation of sub-cortical structures, and finally segmentation).
2.  extraction of the cortical mesh.
3.  processing of the surface meshes (smoothing, topology fixing, inflation, co-registration with a spherical template).

Here is a [link](http://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllDevTable) to the different processing steps. Although the FreeSurfer procedure can be invoked using only a few FreeSurfer commands, below we will describe the (sub)commands that will achieve the same. These commands sequentially generate a series of files (volumetric, surface and transformation matrices). Each of the output files serves as input to the sequential analysis steps. A table of file dependencies can be found [here](http://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllFilesVsSteps).

There are a few analysis steps in FreeSurfer which are not guaranteed to give a nice result, and may require some user interaction to get it right. Moreover, FreeSurfer can be quite picky with respect to the exact format of the MRI-volumes. One step which in our experience is notorious for not being very robust in older versions of FreeSurfer is automatic skull-stripping. Therefore, we used to advocate a hybrid approach that uses SPM or FSL for an initial segmentation of the anatomical MRI during the preparation. With this segmentation, we can create a skull-stripped image, which is a prerequisite for a correct segmentation in FreeSurfer. Since this approach is a bit convoluted (because it required the skullstripped image to be copied into the FreeSurfer directory in a specific format), and given the interdependencies between different files generated along the FreeSurfer pipeline (which moreover are FreeSurfer version specific), tapping into this pipeline at a random point is quite complicated. For this reason we discontinue the dissemination of this hybrid approach, and hope for the better that more recent versions of FreeSurfer work more robustly.

In order to be able to use FreeSurfer, you need to have a working installation of the package. It can be downloaded from [here](http://surfer.nmr.mgh.harvard.edu/fswiki). If you are working at the Donders Centre for Cognitive Neuroimaging (DCCN), FreeSurfer is available at the compute cluster, and you can find more versions of FreeSurfer under the /opt/FreeSurferXXX directories, and it will be typically available in a terminally (i.e. the module is automatically loaded upon opening a terminal). If you are working at the MPI for Psycholinguistics, you should install the software yourself in your directory. This tutorial has been written and tested with FreeSurfer 6.0, but most likely higher versions will also work. You can run the commands just copying and pasting them into the terminal window of the Linux system.

To get started, you need to set up your environment variables. Please pay close attention to the spaces in the following commands, or the lack thereof.

```shell
export FREESURFER_HOME=<path to FreeSurfer>
export SUBJECTS_DIR=<Subject directory>
export SUBJECTNAME=<Subject name>
```

SUBJECTS_DIR is the directory where you will store all the FreeSurfer-processed anatomical data of all your subjects. Then, type this command to set up FreeSurfer (this is not needed when at DCCN, but probably won't hurt)

```shell
source $FREESURFER_HOME/SetUpFreeSurfer.sh
```

The following populates an empty subject-specific directory with empty subdirectories

```shell
mksubjdirs $SUBJECTS_DIR/$SUBJECTNAME
```

Now, we are ready to start using FreeSurfer. As a first step, we have to 'convert' the anatomical MRI once more, but now using a FreeSurfer command. You start by putting the prepared acpc-registered MRI file which you created during the preparation steps in the subject specific "mri" directory. Subsequently, this image is once more converted (adjusting the image orientation), using the mri_convert function from FreeSurfer.

```shell
cp $SUBJECTS_DIR/$SUBJECTNAME.mgz $SUBJECTS_DIR/$SUBJECTNAME/mri/$SUBJECTNAME.mgz

cd $SUBJECTS_DIR/$SUBJECTNAME/mri
mri_convert -c -oc 0 0 0 $SUBJECTNAME.mgz orig.mgz
cp orig.mgz orig/001.mgz
# This last step is needed in version 6.0, not needed in 5.3

# Now run the automatic processing
recon-all -autorecon1 -subjid $SUBJECTNAME
recon-all -autorecon2 -subjid $SUBJECTNAME
recon-all -autorecon3 -subjid $SUBJECTNAME
```

After these steps (which may take quite a while) you end up with a bunch of files in the **Subject01/surf/** directory. The commands referenced above are also available as a Bash-script in fieldtrip/bin/ft_freesurferscript.sh, for instance to be used in a batch processing mode.

#### 2. Source model: Creation of the mesh using HCP workbench

Just like with FreeSurfer, you have to first take care that Connectome workbench is installed and available on the path. If you work on the compute cluster of the DCCN in Nijmegen, this is already installed. Otherwise, please refer to the Connectome workbench documentation to set up the software [here](https://www.humanconnectome.org/software/connectome-workbench). In addition, this step needs as set of template files, that for now need to be retrieved from two different locations. First, you need to get the standard/mesh_atlases directory from [here](https://github.com/Washington-University/HCPpipelines), which is located in the global/templates/ directory. One way to do this would be to selectively copy the contents of this directory to a location on your file system. Then, you also need to copy the template spherical meshes from fieldtrip/template/sourcemodel to the same directory. The files you need are the ones that are named L.\*.gii, and R.\*.gii. Once all files are in place, you should ensure that the Connectome workbench module is loaded and ready to use. The precise details of how to do this will depend on your local computing infrastructure, but if you are working at the Center for Cognitive Neuroimaging at the Donders Institute in Nijmegen you can do this by typing the following command in your Linux/Unix terminal:

    module load hcp-workbench

Then you can run the fieldtrip/bin/ft_postfreesurferscript.sh from the Linux command line, in the following way:

    <PATH_TO_FIELDTRIP>/fieldtrip/bin/ft_postfreesurferscript.sh <OUTPUTDIRECTORY> <SUBJECTNAME> <TEMPLATEDIRECTORY>

Where the <OUTPUTDIRECTORY> is the path to where the FreeSurfer results are located, <SUBJECTNAME> is, in this case Subject01, and <TEMPLATEDIRECTORY> is the path to where the templates are stored. If the script runs without error you will find in the Subject01 directory a folder, called workbench, which contains a bunch of files. These files are left and right hemispheric cortical meshes at different resolutions, with 164/32/8/4k vertices per hemisphere. Most practically for M/EEG source reconstruction purposes, we typically use the 8k or 4k meshes for further processing. It's up to you if you want to keep the 32k and 164k resolution images.

#### 3. Source model: Co-registration of the source space to the sensor-based head coordinate system

We now have the cortical meshes as a pair of gifti files, one for each hemisphere, where the coordinates of the vertices are expressed in the acpc-based coordinate system. The meshes can be loaded into MATLAB using the following code (here we use the 8k resolution meshes):

    datapath = fullfile(mripath,subjectname,'workbench');
    filename = fullfile(datapath,[subjectname,'.L.midthickness.8k_fs_LR.surf.gii']);
    sourcemodel = ft_read_headshape({filename, strrep(filename, '.L.', '.R.')});

As a final step for these meshes to be used for M/EEG forward and inverse modelling, we need to co-register the source space to the sensor-array (i.e., we have to express the positions of the sources in the same coordinate system as the sensors). For this, we will use the transformation matrices computed earlier in this tutorial. Specifically, using a single anatomical volume, we obtained 2 transformation matrices, that describe the mapping of voxel indices to the sensor-based coordinate system **transform_vox2ctf** and to the acpc-based coordinate system **transform_vox2acpc**. These two matrices can be combined to yield a transformation matrix that transforms from acpc-based coordinates to sensor-based coordinates:

    load(fullfile(mripath,[subjectname,'_transform_vox2acpc']));
    load(fullfile(mripath,[subjectname,'_transform_vox2ctf']));
    transform_acpc2ctf = transform_vox2ctf/transform_vox2acpc;

Then, this transformation can be applied to the vertex-positions in the source model, and with some additional small adjustments the source model can be saved to file.

    sourcemodel = ft_transform_geometry(transform_acpc2ctf, sourcemodel);
    sourcemodel.inside = sourcemodel.atlasroi>0;
    sourcemodel = rmfield(sourcemodel, 'atlasroi');
    save(fullfile(mripath,sprintf('%s_sourcemodel_15684',subjectname)), 'sourcemodel');

Optionally, you can then plot the source model to check the output using the following code:

    figure
    ft_plot_mesh(sourcemodel, 'maskstyle', 'opacity', 'facecolor', 'black', 'facealpha', 0.25, 'edgecolor', 'red',   'edgeopacity', 0.5);

That concludes this part of the tutorial.

## Performing group analysis on 3-dimensional source-reconstructed data

When you are doing a group study, where you want to combine the source-reconstructed data across multiple subjects, you can do this in two ways:

1.  Interpolation of functional data followed by volumetric spatial normalization;
2.  Anticipate the spatial normalization, and perform source reconstruction for each subject on a subject-specific grid, that maps onto a template grid in spatially normalized space.

We recommend the second strategy, but for completeness we also describe the first strategy.

### Interpolation, followed by spatial normalization

This is the simplest method, but not the most efficient. You start with a single subject source estimation on a 3D grid that is constructed individually for each subject (see above). After computing the source estimate (i.e. the "functional data"), you interpolate the functional data onto the anatomical data using **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)**. Subsequently you spatially transform the anatomical and the functional data for each subject to a template image using **[ft_volumenormalise](/reference/ft_volumenormalise)**. Having done that for every subject, and having used the same template image for each of the subjects, all grid points are expressed in normalized MNI coordinates and can be statistically compared between conditions over all subjects.

### Subject-specific grids that are equivalent across subjects in normalized space

##### Procedure

The idea is to use a template grid that is defined in normalized space, e.g., based on a template anatomical MRI in MNI coordinates. Subsequently, each individual MRI is warped to this template MRI, and the inverse of this warp is applied to the template dipole grid. Hereby the individual subjects' grids are not regularly spaced anymore (meaning the distance between 2 grid points can vary), see figure 1. However, as a consequence of this warping procedure, homologous grid points across subjects are located at exactly the same location in normalized MNI space. As a consequence, the source-reconstructed activity can be directly averaged across subjects. You can either define a template grid yourself, or use one from a set of predefined template grids that are included in fieldtrip: fieldtrip/template/sourcemodel/standard_gridXmm.mat.

{% include image src="/assets/img/tutorial/sourcemodel/figure1.gif" width="500" %}

_Figure 1a: Example: the MNI template brain and the brains of 3 subjects._

{% include image src="/assets/img/tutorial/sourcemodel/figure2.gif" width="500" %}

_Figure 1b: Example: the MNI grid and the grid of 3 subjects, note that each grid point points to the same location in all brains, and that the subjects' grids are not regularly spaced._

In the figures above, the spatial deformation of the individual subjects' brains relative to the template brain is exemplified. However, there may be other relevant differences between the coordinate system used for the individual subjects' anatomy and the MNI coordinate system. For example, in MEG-datasets it is custom to use a coordinate system that is defined relative to the three coils that are placed on the nose and the ears, with a specific orientation of the coordinate axes, whereas the MNI/SPM coordinate system is defined in a different way.

First, you need to define a template grid, as mentioned above, and the easiest thing to do so is to load in a pre-existing template grid. These template grids are in fieldtrip/template/sourcemodel, and are called standard_sourcemodel3dXmm, where X denotes the dipole spacing in mm. Below, we use a 10 mm grid. See [Template models for source reconstruction](/template/sourcemodel) for more information.

##### Load a template_grid, recommended

    % NOTE: the path to the template file is user-specific
    ftpath   = '/home/common/matlab/fieldtrip'; % this is the path to FieldTrip at Donders
    load(fullfile(ftpath, 'template/sourcemodel/standard_sourcemodel3d10mm'));
    template_grid = sourcemodel;
    clear sourcemodel;

As an alternative you can create a template grid yourself, like this:

##### Make a template_grid, only if you really want to

    % NOTE: the path to the template file is user-specific
    ftpath   = '/home/common/matlab/fieldtrip'; % this is the path to FieldTrip at Donders
    template = ft_read_mri(fullfile(ftpath, '/external/spm8/templates/T1.nii'));
    template.coordsys = 'spm'; % so that FieldTrip knows how to interpret the coordinate system

    % segment the template brain and construct a volume conduction model (i.e. head model):
    % this is needed to describe the boundary that define which dipole locations are 'inside' the brain.
    cfg          = [];
    template_seg = ft_volumesegment(cfg, template);

    cfg          = [];
    cfg.method   = 'singleshell';
    template_headmodel = ft_prepare_headmodel(cfg, template_seg);
    template_headmodel = ft_convert_units(template_headmodel, 'cm'); % Convert the vol to cm, because the CTF convenction is to express everything in cm.

    % construct the dipole grid in the template brain coordinates
    % the negative inwardshift means an outward shift of the brain surface for inside/outside detection
    cfg              = [];
    cfg.resolution   = 1;
    cfg.tight        = 'yes';
    cfg.inwardshift  = -1.5;
    cfg.headmodel    = template_headmodel;
    template_grid    = ft_prepare_sourcemodel(cfg);

    % make a figure with the template head model and dipole grid
    figure
    hold on
    ft_plot_headmodel(template_headmodel, 'facecolor', 'cortex', 'edgecolor', 'none');alpha 0.5; camlight;
    ft_plot_mesh(template_grid.pos(template_grid.inside,:));

{% include image src="/assets/img/tutorial/sourcemodel/figure3.png" width="300" %}

**fig 2: template grid and headmodel, top view**

##### Make the individual subjects' volume conduction model

It is not required to create a volume conduction model of the head in order to create the source model. We do it here in order to use it later for visualization.

    % read the single subject anatomical MRI, this should be aligned to MEG head coordinates
    % if the MRI is not aligned, you should use ft_volumerealign
    mri = ft_read_mri('Subject01.mri');

    % segment the anatomical MRI
    cfg        = [];
    cfg.output = 'brain';
    seg        = ft_volumesegment(cfg, mri);

    % construct the volume conductor model (i.e. head model) for each subject
    % this is optional, and for the purpose of this tutorial only required for
    % plotting, later on
    cfg        = [];
    cfg.method = 'singleshell';
    headmodel  = ft_prepare_headmodel(cfg, seg);

##### Make the individual subjects' grid

    % create the subject specific grid, using the template grid that has just been created
    cfg           = [];
    cfg.method    = 'basedonmni';
    cfg.template  = template_grid;
    cfg.nonlinear = 'yes';
    cfg.mri       = mri;
    cfg.unit      ='mm';
    grid          = ft_prepare_sourcemodel(cfg);

    % make a figure of the single subject headmodel, and grid positions
    figure; hold on;
    ft_plot_headmodel(headmodel, 'edgecolor', 'none', 'facealpha', 0.4);
    ft_plot_mesh(grid.pos(grid.inside,:));

{% include image src="/assets/img/tutorial/sourcemodel/figure4.png" width="300" %}

**fig 3: template grid in single-subject head coordinates, superimposed onto the headmodel**

{% include markup/red %}
Keep in mind that the .pos field in the source models are subject specific. When you want to do group analysis across subjects, which now in principle is allowed due to the equivalence of the dipole positions in normalized space, you need to replace the positions with the normalized positions of the template sourcemodel. Otherwise, FieldTrip will throw an error.
{% include markup/end %}

## Performing group analysis on cortical-sheet based source-reconstructed data

If you performed source reconstruction on the cortical surface, and you used the recipe explained earlier in this tutorial, single-subject data can be directly compared across subjects, because the dipole locations are surface-registered to a template.

## Summary and further reading

This tutorial explained how to build a sourcemodel that can be used for source reconstruction of EEG or MEG measurements.

You can read more about specific source reconstruction methods in the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and in the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

## See also

{% include seealso tag1="sourcemodel" tag2="meg" %}
