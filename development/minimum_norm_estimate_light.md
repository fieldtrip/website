---
layout: default
tags: fixme
---


FIXME add tags

`<note warning>`
The purpose of this page is just to serve as a scratch pad for the new version of a tutorial site.

There is no guarantee that this page is updated in the end to reflect the final state of the tutorial site.
So chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
`</note>`
# Source reconstruction of event-related fields using minimum-norm estimate

## Introduction


In this tutorial we will show how to do source-analysis with minimum-norm estimate on the event-related fields (MEG) of a single subject. 

We will use an [MEG dataset of a language task](/tutorial/shared/dataset). This tutorial is part of a series of tutorials which use the same datase
 1.  [Trigger-based trial selection](/tutorial/preprocessing)
 2.  [Visual artifact rejection](/tutorial/visual_artifact_rejection)
 3.  [Event related averaging and planar gradient](/tutorial/eventrelatedaveraging)
 4.  [Cluster-based permutation tests on event related fields](/tutorial/cluster_permutation_timelock)
 5.  [Time-frequency analysis using Hanning window, multitapers and wavelets](/tutorial/timefrequencyanalysis)
 6.  [Cluster-based permutation tests on time-frequency data](/tutorial/cluster_permutation_freq)
 7.  [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer)

We will also use MRI images which belong to the same subject, a [template MRI](/template/anatomy) and a [template cortical sheet](/template/sourcemodel).  

We will repeat code to select the trials and preprocess the data as described [here](/tutorial/eventrelatedaveraging). We assume that preprocessing and event-related averaging is already clear for the reader. This tutorial will *not* show how to do group-averaging or statistics. 

The major differences (beside the algorithm of the inverse solution) compared to the source localization procedure shown in the [beamforming](/tutorial/beamformer) tutorial are: 

*  We will calculate the source of the event-related fields rather than the oscillatory activity.

*  We will calculate the source-activation over time and not average the activation over a time-window.

*  We will use a source model that only models the cortex as a surface (i.e. the cortical sheet) and not by scanning on a volumetric grid covering the whole brain. 


## Background

{{page>:tutorial:shared:sourcelocalization_background}}

In this tutorial, the type of **inverse model** used for source-localization is based on minimum-norm estimation (MNE).   

In the [event-related averaging](/tutorial/eventrelatedaveraging) tutorial the event related fields have been computed in three conditions and the [cluster statistics](/tutorial/cluster_permutation_timelock) tutorial  showed significant differences among two conditions. The topographical distribution of the ERFs belonging to each conditions and ERFs belonging to those differences have been plotted. In this tutorial we will calculate a distributed representation of the neuronal activity underlying the sensor level data for each condition. We will also visualize the difference between conditions on the source-level.

The MNE method is favored for tracking the wide-spread activation and analyzing evoked responses over time. The source model only describes the cortical surface and uses a large number of equivalent current dipoles placed at the vertices of this surface grid. MNE estimates the amplitude of the complete source model simultaneously and recovers a distribution of the activity with minimum overall energy that produces data consistent with the measurement ((Ou, W., Hamalainen, M., Golland, P., 2008, A Distributed Spatio-temporal EEG/MEG Inverse Solver)) ((Jensen, O., Hesse, C., 2010, Estimating distributed representation of evoked responses and oscillatory brain activity, In: MEG: An Introduction to Methods, ed. by Hansen, P., Kringelbach, M., Salmelin, R., doi:10.1093/acprof:oso/9780195307238.001.0001)). The most appropriate literature reference for the FieldTrip implementation is [Dale et al. (2000)](/references_to_implemented_methods).

## Procedure

Figure 1. shows the important steps in the minimum-norm estimate. It shows that the computation of the inverse solution is based on the outputs of two independent processing steps: the processing of the anatomical information that leads to the forward solution and the processing of the MEG data. 

In the anatomical processing part we will create the source model and the volume conduction model of the head (i.e. head model). In this tutorial we will use a [template sourcemodel](/template/sourcemodel) and [template headmodel](/template/headmodel) that are both derived from the canonical MNI template MRI. We will spatially transform these to overall match the individuals MRI. Note that this approach is suboptimal because the folding of the cortical sheet will follow the template rather than the individual MRI. However, the advantage is that the results of the source estimation on this individualized template can be easily compared to other subjects' results. A computationally more complex, but also more accurate MNE source estimation on the individual cortical sheet, is described in another tutorial. :!: insert link

