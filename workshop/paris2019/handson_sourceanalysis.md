---
title: Localizing sources of neural sources using beamformer techniques
tags: [tutorial, meg, preprocessing, timelock, beamformer]
---

# Localizing sources of neural activity using beamformer techniques

{% include markup/info %}
This tutorial was written specifically for the practicalMEEG workshop in Paris in December 2019.
{% include markup/end %}

## Introduction

In this tutorial you will learn about applying beamformer techniques in the time domain, using MEG data from an Elekta system. Using beamformers on Elekta data is somewhat more challenging than using beamformers on (for instance) CTF data. This is for two reasons: 1) Elekta MEG data consists of signals of different sensor types (magnetometers and planar gradiometers), and 2) the data are often heavily rank-deficient due to the application of the Maxfilter to clean the data of (movement) artifacts.

It is expected that you understand the previous steps of preprocessing and filtering the sensor data, as covered in the **[raw2erp tutorial](/workshop/paris2019/handson_raw2erp)**. Also, you need to understand how to create a subject specific headmodel and sourcemodel, as explained in the **[head- and sourcemodel tutorial](/workshop/paris2019/handson_anatomy)**.

This tutorial will not cover the frequency-domain option for DICS/PCC beamformers (which is explained [here](/tutorial/beamformer)), nor how to compute minimum-norm-estimated sources of evoked/averaged data (which is explained [here](/tutorial/minimumnormestimate)).

## Procedure

To localise the evoked sources for this example dataset we will perform the following steps:

- Read the data into MATLAB using the same strategy as in the **[raw2erp tutorial](/workshop/paris2019/handson_raw2erp)**.
- Spatially whiten the data to account for differences in sensor type (magnetometers versus gradiometers)
- Compute the covariance matrix using the function **[ft_timelockanalysis](/reference/ft_timelockanalysis)**.
- Construct the leadfield matrix using **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)**, in combination with the previously computed head- and sourcemodels + the whitened gradiometer array.

- Compute a spatial filter and estimate the amplitude of the sources using **[ft_sourceanalysis](/reference/ft_sourceanalysis)**
  - Visualize the results, using **[ft_sourceplot_interactive](/reference/ft_sourceplot_interactive)**.

## Preprocessing

### Reading the data

The aim is to reconstruct the sources underlying the event-related field, when the subject is presented with pictures of faces. in the **[raw2erp tutorial](/workshop/paris2019/handson_raw2erp)** we have computed sensor-level event-related fields, but we also stored the single-epoch data. We start off by loading the precomputed single-epoch data, and the headmodel and sourcemodel that were created during the **[anatomy tutorial](/workshop/paris2019/handson_sourceanalysis)**.

    load(fullfile(subj.outputpath, 'anatomy', sprintf('%s_headmodel', subj.name)));
    load(fullfile(subj.outputpath, 'anatomy', sprintf('%s_sourcemodel', subj.name)));
    headmodel   = ft_convert_units(headmodel,   'm');
    sourcemodel = ft_convert_units(sourcemodel, 'm');
    sourcemodel.inside = sourcemodel.atlasroi>0;

    filename = fullfile(subj.outputpath, 'raw2erp', sprintf('%s_data', subj.name));
    load(filename, 'data');

In this tutorial, we are only going to use the MEG data for the source reconstruction. Therefore, we proceed by selecting the MEG channels from the epoched data.

    cfg         = [];
    cfg.channel = {'MEG'};
    data        = ft_selectdata(cfg, data);

Next, for reasons that will become clear soon, we also select from the epoched data the timewindows just preceding the onset of the stimulus, from a time window between -200 ms and 0.

    cfg         = [];
    cfg.latency = [-0.2 0];
    baseline    = ft_selectdata(cfg, data);

Next, we use **[ft_timelockanalysis](/reference/ft_timelockanalysis)** to compute the sensor-level covariance of the baseline data.

    cfg            = [];
    cfg.covariance = 'yes';
    baseline_avg   = ft_timelockanalysis(cfg, baseline);

Now, if we reorder the channels a bit, we can visualise this covariance matrix as follows:

    selmag  = ft_chantype(baseline_avg.label, 'megmag');
    selgrad = ft_chantype(baseline_avg.label, 'megplanar');

    C = baseline_avg.cov([find(selmag);find(selgrad)],[find(selmag);find(selgrad)]);
    figure;imagesc(C);hold on;plot(102.5.*[1 1],[0 306],'w','linewidth',2);plot([0 306],102.5.*[1 1],'w','linewidth',2);

  {% include image src="/assets/img/workshop/paris2019/cov_meg.png" width="400" %}

  _Figure: MEG sensor covariance matrix_

