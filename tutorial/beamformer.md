---
title: Localizing oscillatory sources using beamformer techniques
tags: [tutorial, meg, freq, source, headmodel, mri, plot, meg-language]
---

# Localizing oscillatory sources using beamformer techniques

## Introduction

In this tutorial we will continue working on the [dataset](/tutorial/meg_language) described in the preprocessing tutorials. Below we will repeat code to select the trials and preprocess the data as described in the first tutorials ([trigger based trial selection](/tutorial/preprocessing), [visual artifact rejection](/tutorial/visual_artifact_rejection)).

In this tutorial you will learn about applying beamformer techniques in the frequency domain. You will learn how to compute appropriate time-frequency windows, an appropriate head model and lead field matrix, and various options for contrasting the effect of interest against some control/baseline. Finally, you will be shown several options for plotting the results overlaid on a structural MRI.

It is expected that you understand the previous steps of preprocessing and filtering the sensor data. Some understanding of the options for computing the head model and forward lead field is also useful.

This tutorial will not cover the time-domain option for LCMV/SAM beamformers (described in Background), nor for beamformers applied to evoked/averaged data (although see an example of how to calculate [virtual sensors using LCMV](/tutorial/virtual_sensors) for an example of this).

{% include markup/info %}
This tutorial contains hands-on material that we use for the [MEG/EEG toolkit course](/workshop/toolkit2015) and it is complemented by this lecture.

{% include youtube id="Ez72OFjSABs" %}
{% include markup/end %}

## Background

In the [Time-Frequency Analysis tutorial](/tutorial/timefrequencyanalysis) we identified strong oscillations in the beta band in a language paradigm. The goal of this section is to identify the sources responsible for producing this oscillatory activity. We will apply a beamformer technique. This is a spatially adaptive filter, allowing us to estimate the amount of activity at any given location in the brain. The inverse filter is based on minimizing the source power (or variance) at a given location, subject to 'unit-gain constraint'. This latter part means that, if a source had power of amplitude 1 and was projected to the sensors by the lead field, the inverse filter applied to the sensors should then reconstruct power of amplitude 1 at that location. Beam forming assumes that sources in different parts of the brain are not temporally correlated.

The brain is divided in a regular three dimensional grid and the source strength for each grid point is computed. The method applied in this example is termed Dynamical Imaging of Coherent Sources (DICS) and the estimates are calculated in the frequency domain (Gross ET al. 2001). Other beam-former methods rely on sources estimates calculated in the time domain, e.g. the Linearly Constrained Minimum Variance (LCMV) and Synthetic Aperture Magnetometry (SAM) methods (van Veen et al., 1997; Robinson and Cheyne, 1997). These methods produce a 3D spatial distribution of the power of the neuronal sources. This distribution is then overlaid on a structural image of the subject's brain. Furthermore, these distributions of source power can be subjected to statistical analysis. It is always ideal to contrast the activity of interest against some control/baseline activity. Options for this will be discussed below, but it is best to keep this in mind when designing your experiment from the start, rather than struggle to find a suitable control/baseline after data collection.

## Procedure

To localize the oscillatory sources for the example dataset we will perform the following step

- Read the data into MATLAB using **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)**
- Compute the cross-spectral density matrix using the function **[ft_freqanalysis](/reference/ft_freqanalysis)**
- Construct a forward model and lead field matrix using **[ft_volumesegment](/reference/ft_volumesegment)**, **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** and **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)**

- Compute a spatial filter and estimate the power of the sources using **[ft_sourceanalysis](/reference/ft_sourceanalysis)**
  - Visualize the results, by first interpolating the sources to the anatomical MRI using **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)** and plotting this with **[ft_sourceplot](/reference/ft_sourceplot)**.

{% include image src="/assets/img/tutorial/beamformer/bf_pipeline.jpg" width="650" %}

## Preprocessing

The aim is to identify the sources of oscillatory activity in the beta band. From the section time-frequency analysis we have identified 18 Hz as the center frequency for which the power estimates should be calculated. We seek to compare the activation in the post-stimulus to the activation in the pre-stimulus interval. We first use **[ft_preprocessing](/reference/ft_preprocessing)** and **[ft_redefinetrial](/reference/ft_redefinetrial)** to extract relevant data. It is important that the length of each data piece is the length of a fixed number of oscillatory cycles. Here 9 cycles are used resulting in a 9/18 Hz = 0.5 s time window. Thus, the post-stimulus time-window range between 0.8 to 1.3 s and the pre-stimulus interval between -0.5 to 0.0 s (see Figure 1).

{% include image src="/assets/img/tutorial/beamformer/tfrbmf.png" width="700" %}