To compute the minimum-norm estimation we perform the following step

 1.  The subject's MRI is read in with **[ft_read_mri](/reference/ft_read_mri)** and normalized with **[ft_volumenormalise](/reference/ft_volumenormalise)**. Since the MRI from disk is already coregistered, we can skip **[ft_volumerealign](/reference/ft_volumerealign)**. 
 2.  To create the sourcemodel, we read in a template cortical sheet with **[ft_read_headshape](/reference/ft_read_headshape)** and warp it with **[ft_transform_geometry](/reference/ft_transform_geometry)**. 
 3.  To create a headmodel, first, we load a template mri and segment it with **[ft_volumesegment](/reference/ft_volumesegment)** and create a mesh using **[ft_prepare_mesh](/reference/ft_prepare_mesh)**. We transform the mesh with **[ft_transform_geometry](/reference/ft_transform_geometry)**. In the last step, we create the from this mesh using **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** .
 4.  To check whether all anatomical information are well-aligned, we read in the sensor locations with **[ft_read_sens](/reference/ft_read_sens)**, then we plot them with **[ft_plot_sens](/reference/ft_plot_sens)** together with the sourcemodel using **[ft_plot_mesh](/reference/ft_plot_mesh)** and the headmodel, using **[ft_plot_vol](/reference/ft_plot_vol)**.
 5.  Then, we will compute the forward solution with **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)**.
 6.  For the inverse solution, we will first preprocess the MEG data using **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)** and compute the average over trials and estimate the noise-covariance using **[ft_timelockanalysis](/reference/ft_timelockanalysis)**. We compute the inverse solution using **[ft_sourceanalysis](/reference/ft_sourceanalysis)** and visualize the results with **[ft_plot_mesh](/reference/ft_plot_mesh)** and **[ft_sourcemovie](/reference/ft_sourcemovie)**.

## Processing of anatomical data


Some of the functions described in this part of the tutorial are using the SPM toolbox which can be found under the fieldtrip/external folder. You do not have to add this toolbox yourself, but it is important that [you set up your MATLAB path properly](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path). 

	
	cd `<PATH_TO_FIELDTRIP>`
	ft_defaults


### Processing of the subject's mri


In the following, we will use the anatomical MRI belonging to Subject01. The file can be obtained from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).
We read in the subject's MRI as follow

	
	mri = ft_read_mri('Subject01.mri');
	
	disp(mri)
	          dim: [256 256 256]
	      anatomy: [256x256x256 int16]
	          hdr: [1x1 struct]
	    transform: [4x4 double]
	     coordsys: 'ctf'


The structure of your MRI variable contains the following field

*  **dim**: This field gives information on the size (i.e. the number of voxels) of the anatomical volume into each direction.

*  **anatomy**: This is a matrix (with the size and number of dimensions specified in **dim**) that contains the anatomical information represented by numbers.

*  **hdr**: Header information of the anatomical images.

*  **transform**: A transformation matrix that aligns the anatomical data (in field **anatomy**) to a certain coordinate system.

*  **coordsys**: The description of the coordinate system which the anatomical data is aligned to.

You can see that the **coordsys** field of anatomical data shows 'ctf'. The subject's MRI should be in [the CTF head coordinate system](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined#details_of_the_ctf_coordinate_system) because this is also how the locations of the MEG sensors are defined relative to the head. Hence, we the source model and head model that we create have to be expressed in the same CTF head coordinate system. 

 
`<note>`
It is also possible to read in anatomical MRI data in [other formats](/dataformat) or from raw DICOM files. The different coordinate systems are explained in this [frequently asked question](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined). If your anatomical MRI is not aligned to the coordinate system in which your sensors are expressed, you can  [align](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions) them using either **[ft_volumerealign](/reference/ft_volumerealign)** or **[ft_electroderealign](/reference/ft_electroderealign)**. This alignment or coregistration is commonly done using [fiducial points](/faq/how_are_the_lpa_and_rpa_points_defined) on the head. 