The figure shows the covariance between all pairs of magnetometers in the left upper square on the diagonal, between all pairs of gradiometers the right lower square, and the covariance between magnetometers and gradiometers in the off- diagonal blocks. As can be seen, the left upper and off-diagonal blocks appear blue, suggesting that the numerical range of the magnetometer is a lot smaller than the numerical range of the gradiometers. In itself, this might not pose a problem, but it will result in a different weighing of gradiometers versus magnetometers when computing the source reconstruction. In addition to the difference in magnitude of the different channel types, the covariance matrix may be poorly estimated (for instance due to a limited amount of data available), or may be rank deficient due to previous processing steps. Examples of processing steps that cause the data to be rank deficient are artifact cleaning procedures based on independent component analysis (ICA), or signal space projections (SSPs). Another important processing step that reduces the rank of the data massively, is Elekta's maxfilter.
It is crucial to account for rank deficiency of the data, because if it's not done properly, the noise (be it numerical or real) will blow up the reconstruction.
Beamformers require the mathematical inverse of the covariance matrix computed from the epochs-of-interest (typically including a basline window but **never** computed on the baseline window alone). State-of-the-art distributed source reconstuction with minimum-norm estimation (MNE) require (implicitly) the mathematical inverse of a noise covariance matrix. Either way, irrespective of your favourite source reconstruction method, mathematical inversion of rank deficient covariance matrices that moreover consist of signals with different orders of magnitude requires some tricks to make the final result numerically well-behaved.
To make this a bit more concrete, we first will have a look at the singular value decomposition (which in this case is similar to a principal component analysis) of the baseline covariance matrix:

    [u,s,v] = svd(baseline_avg.cov);
    figure;plot(log10(diag(s)),'o');

  {% include image src="/assets/img/workshop/paris2019/cov_svd.png" width="400" %}

  _Figure: Singular values of a MEG sensor covariance matrix_

When thus plotted on a log scale, it can be seen that there is a range of 16 orders of magnitude in the signal components, and that there are actually 3 stairs in this singular value spectrum. There is a steep decline around component 70 or so, and another step at component 204. The step at component 204 reflects the magnitude difference between the 204 gradiometer signals and the 102 magnetometer signals. The discontinuity around component 70 reflects the effect of the Maxfilter, which has effectively removed about 236 spatial components out of the data.



### Averaging and computation of the covariance matrix

The function ft_timelockanalysis makes averages of all the trials in a data structure and also estimates the covariance. For a correct covariance estimation it is important that you used the cfg.demean = 'yes' option when the function ft_preprocessing was applied.

The trials belonging to one condition will now be averaged with the onset of the stimulus time aligned to the zero-time point (the onset of the median nerve stimulation). This is done with the function ft_timelockanalysis. The input to this procedure is the data structure generated by ft_preprocessing. At the same time, we need to compute the covariance matrix which is a key ingredient for the lcmv beamfomer. Therefore cfg.covariance = 'yes' has to be specified as well as the time window where the covariance will be estimated. In this case we will use all signal, which may differ from [minimum-norm-estimated source-reconstruction](/tutorial/minimumnormestimate) in that the latter typically creates a 'noise-covariance matrix' on basis of no signal of interest (e.g. baseline).

Note that we have not yet cleaned the data from artifacts. For your own dataset, we recommend that you have a look at the [visual artifact rejection tutorial](/tutorial/visual_artifact_rejection).

    cfg                  = [];
    cfg.covariance       = 'yes';
    timelock             = ft_timelockanalysis(cfg, data);

### Visualize the sensor level results (axial gradients)

We can plot the results with the MATLAB plot command to get a first impression

    figure; plot(timelock.time, timelock.avg)

{% include image src="/assets/img/tutorial/beamformer_lcmv/subjectseftimelock.png" width="400" %}

We can additionally explore the spatiotemporal dynamics using FieldTrip interactive plotting function


	% view the results
	cfg        = [];
	cfg.layout = 'CTF275_helmet.mat';
        cfg.xlim   = [0.045 0.050];
	ft_topoplotER(cfg, timelock);

{% include image src="/assets/img/tutorial/beamformer_lcmv/subjectseftopo.png" width="400" %}


### Visualize the sensor level results (planar gradients)

The present dataset was recorded with a CTF MEG system which has first-order axial gradiometer sensors that measure the gradient of the magnetic field in the radial direction, i.e. orthogonal to the scalp. Often it is helpful to interpret the MEG fields after transforming the data to a planar gradient configuration, i.e. by computing the gradient tangential to the scalp. This representation of MEG data is comparable to the field measured by planar gradiometer sensors. One advantage of the planar gradient transformation is that the signal amplitude typically is largest directly above a source.

With **[ft_megplanar](/reference/ft_megplanar)** we calculate the planar gradient of the averaged data. **[Ft_megplanar](/reference/ft_megplanar)** is used to compute the amplitude of the planar gradient by combining the horizontal and vertical components of the planar gradient;

The planar gradient at a given sensor location can be approximated by comparing the field at that sensor with its neighbours (i.e. finite difference estimate of the derivative). The planar gradient at one location is computed in both the horizontal and the vertical direction with the FieldTrip function **[ft_megplanar](/reference/ft_megplanar)**. These two orthogonal gradients on a single sensor location can be combined using Pythagoras rule with the FieldTrip function **[ft_combineplanar](/reference/ft_combineplanar)**.

