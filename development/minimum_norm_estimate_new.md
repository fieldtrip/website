---
layout: default
---

`<note warning>`
The purpose of this page is just to serve as a scratch pad for the new version of a tutorial site.

There is no guarantee that this page is updated in the end to reflect the final state of the tutorial site.
So chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
`</note>`
# Source reconstruction of event-related fields using minimum-norm estimate

## Introduction

In this tutorial you can find information about how to do source-analysis with minimum-norm estimate on the event-related fields (MEG) of a single subject. We will working on the [dataset](/tutorial/shared/dataset) described in the preprocessing tutorials ([Trigger-based trial selection](/tutorial/preprocessing), [Event related averaging and planar gradient](/tutorial/eventrelatedaveraging)), and we will use also the anatomical images that belong to the same subject.  We will repeat code to select the trials and preprocess the data as described in the [Event related averaging and planar gradient](/tutorial/eventrelatedaveraging) tutorial. We assume that preprocessing and event-related averaging is already clear for the reader. To preprocess the anatomical data, we will use two other software packages (FreeSurfer and MNE Suite). 
 
This tutorial will not show how to do group-averaging and statistics on the source-level. It will also not describe how to do source-localization of oscillatory activation. You can check the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) tutorial if you are interested in the latter.

## Background

In the [Event related averaging and planar gradient](/tutorial/eventrelatedaveraging) tutorial time-locked averages of event related fields of three conditions have been computed and the [Cluster-based permutation tests on event related fields](/tutorial/cluster_permutation_timelock) tutorial showed that there was a significant difference among two conditions. The topographical distribution of the ERFs belonging to each conditions and ERFs belonging to those differences have been plotted. The aim of this tutorial is to calculate a distributed representation of the underlying neuronal activity that resulted in the brain activity observed at the sensor level.

To calculate distributed neuronal activation we will use the minimum-norm estimate. This approach is favored for analyzing evoked responses and for tracking the wide-spread activation over time. It is a distributed inverse solution that discretizes the source space into locations on the cortical surface or in the brain volume using a large number of equivalent current dipoles. It estimates the amplitude of all modeled source locations simultaneously and recovers a source distribution with minimum overall energy that produces data consistent with the measurement ((Ou, W., Hamalainen, M., Golland, P., 2008, A Distributed Spatio-temporal EEG/MEG Inverse Solver)) ((Jensen, O., Hesse, C., 2010, Estimating distributed representation of evoked responses and oscillatory brain activity, In: MEG: An Introduction to Methods, ed. by Hansen, P., Kringelbach, M., Salmelin, R., doi:10.1093/acprof:oso/9780195307238.001.0001)). The reference for the implemented method is [Dale et al. (2000)](/references_to_implemented_methods).
## Procedure

Figure 1. shows the bigger steps in the calculation of the minimum-norm estimate. It shows that the computation of the inverse solution is based on the outputs of two independent processing steps: the processing of the anatomical images that leads to the forward solution and the processing of the MEG data. Creating the source model requires the use of two additional software packages, FreeSurfer and MNE Suite.

![image](/media/tutorial/minimumnormestimate/analysis_protocol_mne.png@550)

*Figure 1. An overview of the bigger steps in the calculation of the minimum-norm estimate*

To compute the distributed neuronal activation using minimum-norm estimate we will perform the following step

*  Preprocess the anatomical images in Matlab: First, the mri image is read in with **[ft_read_mri](/reference/ft_read_mri)**,  then the volume realigned to the ctf coordinate system with  **[ft_volumerealign](/reference/ft_volumerealign)** and resliced with **[ft_volumereslice](/reference/ft_volumereslice)** to ensure that the volume is isotropic. The resliced volume is realigned to the MNI space with  **[ft_volumerealign](/reference/ft_volumerealign)** and segmented to obtain the skull-stripped anatomy and a brainmask with **[ft_volumesegment](/reference/ft_volumesegment)**. The volume realigned to the MNI space and the skull-stripped anatomical volume are written to disk with **[ft_volumewrite](/reference/ft_volumewrite)**;