When you read in your own anatomical data, it may not give information on the coordinate system in which the anatomical data is expressed and/or maybe there is no [transformation matrix](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions) specified. In this case, you can visually inspect and determine the coordinate-system with **[ft_determine_coordsys](/reference/ft_determine_coordsys)**.
`</note>` 

In the next step, we normalize the individual MRI using the MNI template anatomy from SPM. We do not explicitly have to give the MNI template to the function as it is used by default. In the subsequent step, we will also use a template MRI and a template cortical sheet. All templates we use are based on the same "colin27" anatomical MRI.


	
	cfg = [];
	norm_mri = ft_volumenormalise(cfg, mri);
	
	disp(norm_mri)
	     anatomy: [181x217x181 double]
	    transform: [4x4 double]
	          dim: [181 217 181]
	       params: [1x1 struct]
	      initial: [4x4 double]
	     coordsys: 'spm'
	          cfg: [1x1 struct]


After the normalization, the MRI is aligned to the SPM/MNI coordinate system, in which the template cortical sheet and template MRI are also expressed. In **norm_mri.cfg.final** we find a [homogenous transformation matrix](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions) that defines how the voxel positions can be transformed between the CTF head coordinates to the normalized SPM/MNI coordinates. We will use this transformation matrix in the subsequent steps.

### Exercise 1

`<note exercise>`
What is the relation between the following transformation matrices?

*  *mri.transform* 

*  *norm_mri.transform* 

