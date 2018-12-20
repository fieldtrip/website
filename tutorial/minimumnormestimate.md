---
title: Source reconstruction of event-related fields using minimum-norm estimation
tags: [tutorial, timelock, source, meg, headmodel, mri, plot, MEG-language]
---

# Source reconstruction of event-related fields using minimum-norm estimation

## Introduction

In this tutorial you can find information about how to do source reconstruction using minimum-norm estimation, to reconstruct the event-related fields (MEG) of a single subject. We will be working on the [dataset](/tutorial/meg_language) described in the preprocessing tutorials ([Trigger-based trial selection](/tutorial/preprocessing), [Event related averaging and planar gradient](/tutorial/eventrelatedaveraging)), and we will use also the anatomical images that belong to the same subject.  We will repeat code to select the trials and preprocess the data as described in the [Event related averaging and planar gradient](/tutorial/eventrelatedaveraging) tutorial. We assume that preprocessing and event-related averaging is already clear for the reader. To preprocess the anatomical data, we will use two other software packages (FreeSurfer and MNE Suite).

This tutorial will not show how to do group-averaging and statistics on the source-level. It will also not describe how to do source-localization of oscillatory activation. You can check the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) tutorial if you are interested in this latest.

## Background

In the [Event related averaging and planar gradient](/tutorial/eventrelatedaveraging) tutorial time-locked averages of event related fields of three conditions have been computed and the [Cluster-based permutation tests on event related fields](/tutorial/cluster_permutation_timelock) tutorial showed that there was a significant difference among two conditions. The topographical distribution of the ERFs belonging to each conditions and ERFs belonging to those differences have been plotted. The aim of this tutorial is to calculate a distributed representation of the underlying neuronal activity that resulted in the brain activity observed at the sensor level.

To calculate distributed neuronal activation we will use the minimum-norm estimation. This approach is favored for analyzing evoked responses and for tracking the wide-spread activation over time. It is a distributed inverse solution that discretizes the source space into locations on the cortical surface or in the brain volume using a large number of equivalent current dipoles. It estimates the amplitude of all modeled source locations simultaneously and recovers a source distribution with minimum overall energy that produces data consistent with the measurement ((Ou, W., Hamalainen, M., Golland, P., 2008, A Distributed Spatio-temporal EEG/MEG Inverse Solver)) ((Jensen, O., Hesse, C., 2010, Estimating distributed representation of evoked responses and oscillatory brain activity, In: MEG: An Introduction to Methods, ed. by Hansen, P., Kringelbach, M., Salmelin, R., doi:10.1093/acprof:oso/9780195307238.001.0001)). The reference for the implemented method is [Dale et al. (2000)](/references_to_implemented_methods).

## Procedure

Figure 1 shows a schematic of the steps needed for the calculation of the minimum-norm estimate. It shows that the computation of the inverse solution is based on the outputs of two independent processing steps: the processing of the anatomical images that leads to a forward model and the processing of the MEG data. To create a useable source model, additional software is needed, for example FreeSurfer (for the creation of a model of the cortical sheet), and MNE Suite or HCP workbench (to get a minimally distorted low-resultion version of the cortical sheet).

{% include image src="/assets/img/tutorial/minimumnormestimate/pipeline_mne.png" width="550" %}

*Figure 1. A schematic overview of the steps needed for the calculation of the minimum-norm estimate*

The forward model requires three geometric object

*  A volume conduction model of the head, also known as headmodel.
*  A sourcemodel, we advocate a minimally distorted low-resolution description of the cortical sheet.
*  A geometric description of the sensor-array (electrode positions + referencing information for EEG, coil positions/orientation and balancing information for MEG).

The sourcemodel and headmodel are ideally generated from a subject-specific MRI image. The description of the sensor-array typically is represented in the data (MEG), or needs to be constructed, for example with a Polhemus device (EEG). The construction of the head- and sourcemodels that are needed for the remainder of this tutorial is described in the following tutorial

*  [Creating a volume conduction model of the head for source-reconstruction of MEG data](/tutorial/headmodel_meg)
*  [Creating a sourcemodel for source-reconstruction of MEG or EEG data](/tutorial/sourcemodel)

Once we have the headmodel and sourcemodel, we perform the following step

*  compute the forward solution using **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)**;
*  preprocess the MEG data using **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)**;
*  compute the average over trials and estimate the noise-covariance using **[ft_timelockanalysis](/reference/ft_timelockanalysis)**;
*  compute the inverse solution using **[ft_sourceanalysis](/reference/ft_sourceanalysis)** and **[ft_sourcedescriptives](/reference/ft_sourcedescriptives)**;
*  visualize the results with **[ft_plot_mesh](/reference/ft_plot_mesh)** and **[ft_sourcemovie](/reference/ft_sourcemovie)**.