*  Create a volume conduction model from the segmented volume using **[ft_prepare_singleshell](/reference/ft_prepare_singleshell)** and we re-align the volume conduction model to the ctf space using the transformation matrices of the earlier alignments with **[ft_convert_units](/reference/ft_convert_units)** and with **  [ft_transform_geometry](/reference/ft_transform_geometry)**;

*  Create a source space by using FreeSurfer and MNE Suite, and create the source model in Matlab using the functions **[ft_read_headshape](/reference/ft_read_headshape)** and we apply the transformation matrix created earlier with **[ft_convert_units](/reference/ft_convert_units)** and **[ft_transform_geometry](/reference/ft_transform_geometry)**; 

*  compute the forward solution using **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)**;

*  preprocess the MEG data using **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)**;

*  compute the average over trials and estimate the noise-covariance using **[ft_timelockanalysis](/reference/ft_timelockanalysis)**;

*  compute the inverse solution using **[ft_sourceanalysis](/reference/ft_sourceanalysis)** and **[ft_sourcedescriptives](/reference/ft_sourcedescriptives)**;

*  visualize the results with **[ft_plot_mesh](/reference/ft_plot_mesh)** and **[ft_sourcemovie](/reference/ft_sourcemovie)**.

## Processing of anatomical data

The following will use the anatomical MRI belonging to Subject01. The file can be obtained from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).
The functions described in this part of the tutorial are using toolboxes that are under the fieldtrip/external folder. You do not have to add these toolboxes yourself, but it is important that you set up your matlab path properly. You can read about how to set up your matlab path [here](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path). 

	
	addpath `<path to fieldtrip directory>`;
	ft_defaults;

### Preprocessing of the anatomical MRI

The following figure shows the steps of the preprocessing and of the rest of the anatomical processing (volume conduction and source-model).

![image](/media/tutorial/minimumnormestimate/anatomical_preproc_mne.png@500)

*Figure 2. Pipeline for processing of the anatomical data*

The anatomical preprocessing is done in Matlab with FieldTrip. At the end, a segmented mri is created for the volume conduction model, and an anatomical volume with and without brainmask is created in a Freesurfer compatible format for the source-space. The preprocessing involves the following step

*  read in the anatomical images into Matlab with **[ft_read_mri](/reference/ft_read_mri)**

*  (if your mri images are not in the CTF-coordinatesystem, you should realign them with the **[ft_volumerealign](/reference/ft_volumerealign)** function. If you do not know which coordinate system the images are aligned to, you can check it with the **[ft_determine_coordsys](/reference/ft_determine_coordsys)** function.) 

*  reslice the volume with **[ft_volumereslice](/reference/ft_volumereslice)** in order to have a uniform thickness for each slice

*  realign the resliced volume to the MNI space

*  save the CTF and also the MNI-aligned volume (we will need the field 'transform' of these later)

*  obtain a skull-stripped anatomy and a brain mask from the MNI-aligned mri volume using **[ft_volumesegment](/reference/volumesegment)**

*  save the MNI-aligned anatomy and the segmented anatomy in Freesurfer compatible format, using **[ft_volumewrite](/reference/ft_volumewrite)**. These two will be used for creating the source model.

The input of the preprocessing is the anatomical MRI. We will create four outputs that will be necessary for the subsequent processing: 2 files in .mgz format that will be used for creating the source space, a matlab structure called "seg" that will be used for creating the volume conduction model, and a transformation matrix that will help us later to transform the volume conductor and the source-model to CTF space later.

#### 1. Preprocessing of the anatomical MRI: read in MRI data

	
	mri = ft_read_mri('Subject01.mri');

#### 2. Preprocessing of the anatomical MRI: realign to CTF

The volume conduction model describes the geometry and the electrical (conductive) properties of the head. The volume conduction model (or headmodel) requires a geometrical description of the head. In this tutorial we have an anatomical MRI of the subject from which we can construct the head model. [Here](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined), you can read more about the coordinate systems. And [here](/tutorial/headmodel), you can read more about the headmodel.

In this example, we are using an MRI which has been already processed to contain a transformation matrix that corresponds to the CTF convention. Therefore, it does not need to be realigned. 