*  *norm_mri.cfg.final*
If you are not familiar with the concept of homogenous transformation matrices, please read [this page](http://bishopw.loni.ucla.edu/air5/homogenous.html).

FIXME if I am correct then 1*3=2, please check. L: When we figured this out, may I need to rerun the entire analysis again.

`</note>`

### Source model  

We read in a [template cortical sheet](/template/sourcemodel) from the FieldTrip template directory. The path to the data depends on where your FieldTrip directory is located.  

	
	temp_sheet_orig = ft_read_headshape('fieldtrip/template/sourcemodel/cortex_8196.surf.gii');
	
	disp(temp_sheet_orig)
	     pnt: [8196x3 single]
	     fid: [1x1 struct]
	     tri: [16384x3 int32]
	    unit: 'mm'

The brain surface is represented by points (vertices) that are connected into triangles. The x, y and z coordinates of each vertex is given in the **pnt** field. Each row of the **tri** field contains the indices of three vertices that describe a triangle.

	
	disp(temp_sheet_orig.pnt(1:3,:))
	  -10.1924 -104.5533   -4.3301
	  -16.6946 -103.9027   -4.2946
	   -7.7264 -103.1324    0.8651
	
	disp(temp_sheet_orig.tri(1:3,:))
	        3958        3893        3917
	        3893        3870        3845
	        3917        3893        3845


### Exercise 2

`<note exercise>`
What are the coordinates of the three points which define the first triangle (i.e the first row) of *temp_sheet_orig.tri*?
`</note>`  

The template cortical sheet needs to be transformed from [MNI/SPM into CTF coordinates](/faq/ how_are_the_different_head_and_mri_coordinate_systems_defined ). For this, we use the inverse of the transformation matrix from the earlier sectio

	
	ind_cortex = ft_transform_geometry(inv(norm_mri.cfg.final), temp_sheet_orig);

### Exercise 3

`<note exercise>`
Plot the points of the transformed and the original template sheet using

	
	x = ind_cortex.pnt(:,1);
	y = ind_cortex.pnt(:,2);
	z = ind_cortex.pnt(:,3);
	figure;
	plot3(x,y,z,'LineStyle','none','Marker','.');
	xlabel('X');
	ylabel('Y');
	zlabel('Z');
	grid on;
	
	x = temp_sheet_orig.pnt(:,1);
	y = temp_sheet_orig.pnt(:,2);
	z = temp_sheet_orig.pnt(:,3);
	figure;
	plot3(x,y,z,'LineStyle','none','Marker','.');
	xlabel('X');
	ylabel('Y');
	zlabel('Z');
	grid on;

What is the difference in the location of the points between the original (temp_sheet_orig) and the individualized (ind_cortex) sheet?
`</note>`

The location of the vertices of the cortical sheet are now expressed in the CTF coordinate system relative to a point between the two ears. However, the sheet also needs to be in the same units as at the gradiometer positions. Therefore, we convert the units to 'cm'.


	
	ind_cortex = ft_convert_units(ind_cortex, 'cm');

This completes the construction of the source model.

### Head model


#### Segmentation

In this section, we will create an individualized template volume conduction model of the head. We will segment the [template MRI](/template/anatomy) with 1mm resolution and create a mesh that describes the inside of the skull. You can download the template MRI from the FieldTrip/template/anatomy directory. The path to the file will depend on where your version of FieldTrip is located.
First, the template anatomical MRI is [segmented](/faq/how_is_the_segmentation_defined) into a brainmask, i.e the voxels which belong to the brain tissue are set to 1 and all others are set to 0. We will use **[ft_volumesegment](/reference/ft_volumesegment)** for this.

	
	template_mri          = ft_read_mri('... fieldtrip/template/anatomy/single_subj_T1_1mm.nii');
	template_mri.coordsys = 'spm';  % we know that the template is in spm/mni coordinates 
	clear mri;                      % to avoid confusion between the template and subject's MRI


`<note important>`
Note that the segmentation can be time consuming (~15 mins) and if you want, you can load the pre-computed result and skip ahead to the next step. The segmented MRI of this tutorial can be downloaded from the [ftp server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/mne) (template_seg.mat). 
`</note>`

FIXME the naming of the tutorials and ftp directories has to be consistent (there is now minimumnormestimate, minimum_norm_estimate_light and mne)

	
	cfg           = [];
	cfg.output    = {'brain'};
	template_seg  = ft_volumesegment(cfg, template_mri);
	
	disp(template_seg)
	          dim: [181 217 181]
	    transform: [4x4 double]
	     coordsys: 'spm'
	         unit: 'mm'
	        brain: [181x217x181 logical]
	          cfg: [1x1 struct]


The *template_seg* structure is similar to the MRI data structure, but contains the following new field


*  **brain**: binary representation of the brain tissue

*  **cfg**: configuration information of the function which created *template_seg*

The procedure of the segmentation does not change the units, coordinate system, nor the size of the volume. You can see this in the first three fields (**dim**, **transform** and **coordsys**) which are the same as the corresponding fields of the input MRI data structure. The field **transform** specifies how each voxel of the **brain** volume can be expressed in the coordinate system defined in the **coordsys** field. 


#### Mesh


The surface of the brain approximates the inside of the skull. We construct a triangulated surface description from the binary brainmask of *template_seg* by the **[ft_prepare_mesh](/reference/ft_prepare_mesh)** function. 

	
	cfg = [];
	cfg.numvertices = 3000;
	template_mesh = ft_prepare_mesh(cfg, template_seg);
	
	disp(template_mesh);
	     pnt: [3000x3 double]
	     tri: [5996x3 double]
	    unit: 'mm'
	     cfg: [1x1 struct]


The *template_mesh* contains the following field


*  **pnt**: represents the vertices of the surface. 

*  **tri**:  each row defines three vertices (row numbers of the **pnt** field) that form a triangle.

*  **unit**:  The units in which the vertices are expressed.

Similar to the cortical sheet, we transform the mesh that describes the inside of the skull using the transformation matrix of the normalized individual MRI from the earlier step and convert its units to 'cm'.

	
	ind_insideskull = ft_transform_geometry(inv(norm_mri.cfg.final), template_mesh);
	ind_insideskull = ft_convert_units(ind_insideskull, 'cm');


#### Volume conduction model of the head


We have the right geometry of the brain (an individualized template) from the earlier step, so we can finally create the volume conduction model. We will use the single shell type model which is suitable for MEG data.

	
	cfg = [];
	cfg.method = 'singleshell';
	vol = ft_prepare_headmodel(cfg, ind_insideskull);
	
	disp(vol)
	     bnd: [1x1 struct]
	    type: 'singleshell'
	    unit: 'cm'
	     cfg: [1x1 struct]


The *vol* data structure contains the following field


*  **bnd**: contains the geometrical description of the head model.

*  **type**: describes the method that was used to create the headmodel.

*  **unit**: the unit of measurement of the geometrical data in the bnd field

*  **cfg**: configuration of the function that was used to create vol

The **bnd** field describes a surface with vertices and triangles (in the **vol.bnd.pnt** and **vol.bnd.tri** fields) as the geometrical description of the volume conductor. 


### Visualization


As the final step of the anatomical processing pipeline it is important to check the alignment and the transformation of all geometrical data. We will plot the sensors together with the source and head model to check whether they are aligned to each other and have the right proportions. 

The location of the MEG channels are defined in the .ds file of the tutorial data. First, we need to get this information using the **[ft_read_sens](/reference/ft_read_sens)** function. (The .zip file that can be downloaded from the [FieldTrip ftp server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip) also contains the .ds file.) Then, we will plot the sensors (MEG channels) with the **[ft_plot_sens](/reference/ft_plot_sens)** function. Second, we will plot the head model and the source model in the same figure with the sensors using **[ft_plot_vol](/reference/ft_plot_vol)** and **[ft_plot_mesh](/reference/ft_plot_mesh)**, respectively. 

	
	% read in the sensor positions for this subject
	sens = ft_read_sens('Subject01.ds');
	
	figure
	hold on
	ft_plot_mesh(ind_cortex, 'edgecolor', 'none', 'facecolor', 'red'); 
	camlight  % add some light for the 3-D effect
	ft_plot_vol(vol); 
	alpha 0.5  % make it a bit transparent
	ft_plot_sens(sens, 'coil', 'true');
	axis on
	grid on



{{:tutorial:minimumnormestimate:headm_sourcem_sens3.jpg?400|}}

*Figure 2. Head model, sourcemodel and sensors plotted in the same figure*

### Exercise 4

`<note exercise>`
Plot also the sensor labels and check whether all anatomical information is defined in CTF head coordinates!
`</note>`

## Processing of functional data


In the following section, we will use the MEG data belonging to Subject01. The raw data can be obtained from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).
For both preprocessing and averaging, we will follow the steps outlined in the [Event related averaging](/tutorial/eventrelatedaveraging) tutorial. We will use the trials belonging to the FC and FIC conditions. 