Calculate the planar gradient of the averaged dat

    % calculate planar gradients
    cfg                 = [];
    cfg.feedback        = 'yes';
    cfg.method          = 'template';
    cfg.template        = 'ctf275_neighb.mat';
    cfg.neighbours      = ft_prepare_neighbours(cfg, timelock);

    cfg.planarmethod    = 'sincos';
    timelock_planar     = ft_megplanar(cfg, timelock);

Compute the amplitude of the planar gradient by combining the horizontal and vertical components of the planar gradient according to Pythagoras rule, and visualize the results (can you see the differences between the axial and planar gradients?

    % combine planar gradients
    cfg                 = [];
    timelock_planarcomb = ft_combineplanar(cfg, timelock_planar);


	% view the results
	cfg        = [];
	cfg.layout = 'CTF275_helmet.mat';
        cfg.xlim   = [0.045 0.050];
	ft_topoplotER(cfg, timelock_planarcomb);


## The forward model and lead field matrix

### Head model

The first step in the procedure is to construct a forward model. The forward model allows us to calculate an estimate of the field measured by the MEG sensors for a given current distribution. In MEG analysis a forward model is typically constructed for each subject. There are many types of forward models which to various degrees take the individual anatomy into account. We will here use a semi-realistic head model developed by Nolte (2003). It is based on a correction of the lead field for a spherical volume conductor by a superposition of basis functions, gradients of harmonic functions constructed from spherical harmonics.

The first step in constructing the forward model is to find the brain surface from the subject's MRI, using [ft_volumesegment](/reference/ft_volumesegment). The MRI scan used in this tutorial has already been realigned to the same coordinate system as the MEG data (in this case 'CTF', see [this page](/faq/how_can_i_convert_an_anatomical_mri_from_dicom_into_ctf_format) on how to realign your subject's brain volume.

    % read and segment the subject's anatomical scan
    load('SubjectSEF_mri.mat'); % matfile containing the realigned anatomical scan

    cfg        = [];
    cfg.output = 'brain';
    seg = ft_volumesegment(cfg, mri);

    % make a figure of the mri and segmented volumes
    segmentedmri           = seg;
    segmentedmri.transform = mri.transform;
    segmentedmri.anatomy   = mri.anatomy;
    cfg                    = [];
    cfg.funparameter       = 'brain';
    ft_sourceplot(cfg, segmentedmri);

Now prepare the head model from the segmented brain surface:


	% compute the subject's headmodel/volume conductor model
	cfg                = [];
	cfg.method         = 'singleshell';
	headmodel          = ft_prepare_headmodel(cfg, seg);
	headmodel          = ft_convert_units(headmodel, 'cm'); % mm to cm, since the grid will also be expressed in cm

{% include markup/warning %}
If you want to do a beamformer source reconstruction on EEG data, you have to pay special attention to the EEG referencing. The forward model will be made with an common average reference (except in some rare cases like with bipolar iEEG electrode montages), i.e. the mean value over all electrodes is zero. Consequently, this also has to be true in your data.

Prior to averaging the data with ft_timelockanalysis you have to ensure with ft_preprocessing that all channels are re-referenced to the common average reference.

Furthermore, after selecting the channels you want to use in the sourcereconstruction (excluding the bad channels) and after re-referencing them, you should not make sub-selections of channels any more and throw out channels, because that would cause the data not be average referenced any more.  
{% include markup/end %}

### Source model

Now prepare the source model. Here one has the option to make a 'normalized grid', such that the grid points in different subjects are aligned in MNI-space. For more details on how to make a normalized grid, see [here](/example/create_single-subject_grids_in_individual_head_space_that_are_all_aligned_in_mni_space). In this tutorial, we continue with non-normalized grid points:


	% create the subject specific grid
        grad = ft_read_sens('SubjectSEF.ds');

	cfg             = [];
	cfg.grad        = grad;
	cfg.headmodel   = headmodel;
	cfg.resolution  = 0.5;
	cfg.inwardshift = -1;
	sourcemodel     = ft_prepare_sourcemodel(cfg);

	% make a figure of the single subject headmodel, and grid positions
        figure;
	ft_plot_sens(grad, 'style', '*b');
	ft_plot_headmodel(headmodel, 'edgecolor', 'none'); alpha 0.4;
	ft_plot_mesh(sourcemodel.pos(sourcemodel.inside,:));

### Leadfield

Combine all the information into the leadfield matrix:


	% create leadfield
	cfg                  = [];
	cfg.grad             = grad;  % gradiometer distances
	cfg.headmodel        = headmodel;   % volume conduction headmodel
	cfg.sourcemodel      = sourcemodel;
	cfg.channel          = {'MEG'};
	cfg.singleshell.batchsize = 2000;
        lf                   = ft_prepare_leadfield(cfg);

## Source analysis

	% create spatial filter using the lcmv beamformer
	cfg                  = [];
	cfg.method           = 'lcmv';
	cfg.sourcemodel      = lf; % leadfield
	cfg.headmodel        = headmodel; % volume conduction model (headmodel)
	cfg.lcmv.keepfilter  = 'yes';
	cfg.lcmv.fixedori    = 'yes'; % project on axis of most variance using SVD
	source               = ft_sourceanalysis(cfg, timelock);