**I THINK THAT THE SECTION BELOW (UNTIL THE END OF THIS SECTION) SHOULD BE MADE INTO A SEPARATELY LINK. OTHERWISE, IT IS CONFUSING WHEN YOU SAY THAT YOU DON'T NEED TO REALIGN AND THEN SHOW THE CODE ANYWAY. FURTHERMORE, IF IT IS A TUTORIAL, THEN THE IMMEDIATE CODE BELOW WON'T WORK BECAUSE THERE IS NO VARIABLE mri_other THAT CAN BE USED AS AN INPUT ARGUMENT.  ALSO IF MADE INTO A SEPARATE LINK.**

But if you are not sure of the coordinate system of your mri, you can use the following function to check i

	
	mri_other = ft_determine_coordsys(mri_other, 'interactive', 'yes');

If it worked well, you will see the coordinate system specified in the mri structure in the mri.coordsys field. If 'coordsys' is not 'ctf', you will need to align your mri to the fiducial points (LPA, RPA and nasion) with the **[ft_volumerealign](/reference/ft_volumerealign)** function. This function does not change the anatomical data, instead it creates a transformation matrix that aligns the anatomical data to the intended coordinate system (in this case CTF).

	
	cfg        = [];
	cfg.method = 'interactive';
	mri        = ft_volumerealign(cfg, mri_other);

#### 3. Preprocessing of the anatomical MRI: reslicing

This steps reslices the anatomical volume in a way that each slice will be equaly thick. We use 1 mm thick slices and we specify the dimension as 256X256X256, because this is the format which FreeSurfer works with. 

	
	cfg            = [];
	cfg.resolution = 1;
	cfg.dim        = [256 256 256];
	mrirs          = ft_volumereslice(cfg, mri);
	save mrirs;

#### 4. Preprocessing of the anatomical MRI: Re-align to MNI

The creation of the source-space for the minimum-norm estimate will happen with the help of two additional software packages, FreeSurfer and the MNE Suite. Before using this software the anatomical MRI has to be preprocessed in FieldTrip which involves the creation of a brainmask, and coregistering the MRI to a coordinate frame that Freesurfer understands (e.g., the Talairach or MNI coordinate system).

You will use **[ft_volumerealign](/reference/ft_volumerealign)** to navigate through the anatomical volume, and identify the landmarks which define the Talairach coordinate system. **This means that you need to identify the anterior commissure, the posterior commissure, and an interhemispheric point (which defines the XZ-plane), also referred to as landmarks**. You can navigate through the slices (at each of the 3 dimensions x, y, and z) with the arrow keys **on the keyboard (??)**. 