### Preprocessing of MEG data

{{page>:tutorial:shared:preprocessing_fc_lp}}

{{page>:tutorial:shared:preprocessing_fic_lp}}

### Averaging and noise-covariance estimation

The function **[ft_timelockanalysis](/reference/ft_timelockanalysis)** makes averages of all the trials in a data structure and also estimates the noise-covariance. We will use the noise covariance in the calculation of the [common filter](/example/common_filters_in_beamforming) (i.e. the filter used in the source analysis which is common for both conditions). Therefore, we will append the trials of both conditions, calculate the noise covariance and their average. (For a correct noise-covariance estimation it is important to use the cfg.demean = 'yes' option when the function **[ft_preprocessing](/reference/ft_preprocessing)** was applied.) When the input data contains trials (and not the average of them) the noise-covariance is estimated for each trial separately and subsequently averaged over trials. We will also average the trials separately for each condition.

	
	% averaging of all trials and noise covariance estimation
	cfg = [];
	dataall = ft_appenddata(cfg, dataFC_LP, dataFIC_LP);
	
	cfg = [];
	cfg.covariance = 'yes';
	dataall_tlck = ft_timelockanalysis(cfg, dataall);
	
	% averaging the conditions
	cfg = [];
	avgFIC = ft_timelockanalysis(cfg, dataFIC_LP);
	
	cfg = [];
	avgFC = ft_timelockanalysis(cfg, dataFC_LP);
	
	disp(dataall_tlck)
	       avg: [149x900 double]
	       var: [149x900 double]
	       dof: [149x900 double]
	       cov: [149x149 double]
	    dimord: 'chan_time'
	      time: [1x900 double]
	     label: {149x1 cell}
	      grad: [1x1 struct]
	       cfg: [1x1 struct]


You can see that the average of all data (dataall_tlck) also has a **cov** field that contains the noise covariance matrix.

## Forward solution

