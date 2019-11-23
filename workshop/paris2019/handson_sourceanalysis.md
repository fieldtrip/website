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

### Reading the data, and some issues with covariance matrices

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
Just using the 'normal' way of computing the covariance matrix' inverse, by using MATLAB's inv() function is asking for numerical problems, because the spatial components with very small singular values (which don't reflect any real signal) are blown up big time in the inverse. For this reason, regularised or truncated inversion techniques are to be used. In addition to applying more thoughtful algorithms for matrix inversion, spatial prewhitening techniques can be used, which manipulate the data in a way to make them, as the name suggests, spatially (more or less) white. This means that the signals are uncorrelated to each other, and have the same variance. As a byproduct, when the whitening is done separately for the magnetometers and gradiometers, the scale difference between the different channel types disappears, and thus prewhitening results in an 'equal' treatment of both channel types, and allows for a relatively straightforward combination of the different channel types during source reconstruction.

### Spatial whitening of the task data, using the activity from the baseline

The function **[ft_denoise_prewhiten](/reference/ft_denoise_prewhiten)** can be used for the prewhitening. As an input, it requires a data structure of the to-be-prewhitened data, and a data structure that contains a covariance structure that is used for the computation of the prewhitening operator. For MEG data, one can use an empty room recording for this, or a data structure containing data from a well-defined baseline window. Here, we use the 200 ms time window prior to the onset of the stimulus. In its default behaviour, ft_denoise_prewhiten does a separate prewhitening of the different channeltypes in the input data, so the magnetometers and gradiometers will be prewhitened separately.

    % the following lines detect the location of the first large 'cliff' in the singular value spectrum of the grads and mags
    [u,s_mag,v]  = svd(baseline_avg.cov(selmag,  selmag));  
    [u,s_grad,v] = svd(baseline_avg.cov(selgrad, selgrad));
    d_mag = -diff(log10(diag(s_mag))); d_mag = d_mag./std(d_mag);
    kappa_mag = find(d_mag>4,1,'first');
    d_grad = -diff(log10(diag(s_grad))); d_grad = d_grad./std(d_grad);
    kappa_grad = find(d_grad>4,1,'first');

    cfg            = [];
    cfg.channel    = 'meg';
    cfg.kappa      = min(kappa_mag,kappa_grad);
    dataw_meg      = ft_denoise_prewhiten(cfg, data, baseline_avg);

The prewhitening operator is defined as the inverse of the matrix square root of the covariance matrix that is to be used for the prewhitening. The cfg.kappa option in **[ft_denoise_prewhiten](/reference/ft_denoise_prewhiten)** ensures that a regularised inverse is used. Kappa refers to the number of spatial components to be retained in the inverse, and should be at most the number before which the steep cliff in singular values occurs.

#### Exercise 1:
{% include markup/info %}
 Select the 200 ms baseline from the dataw_meg structure, compute the covariance, and inspect the covariance matrix with imagesc() after grouping the magnetometers and the gradiometers. Also inspect the singular value spectrum of the whitened baseline covariance matrix.
{% include markup/end %}

## Compute the covariance matrix of the prewhitened data

## Compute the forward model

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
