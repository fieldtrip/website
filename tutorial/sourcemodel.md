---
title: Creating a sourcemodel for source-reconstruction of MEG or EEG data
tags: [tutorial, source, meg, sourcemodel, mri, plot, MEG-language]
---

# Creating a sourcemodel for source-reconstruction of MEG or EEG data

## Introduction

In this tutorial you can find information about how to construct a source model that can be used for source reconstruction of EEG or MEG data. The source model describes a set of positions (and possibly orientations) of equivalent current dipoles that are taken into consideration when doing the source reconstruction. Note that not all source reconstruction methods require an explicit definition of a source model. Note also, that by and large source models should have the same specifications, irrespective of whether you are reconstructing EEG or MEG data. In this tutorial we will show how to use subject-specific anatomical data to create different types of source models. Which source model is most appropriate depends on the source reconstruction algorithm used, the additional analysis steps you have in mind, and on your own preferences. The anatomical MRI data is available from the [ftp server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).

This tutorial will **not** show how to perform the source reconstruction itself. If you are interested in source reconstruction methods, you can go to the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and to the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

## Background

Depending of the source reconstruction algorithm you want to use, you have to a priori specify a model that describes the locations of the sources (and sometimes the orientation) that you want to take into account. Specifically, this pertains to distributed source modelling approaches (e.g. Minimum Norm Estimation procedures), and for scanning approaches (e.g. beamformers). Dipolefitting approaches in general do not require an a priori source model (apart from when you want to use the option 'gridsearch').
In general, one could construct a source model that defines positions of dipoles on a 3-dimensional grid (this is sometimes referred to as a volumetric source model), or on a 2-dimensional surface (typically the cortical sheet).

## Procedure

We will describe a few different ways to create a source model based on the anatomical mri of the [tutorial data set](/tutorial/meg_language) which is available [here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip). Some of these procedures can be done entirely using high-level FieldTrip functions. Other procedures require the use of external software, in particular Freesurfer, or HCP-workbench.

*  Construction of a source model based on a regular 3-dimensional grid of dipole positions;
*  Construction of a source model based on a surface description of the cortical sheet;
*  Performing group analysis on 3-dimensional source-reconstructed data.
*  Performing group analysis on cortical-sheet based source-reconstructed data.

## Construction of a source model based on a regular 3-dimensional grid of dipole positions

Content is coming soon!

## Construction of a source model based on a surface description of the cortical sheet

### Preprocessing of the anatomical MRI, reslicing and coregistration

The anatomical preprocessing is done in MATLAB with FieldTrip. The goal of this step is to create a file with a T1w anatomical image that can be used for the creation of two 'geometric objects': a volume conduction model, and a cortical sheet based source model. Moreover, this image will be used to create coregistration information to the different coordinate systems involved. One annoying thing to be aware of, and to think about in advance, is the fact that typically different parts of the pipeline assume (or require) different conventions of coordinate systems. Specifically, geometric information (sensor locations) in MEG/EEG data is typically expressed in a coordinate system that is defined based on external anatomical landmarks, whereas software used for processing of structural data usually requires coordinates to be expressed according to brain-anatomy related landmarks, such as the anterior and posterior commissures. More information about coordinate systems can be found at the [frequently asked question about coordinate systems](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined). To make a long story short, for now it suffices to know that you're safe if you know how to convert back and forth between the different relevant coordinate systems. The least error-prone and most convenient way to do this, is to create a well-defined reference anatomical image, which will be created with the following step

*  read in the anatomical images into MATLAB with **[ft_read_mri](/reference/ft_read_mri)**
*  ensure that the coordinate system is according to MNI's RAS convention, which can be checked with **[ft_determine_coordsys](/reference/ft_determine_coordsys)** and imposed with **[ft_volumerealign](/reference/ft_volumerealign)**.
*  reslice the volume with **[ft_volumereslice](/reference/ft_volumereslice)** in order to have a uniform thickness for each slice, and to have the axes of the coordinate system lined up with the 'voxel axes'.
*  save the coregistration matrix that defines the transformation from voxels to MNI-RAS.
*  save the resliced anatomy in FreeSurfer compatible format, using **[ft_volumewrite](/reference/ft_volumewrite)**. This anatomical image will serve as starting point for the creation of the cortical sheet based source model.