**When you have identified the landmarks you can stored their voxel coordinates (location) by pressing the keys on the keyboard that correspond to the first letter in the name of the landmark ('a', 'p', and 'z' at the right locations. When all landmarks have been identified, press the 'q' key (for quit), the transformation matrix is updated to reflect the transformation from voxel space into Talairach space.**

For a detail guide on identifying landmarks in the anatomical volume see this link: [page](http://neuroimage.usc.edu/brainstorm/CoordinateSystems)

**moved and edited text for this link**

`<note warning>`Importantly, the implicit assumption is that the original transformation matrix correctly describes a right-handed coordinate system (otherwise left and right may become mixed up). In this example, we are using an MRI which has been already processed to contain a correct transformation matrix (in this case corresponding to the CTF convention, which is also a right-handed coordinate system). If you are processing MRI scans in the native file format without explicit orientation information, the previous step may lead to a left/right flip. **I THINK THIS LEFT/RIGHT FLIP NEEDS TO BE EXPLAINED MORE. DO YOU MEAN THAT THE LEFT HEMISPHERE BECOMES THE RIGHT, AND THE RIGHT BECOMES THE LEFT? IS THAT THE SAME/DIFF AS SEEING THE REFLECTION OF THE BRAIN??**
`</note>`

	
	load mrirs;
	cfg        = [];
	cfg.method = 'interactive';
	mri_mni    = ft_volumerealign(cfg, mrirs);
	save mri_mni mri_mni                  %we will need this structure at 
	                                      %later stages (save to disk)

####  5. Preprocessing of the anatomical MRI: segmentation

This step uses a segmentation of the anatomy, where gray, white and the cerebro-spinal fluid compartments are differentiated, to create a skull-stripped anatomy and a brainmask. The brainmask is a binary mask of the inner skull.  The function **[ft_volumesegment](/reference/ft_volumesegment)** will produce the required output.

	
	% segmentation of the mri
	load mri_mni;
	cfg           = [];
	cfg.coordsys  = 'spm';
	cfg.output    = {'skullstrip' 'brain'};
	seg           = ft_volumesegment(cfg, mri_mni);
	save seg seg;

The seg structure will be used later for creating the volume conduction model. Also the skull-stripped anatomy will be later saved to disk in a Freesurfer compatible format, to facilitate the creation of the source model.

#### 6. Preprocessing of the anatomical MRI: save to disk

	
	load mri_mni;
	load seg;
	
	
	% save both the original anatomy, and the masked anatomy in a freesurfer compatible format
	cfg             = [];
	cfg.filename    = 'Subject01';
	cfg.filetype    = 'mgz';
	cfg.parameter   = 'anatomy';
	ft_volumewrite(cfg, mri_mni);
	
	cfg.filename    = 'Subject01masked';
	ft_volumewrite(cfg, seg);

`<note warning>`Importantly, the mgz-filetype can only be used on the Linux and Mac platforms (and on Windows running virtual box). When you are processing the anatomical information on one of these platforms it is OK to save as mgz (and useful too, because it compresses the files and uses less diskspace as a consequence). Note however that these files cannot be saved and read on a Windows PC. If you have your Matlab installed on Windows, you may try to save the volume as a nifti file, for example. For this, you have to use cfg.filetype = 'nifti'. And you can convert the nifti file to mgz using [mri_convert](http://surfer.nmr.mgh.harvard.edu/fswiki/mri_convert) with FreeSurfer. 
`</note>`

The matlab-based preprocessing of the anatomical data is now finished. We created two .mgz files that will be used for creating the source model and a seg structure that will be used for creating the volume conduction model.

However, it is important that the anatomical MRI and the sensor positions are expressed in the same coordinate system. The MEG sensor positions are always defined relative to the fiducial coils. If we want to create a volume conduction model and a sourcemodel, the anatomical data must also be expressed relative to these points (i.e., in the CTF coordinate system). Therefore, we saved also the mri volume aligned to MNI and also CTF coordinates. We will use the transformation matrices of these volumes to transform the volume conduction model and the sourcespace to the CTF coordinate system.
### Source model

#### Source model: Introduction

This part describes how to set up the source-space for the minimum norm estimate. This entails the creation of a triangulated cortical mesh, ideally consisting of a number of approximately equally sized triangles that form a topological sphere. The latter property is required to create an inflated cortex and to do intersubject realignment. The following uses Freesurfer to create a topologically correct description of the cortex. This typically yields a mesh with > 100000 vertices per hemisphere which is too much for a workable minimum norm estimate. Therefore, we use the MNE-suite to downsample the triangulated meshes. This step serves the purpose of retaining a topologically correct description of the surface, and keeping the variance in triangle size low. In contrast, Matlab's reducepatch function breaks the topology and leads to a bigger variance in triangle size. 
The creation process of the source-space can be divided into 4 stages (after the preprocessing steps
 1.  Volumetric processing in Freesurfer.
 2.  Surface based processing in Freesurfer.
 3.  Creation of the mesh using MNE-suite.
 4.  Coregistration of the source space to the sensor-based coordinate system with FieldTrip.

**The volumetric and surface based processing (first and the second steps) takes 10 hours altogether. These steps will run on the computer for themselves. There is only one checkpoint between the volume and the surface based processing where an intermediate result can be checked interactively. **

The input of the creation process of the source-space are mgz files that were created in the preprocessing. The output is the source model that is a matlab structure called 'sourcespace' in this tutorial. 

The instructions about how to install and run Freesurfer and MNE Suite are aimed at users at the Center of Neuroimaging of the Donders Institute and at the MPI for Psycholinguistics in Nijmegen.
    
#### 1. Source model: Volumetric processing in Freesurfer

Freesurfer's anatomical processing pipeline consists of a series of automated steps, which essentially consist o
 1.  processing steps on a volumetric anatomical MRI (image intensity normalization, co-registration with Talairach space, skull stripping, automatic segmentation of sub-cortical structures, and finally segmentation) 
 2.  extraction of the cortical mesh
 3.  processing of the surface meshes (smoothing, topology fixing, inflation, co-registration with a spherical template)

Here is a [link](http://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllDevTable) to the different processing steps. Although the Freesurfer procedure can be invoked using only a few Freesurfer commands, below we will describe the (sub)commands that will achieve the same. These commands sequentially generate a series of files (volumetric, surface and transformation matrices). Each of the output files serves as input to the sequential analysis steps. A table of file dependencies can be found [here](http://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllFilesVsSteps).
There are a few analysis steps in Freesurfer, which are not guaranteed to give a nice result, and require some user interaction to get it right. Moreover, Freesurfer can be quite picky with respect to the exact format of the MRI-volumes. **One step, which in our experience is notorious for not being very robust, is automatic skull-stripping.** Therefore, we advocate a hybrid approach that uses SPM for an initial segmentation of the anatomical MRI during the preprocessing. With this segmentation, we created a brainmask that provides a robustly skull-stripped image, which is a prerequisite for a correct segmentation in Freesurfer. Although this approach may seem a bit convoluted (you may rightfully ask why we need to redo the segmentation in Freesurfer if we already did it in SPM), the interdependencies between different files generated along the Freesurfer pipeline make tapping into this pipeline at a random point quite complicated. For this reason a large part of the volumetric processing in Freesurfer needs to be done as well.

In order to be able to use Freesurfer, you need to have a working installation of the package. It can be downloaded from [here](http://surfer.nmr.mgh.harvard.edu/fswiki). If you are working at the Center of Neuroimaging of the Donders Institute you can find more versions of Freesurfer under the /opt/FreesurferXXX directories. (If you are working at the MPI for Psycholinguistics, you should install the software yourself in your directory.) We recommend to use Freesurfer 5.1.0. **You can run the commands below by just copying and pasting them into the terminal window of the Linux system (from where you use/initiate  Matlab).**

**%% I totally skipped past the previous line and got confused with the code below, CAN WE KEEP THE PREVIOUS LINE IN BOLD?? I also added a comment above the first box of code below.  ALSO FOR CLARITY, CAN WE INSERT A COMMENT IN THE FIRST CODE BOX THAT RETURNS/RESUMES TO BEING EXECUTED IN MATLAB?**

To get started, you need to set up your environmental variables. (Pay attention to the (lack of) spaces.)
`<code>`% run this code in linux
export FREESURFER_HOME=`<path to Freesurfer>`
export SUBJECTS_DIR=`<Subject directory>``</code>`     
SUBJECTS_DIR is the directory where you will store all the Freesurfer-processed anatomical data of all your subjects. Then, type this command to set up Freesurfe
`source $FREESURFER_HOME/SetUpFreeSurfer.sh`
It is useful to set up a subject-specific director
`mksubjdirs $SUBJECTS_DIR/Subject01`
Now, we are ready to start using Freesurfer. As a first step in the volumetric pipeline, we have to 'convert' the anatomical MRI once more, but now using a Freesurfer command. You can find now a new folder in the subject directory called "mri" into which you will copy both the masked and the original mgz files you created in the previous preprocessing steps in FieldTrip. All the Freesurfer commands will be called from the "mri" directory. (The first three lines of the following code is doing all of these for you.)

	
	cp Subject01masked.mgz $SUBJECTS_DIR/Subject01/mri/Subject01masked.mgz
	cp Subject01.mgz $SUBJECTS_DIR/Subject01/mri/Subject01.mgz
	cd $SUBJECTS_DIR/Subject01/mri/
	mri_convert -c -oc 0 0 0 Subject01masked.mgz orig.mgz
	mri_convert -c -oc 0 0 0 Subject01.mgz orig-nomask.mgz

We now have a 'brainmasked' anatomical volume in orig.mgz, which is the starting input volume to the following pipelin

	
	recon-all -talairach -subjid Subject01
	recon-all -nuintensitycor -subjid Subject01
	recon-all -normalization -subjid Subject01
	cp T1.mgz brainmask.mgz
	recon-all -gcareg -subjid Subject01
	recon-all -canorm -subjid Subject01
	recon-all -careg -subjid Subject01
	recon-all -calabel -subjid Subject01
	recon-all -normalization2 -subjid Subject01
	recon-all -segmentation -subjid Subject01
	recon-all -fill -subjid Subject01

This ends the part of the Freesurfer pipeline concerned with volumetric processing. At this stage you should have a file **filled.mgz** containing the segmentation of the cortical white matter (cerebellum is not included!). You can check how this looks using FieldTrip, by doing the followin

	
	% go to the Subject01/mri directory
	mri = ft_read_mri('filled.mgz');
	cfg = [];
	cfg.interactive = 'yes';
	figure;ft_sourceplot(cfg, mri);

![image](/media/tutorial/minimumnormestimate/filled01new.png@550)

*Figure 3. Filled mgz created by Freesurfer. The two hemispheres have different colors (white and grey), cerebellum is not included.*

#### 2. Source model: Surface based processing in Freesurfer

The surface construction is done by the following sequence of commands (from the Subject01/mri directory

	
	recon-all -tessellate -subjid Subject01
	recon-all -smooth1 -subjid Subject01
	recon-all -inflate1 -subjid Subject01
	recon-all -qsphere -subjid Subject01
	recon-all -fix -subjid Subject01
	cp brain.mgz brain.finalsurfs.mgz
	recon-all -finalsurfs -subjid Subject01
	recon-all -smooth2 -subjid Subject01
	recon-all -inflate2 -subjid Subject01
	recon-all -sphere -subjid Subject01
	recon-all -surfreg -subjid Subject01

After these steps (which may take quite a while) you end up with a bunch of files in the **Subject01/surf/** directory. We are going to use **lh.white** and **rh.white** to create the source space in the next step.

#### 3. Source model: Creation of the mesh using MNE Suite

Just like with Freesurfer, we have to first take care that MNE-suite is installed, and that some environmental variables are correctly specified. If you are working at the Center of Neuroimaging of the Donders Institute, you can find the MNE Suite under the /opt/mne directory. At the MPI for Psycholinguistics, MNE Suite is installed under the /mnt/data1/mne directory.

	
	export MNE_ROOT=`<MNE directory>`
	cd $MNE_ROOT/bin
	. ./mne_setup_sh
	export SUBJECTS_DIR=`<Subject directory>`
	export SUBJECT=Subject01

Now we can create the source space

	
	mne_setup_source_space --ico -6

This step creates a bunch of files in `<Subject directory>`/Subject01/bem/**, containing different representations of the source space. In subsequent steps, FieldTrip will use the **Subject01-oct-6-src.fif** file. We can already have a look in MATLAB at how the source space looks.

	
	bnd = ft_read_headshape('Subject01-oct-6-src.fif', 'format', 'mne_source');
	figure;ft_plot_mesh(bnd);

![image](/media/tutorial/minimumnormestimate/sspace01new.png@450)

*Figure 4. The source-space downsampled by MNE Suite*

#### 4. Source model: Co-registration of the source space to the sensor-based head coordinate system

We have the source locations co-registered to the Talairach (MNI) coordinate system, so now we need to co-register the source space to the sensor-array (i.e., we have to express the positions of the sources in the same (CTF) coordinate system as the sensors). For this, we will use transformation matrices of the earlier re-aligned mri volumes. By combining the transformation matrix of the volume that is aligned to the CTF coordinates (from voxel space to CTF space) and the transformation of the volume that is aligned to the MNI coordinates (from voxel space to MNI space), we will get a matrix that transforms the data from CTF to MNI space. We will apply this transformation matrix to the source-points. Next to this, we will convert the units to cm.

	
	load mrirs % mri volumed aligned to the CTF coordinate system (and resliced)
	           % (see Preprocessing of the anatomical MRI,step 3)
	load mri_mni % mri volume aligned to the Talairach (MNI) coordinate system 
	             % (see Preprocessing of the anatomical MRI,step 4)
	
	mrirs = ft_convert_units(mrirs, 'cm');
	mri_mni = ft_convert_units(mri_mni, 'cm');
	T   = mrirs.transform*inv(mri_mni.transform);
	
	% go to the Subject01/bem directory
	bnd  = ft_read_headshape('Subject01-oct-6-src.fif', 'format', 'mne_source');
	sourcespace = ft_convert_units(bnd, 'cm');
	sourcespace = ft_transform_geometry(T, sourcespace);
	save sourcespace sourcespace;
	save T T; %we will need the transformation matrix also in the next step

### Volume conduction model

We create the volume conduction model from the segmented volume (see Preprocessing of the anatomical MRI, step 5). In order to get a volume conduction model that is aligned with the source space we will apply the same transformation matrix (T) on the volume conductor as the transformation matrix that we applied on the sourcespace. 

	
	load seg;
	load T;
	
	
	cfg = [];
	vol = ft_prepare_singleshell(cfg,seg);
	vol.bnd = ft_transform_geometry(T, vol.bnd);
	save vol vol;

It is useful to check if the resulting sourcespace and the volume conductor are aligned.
To plot, you can use this cod

	
	% load vol                                       % volume conduction model
	load sourcespace;
	figure;hold on;
	ft_plot_vol(vol, 'facecolor', 'none');alpha 0.5;
	ft_plot_mesh(sourcespace, 'edgecolor', 'none'); camlight 

If they are not aligned, it may be because **vol** is not expressed in CTF coordinates.  You can check using **[ft_determine_coordsys](/reference/ft_determine_coordsys)**.  

![image](/media/tutorial/minimumnormestimate/sourcespace_vol01new.png@450)

*Figure 5. The final version of the source-space aligned and plotted together with the volume conductor* 
## Processing of functional data

The following will use the MEG data belonging to Subject01. The file can be obtained from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).
For both preprocessing and averaging, we will follow the steps that have been written in the [Event related averaging and planar gradient](/tutorial/eventrelatedaveraging) tutorial. We will use trials belonging to two conditions (FC and FIC) and we will calculate their difference.

### Preprocessing of MEG data

{{page>:tutorial:shared:preprocessing_fc_lp}}

{{page>:tutorial:shared:preprocessing_fic_lp}}
### Averaging and noise-covariance estimation

The function **[ft_timelockanalysis](/reference/ft_timelockanalysis)** makes averages of all the trials in a data structure and also estimates the noise-covariance. For a correct noise-covariance estimation it is important that you used the cfg.demean = 'yes' option when the function **[ft_preprocessing](/reference/ft_preprocessing)** was applied.

The trials belonging to one condition will now be averaged with the onset of the stimulus time aligned to the zero-time point (the onset of the last word in the sentence). This is done with the function **[ft_timelockanalysis](/reference/ft_timelockanalysis)**. The input to this procedure is the dataFC_LP structure generated by **[ft_preprocessing](/reference/ft_preprocessing)**.  At the same time, we need to compute the noise-covariance matrix, therefore cfg.covariance = 'yes' has to be specified as well as the time window where the noise-covariance will be estimated. Here, we use the baseline where there is no signal of interest yet.

	
	  load dataFC_LP;
	  load dataFIC_LP;
	  cfg = [];
	  cfg.covariance = 'yes';
	  cfg.covariancewindow = [-inf 0]; %it will calculate the covariance matrix 
	                                   % on the timepoints that are  
	                                   % before the zero-time point in the trials
	  tlckFC = ft_timelockanalysis(cfg, dataFC_LP);
	  tlckFIC = ft_timelockanalysis(cfg, dataFIC_LP);
	  save tlck tlckFC tlckFIC;

## Forward solution

The source space, the volume conduction model  and the position of the sensors are necessary inputs for creating the leadfield (forward solution) with the **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)** function. The sensor positions are contained in the grad field of the averaged data. However, the grad field contains the positions of all channels, therefore, the used channels have to be also specified.  

	
	load tlck;
	load sourcespace;
	load vol;
	
	cfg = [];
	cfg.grad = tlckFC.grad;                      % sensor positions
	cfg.channel = {'MEG', '-MLP31', '-MLO12'};   % the used channels
	cfg.grid.pos = sourcespace.pnt;              % source points
	cfg.grid.inside = 1:size(sourcespace.pnt,1); % all source points are inside of the brain
	cfg.vol = vol;                               % volume conduction model
	leadfield = ft_prepare_leadfield(cfg);
	
	save leadfield leadfield;

## Inverse solution

FIXME

The **[ft_sourceanalysis](/reference/ft_sourceanalysis)** function calculates the inverse solution. The method used (minimum-norm estimation) has to be specified with the cfg.method option. The averaged functional data, the forward solution (the output of the **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)** function), the volume conduction model (in this case, the output of the **[ft_prepare_singleshell](/reference/ft_prepare_singleshell)** function) and the noise-covariance matrix (the cov field of the output of the **[ft_timelockanalysis](/reference/ft_timelockanalysis)** function) has to be provided. 

The lambda value is a scaling factor that is responsible for scaling the noise-covariance matrix. If it is zero the noise-covariance estimation will be not taken into account during the computation of the inverse solution. Noise-covariance is estimated in each trial separately and then averaged, while the functional data (of which we calculate the source-analysis) is simply averaged across all the trials. Therefore,  the higher the number of trials the lower the noise is in the averaged, functional data, but the number trials is not reducing the noise in the noise-covariance estimation. This is the reason while it is useful to use a scaling factor for the noise-covariance matrix if we want to estimate more realistically the amount of noise.  

You do not have to specify of the noise-covariance matrix separatly, because it is in the tlckFC.cov and in the tlckFIC.cov fields, and ft_sourceanalysis will take it into account automatically.

	
	load tlck;
	load leadfield;
	load vol;
	
	cfg=[];
	cfg.method = 'mne';
	cfg.grid = leadfield;
	cfg.vol = vol;
	cfg.lambda = 1e8;
	sourceFC = ft_sourceanalysis(cfg,tlckFC);
	sourceFIC = ft_sourceanalysis(cfg, tlckFIC);
	
	save source sourceFC sourceFIC;

## Visualization

You can plot the inverse solution onto the source-space at a specific time-point with the **[ft_plot_mesh](/reference/ft_plot_mesh)** function.

	
	load sourceFIC;
	load sourcespace;
	
	bnd.pnt = sourcespace.pnt;
	bnd.tri = sourcespace.tri;
	m=sourceFIC.avg.pow(:,450); % plotting the result at the 450th time-point that is 
	                         % 500 ms after the zero time-point
	ft_plot_mesh(bnd, 'vertexcolor', m);

![image](/media/tutorial/minimumnormestimate/plotmeshsourceic01new.png@450)

*Figure 6. The result of the source-reconstruction of the FIC condition plotted onto the source-space at 500 ms after the 0 time-point*

But we would like to know where the difference between the conditions can be localized. Therefore, we calculate the difference of the two conditions, and we use **[ft_sourcemovie](/reference/ft_sourcemovie)** to visualize the results.

	
	cfg = [];
	cfg.projectmom = 'yes';
	sdFC = ft_sourcedescriptives(cfg,sourceFC);
	sdFIC = ft_sourcedescriptives(cfg, sourceFIC);
	
	sdDIFF = sdIC;
	sdDIFF.avg.pow = sdFIC.avg.pow - sdFC.avg.pow;
	sdDIFF.tri = sourcepspace.tri;
	
	save sd sdFC sdFIC sdDIFF;
	
	cfg = [];
	cfg.mask = 'avg.pow';
	ft_sourcemovie(cfg,sdDIFF);
	

![image](/media/tutorial/minimumnormestimate/sourcemovie01new.png@500)

*Figure 7. One frame from the movie that shows the differences of the two source-reconstructions*
## Summary and further readings

In this tutorial we showed how to do MNE source reconstruction method on a single subject data. We compared the averaged ERF in two conditions and we reconstructed the sources and we calculated the difference of the two source-reconstruction. We showed also how you can visualize the results.

Functions and tutorial pages that show how to average, and how to analyze statistically source-reconstructions across subjects or how to compare those to a template brain are still under development.