## Processing of functional data

The following will use the MEG data belonging to Subject01. The file can be obtained from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).
For both preprocessing and averaging, we will follow the steps that have been written in the [Event related averaging and planar gradient](/tutorial/eventrelatedaveraging) tutorial. We will use trials belonging to two conditions (FC and FIC) and we will calculate their difference.

### Preprocessing of MEG data

{% include /shared/tutorial/preprocessing_fc_lp.md %}

{% include /shared/tutorial/preprocessing_fic_lp.md %}

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
	cfg.headmodel = vol;                               % volume conduction model
	leadfield = ft_prepare_leadfield(cfg);

	save leadfield leadfield;

## Inverse solution

The **[ft_sourceanalysis](/reference/ft_sourceanalysis)** function calculates the inverse solution. The method used (minimum-norm estimation) has to be specified with the cfg.method option. The averaged functional data, the forward solution (the output of the **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)** function), the volume conduction model (in this case, the output of the **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** function) and the noise-covariance matrix (the cov field of the output of the **[ft_timelockanalysis](/reference/ft_timelockanalysis)** function) have to be provided.

The lambda value is a scaling factor that is responsible for scaling the noise-covariance matrix. If it is zero the noise-covariance estimation will be not taken into account during the computation of the inverse solution. Noise-covariance is estimated in each trial separately and then averaged, while the functional data (of which we calculate the source-analysis) is simply averaged across all the trials. Therefore,  the higher the number of trials the lower the noise is in the averaged, functional data, but the number trials is not reducing the noise in the noise-covariance estimation. This is the reason while it is useful to use a scaling factor for the noise-covariance matrix if we want to estimate more realistically the amount of noise.  

You do not have to specify of the noise-covariance matrix separatly, because it is in the tlckFC.cov and in the tlckFIC.cov fields, and ft_sourceanalysis will take it into account automatically.

	load tlck;
	load leadfield;
	load vol;

	cfg        = [];
	cfg.method = 'mne';
	cfg.grid   = leadfield;
	cfg.headmodel     = vol;
	cfg.mne.prewhiten = 'yes';
	cfg.mne.lambda    = 3;
	cfg.mne.scalesourcecov = 'yes';
	sourceFC  = ft_sourceanalysis(cfg,tlckFC);
	sourceFIC = ft_sourceanalysis(cfg, tlckFIC);

	save source sourceFC sourceFIC;

## Visualization

You can plot the inverse solution onto the source-space at a specific time-point with the **[ft_plot_mesh](/reference/ft_plot_mesh)** function.

	load source;
	load sourcespace;

	bnd.pnt = sourcespace.pnt;
	bnd.tri = sourcespace.tri;
	m=sourceFIC.avg.pow(:,450); % plotting the result at the 450th time-point that is
	                         % 500 ms after the zero time-point
	ft_plot_mesh(bnd, 'vertexcolor', m);

{% include image src="/assets/img/tutorial/minimumnormestimate/plotmeshsourceic01new.png" width="450" %}

//Figure 6. The result of the source-reconstruction of the FIC condition plotted onto the source-space at 500 ms after the 0 time-point
//

But we would like to know where the difference between the conditions can be localized. Therefore, we calculate the difference of the two conditions, and we use **[ft_sourcemovie](/reference/ft_sourcemovie)** to visualize the results.

	cfg = [];
	cfg.projectmom = 'yes';
	sdFC = ft_sourcedescriptives(cfg,sourceFC);
	sdFIC = ft_sourcedescriptives(cfg, sourceFIC);

	sdDIFF = sdFIC;
	sdDIFF.avg.pow = sdFIC.avg.pow - sdFC.avg.pow;
	sdDIFF.tri = sourcespace.tri;

	save sd sdFC sdFIC sdDIFF;

	cfg = [];
	cfg.mask = 'avg.pow';
	ft_sourcemovie(cfg,sdDIFF);

{% include image src="/assets/img/tutorial/minimumnormestimate/sourcemovie01new.png" width="500" %}
*Figure 7. One frame from the movie that shows the differences of the two source-reconstructions*

## Summary and further readings

In this tutorial we showed how to do MNE source reconstruction method on a single subject data. We compared the averaged ERF in two conditions and we reconstructed the sources and we calculated the difference of the two source-reconstruction. We showed also how you can visualize the results.

Functions and tutorial pages that show how to average, and how to analyze statistically source-reconstructions across subjects or how to compare those to a template brain are still under development.

FAQ
{% include seealso tag1="source" tag2="faq" %}

Example script
{% include seealso tag1="source" tag2="example" %}