Then we may need to also create coregistration information to the coordinate system used in the MEG/EEG data.

*  realign the resliced anatomical data to the MEG/EEG based coordinate system with **[ft_volumerealign](/reference/ft_volumerealign)**.
*  save the coregistration matrix that defines the transormation from voxels to the MEG/EEG coordinate system.

Thus, the input of the preprocessing is the anatomical MRI. The output is a realigned and resliced anatomical image, as well as a set of transformation matrices.

#### 1. Preprocessing of the anatomical MRI: read in MRI data

	mri = ft_read_mri('Subject01.mri');

#### 2. Preprocessing of the anatomical MRI: impose coordinate system according to MNI convention

In this example, we are using an MRI which has been processed to contain a transformation matrix that corresponds to the CTF convention. As outlined above, life will be much easier if the coordinate system is in accordance with the MNI convention. Therefore, it needs to be 'realigned'. In general, it may be not clear what coordinate system is attached to the anatomical image.  

To find out about the coordinate system of your mri, you can use the following function to check i

	mri = ft_determine_coordsys(mri, 'interactive', 'yes');

If it worked well, you will see the coordinate system specified in the mri structure in the mri.coordsys field. If 'coordsys' is not 'spm', you will need to align your mri to the anatomical landmarks (anterior commissure, posterior commissure, and a point that defines the postive z-direction) with the **[ft_volumerealign](/reference/ft_volumerealign)** function. The mnemonic 'spm' for the coordsys is used to indicate this MNI-based convention. Ft_volumerealign does not change the anatomical data, instead it creates a transformation matrix that aligns the anatomical data to the intended coordinate system.

	cfg = [];
	cfg.method = 'interactive';
	cfg.coordsys = 'spm';
	mri_spm    = ft_volumerealign(cfg, mri);

#### 3. Preprocessing of the anatomical MRI: reslicing

This step reslices the anatomical volume in a way that each slice will be equally thick. We use 1 mm thick slices and we specify the dimension as 256X256X256, because this is the format which FreeSurfer works with.

	cfg            = [];
	cfg.resolution = 1;
	cfg.dim        = [256 256 256];
	mri_spm_rs     = ft_volumereslice(cfg, mri_spm);
	transform_vox2spm = mri_spm_rs.transform;

For convenience, you can now save the transformation matrix.

	save('Subject01_transform_vox2spm', 'transform_vox2spm');

#### 4. Preprocessing of the anatomical MRI: save to disk

	% save the resliced anatomy in a FreeSurfer compatible format
	cfg             = [];
	cfg.filename    = 'Subject01';
	cfg.filetype    = 'mgz';
	cfg.parameter   = 'anatomy';
	ft_volumewrite(cfg, mri_spm_rs);