_Figure: The time-frequency presentation used to determine the time- and frequency-windows prior to beamforming. The squares indicate the selected time-frequency tiles for the pre- and post-response.._

{% include /shared/tutorial/preprocessing_fic.md %}

### Time windows of interest

Now we select the time windows of interest: the pre- and post stimulus windows. This requires the preprocessed data (see above), which is available from the [FieldTrip ftp server (dataFIC.mat)](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/beamformer/dataFIC.mat). Load the data with the following comman

    load dataFIC

Now 'cut' out the pre- and post-stimulus time window

    cfg = [];
    cfg.toilim = [-0.5 0];
    dataPre = ft_redefinetrial(cfg, dataFIC);

    cfg.toilim = [0.8 1.3];
    dataPost = ft_redefinetrial(cfg, dataFIC);

As mentioned in the Background, it is ideal to contrast the activity of interest against some control.

1.  Suitable control windows are, for exampl
    - Activity contrasted with baseline (example shown here using dataPre)
    - Activity of condition 1 contrasted with condition 2 (example not shown)
2.  However, if no other suitable data condition or baseline time-window exists, then
    - Activity contrasted with estimated noise (example shown below)
    - Use normalized leadfields (mentioned in ['the forward model and lead field matrix'](/tutorial/beamformer?&#the_forward_model_and_lead_field_matrix) section and Exercise 4 below)

The null hypothesis for both options within (1) is that the data in both conditions are the same, and thus the best spatial filter is the one that is computed using both data conditions together (also known as ['common filters'](/example/common_filters_in_beamforming)). This common filter is then applied separately to each condition.

### Exercise 1: data length

{% include markup/info %}
Why is it important that the length of each data piece is the length of a fixed number of oscillatory cycles?
{% include markup/end %}

## Calculating the cross spectral density matrix

The beamformer technique is based on an adaptive spatial filter. The DICS spatial filter is derived from the frequency counterpart of the covariance matrix: the cross-spectral density matrix. This matrix contains the cross-spectral densities for all sensor combinations and is computed from the Fourier transformed data of the single trials. It is given as output when cfg.output = 'powandcsd'. The frequency of interest is 18 Hz and the smoothing window is +/-4 Hz:

    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'powandcsd';
    cfg.tapsmofrq = 4;
    cfg.foilim    = [18 18];
    freqPre = ft_freqanalysis(cfg, dataPre);

    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'powandcsd';
    cfg.tapsmofrq = 4;
    cfg.foilim    = [18 18];
    freqPost = ft_freqanalysis(cfg, dataPost);

## The forward model and lead field matrix

### Head model

The first step in the procedure is to construct a forward model. The forward model allows us to calculate an estimate of the field measured by the MEG sensors for a given current distribution. In MEG analysis a forward model is typically constructed for each subject. There are many types of forward models which to various degrees take the individual anatomy into account. We will here use a semi-realistic head model developed by Nolte (2003). It is based on a correction of the lead field for a spherical volume conductor by a superposition of basis functions, gradients of harmonic functions constructed from spherical harmonics.

The first step in constructing the forward model is to find the brain surface from the subjects MRI. This procedure is termed segmentation.
Note that segmentation is quite time consuming. If you have access to the preprocessed file you can skip ahead to 'load segmentedmri'.

Otherwise, segmentation involves the following steps ((**[ft_volumesegment](/reference/ft_volumesegment)** makes use of SPM. The necessary SPM-files are located in fieldtripXXX/external/spm8)

    mri = ft_read_mri('Subject01.mri');
    cfg = [];
    cfg.write      = 'no';
    [segmentedmri] = ft_volumesegment(cfg, mri);

Alternatively, you can load the segmented MRI available from the [FieldTrip ftp server (segmentedmri.mat)](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/beamformer/segmentedmri.mat

    load segmentedmri

Now prepare the head model from the segmented brain surfac

    cfg = [];
    cfg.method = 'singleshell';
    headmodel = ft_prepare_headmodel(cfg, segmentedmri);

{% include markup/warning %}
If you want to do a beamformer source reconstruction on EEG data, you have to pay special attention to the EEG referencing. The forward model will be made with an common average reference (except in some rare cases like with bipolar iEEG electrode montages), i.e. the mean value over all electrodes is zero. Consequently, this also has to be true in your data.

Prior to doing the spectral decomposition with ft_freqanalysis you have to ensure with ft_preprocessing that all channels are re-referenced to the common average reference.

Furthermore, after selecting the channels you want to use in the sourcereconstruction (excluding the bad channels) and after re-referencing them, you should not make sub-selections of channels any more and throw out channels, because that would cause the data not be average referenced any more.  
{% include markup/end %}

### Exercise 2: head model

{% include markup/info %}
Why might a single sphere model be inadequate for performing beamformer estimates?
{% include markup/end %}

### Compute lead field

The next step is to discretize the brain volume into a grid (the sourcemodel). For each grid point the lead field matrix is calculated. It is calculated with respect to a grid with a 1 cm resolution.

{% include markup/warning %}
Sensors MLP31 and MLO12 were removed from the data set. Thus it is essential to remove these sensors as well when calculating the lead fields.
{% include markup/end %}

    cfg                 = [];
    cfg.grad            = freqPost.grad;
    cfg.headmodel       = headmodel;
    cfg.reducerank      = 2;
    cfg.channel         = {'MEG','-MLP31', '-MLO12'};
    cfg.resolution = 1;   % use a 3-D grid with a 1 cm resolution
    cfg.sourcemodel.unit       = 'cm';
    [grid] = ft_prepare_leadfield(cfg);

As mentioned earlier on, if you are not contrasting the activity of interest against another condition or baseline time-window, then you may choose to normalize the lead field (cfg.normalize='yes'), which will help control against the power bias towards the center of the head.

## Source Analysis: without contrasting condition

Using the cross-spectral density and the lead field matrices a spatial filter is calculated for each grid point. By applying the filter to the Fourier transformed data we can then estimate the power for the pre- and post-stimulus activity. This results in a power estimate for each grid point. We first show the example as if you only had dataPost (and no dataPre against which to make a contrast).

    cfg              = [];
    cfg.method       = 'dics';
    cfg.frequency    = 18;
    cfg.sourcemodel         = grid;
    cfg.headmodel    = headmodel;
    cfg.dics.projectnoise = 'yes';
    cfg.dics.lambda       = 0;

    sourcePost_nocon = ft_sourceanalysis(cfg, freqPost);

The purpose of cfg.dics.projectnoise will become more clear in the section on Neural Activity Index. The purpose of lambda is discussed in Exercise 6.

Save the outpu
save sourcePost_nocon sourcePost_nocon

The beamformer procedure estimates the power in the beta frequency band at each grid point in the brain volume. The grid of estimated power values can be plotted superimposed on the anatomical MRI. This requires the output of **[ft_sourceanalysis](/reference/ft_sourceanalysis)** (see above or download from the [FieldTrip ftp server (sourcePost_nocon.mat)](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/beamformer/sourcePost_nocon.mat)) and the subject's MRI (also is available from the [ftp server (Subject01.zip)](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip)).

    load sourcePost_nocon

The function **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)** aligns the measure of power increase with the structural MRI of the subject. The alignment is done according to the anatomical landmarks (nasion, left and right ear canal) that were both determined in the MEG measurement and in the MRI scan. Using the ft_volumereslice function before doing the interpolation ensures that the MRI is well behaved, because the reslicing causes the voxel axes to be aligned with the head coordinate axe

    mri = ft_read_mri('Subject01.mri');
    mri = ft_volumereslice([], mri);

    cfg            = [];
    cfg.downsample = 2;
    cfg.parameter = 'pow';
    sourcePostInt_nocon  = ft_sourceinterpolate(cfg, sourcePost_nocon , mri);

Plot the interpolated data:

    cfg              = [];
    cfg.method       = 'slice';
    cfg.funparameter = 'pow';
    figure
    ft_sourceplot(cfg,sourcePostInt_nocon);

{% include image src="/assets/img/tutorial/beamformer/figure1bf.png" width="500" %}

_Figure: The power estimates of the post-stimulus activity only at ~18 Hz. Note the strong noise bias toward the center of the head. The image was done using **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)** and **[ft_sourceplot](/reference/ft_sourceplot)**.._

Notice that the power is strongest in the center of the brain. There are several ways of circumventing the noise bias towards the center of the head which we will show below.

### Exercise 3: center of head bias

{% include markup/info %}
Discuss why the source power is overestimated in the center of the brain. Hint 1: what are the leadfield values in the center of the head? Why? Hint 2: Remember the 'unit-gain constraint' of beamformer spatial filters.
{% include markup/end %}

### Neural Activity Index

If it is not possible to compare two conditions (e.g. A versus B or post versus pre) one can apply the neural activity index (NAI), in order to remove the center of the head bias shown above. The NAI is the power normalized with an estimate of the spatially inhomogeneous noise. An estimate of the noise has been done by **[ft_sourceanalysis](/reference/ft_sourceanalysis)**, by setting cfg.dics.projectnoise='yes' (default is 'no'). This noise estimate was computed on the basis of the smallest eigenvalue of the cross-spectral density matrix. To calculate the NAI do the followin

    sourceNAI = sourcePost_nocon;
    sourceNAI.avg.pow = sourcePost_nocon.avg.pow ./ sourcePost_nocon.avg.noise;

    cfg = [];
    cfg.downsample = 2;
    cfg.parameter = 'pow';
    sourceNAIInt = ft_sourceinterpolate(cfg, sourceNAI , mri);

Plot it:

    cfg = [];
    cfg.method        = 'slice';
    cfg.funparameter  = 'pow';
    cfg.maskparameter = cfg.funparameter;
    cfg.funcolorlim   = [4.0 6.2];
    cfg.opacitylim    = [4.0 6.2];
    cfg.opacitymap    = 'rampup';
    figure
    ft_sourceplot(cfg, sourceNAIInt);

{% include image src="/assets/img/tutorial/beamformer/figure2bf.png" width="500" %}

_Figure: The neural activity index (NAI) plotted for the post-stimulus time window normalized with respect to the noise estimate.._

### Exercise 4: lead field normalization

{% include markup/info %}
Another option, besides contrasting to the noise estimate, is to normalize the lead field when you compute it (cfg.normalize='yes' in the call to ft_prepare_leadfield). Recompute the lead field and source estimate this way and plot the result.
{% include markup/end %}

## Source Analysis: Contrast activity to another interval

One approach is to compare the post- and pre-stimulus interval, which we describe now here. Another approach is to contrast the same window of interest (relative in time to some stimulus or response) between two or more conditions, which we do not show here, but the calls to FieldTrip functions are conceptually the same.

Importantly, if you later want to compare the two conditions statistically, you have to compute the sources based on an inverse filter computed from both conditions, so called ['common filters'](/example/common_filters_in_beamforming), and then apply this filter separately to each condition to obtain the source power estimate in each condition separately.

First we compute a single data structure with both conditions, and compute the frequency domain CSD.

    dataAll = ft_appenddata([], dataPre, dataPost);

    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'powandcsd';
    cfg.tapsmofrq = 4;
    cfg.foilim    = [18 18];
    freqAll = ft_freqanalysis(cfg, dataAll);

Then we compute the inverse filter based on both conditions. Note the use of cfg.keepfilter so that the output saves this computed filter.

    cfg              = [];
    cfg.method       = 'dics';
    cfg.frequency    = 18;
    cfg.sourcemodel         = grid;
    cfg.headmodel    = headmodel;
    cfg.dics.projectnoise = 'yes';
    cfg.dics.lambda       = '5%';
    cfg.dics.keepfilter   = 'yes';
    cfg.dics.realfilter   = 'yes';
    sourceAll = ft_sourceanalysis(cfg, freqAll);

By placing this pre-computed filter inside cfg.sourcemodel.filter, it can now be applied to each condition separately.

    cfg.sourcemodel.filter = sourceAll.avg.filter;
    sourcePre_con  = ft_sourceanalysis(cfg, freqPre );
    sourcePost_con = ft_sourceanalysis(cfg, freqPost);

    save sourcePre_con sourcePre_con
    save sourcePost_con sourcePost_con

Now we can compute the contrast of (post-pre)/pre. In this operation we assume that the noise bias is the same for the pre- and post-stimulus interval and it will thus be removed.

    sourceDiff = sourcePost_con;
    sourceDiff.avg.pow = (sourcePost_con.avg.pow - sourcePre_con.avg.pow) ./ sourcePre_con.avg.pow;

Load and reslice the MRI if not done already in previous ste

    mri = ft_read_mri('Subject01.mri');
    mri = ft_volumereslice([], mri);

Then interpolate the source to the MR

    cfg            = [];
    cfg.downsample = 2;
    cfg.parameter  = 'pow';
    sourceDiffInt  = ft_sourceinterpolate(cfg, sourceDiff , mri);

Now plot the power ratios:

    cfg = [];
    cfg.method        = 'slice';
    cfg.funparameter  = 'pow';
    cfg.maskparameter = cfg.funparameter;
    cfg.funcolorlim   = [0.0 1.2];
    cfg.opacitylim    = [0.0 1.2];
    cfg.opacitymap    = 'rampup';
    ft_sourceplot(cfg, sourceDiffInt);

{% include image src="/assets/img/tutorial/beamformer/figure4bf.png" width="500" %}

_Figure: sourceplot with method "slice" ._

### Exercise 5: comparing normalizations

{% include markup/info %}
Compare figure 3 and 4. It appears that normalizing the power with the baseline activity result in fewer and more focal sources. Why?
{% include markup/end %}

### Exercise 6: regularization

{% include markup/info %}
The regularization parameter was cfg.dics.lambda = '5%'. Change it to 0 or to '10%' and plot the power estimate with respect to baseline. How does the regularization parameter affect the properties of the spatial filter?  
{% include markup/end %}

## Plotting options

To plot an 'orthogonal cut

    cfg = [];
    cfg.method        = 'ortho';
    cfg.funparameter  = 'pow';
    cfg.maskparameter = cfg.funparameter;
    cfg.funcolorlim   = [0.0 1.2];
    cfg.opacitylim    = [0.0 1.2];
    cfg.opacitymap    = 'rampup';
    ft_sourceplot(cfg, sourceDiffInt);

{% include image src="/assets/img/tutorial/beamformer/figure7bf.png" width="500" %}

_Figure: sourceplot with method "ortho"._

The FieldTrip function **[ft_volumenormalise](/reference/ft_volumenormalise)** normalises anatomical and functional volume data to a template anatomical MRI. Spatially aligning the source structures for multiple subjects allows you to compute grandaverages and over subjects statistics. Here we will illustrate the use of volume normalisation for one subject.

    cfg = [];
    cfg.nonlinear     = 'no';
    sourceDiffIntNorm = ft_volumenormalise(cfg, sourceDiffInt);

When plotting the orthogonal view it is possible to enter interactive mode by specifying cfg.interactive='yes'. This allows you to 'browse' through the brain volume by specifying the location of cut with a mouse click. To exit the interactive mode press 'q'.

    cfg = [];
    cfg.method        = 'ortho';
    cfg.interactive   = 'yes';
    cfg.funparameter  = 'pow';
    cfg.maskparameter = cfg.funparameter;
    cfg.funcolorlim   = [0.0 1.2];
    cfg.opacitylim    = [0.0 1.2];
    cfg.opacitymap    = 'rampup';
    ft_sourceplot(cfg, sourceDiffIntNorm);

{% include image src="/assets/img/tutorial/beamformer/figure8bf.png" width="500" %}

_Figure: sourceplot with method "ortho" after volume normalisation._

You can also project the power onto a surface using **[ft_sourceplot](/reference/ft_sourceplot)**. FieldTrip has several surface .mat files available. The surface files are in MNI coordinates, so therefore the volume has to be normalized to match those coordinates. This can be done with the FieldTrip function **[ft_volumenormalise](/reference/ft_volumenormalise)** (see above, as well).

    cfg = [];
    cfg.nonlinear     = 'no';
    sourceDiffIntNorm = ft_volumenormalise(cfg, sourceDiffInt);

Now the data can be plotted

    cfg = [];
    cfg.method         = 'surface';
    cfg.funparameter   = 'pow';
    cfg.maskparameter  = cfg.funparameter;
    cfg.funcolorlim    = [0.0 1.2];
    cfg.funcolormap    = 'jet';
    cfg.opacitylim     = [0.0 1.2];
    cfg.opacitymap     = 'rampup';
    cfg.projmethod     = 'nearest';
    cfg.surffile       = 'surface_white_both.mat';
    cfg.surfdownsample = 10;
    ft_sourceplot(cfg, sourceDiffIntNorm);
    view ([90 0])

{% include image src="/assets/img/tutorial/beamformer/bf_tut_surfacepowrelnorm_comfilt.png" width="500" %}

_Figure: sourceplot with method "surface"._

## Summary and suggested further reading

Beamforming source analysis in the frequency domain with DICS has been demonstrated. An example of how to compute a head model (single shell) and forward lead field was shown. Various options for contrasting the time-frequency window of interest against a control was shown, including against 'noise' (NAI: minimum eigenvalue of the CSD) and against the pre-stimulus window using a 'common filter'. Options at each stage and their influence on the results were discussed, such as lead field normalization and CSD matrix regularization. Finally, options for plotting on slices, orthogonal views, or on the surface were shown.

Details on head models can be found [here](/tutorial/headmodel_meg) or [here](/example/make_leadfields_using_different_headmodels). Computing event-related fields with [MNE](/tutorial/minimumnormestimate) or [LCMV](/tutorial/beamformer_lcmv) might be of interest. More information on [common filters can be found here](/example/common_filters_in_beamforming).
If you are doing a group study where you want the grid points to be the same over all subjects, [see here](/example/create_single-subject_grids_in_individual_head_space_that_are_all_aligned_in_mni_space). See [here for source statistics](/example/source_statistics).

FAQ
{% include seealso tag1="source" tag2="faq" %}

Example script
{% include seealso tag1="source" tag2="example" %}