The source model, the volume conduction model and the sensor positions are needed for creating the forward solution with **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)**. The sensor positions are contained in the **grad** field of the MEG data. However, the **dataall_tlck.grad** includes also the position of the bad channels and reference channels, therefore the relevant channels for the leadfield have to be specified.

	
	cfg         = [];
	cfg.grad    = dataall_tlck.grad;            % sensor positions
	cfg.channel = {'MEG', '-MLP31', '-MLO12'};  % the used channels
	cfg.grid    = ind_cortex;                  % source points
	cfg.vol     = vol;                          % volume conduction model
	leadfield   = ft_prepare_leadfield(cfg);
	
	disp(leadfield)
	          pos: [8196x3 single]
	         unit: 'cm'
	          tri: [16384x3 int32]
	       inside: [8188x1 double]
	      outside: [8x1 double]
	          cfg: [1x1 struct]
	    leadfield: {1x8196 cell}



The *leadfield* contains the following field

*  **pos**: the dipole positions, i.e. the vertices of the cortical sheet

*  **unit**: the units in which the sourcepoints are defined

*  **inside**: the source points that represent the brain 

*  **outside**: the source points that are outside the brain, therefore the leadfield was not computed at these points

*  **leadfield**: the forward solution (as Nchannel*33 matrix) for each source point

For beamformer source reconstructions we typically scan a regular 3-D grid that span a "box" that encompasses the whole brain. In the 3-D grid the points inside the source compartment (i.e. the brain) are marked *inside* and the points outside are marked as *outside* and excluded from the scan.

For the cortical sheet source model the source points are all supposed to be inside the brain compartment. However, you can see that some points are marked as *outside* in the leadfield. These points stick out from the headmodel. We will use the **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)** function to move these inward. 

`<note important>`
If you see that many points are marked *outside*, something seems to be wrong with the coregistrationYou can check by visual inspection. 
`</note>`  

	
	ind_cortex_orig = ind_cortex;
	
	cfg            = [];
	cfg.moveinward = 0.01;
	cfg.grid       = ind_cortex_orig;
	cfg.vol        = vol;
	ind_cortex    = ft_prepare_sourcemodel(cfg);
	
	disp(ind_cortex)
	        pos: [8196x3 single]
	       unit: 'cm'
	        tri: [16384x3 int32]
	     inside: [1x8196 double]
	    outside: []
	        cfg: [1x1 struct]


Now the field **outside** is empty, i.e. we do not have any sourcepoints outside the brain surface of the headmodel anymore.

### Exercise 5

`<note exercise>`
Which points have been moved in the cortical sheet? Compare the pos and pnt fields of the new and the original sheets. Plot all points with plot3, and use different colors for the points which are different in the two cortical sheets.
`</note>`

We compute the leadfield again with the modified cortical sheet.

	
	cfg         = [];
	cfg.grad    = dataall_tlck.grad;            % sensor positions
	cfg.channel = {'MEG', '-MLP31', '-MLO12'};  % the used channels
	cfg.grid    = ind_cortex;                  % source points
	cfg.vol     = vol;                          % volume conduction model
	leadfield   = ft_prepare_leadfield(cfg);
	
	disp(leadfield)
	          pos: [8196x3 single]
	         unit: 'cm'
	          tri: [16384x3 int32]
	       inside: [1x8196 double]
	      outside: []
	    leadfield: {1x8196 cell}
	          cfg: [1x1 struct]

## Inverse solution


The goal of the analysis in this tutorial is to contrast the data between the two conditions in the time window of interest relative to the stimulus. If we later want to compare the two conditions statistically, we have to compute the sources based on an inverse estimation based on both conditions, i.e. the so called ['common filters'](/example/common_filters_in_beamforming) approach, and then apply this inverse estimation "filter" separately to each condition to obtain the source estimates per condition. The rationale is that you don't want differences in noise-levels between the conditions to explain differences in the source estimates. 

The following computes the filter using the average and the noise-covariance matrix of all trials over conditions, and subsequently computes the source estimate for each condition.


	
	% compute the filter
	cfg                    = [];
	cfg.grid               = leadfield;
	cfg.vol                = vol;
	cfg.method             = 'mne';
	cfg.mne.lambda         = 2;
	cfg.mne.keepfilter     = 'yes';
	cfg.mne.prewhiten      = 'yes';
	cfg.mne.scalesourcecov = 'yes';
	sourceAll = ft_sourceanalysis(cfg, dataall_tlck);