{% include markup/danger %}
Importantly, the mgz-filetype can **only** be used on Linux and Mac platforms. When you are processing the anatomical information on one of these platforms it is OK to save as mgz (and useful too, because it compresses the files and uses less diskspace as a consequence). These files cannot be saved nor read on a Windows PC. If you use MATLAB on Windows, you can save the volume as a nifti file using cfg.filetype = 'nifti'. Subsequently, if needed, you can convert it to mgz using [mri_convert](http://surfer.nmr.mgh.harvard.edu/fswiki/mri_convert) with FreeSurfer.
{% include markup/end %}

#### 5. Preprocessing of the anatomical MRI: impose coordinate system according to M/EEG convention

Since this example is concerned with CTF-MEG data, we will need to get coregistration information that expresses anatomical information in coordinates according to the CTF-convention. To this end, we do a second realignment, now using the resliced anatomical image.

	cfg          = [];
	cfg.method   = 'interactive';
	cfg.coordsys = 'ctf';
	mri_ctf_rs   = ft_volumerealign(cfg, mri_spm_rs);
	transform_vox2ctf = mri_ctf_rs.transform;

For convenience, you can now save the transformation matrix.

	save('Subject01_transform_vox2ctf', 'transform_vox2ctf');

The MATLAB-based preprocessing of the anatomical data is now finished. We created an .mgz files that can be used for the creation of a cortical-sheet based source model and a volume conduction model. Moreover, 2 coregistration matrices have been constructed that allow to switch between coordinate systems.

###  Creation of cortical sheet with Freesurfer and downsampling with MNE suite

#### Source model: Introduction

We will use FreeSurfer to create a source model that is based on a description of the cortical sheet. Essentially, we will construct a triangulated cortical mesh, ideally consisting of a number of approximately equally sized triangles that form a topological sphere for each of the cerebral hemispheres. The latter property is required to create an inflated cortex and to do intersubject realignment. FreeSurfer generates meshes with > 100000 vertices per hemisphere, which is too much for a workable M/EEG source reconstruction. Therefore, we use the MNE-suite to downsample the triangulated meshes. This step serves the purpose of retaining a topologically correct description of the surface, and keeping the variance in triangle size low. In contrast, MATLAB's reducepatch function breaks the topology and leads to a bigger variance in triangle size.
The creation process of the source-space can be divided into 4 stages (after the preprocessing steps
 1.  Volumetric processing in FreeSurfer.
 2.  Surface based processing in FreeSurfer.
 3.  Creation of the mesh using MNE-suite.
 4.  Coregistration of the source space to the sensor-based coordinate system with FieldTrip.

The volumetric and surface based processing (first and the second steps) can be together 10 hours long. These steps will run on the computer from themselves. There is only one checkpoint between the volume and the surface based processing when an intermediate result can be checked interactively.

The input of the creation process of the source-space are mgz files that were created in the preprocessing. The output is the source model that is a MATLAB structure called 'sourcespace' in this tutorial.

The instructions about how to install and run FreeSurfer and MNE Suite are aimed at users at the Center of Neuroimaging of the Donders Institute and at the MPI for Psycholinguistics in Nijmegen.

#### 1. Source model: Volumetric processing in FreeSurfer

FreeSurfer's anatomical processing pipeline consists of a series of automated steps, which essentially consist o
 1.  processing steps on a volumetric anatomical MRI (image intensity normalization, co-registration with Talairach space, skull stripping, automatic segmentation of sub-cortical structures, and finally segmentation)
 2.  extraction of the cortical mesh
 3.  processing of the surface meshes (smoothing, topology fixing, inflation, co-registration with a spherical template)

Here is a [link](http://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllDevTable) to the different processing steps. Although the FreeSurfer procedure can be invoked using only a few FreeSurfer commands, below we will describe the (sub)commands that will achieve the same. These commands sequentially generate a series of files (volumetric, surface and transformation matrices). Each of the output files serves as input to the sequential analysis steps. A table of file dependencies can be found [here](http://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllFilesVsSteps).
There are a few analysis steps in FreeSurfer which are not guaranteed to give a nice result, and require some user interaction to get it right. Moreover, FreeSurfer can be quite picky with respect to the exact format of the MRI-volumes. One step which in our experience is notorious for not being very robust is automatic skull-stripping. Therefore, we advocate a hybrid approach that uses SPM for an initial segmentation of the anatomical MRI during the preprocessing. With this segmentation, we can create a skull-stripped image, which is a prerequisite for a correct segmentation in FreeSurfer. Although this approach may seem a bit convoluted (you may rightfully ask why we need to redo the segmentation in FreeSurfer if we already did it in SPM), the interdependencies between different files generated along the FreeSurfer pipeline make tapping into this pipeline at a random point quite complicated. For this reason a large part of the volumetric processing in FreeSurfer needs to be done as well.

To create a skullstripped anatomical image, you can do the following. We assume that you have executed all steps that are described in the section about preprocessing of the anatomical MRI, and that you have a file that contains the resliced anatomical image, expressed in the MNI-RAS coordinate system.

	mri = ft_read_mri('Subject01.mgz');
	mri.coordsys = 'spm';

	cfg = [];
	cfg.output = 'brain';
	seg = ft_volumesegment(cfg, mri);
	mri.anatomy = mri.anatomy.*double(seg.brain);

	cfg             = [];
	cfg.filename    = 'Subject01masked';
	cfg.filetype    = 'mgz';
	cfg.parameter   = 'anatomy';
	ft_volumewrite(cfg, mri);

In order to be able to use FreeSurfer, you need to have a working installation of the package. It can be downloaded from [here](http://surfer.nmr.mgh.harvard.edu/fswiki). If you are working at the Center of Neuroimaging of the Donders Institute you can find more versions of FreeSurfer under the /opt/FreeSurferXXX directories. (If you are working at the MPI for Psycholinguistics, you should install the software yourself in your directory.) We recommend to use FreeSurfer 5.3. You can run the commands just copying and pasting them into the terminal window of the Linux system (from where you used also MATLAB).

To get started, you need to set up your environment variables. Please pay close attention to the spaces in the following commands, or the lack thereof.

	export FREESURFER_HOME=`<path to FreeSurfer>`
	export SUBJECTS_DIR=`<Subject directory>`

SUBJECTS_DIR is the directory where you will store all the FreeSurfer-processed anatomical data of all your subjects. Then, type this command to set up FreeSurfe

	source $FREESURFER_HOME/SetUpFreeSurfer.sh

The following populates an empty subject-specific directory with subdirectorie

	mksubjdirs $SUBJECTS_DIR/Subject01

Now, we are ready to start using FreeSurfer. As a first step in the volumetric pipeline, we have to 'convert' the anatomical MRI once more, but now using a FreeSurfer command. You start by making a new folder in the subject directory called "mri" into which you will copy both the masked and the original mgz files you created in the previous preprocessing steps in FieldTrip. All subsequent FreeSurfer commands will be called from the "mri" directory.

	cp Subject01masked.mgz $SUBJECTS_DIR/Subject01/mri/Subject01masked.mgz
	cp Subject01.mgz       $SUBJECTS_DIR/Subject01/mri/Subject01.mgz
	cd $SUBJECTS_DIR/Subject01/mri

	mri_convert -c -oc 0 0 0 Subject01masked.mgz brainmask.mgz
	mri_convert -c -oc 0 0 0 Subject01.mgz       orig.mgz

	recon-all -talairach      -subjid Subject01
	recon-all -nuintensitycor -subjid Subject01
	recon-all -normalization  -subjid Subject01
	recon-all -gcareg         -subjid Subject01
	recon-all -canorm         -subjid Subject01
	recon-all -careg          -subjid Subject01
	recon-all -careginv       -subjid Subject01
	recon-all -calabel        -subjid Subject01
	recon-all -normalization2 -subjid Subject01
	recon-all -maskbfs        -subjid Subject01
	recon-all -segmentation   -subjid Subject01
	recon-all -fill           -subjid Subject01

This ends the part of the FreeSurfer pipeline concerned with volumetric processing. At this stage you should have a file **filled.mgz** containing the segmentation of the cortical white matter (cerebellum is not included!). You can check how this looks using FieldTrip, by doing the followin

	cd `<Subject directory>`/Subject01/mri
	mri = ft_read_mri('filled.mgz');

	cfg = [];
	cfg.interactive = 'yes';
	ft_sourceplot(cfg, mri);

{% include image src="/assets/img/tutorial/sourcemodel/filled01new.png" width="550" %}

*Figure 3. Filled mgz created by FreeSurfer. The two hemispheres have different colors (white and grey), cerebellum is not included.*

#### 2. Source model: Surface based processing in FreeSurfer

The surface construction is done by the following sequence of commands (from the Subject01/mri directory

	recon-all -fill       -subjid Subject01
	recon-all -tessellate -subjid Subject01
	recon-all -smooth1    -subjid Subject01
	recon-all -inflate1   -subjid Subject01
	recon-all -qsphere    -subjid Subject01
	recon-all -fix        -subjid Subject01
	recon-all -white      -subjid Subject01
	recon-all -finalsurfs -subjid Subject01
	recon-all -smooth2    -subjid Subject01
	recon-all -inflate2   -subjid Subject01

	# then use a shortcut command to do the rest, but we need the rawavg.mgz file to exist
	cp $SUBJECTS_DIR/Subject01/mri/Subject01.mgz $SUBJECTS_DIR/Subject01/mri/rawavg.mgz
	recon-all -autorecon3 -subjid Subject01

After these steps (which may take quite a while) you end up with a bunch of files in the **Subject01/surf/** directory. We are going to use **lh.white** and **rh.white** to create the source space in the next step.

#### 3. Source model: Creation of the mesh using MNE Suite

Just like with FreeSurfer, we have to first take care that MNE-suite is installed, and that some environmental variables are correctly specified. If you are working in Nijmegen at the DCCN, you can find the MNE suite under the /opt/mne directory. At the MPI, the MNE suite is installed under the /mnt/data1/mne directory.

	export MNE_ROOT=`<path to MNE>`
	source $MNE_ROOT/bin/mne_setup.sh

	export SUBJECTS_DIR=`<Subject directory>`
	export SUBJECT=Subject01

Now we can create the source space

	mne_setup_source_space --ico -6

This step creates a bunch of files in `<Subject directory>`/Subject01/bem/**, containing different representations of the source space. In subsequent steps, FieldTrip will use the **Subject01-oct-6-src.fif** file. We can already have a look in MATLAB at how the source space looks.

	sourcespace = ft_read_headshape('Subject01-oct-6-src.fif', 'format', 'mne_source');

	figure
	ft_plot_mesh(sourcespace);

{% include image src="/assets/img/tutorial/sourcemodel/sspace01new.png" width="450" %}

*Figure 4. The source-space downsampled by MNE Suite*

#### 4. Source model: Co-registration of the source space to the sensor-based head coordinate system

We have the source locations co-registered to the MNI coordinate system, so now we need to co-register the source space to the sensor-array (i.e., we have to express the positions of the sources in the same coordinate system as the sensors). For this, we will use the transformation matrices computed in earlier in this tutorial. Specifically, using the resliced anatomical data in the mrirs-structure, we obtained a set of 2 transformation matrices, that describe the mapping of anatomical volumetric voxel indices into the sensor-based coordinate system **transform_vox2ctf** and into the MNI coordinate system **transform_vox2spm**. These two matrices can be combined in the following way, to yield a transformation matrix that transforms from MNI coordinates to sensor-based coordinates:

	T = transform_vox2ctf/transform_vox2spm;

Now we can use this transformation matrix, to get it in the correct coordinate system.

	% go to the Subject01/bem directory
	sourcespace = ft_read_headshape('Subject01-oct-6-src.fif', 'format', 'mne_source');
	sourcespace = ft_convert_units(sourcespace, 'mm');
	sourcespace = ft_transform_geometry(T, sourcespace);

	save sourcespace sourcespace

## Performing group analysis on 3-dimensional source-reconstructed data

When you are doing a group study, where you want to combine the source-reconstructed data across multiple subjects, you can do in several way

 1.  Interpolation of functional data followed by volumetric spatial normalization;
 2.  Anticipate the spatial normalization, and perform source-reconstruction for each subject on a subject-specific grid, that maps onto a template grid in spatially normalized space.

We recommend the second strategy, but for completeness we also describe the first strategy.

### Interpolation, followed by spatial normalization

This is the simplest method, but not the most accurate. You start with a single subject source estimation on a 3D grid that is constructed individually for each subject. After computing the source estimate (i.e. the "functional data"), you interpolate the functional data onto the anatomical data using **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)**. Subsequently you spatially transform the anatomical and the functional data for each subject to the MNI template using **[ft_volumenormalise](/reference/ft_volumenormalise)**. Having done that for every subject, all data is expressed in MNI coordinates and can be statistically compared between conditions over all subjects.

###  Subject-specific grids that are equivalent across subjects in normalized space

##### Procedure

The idea is to use a template grid that is defined in normalized space, e.g. based on a template anatomical MRI in MNI coordinates. Subsequently, each individual MRI is warped to this template MRI, and the inverse of this warp is applied to the template dipole grid. Hereby the individual subjects' grids are not regularly spaced anymore (meaning the distance between 2 grid points can vary), see figure 1. However, as a consequence of this warping procedure, homologous grid points across subjects are located at exactly the same location in normalized MNI space. As a consequence, the source-reconstructed activity can be directly averaged across subjects. You can either define a template grid yourself, or use one from a set of predefined template grids that are included in fieldtrip: fieldtrip/template/sourcemodel/standard_gridXmm.mat.

{% include image src="/assets/img/tutorial/sourcemodel/brains.gif" width="500" %}--" %}

**Figure 1a: Example: the MNI template brain and the brains of 3 subjects**

{% include image src="/assets/img/tutorial/sourcemodel/mni_grids2.gif" width="500" %}--" %}

**Figure 1b: Example: the MNI grid and the grid of 3 subjects, note that each grid point points to the same location in all brains, and that the subjects' grids are not regularly spaced**

In the figures above, the spatial deformation of the individual subjects' brains relative to the template brain is exemplified. However, there may be other relevant differences between the coordinate system used for the individual subjects' anatomy and the MNI coordinate system. For example, in MEG-datasets it is custom to use a coordinate system that is defined relative to the three coils that are placed on the nose and the ears, with a specific orientation of the coordinate axes, whereas the MNI/SPM coordinate system is defined in a different way.

First, you need to define a template grid, as mentioned above, and the easiest thing to do so is to load in a pre-existing template grid, like this:

##### Load a template_grid, recommended

	% NOTE: the path to the template file is user-specific
	ftpath   = '/home/common/matlab/fieldtrip'; % this is the path to FieldTrip at Donders
	load(fullfile(ftpath, 'template/sourcemodel/standard_sourcemodel3d10mm');
	template_grid = sourcemodel;
	clear sourcemodel;

As an alternative you can create a template grid yourself, like thi

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
	cfg = [];
	cfg.grid.resolution = 1;
	cfg.grid.tight      = 'yes';
	cfg.inwardshift     = -1.5;
	cfg.headmodel       = template_headmodel;
	template_grid       = ft_prepare_sourcemodel(cfg);

	% make a figure with the template head model and dipole grid
	figure
	hold on
	ft_plot_vol(template_headmodel, 'facecolor', 'cortex', 'edgecolor', 'none');alpha 0.5; camlight;
	ft_plot_mesh(template_grid.pos(template_grid.inside,:));

{% include image src="/assets/img/tutorial/sourcemodel/mni_fig1a.png" width="300" %}

**fig 2: template grid and headmodel, top view**

##### Make the individual subjects' volume conduction model

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
	cfg                = [];
	cfg.grid.warpmni   = 'yes';
	cfg.grid.template  = template_grid;
	cfg.grid.nonlinear = 'yes';
	cfg.mri            = mri;
	cfg.grid.unit      ='mm';
	grid               = ft_prepare_sourcemodel(cfg);

	% make a figure of the single subject headmodel, and grid positions
	figure; hold on;
	ft_plot_vol(headmodel, 'edgecolor', 'none', 'facealpha', 0.4);
	ft_plot_mesh(grid.pos(grid.inside,:));

{% include image src="/assets/img/tutorial/sourcemodel/mni_fig2b.png" width="300" %}

**fig 3: template grid in single-subject head coordinates, superimposed onto the headmodel**

{% include markup/danger %}
Keep in mind that the .pos field in the source models are subject specific. When you want to do group analysis across subjects, which now in principle is allowed due to the equivalence of the dipole positions in normalized space, you need to replace the positions with the normalized positions of the template sourcemodel. Otherwise, FieldTrip will throw an error.
{% include markup/end %}

## Performing group analysis on cortical-sheet based source-reconstructed data

Content is coming soon!

## Summary and further reading

In this tutorial, it was explained how to build a sourcemodel that can be used for source-reconstruction of measured EEG or MEG activity.

You can read more about specific source-reconstruction methods in the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and in the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials.

## See also

{% include seealso tag1="sourcemodel" tag2="meg" %}