The configuration structure for this function contains some general options that are used in all source analysis methods, but also some method-specific options. In order to use the computed filters later, we need to specify the 'keepfilter' option. The 'lambda' value is responsible for scaling the noise-covariance matrix. If it is zero, the noise-covariance estimation will not be taken into account during the computation of the inverse solution. The options 'prewhiten' and 'scalesourcecov' options modify the leadfield matrix and the source covariance matrix for a more optimal solution. We do not need to specify the noise-covariance matrix in the configuration structure, as it is contained in **dataall_tlck.cov**.

During execution of the source analysis, some text is printed on screen that shows whether the specified options are taken into accoun

*  using headmodel specified in the configuration 

*  estimating current density distribution for repetition 1 

*  using pre-computed leadfields: some of the specified options will not have an effect

*  computing the solution where the noise covariance is used for regularisation

*  prewhitening the leadfields using the noise covariance

*  scaling the source covariance


	
	% compute source-analysis
	cfg             = [];
	cfg.method      = 'mne';
	cfg.grid        = leadfield;
	cfg.grid.filter = sourceAll.avg.filter;
	cfg.vol         = vol;
	sourceFC = ft_sourceanalysis(cfg, avgFC);
	
	cfg = [];
	cfg.method      = 'mne';
	cfg.grid        = leadfield;
	cfg.grid.filter = sourceAll.avg.filter;
	cfg.vol         = vol;
	sourceFIC = ft_sourceanalysis(cfg, avgFIC);
	
	disp(sourceFC)
	       time: [1x900 double]
	        pos: [8196x3 single]
	     inside: [8196x1 double]
	    outside: [1x0 double]
	     method: 'average'
	        avg: [1x1 struct]
	        cfg: [1x1 struct]
	
	disp(sourceFC.avg)
	    mom: {8196x1 cell}
	    pow: [8196x900 double]


When computing the source estimate, the following text printed on screen shows that the common filter has been used in the computatio

*  using pre-computed spatial filter: some of the specified options will not have an effect

The **pos**, **inside** and **outside** fields of the source contains specifies the points for which the source was calculated. These fields should be the same as in the *leadfield* and in the *sourcemodel*. The **time** field describes the timepoints for which the sources were estimated and should be the same as in the event-related input data (//avgFC// and *dataFC_LP*). The **sourceFC.avg.pow** contains the power estimate at each source- and timepoints. 

### Exercise 6

`<note exercise>`
Compute the source estimate for the FIC condition using a filter where cfg.mne.lambda = 0 was specified. Plot the result at 500 ms (see the plotting in the next section) and compare it to the original result. What is the difference?
`</note>` 
## Visualization

You can plot the estimated source strength at a specific time-point with the low-level **[ft_plot_mesh](/reference/ft_plot_mesh)** function.

	
	bnd.pnt = sourcemodel.pnt;
	bnd.tri = sourcemodel.tri;
	
	% get the estimate at the 450th time-point, which is 500 ms after stimulus onset
	value = sourceFIC.avg.pow(:,450); 
	
	ft_plot_mesh(bnd, 'vertexcolor', value);


{{:tutorial:minimumnormestimate:mnesource2.jpg?500|}}

*Figure 3. The result of the source-reconstruction of the FIC condition plotted at 500 ms*

### Exercise 7

`<note exercise>`
Plot the source in MNI space together with a slice of the MNI template MRI (use ft_plot_slice).
`</note>` 

## Summary and suggested further reading


In this tutorial, we demonstrated the minimum-norm estimate method for source reconstruction using a individualized template. If you would like to compute the source estimation on an individual cortical sheet, you can go to this tutorial (:!: Insert link). Two other tutorials show in more detail how to construct a volume conduction model for [MEG](/tutorial/headmodel_meg) and [EEG](/tutorial/headmodel_eeg) data.

Here you can find related FAQs: 

{{topic>faq +source &list}}

and example script

{{topic>example +source &list}}


