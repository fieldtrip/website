---
title: Analysis of auditory evoked fields in sensor and source space
---

# Analysis of auditory evoked fields in sensor and source space

## Introduction

In this tutorial we will analyze auditory evoked fields in the context of a widely studied sensory gating paradigm. First we will analyze the data on sensor level in both time and time-frequency domain. On the basis of this analysis we will define relevant latencies and/or time-frequency tiles that will be subsequently analyzed in source space using beamforming techniques. Finally we will try to identify relevant "nodes" based on statistical contrasts in source space and perform some connectivity metric on these task relevant nodes.

## Background

The data in this tutorial has been acquired with 148 sensor magnetometer system 4D/Neuroimaging. The experimental paradigm is illustrated in the figure below. An auditory stimulus of 3ms duration is presented twice with an inter-stimulus interval of 500 ms. The first presentation is typically labeled as 'S1' and the second 'S2', yet the stimuli are identical. This paired-click trial is presented 100 times with an inter-trial interval of 8 seconds. The sensory gating phenomenon refers to a decrease in neuronal activity after S2 and is typically quantified as a ratio (S2/S1) of the early M50 (30-90ms post stimulus) component of the event-related field.

{% include image src="/assets/img/tutorial/salzburg/figure1.png" width="600" %}

## Procedure

### Loading the data

In the following section we will read and epoch the data. Subsequently we will apply some processing steps, e.g., rejecting bad trials by visual inspection and decomposing the data by means of independent component analysis. The late step will allow us to disregard data components likely reflective for cardiac and ocular activity.

The following steps had been performed:

- Defining triggers around which the data will be segmented using **[ft_definetrial](/reference/ft_definetrial)**. The data is segmented to include 2 seconds prior to S1 onset (i.e. baseline) and 1.57 second post S1 onset (i.e. event-related interval including S1 and S2).
- Calling **[ft_preprocessing](/reference/ft_preprocessing)** without applying any preprocessing steps yet.

To run the following section of code you need the original dataset and trial function: [c,rfhp0.1Hz](https://download.fieldtriptoolbox.org/tutorial/salzburg/c,rfhp0.1Hz), [config](https://download.fieldtriptoolbox.org/tutorial/salzburg/config), and [ft_trialfun_sensorygating.m](https://download.fieldtriptoolbox.org/tutorial/salzburg/ft_trialfun_sensorygating.m)

    clear all
    close all

    cfg = [];
    cfg.dataset = 'c,rfhp0.1Hz';
    cfg.trialfun = 'ft_trialfun_sensorygating';
    cfg.trialdef.prestim = 2; %sec
    cfg.trialdef.poststim = 2; %sec
    cfg.channel = {'MEG' '-A28' '-A148' };
    cfg = ft_definetrial(cfg);
    data = ft_preprocessing(cfg);

The epoched data can be downloaded [here](https://download.fieldtriptoolbox.org/tutorial/salzburg/dataclean.mat).

Load the data using the following command:

    load dataclean

First we will visual inspection of the data in order to reject trials contaminated by movements and/or other artifacts such as SQUID jumps. We will use **[ft_rejectvisual](/reference/ft_rejectvisual)** where we want a summary of the activity over trials and sensors, i.e. _cfg.method_ = 'summary';. It is recommended to explore the topography and time course of data that will be classified as artificial. The configuration option _cfg.layout_ = '4D148.lay'; allows us to do so.

    cfg = [];
    cfg.fontsize = 12;
    cfg.method = 'summary';
    cfg.layout = '4D148.lay';
    dataclean = ft_rejectvisual(cfg, data);
    save dataclean dataclean

Next, we perform the independent component analysis according to the following step

- Resampling the data to a lower sample rate in order to speed up ICA computation **[ft_resampledata](/reference/ft_resampledata)**.
- Perform the independent components analysis on the resampled data **[ft_componentanalysis](/reference/ft_componentanalysis)**
- Repeat the independent components analysis on the original data by applying the linear demixing and topography lebels form the previous step

Note, that we will compute the ICA twice in order to retain the original sampling rate. The option **cfg.resamplefs** depends on your knowledge about the spectral characteristics of the artifacts you would like to discover. Vertical and horizontal eye movements are typically dominated by high energy in the low frequency < 10 Hz. Therefore everything above the Nyquist frequency of the targeted signal, in this case 20 Hz, is an appropriate sampling rate. Cardiac artifacts vary over the entire frequency spectrum, although there is some dominance in the slower frequencies too. The decision about the new sampling frequency thus strongly depends on your needs. If you are interested in the detection of caridac and oculo-motor activity, a sampling rate of >100 Hz will be appropriate for most of the cases.

    cfg = [];
    cfg.resamplefs = 140;
    cfg.detrend    = 'no';
    datads = ft_resampledata(cfg, dataclean);
    % perform the independent component analysis (i.e., decompose the data)
    cfg        = [];
    cfg.method = 'runica';
    cfg.runica.maxsteps =50;
    comp = ft_componentanalysis(cfg, datads);
    cfg           = [];
    cfg.unmixing  = comp.unmixing;
    cfg.topolabel = comp.topolabel;
    comp = ft_componentanalysis(cfg, data);

Now we could explore the decomposed data by using **[ft_databrowser](/reference/ft_databrowser)**

    cfg = [];
    cfg.channel = {comp.label{1:5}}; % components to be plotted
    cfg.layout = '4D148.lay'; % specify the layout file that should be used for plotting
    cfg.compscale = 'local';
    ft_databrowser(cfg, comp);

Take your time to browse and evaluate the topographies and the corresponding time courses. We will reject several of these with **[ft_rejectcomponent](/reference/ft_rejectcomponent)**

    cfg = [];
    cfg.component = [3 6 7 16];
    dataica = ft_rejectcomponent(cfg, comp);

The ica corrected data can be downloaded [here](https://download.fieldtriptoolbox.org/tutorial/salzburg/dataica.mat).

### Computing and plotting of the auditory evoked fields

Now we can average over trials using **[ft_timelockanalysis](/reference/ft_timelockanalysis)** and plot the evoked activity using the plotting functions **[ft_multiplotER](/reference/ft_multiplotER)**,**[ft_singleplotER](/reference/ft_singleplotER)** and **[ft_topoplotER](/reference/ft_topoplotER)**.

    cfg=[]
    tlk=ft_timelockanalysis(cfg,dataica);

    cfg=[];
    cfg.layout = '4D148.lay';
    figure;
    ft_multiplotER(cfg,tlk);

    cfg=[];
    cfg.channel = {'A77'};
    cfg.xlim    = [-.2 1];
    figure;
    subplot(2,2,1);ft_singleplotER(cfg,tlk);
    cfg =[];
    cfg.layout = '4D148.lay';
    cfg.xlim = [0.114416 0.136568];
    cfg.zlim = [-2e-13 2e-13];
    subplot(2,2,2); ft_topoplotER(cfg,tlk);
    title('S1')
    cfg.xlim = cfg.xlim+0.5;
    subplot(2,2,4); ft_topoplotER(cfg,tlk);
    title('S2')

{% include image src="/assets/img/tutorial/salzburg/figure2.png" width="600" %}

### Computing and plotting time-frequency power representations

Now we will compute the time-frequency representation of the event-related fields by considering each trial individually and subsequently averaging over trials. It is recommended that you make yourself familiar with the different strategies in frequency and time-frequency analysis [here](/tutorial/timefrequencyanalysis).

    cfg              = [];
    cfg.output       = 'pow';
    cfg.method       = 'mtmconvol';
    cfg.taper        = 'hanning';
    cfg.foi          = 2:2:30;
    cfg.t_ftimwin    = ones(length(cfg.foi),1).*0.5;
    cfg.toi          = -1.5:.05:1;
    cfg.keeptrials ='no';
    tfr= ft_freqanalysis(cfg,  dataica);
    % baseline correction
    cfg=[];
    cfg.baseline=[-1.75 -.25];
    cfg.baselinetype='db';
    tfrbl = ft_freqbaseline(cfg, tfr);

Subsequently we plot and evaluate the result.

    cfg=[];
    cfg.channel = {'A77'};
    cfg.xlim    = [-.2 1];
    figure;
    subplot(2,2,1);ft_singleplotTFR(cfg,tfrbl);
    cfg =[];
    cfg.layout = '4D148.lay';
    cfg.xlim = [0.06 0.3];
    cfg.ylim = [5 8];
    cfg.zlim = [-2 2]
    subplot(2,2,2); ft_topoplotTFR(cfg,tfrbl);
    title('S1')
    cfg.xlim = cfg.xlim+0.5;
    subplot(2,2,4); ft_topoplotTFR(cfg,tfrbl);
    title('S2')

{% include image src="/assets/img/tutorial/salzburg/figure3.png" width="600" %}

Sometimes one might be interested in power modulations significantly different from pre stimulus baseline. In the following section we will illustrate how to achieve this.

### Within subject statistics on time-frequency representations

We will apply the following steps. First the data is segmented into pre and post stimulus intervals of equal length using **[ft_redefinetrial](/reference/ft_redefinetrial)**. Thereafter time-frequency representation of power is computed on these intervals separately by keeping the individual trials in the output structure.

test

    %%
    cfg=[];
    cfg.toilim = [-2 -.5];
    datapre = ft_redefinetrial(cfg,dataica);
    cfg.toilim = [-.5 1];
    datapst = ft_redefinetrial(cfg,dataica);
    %%
    cfg              = [];
    cfg.output       = 'pow';
    cfg.method       = 'mtmconvol';
    cfg.taper        = 'hanning';
    cfg.foi          = 0:2:30;
    cfg.t_ftimwin    = ones(length(cfg.foi),1).*0.5;
    cfg.toi          = -2:.05:-.5;
    cfg.keeptrials ='yes';
    tfrpre= ft_freqanalysis(cfg,  datapre);
    cfg.foi          = 0:2:30;
    cfg.toi          = -.5:.05:1;
    tfrpst= ft_freqanalysis(cfg,  datapst);

Since the data is of equal length we equalize the time axis of pre and post stimulus segments as well as assuring that both frequency dimensions are also the same.

    tfrpre.time = tfrpst.time
    tfrpre.freq = round(tfrpre.freq);
    tfrpst.freq = round(tfrpst.freq);

Now we compute the statistical evaluation using permutation approach. All of the details are explained [elsewere](/tutorial/cluster_permutation_freq).

    cfg = [];
    cfg.channel          = {'MEG'};
    cfg.latency          = [0 1];
    cfg.method           = 'montecarlo';
    cfg.statistic        = 'ft_statfun_actvsblT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = 0;
    cfg.alpha            = 0.025;
    cfg.numrandomization = 500;
    % prepare_neighbours determines what sensors may form clusters
    cfg_neighb.method    = 'distance';
    cfg.neighbours       = ft_prepare_neighbours(cfg_neighb, tfrpre);

    ntrials = size(tfrpst.powspctrm,1);
    design  = zeros(2,2*ntrials);
    design(1,1:ntrials) = 1;
    design(1,ntrials+1:2*ntrials) = 2;
    design(2,1:ntrials) = [1:ntrials];
    design(2,ntrials+1:2*ntrials) = [1:ntrials];

    cfg.design   = design;
    cfg.ivar     = 1;
    cfg.uvar     = 2;

    cfg.design           = design;
    cfg.ivar             = 1;

    [stat] = ft_freqstatistics(cfg, tfrpst, tfrpre);
    save stat stat

Now we can plot the result in a similar way as illustrated above. The difference now is that the functional data is expressed in units of t-values. In addition we use now a mask to illustrate the time-frequency tile on the basis of which we reject the H0- the data from pre and post stimulus interval is exchangeable.

    cfg=[];
    cfg.channel = {'A77'};
    cfg.parameter = 'stat';
    cfg.maskparameter = 'mask';
    cfg.maskstyle     = 'outline';
    cfg.zlim = [-5 5]
    cfg.xlim    = [0 .7];
    figure;
    subplot(2,2,1);ft_singleplotTFR(cfg,stat);
    cfg =[];
    cfg.layout = '4D148.lay';
    cfg.parameter = 'stat';
    cfg.xlim = [0.06 0.3];
    cfg.ylim = [5 8];
    cfg.zlim = [-5 5]
    subplot(2,2,2); ft_topoplotTFR(cfg,stat);
    title('S1')
    cfg.xlim = cfg.xlim+0.5;
    subplot(2,2,4); ft_topoplotTFR(cfg,stat);
    title('S2')

{% include image src="/assets/img/tutorial/salzburg/figure4.png" width="600" %}

## Localizing auditory evoked fields using beamforming techniques in parceled brain space

In this section we would demonstrate how to derive the time series of neuronal activity at a particular brain location. We will apply a beamforming technique.

{% include markup/info %}
Before you continue it is recommended to make your self familiar with the relevant concepts by watching the following lecture.

{% include youtube id="7eS11DtbIPw" %}
{% include markup/end %}

Furthermore the details around how to compute the ingredients needed herein (e.g., headmodel, leadfield) are not further explained here. All of the necessary steps in head modeling are explained here, and source modeling [here](/example/sourcemodel_aligned2mni_atlas).

We will start with loading a precomputed headmodel [here](https://download.fieldtriptoolbox.org/tutorial/salzburg/hdm.mat). We will first construct a regular dipole grid using **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)**. Subsequently we want to determine the grid locations corresponding to particular brain areas (parcels). For this step we will read an anatomical atlas using **[ft_read_atlas](/reference/fileio/ft_read_atlas)** and generate a binary mask with entries of ones indicating grid points corresponding to brain parcels using **[ft_volumelookup](/reference/ft_volumelookup)**. Finally, on the basis of the individual anatomy we will construct a source model that is inverse-warped to this atlas-based source model in mni space.

##### Create template grid based on the standard head model

    load('~/fieldtrip/template/headmodel/standard_singleshell');

    cfg = [];
    cfg.xgrid  = -20:1:20;
    cfg.ygrid  = -20:1:20;
    cfg.zgrid  = -20:1:20;
    cfg.unit   = 'cm';
    cfg.tight  = 'yes';
    cfg.inwardshift = -1.5;
    cfg.headmodel        = vol;
    template_grid  = ft_prepare_sourcemodel(cfg);

    figure;
    ft_plot_mesh(template_grid.pos(template_grid.inside,:));
    hold on
    ft_plot_headmodel(vol,  'facecolor', 'cortex', 'edgecolor', 'none');alpha 0.5; camlight;

{% include image src="/assets/img/tutorial/salzburg/figure5.png" width="600" %}

##### Load atlas and create a binary mask

    atlas = ft_read_atlas('~/fieldtrip/template/atlas/aal/ROI_MNI_V4.nii');

    atlas = ft_convert_units(atlas,'cm'); % assure that atlas and template_grid are expressed in the %same units

    cfg = []
    cfg.atlas = atlas;
    cfg.roi = atlas.tissuelabel;
    cfg.inputcoord = 'mni';
    mask = ft_volumelookup(cfg,template_grid);

    % create temporary mask according to the atlas entries
    tmp                  = repmat(template_grid.inside,1,1);
    tmp(tmp==1)          = 0;
    tmp(mask)            = 1;

    % define inside locations according to the atlas based mask
    template_grid.inside = tmp;

    % plot the atlas based grid
    figure; ft_plot_mesh(template_grid.pos(template_grid.inside,:));

{% include image src="/assets/img/tutorial/salzburg/figure6.png" %}

##### Inverse-warp the subject specific grid to the atlas based template grid

For this step the individual volume is required, which can be downloaded [here](https://download.fieldtriptoolbox.org/tutorial/salzburg/mri.mat).

    cfg                = [];
    cfg.warpmni   = 'yes';
    cfg.template  = template_grid;
    cfg.nonlinear = 'yes';
    cfg.mri            = mri;
    sourcemodel        = ft_prepare_sourcemodel(cfg);

##### Plot the final source model together with the individual head model and the sensor array

    close all
    % the 4D/bti system is expressed in units of 'm', therefore we force all geometrical objects to have the same unit
    hdm = ft_convert_units(hdm, 'm');
    sourcemodel = ft_convert_units(sourcemodel, 'm');

    figure; hold on     % plot all objects in one figure

    ft_plot_headmodel(hdm,  'facecolor', 'cortex', 'edgecolor', 'none');alpha 0.5; %camlight;
    alpha 0.4           % make the surface transparent

    ft_plot_mesh(sourcemodel.pos(sourcemodel.inside,:)); % plot only locations inside the volume

    ft_plot_sens(dataica.grad,'style','*r'); % plot the sensor array
    view ([0 -90 0])

{% include image src="/assets/img/tutorial/salzburg/figure7.png" %}

### Compute the leadfield

We first create the leadfield using [**reference: ft_prepare_leadfield](/\*\*reference/ ft_prepare_leadfield) using the individual head model from the previous step, the sensor array and the sourcemodel.

    cfg                 = [];
    cfg.channel         = dataica.label; % ensure that rejected sensors are not present
    cfg.grad            = dataica.grad;
    cfg.headmodel       = hdm;
    cfg.lcmv.reducerank = 2; % default for MEG is 2, for EEG is 3
    cfg.grid = sourcemodel;
    [grid] = ft_prepare_leadfield(cfg);

We want to reconstruct the locations of the M100 component. In the present case this component is maximal around 50 to 180ms post stimulus onset. Therefore we segment the data around this interval using [**reference: ft_redefinetrial](/\*\*reference/ ft_redefinetrial). Furthermore we would contrast the source solution against a prestimulus baseline of equal length.

    cfg = [];
    cfg.toilim = [-.18 -.05];
    datapre = ft_redefinetrial(cfg, dataica);
    cfg.toilim = [.05 .18];
    datapost = ft_redefinetrial(cfg, dataica);

### Compute data covariance

The spatial filters are computed on the basis of the covariance matrix obtained from the data. In the following step we compute this matrix for an interval accounting for the pre and post stimulus intervals of interest. For this we make a call to [**reference: ft_timelockanalysis](/**reference/ ft_timelockanalysis) with the ** cfg.covariance = 'yes';** and ** cfg.covariancewindow = [xx yy];\*\*. These configuration will ensure the covariance matrix to be present in the output structure.

    cfg = [];
    cfg.covariance='yes';
    cfg.covariancewindow = [-.3 .3];
    avg = ft_timelockanalysis(cfg,dataica);

    cfg = [];
    cfg.covariance='yes';
    avgpre = ft_timelockanalysis(cfg,datapre);
    avgpst = ft_timelockanalysis(cfg,datapost);

Now we make a first call to [** reference: ft_sourceanalysis](/\*\* reference/ ft_sourceanalysis) in order to compute the spatial filters on the basis of the entire data and keep them in the output for a later use.

    cfg=[];
    cfg.method='lcmv';
    cfg.grid=grid;
    cfg.headmodel=hdm;
    cfg.lcmv.keepfilter='yes';
    cfg.channel = dataica.label;
    sourceavg=ft_sourceanalysis(cfg, avg);

### Perform sourcanalysis

Subsequently we reconstruct the activity in the pre and post stimulus intervals using the precomputed filters.

    cfg=[];
    cfg.method='lcmv';
    cfg.grid=grid;
    cfg.sourcemodel.filter=sourceavg.avg.filter;
    cfg.headmodel=hdm;
    sourcepreS1=ft_sourceanalysis(cfg, avgpre);
    sourcepstS1=ft_sourceanalysis(cfg, avgpst);

Now we can subtract the two conditions, normalize by the power in the pre stimulus interval and multiply by 100. Thereby the data is expressed in percentage change from pre stimulus baseline.

    cfg = [];
    cfg.parameter = 'avg.pow';
    cfg.operation = '((x1-x2)./x2)*100';
    S1bl=ft_math(cfg,sourcepstS1,sourcepreS1);

The result is then interpolated on the template mri after the individual dipole locations are set back to be equal with the template_grid locations. This is done with [**reference: ft_sourceinterpolate](/\*\*reference/ ft_sourceinterpolate).

    if isunix
      templatefile = '~fieldtrip/template/anatomy/single_subj_T1.nii';
    elseif ispc
      templatefile = 'H:\~\fieldtrip\template\anatomy\single_subj_T1.nii';
    end
    template_mri = ft_read_mri(templatefile);
    S1bl.pos=template_grid.pos;
    cfg              = [];
    cfg.voxelcoord   = 'no';
    cfg.parameter    = 'pow';
    cfg.interpmethod = 'nearest';
    source_int  = ft_sourceinterpolate(cfg, S1bl, template_mri);

Finally, we can plot the result using [**reference: ft_sourceplot](/\*\*reference/ ft_sourceplot).

    cfg               = [];
    cfg.method        = 'ortho';
    cfg.funparameter  = 'pow';
    cfg.location = [64 -32 8];
    cfg.funcolormap = 'jet';
    ft_sourceplot(cfg,source_int);

{% include image src="/assets/img/tutorial/salzburg/figure8.png" %}

### Plot the result in parceled brain space

It is now possible to integrate the result over the brain parcels using the brain atlas and [**reference: ft_sourceparcellate](/**reference/ ft_sourceparcellate). First, we load the template mri corresponding to the brain atlas located in the spm8/templates directory and interpolate the result on this template once more. Subsequently we call [**reference: ft_sourceparcellate](/\*\*reference/ ft_sourceparcellate) with this sourceinterpolated structure and the brain atlas.

    templatefile = '~fieldtrip/external/spm8/templates/T1.nii';
    template_mri = ft_read_mri(templatefile);
    cfg              = [];
    cfg.voxelcoord   = 'no';
    cfg.parameter    = 'pow';
    cfg.interpmethod = 'nearest';
    source_int  = ft_sourceinterpolate(cfg, S1bl, template_mri);
    %%
    cfg=[];
    parcel = ft_sourceparcellate(cfg, source_int, atlas);

    parcel =

                label: {1x116 cell}  % brain parcels labels
              anatomy: [116x1 double]
        anatomydimord: 'chan_unknown'
                  pow: [116x1 double]% one value of brain activity per parcel
            powdimord: 'chan'
        brainordinate: [1x1 struct]
                  cfg: [1x1 struct]

We create a dummy structure where we identify the power values per voxel and use this for subsequent plotting.

    dummy=atlas;
    for i=1:length(parcel.pow)
          dummy.tissue(find(dummy.tissue==i))=parcel.pow(i);
    end
    %%
    source_int.parcel=dummy.tissue;
    source_int.coordsys = 'mni';
    cfg=[];
    cfg.method = 'ortho';
    cfg.funparameter = 'parcel';
    cfg.funcolormap    = 'jet';
    cfg.renderer = 'zbuffer';
    cfg.location = [-42 -20 6];
    cfg.atlas = atlas;
    cfg.funcolorlim = [-30 30];
    ft_sourceplot(cfg,source_int);

{% include image src="/assets/img/tutorial/salzburg/figure9.png" %}

Alternatively, the maximal activity in the left Heschl gyrus can be plotted on the brain surface as follows.

    cfg = [];
    cfg.method         = 'surface';
    cfg.funparameter   = 'parcel';
    cfg.funcolorlim    = [-30 30];
    cfg.funcolormap    = 'jet';
    cfg.projmethod     = 'nearest';
    cfg.surfinflated   = 'surface_inflated_both_caret.mat';
    cfg.projthresh     = 0.8;
    cfg.camlight       = 'no';
    ft_sourceplot(cfg, source_int);
    view ([-70 20 50])
    light ('Position',[-70 20 50])
    material dull

{% include image src="/assets/img/tutorial/salzburg/figure10.png" %}

### Apply statistical threshold for plotting the result on source level

In the previous section we used an arbitrary threshold (80% of maximum) to illustrate the "hill" of the activity. However, in some situations one might be interested in the spatial activation pattern that is statistically different from pre stimulus baseline. In order to achieve this we will keep the units of observation (i.e. trials) and apply nonparametric permutation approach to quantify the spatial activation pattern after stimulus presentation.

It is recommended to make yourself familiar with the permutation framework before you continue. This is explained in detail in the statics tutorial. You might also consult this on-line lecture.

{% include markup/info %}
This tutorial contains the hands-on material of the [Salzburg workshop](/workshop/salzburg). The background is explained in this lecture, which was recorded at the [Aston MEG-UK workshop](/workshop/birmingham).

{% include youtube id="vOSfabsDUNg" %}
{% include markup/end %}

First we keep single trial information and perform source analysis once again. It is important to estimate the spatial filter on the basis of all data and not the single trials. The latter is typically noisy and results in not very robust estimates.

    cfg = [];
    cfg.covariance='yes';
    cfg.keeptrials = 'yes';
    avgpre = ft_timelockanalysis(cfg,datapre);
    avgpst = ft_timelockanalysis(cfg,datapost);
    %%
    cfg=[];
    cfg.method='lcmv';
    cfg.grid=grid;
    cfg.headmodel=hdm;
    cfg.lcmv.keepfilter='yes';
    cfg.channel = dataica.label;
    sourceavg=ft_sourceanalysis(cfg, avg);
    cfg=[];
    cfg.method='lcmv';
    cfg.grid=grid;
    cfg.sourcemodel.filter=sourceavg.avg.filter;
    cfg.rawtrial = 'yes';
    cfg.headmodel=hdm;
    sourcepreS1=ft_sourceanalysis(cfg, avgpre);
    sourcepstS1=ft_sourceanalysis(cfg, avgpst);

Now statistical analysis can be performed.

    cfg = [];
    cfg.parameter    = 'pow';
    cfg.dim          = grid.dim;
    cfg.method           = 'montecarlo';
    cfg.statistic        = 'ft_statfun_depsamplesT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.tail             = 0;
    cfg.clustertail      = 0;
    cfg.alpha            = 0.025;
    cfg.numrandomization = 1000;

    ntrials = numel(sourcepreS1.trial);
    design  = zeros(2,2*ntrials);
    design(1,1:ntrials) = 1;
    design(1,ntrials+1:2*ntrials) = 2;
    design(2,1:ntrials) = [1:ntrials];
    design(2,ntrials+1:2*ntrials) = [1:ntrials];

    cfg.design   = design;
    cfg.ivar     = 1;
    cfg.uvar     = 2;
    stat = ft_sourcestatistics(cfg,sourcepstS1,sourcepreS1);
    stat.pos=template_grid.pos; % keep positions for plotting later

Subsequently we interpolate the result and the binary mask containing information of significant deferences per voxel.

    stat.inside=template_grid.inside;
    cfg              = [];
    cfg.voxelcoord   = 'no';
    cfg.parameter    = 'stat';
    cfg.interpmethod = 'nearest';
    statint  = ft_sourceinterpolate(cfg, stat, template_mri);
    cfg.parameter    = 'mask';
    maskint  = ft_sourceinterpolate(cfg, stat, template_mri);
    statint.mask = maskint.mask;

And plot the result masked for significant activations where the functional data is now expressed in t-values.

    statint.coordsys = 'mni';
    cfg               = [];
    cfg.method        = 'ortho';
    cfg.funparameter  = 'stat';
    cfg.maskparameter = 'mask';
    cfg.atlas         = atlas;
    cfg.location = 'max';
    cfg.funcolorlim   = [-5 5];
    cfg.funcolormap = 'jet';
    ft_sourceplot(cfg,statint);

{% include image src="/assets/img/tutorial/salzburg/figure11.png" %}

We repeat the steps from above and plot the result in parceled brain space.

    cfg=[];
    parcel = ft_sourceparcellate(cfg, statint, atlas);
    parcelmask = ft_sourceparcellate(cfg, maskint, atlas);
    %% create dummy struct
    dummy=atlas;
    dummymask = atlas;
    for i=1:length(parcel.stat)
          dummy.tissue(find(dummy.tissue==i))=parcel.stat(i);
          dummymask.tissue(find(dummymask.tissue==i))=parcelmask.mask(i);
    end
    %% plot the result
    statint.parcel=dummy.tissue;
    statint.coordsys = 'mni';
    statint.mask  = dummymask.tissue;
    cfg=[];
    cfg.method = 'slice';
    cfg.funparameter = 'parcel';
    cfg.funcolormap    = 'jet';
    cfg.maskparameter = 'mask';
    cfg.renderer = 'zbuffer';
    cfg.funcolorlim   = [-5 5];
    cfg.atlas = atlas;
    ft_sourceplot(cfg,statint);

{% include image src="/assets/img/tutorial/salzburg/figure12.png" %}

The two different thresholds (80% of maximum vs. permutation statistics) seem to convey slightly different results. While a predominant activation in the left heschl gyrus was observed as a maximal difference between pre and post stimulus interval, the statistical evaluation suggest right temporal activation together with distributed activity in prefrontal areas. At first this appears somewhat puzzling yet evaluating the spatial extend of the activity in the left heschl gyrus suggest a very focal circumscribed source likely involving very few voxels. On the other hand during the call to [**reference: ft_sourcestatistics](/\*\*reference/ ft_sourcestatistics) we used a particular configuration for the clusterstatistics- 'maxsum'. Using this option only voxel clusters with largest summed activity are considered during the sampling of the distribution. The right temporal area is characterized by rather broad spatial homogeneity that leads to greater statistical sensitivity. Instead of 'maxsum' it is also possible to use 'max' values during the montercarlo sampling of the distribution. When we do so it becomes apparent that on the basis of the activity in the left heschl gyrus we can reject H0 too.

{% include image src="/assets/img/tutorial/salzburg/figure13.png" width="800" %}

## Connectivity analysis

Often the research question is concerned with description of interactions between relevant nodes in a given network. For example, it is hypothesized that conditions such as tinnitus are not driven by malfunction in primary auditory cortices alone. Instead, it is assumed that aberrant interaction between primary and higher order regions may mediate the manifestation of the commonly described symptoms.

So far we have identified three potential "nodes" involved in the processing of a simple auditory stimulus. However, source analysis is more than mere enumeration of brain locations. Each of these nodes is associated with a time course, which shall be evaluated in the following section.

### Reconstruct the time course of activity at a particular brain location

Based on visual inspection of the data provided by the interactive navigation after the call to **[ft_sourceplot](/reference/ft_sourceplot)** we can determine the coordinates of the locations subject to further examination.

Alternative approach is enabled due to the utilized parcellation strategy. We can derive the coordinates of all locations corresponding to a particular parcel, e.g., left heschl gyrus. In the following we will reduce the data to three loacations: left and right heschl gyri and left Cingulum_Mid in the frontal cortex.

{% include markup/warning %}
We used statistics to reject the hypothesis that: the data in the pre and post stimulus intervals is exchangeable. It might appear that the decision about which nodes to choose is based on this statistical evaluation. However this is false. The spatial aspect of the data is not subject to hypothesis testing. We motivate our decision on the basis of our interpretation of the conclusion- the data is not exchangeable. The interpretation and not the statistical testing per se is based on prior knowledge, knowledge about function-anatomy, credible expectations of spatial patterns in the context of the experimental design and many other factors. Consulting this [FAQ](/faq/how_not_to_interpret_results_from_a_cluster-based_permutation_test) is recommended.
{% include markup/end %}

First, we interpolate the statistical result and the atlas.

    cfg = [];
    cfg.interpmethod = 'nearest';
    cfg.parameter = 'tissue';
    stat_atlas = ft_sourceinterpolate(cfg, atlas, stat);

Determine the index of the label of interest,

    x = find(ismember(atlas.tissuelabel,'Heschl_L'));

and determine the index points of locations within the desired parcel.

    indxHGL = find(stat_atlas.tissue==x);

These steps can be repeated for all desired parcels. In the present case the ramining tw

    x=find(ismember(atlas.tissuelabel,'Heschl_R'));
    indxHGR = find(stat_atlas.tissue==x);

    x=find(ismember(atlas.tissuelabel,'Cingulum_Mid_L'));
    indxCML = find(stat_atlas.tissue==x);

Next, we normalise the individual MRI to derive parameters allowing to convert the mni- coordinates of the desired parcels into individual coordinates. For this we use **[ft_warp_apply](/reference/utilities/ft_warp_apply)**.

    template_grid=ft_convert_units(template_grid,'mm'); % ensure no unit mismatch
    norm=ft_volumenormalise([],mri);

    posCML=template_grid.pos(indxCML,:); % xyz positions in mni coordinates
    posHGL=template_grid.pos(indxHGL,:); % xyz positions in mni coordinates
    posHGR=template_grid.pos(indxHGR,:); % xyz positions in mni coordinates

    posback=ft_warp_apply(norm.params,posCML,'sn2individual');
    btiposCML= ft_warp_apply(pinv(norm.initial),posback); % xyz positions in individual coordinates

    posback=ft_warp_apply(norm.params,posHGL,'sn2individual');
    btiposHGL= ft_warp_apply(pinv(norm.initial),posback); % xyz positions in individual coordinates

    posback=ft_warp_apply(norm.params,posHGR,'sn2individual');
    btiposHGR= ft_warp_apply(pinv(norm.initial),posback); % xyz positions in individual coordinates

Now we create a source model for these particular locations only.

    cfg=[];
    cfg.headmodel=hdm;
    cfg.channel=dataica.label;
    cfg.sourcemodel.pos=[btiposCML;btiposHGL;btiposHGR]./1000; % units of m
    cfg.grad=dataica.grad;
    sourcemodel_virt=ft_prepare_leadfield(cfg);

And repeat the source analysis steps for above but now for 3 parcels represented in a total of 21 locations.

    %% keep covariance in the output
    cfg = [];
    cfg.channel=dataica.label;
    cfg.covariance='yes';
    cfg.covariancewindow=[0 1];
    avg = ft_timelockanalysis(cfg,dataica);

    %% perform source analysis
    cfg=[];
    cfg.method='lcmv';
    cfg.grid = sourcemodel_virt;
    cfg.headmodel=hdm;
    cfg.lcmv.keepfilter='yes';
    cfg.lcmv.fixedori='yes';
    cfg.lcmv.lamda='5%';
    source=ft_sourceanalysis(cfg, avg);

On the basis of the computed filters, kept in the output, it is now possible to multiply them with the data. This operation will yield time series commonly known as virtual sensors.

    spatialfilter=cat(1,source.avg.filter{:});
    virtsens=[];
    for i=1:length(dataica.trial)
        virtsens.trial{i}=spatialfilter*dataica.trial{i};

    end
    virtsens.time=dataica.time;
    virtsens.fsample=dataica.fsample;
    indx=[indxFML;indxHGL;indxHGR];
    for i=1:length(virtsens.trial{1}(:,1))
        virtsens.label{i}=[num2str(i)];
    end

Since our main interest is the time courses common to a given parcel we can average over within parcel locations.

    cfg = [];
    cfg.channel = virtsens.label(1:16); % cingulum is prepresented by 16 locations
    cfg.avgoverchan = 'yes';
    virtsensCML = ft_selectdata(cfg,virtsens);
    virtsensCML.label = {'CML'};

    cfg.channel = virtsens.label(17:19); % left heschl by 3
    virtsensHGL = ft_selectdata(cfg,virtsens);
    virtsensHGL.label = {'HGL'};

    cfg.channel = virtsens.label(20:21); % right heschl by 2
    virtsensHGR = ft_selectdata(cfg,virtsens);
    virtsensHGR.label = {'HGR'};

    %% append the data
    virtsensparcel=ft_appenddata([],virtsensCML,virtsensHGL,virtsensHGR);

Now we compute the source wave forms, plot and evaluate the result.

    cfg=[];
    tlkvc=ft_timelockanalysis(cfg, virtsensparcel);
    figure;
    for i=1:length(tlkvc.label)
        cfg=[];
        cfg.channel = tlkvc.label{i};
        cfg.parameter = 'avg';
        cfg.xlim    = [-.1 1];

        subplot(2,2,i);ft_singleplotER(cfg,tlkvc);
    end

{% include image src="/assets/img/tutorial/salzburg/figure14.png" width="600" %}

### Compute cortico-cortical coherence

One of various and equally valid methods of assessing connectivity is the concept of coherence. By using this metric we want to evaluate the presence of a temporal relationship between the nodes as a function of frequency. This can be done for the entire time interval of interest or by applying sliding window approach and represent the result as function of time and frequency. The latter is applied below.

First, we use **[ft_freqanalysis](/reference/ft_freqanalysis)** much in the same way as demonstrated above. The only difference is that the phase information is kept in the output by the configuration option **cfg.output = 'powandcsd'**.

    cfg         = [];
    cfg.method       = 'mtmconvol';
    cfg.taper        = 'hanning';
    cfg.output  = 'powandcsd';
    cfg.foi          = 2:2:40;
    cfg.t_ftimwin    = ones(length(cfg.foi),1).*0.5;
    cfg.toi          = -2:0.05:1;
    tfr = ft_freqanalysis(cfg, virtsensparcel);

Now we can plot and evaluate the result of the power estimates essentially confirming the pattern we already observed.

    figure;
    for i=1:length(tfr.label)
        cfg=[];
        cfg.channel = tfr.label{i};
        cfg.baselinetype    = 'db';
        cfg.baseline        = [-inf 0];
        cfg.zlim    = [-2 2];
        cfg.xlim    = [-.5 1.6];
        cfg.ylim    = [0 20];
        subplot(2,2,i);ft_singleplotTFR(cfg,tfr);
    end

{% include image src="/assets/img/tutorial/salzburg/figure15.png" width="600" %}

The slow frequency increases in energy are likely related to the evoked components in the data. In addition an increase in amplitude around 10-14Hz is also observed. In the next step we would like to evaluate to what extend this patterns represent a temporal relationship between the nodes.
First we compute coherence using **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)**.

    cfg = [];
    cfg.method = 'coh';
    coherence = ft_connectivityanalysis(cfg, tfr);

and restructure the output such that it can be plotted with an appropriate plotting function.

    coh=tfr;
    coh.powspctrm = coherence.cohspctrm;
    coh.label = {'CML-HGR','HGL-HGR','HGL-CML'};

    %% and plot the result
    figure;
    for i=1:length(coh.label)
        cfg=[];
        cfg.channel = coh.label{i};
        cfg.xlim    = [-.1 1];
        cfg.ylim    = [0 20];
        subplot(2,2,i);ft_singleplotTFR(cfg,coh);
    end

{% include image src="/assets/img/tutorial/salzburg/figure16.png" width="400" %}

The color scale in this figure now represents the strength of coherence, which varies always between 0 and 1. Descriptively we can conclude that cingulum and right auditory cortex comunicate strongly ~7Hz in the first 300 ms after stimulus presentation. Both auditory corticies are strongly linked at ~11Hz for some 200 ms starting after 300 ms post stimulus. Finally, cingulum and left auditory cortex seem to be linked at rather faster frequency ~ 14Hz.

However this descriptive description of the obtained result could be entirely wrong. This is because an additional confound commonly known as volume conduction is also present in the data. The consequence of such a confound is that a single source could emerge at multiple nodes. Accordingly these nodes would appear connected but in reality they are not.

A property of volume conduction is instantaneousness. As a consequence a given pattern of activity is visible at two independent sites with no time delay. This is typically described as a zero phase lag relationship. Mathematically, a cosine function has a phase angle of zero degree. Now, consider a complex plain with real (abscissa) and imaginary (ordinate) components. According to the definition, volume conduction, i.e. zero phase lag relationship, is entirely represented along the real axis. This suggest that in order to disregard the contribution of volume conduction one could take into account only signals that have non zero values on the imaginary axis. This strategy is also known as the imaginary part of coherency. The following section demonstrates how to assess this quantity.

    cfg = [];
    cfg.method = 'coh';
    cfg.complex = 'imag'; % ensure only imaginary parts kept in the output
    coherence = ft_connectivityanalysis(cfg, tfr);

    %% reorganize the data and take the absolute value
    coh=tfr;
    coh.powspctrm = abs(coherence.cohspctrm);
    coh.label = {'CML-HGR','HGL-HGR','HGL-CML'};

    %% and plot the result
    figure;
    for i=1:length(coh.label)
        cfg=[];
        cfg.channel = coh.label{i};
        cfg.xlim    = [-.1 1];
        cfg.ylim    = [0 20];
        subplot(2,2,i);ft_singleplotTFR(cfg,coh);
    end

{% include image src="/assets/img/tutorial/salzburg/figure17.png" width="400" %}

#### Exercise: coherence vs. imaginary part of coherency

{% include markup/info %}
Take your time to evaluate both outputs. To what extend the description of the interacting sources still holds?
{% include markup/end %}

### Compute non-parametric granger causality

In addition to describing a correlation between time series at two or more locations often the research question is concerned with the directionality of this correlation. The former is typically termed functional connectivity and the latter effective connectivity. That is, whether or not a time course of activity at location A not only relates to B but also effects its time course.

One way of assessing effective connectivity is by using the concept of Granger causality. This technique essentially estimates how much of the future variability of the time course in B is predicted by the knowledge about past time course behavior in A. A key parameter in this technique is the decision with respect to how far in the past of A one have to look in order to reliably estimate the future in B without fully explaining the data, i.e. over fitting. This parameter is very often difficult to estimate.

An alternative is a non parametric estimation where the essential ingredients for GC to work are estimated on the basis of spectral matrix factorization. These concepts and the basic analysis steps a covered in the [connectivity tutorial](/tutorial/connectivity). Here we will show how to apply non-parametric Granger analysis to address the research question to what extend there are "pre established" routes between frontal and auditory areas preceding stimulus onset.

The presence of transient activity such as evoked responses is a major violation of the assumptions in Granger analysis. Therefore we will focus on time intervals before stimulus presentation that is not contaminated by evoked responses. Moreover, for simplicity and illustrative purposes we will reduce the data set to two nodes- cingulum mid left and left heschl gyrus.

    cfg = [];
    cfg.channel = {'HGL','CML'};
    cfg.latency = [-2 0];
    prestimdata=ft_selectdata(cfg,virtsensparcel);

A requirement of the method is that frequency analysis is performed for 0Hz(DC) up to the Nyquist frequency. Moreover, a padding of the data with zeros is applied in order to minimized the effects of sharp changes in the estimated granger spectrum due for example to line noise.

    cfg            = [];
    cfg.output     = 'fourier';
    cfg.method     = 'mtmfft';
    cfg.taper      = 'dpss';
    cfg.tapsmofrq  = 2;
    cfg.keeptrials = 'yes';
    cfg.pad = 2;
    cfg.padtype = 'zero';
    freq    = ft_freqanalysis(cfg, prestimdata);

    cfg           = [];
    cfg.method    = 'granger';
    cfg.granger.sfmethod = 'bivariate';
    granger      = ft_connectivityanalysis(cfg, freq);

and plot the result...

    cfg = [];
    cfg.parameter = 'grangerspctrm';
    cfg.xlim      = [0 40];
    figure; ft_connectivityplot(cfg,granger);

{% include image src="/assets/img/tutorial/salzburg/figure18.png" width="400" %}

Again, we can now **descriptively** evaluate the output. Left auditory cortex appears to regulate activity in frontal areas at around 20 Hz. In turn, frontal areas exert a 10Hz drive over the left primary auditory cortex.

Although such a conclusion might appear in line with some theories on cortical computations and fit with the notion of prefrontal controllers etc. this conclusion is not the only interpretation of the present finding.

Consider a case where an unknown third source party biases activity in the locations of examinations in such a way that its power is projected strongly to a given location A as compared to B. Consider also constant noise level present in the data. In such a scenario due to different levels of SNR in location A and B, past knowledge of A will always help to "predict" future state of B than B alone. In other words, the output of the granger analysis will confirm effective connectivity between the nodes of examination despite the fact that there is none. The down side of scenarios like this is that they represent a rule rather than an exception. However, the motivation behind these types of analysis is not to prove the presence of effective connection between the nodes but to guide our uncertainty in the decision and interpretation of the data.

Accordingly we seek for an alternative evaluation that will aid and support such decisions. One possibility is to flip the time axis of the data, that is future becomes past and past future. This manipulation will not affect the SNR issue described above such that a similar granger spectrum in the original and in the flipped version will add confidence in our decision that the effective connectivity we are after is actually not present in the data. However, in the case of discrepancy this also does not mean that there IS effective connectivity not biased by scenarios and source constellations different from the example above. It will merely reduce our uncertainty in the data interpretation in turn of a great value in generating testable predictions for future examinations.

In the following we flip the time axis.

    tmpdata=prestimdata;
    for jj=1:length(tmpdata.trial)
    tmpdata.trial{jj}=fliplr(tmpdata.trial{jj});
    end

And compute granger analysis on these flipped data.

    cfg            = [];
    cfg.output     = 'fourier';
    cfg.method     = 'mtmfft';
    cfg.taper      = 'dpss';
    cfg.tapsmofrq  = 2;
    cfg.keeptrials = 'yes';
    cfg.pad = 2;
    cfg.padtype = 'zero';
    freq    = ft_freqanalysis(cfg, tmpdata);

    cfg           = [];
    cfg.method    = 'granger';
    cfg.granger.sfmethod = 'bivariate';
    grangerflip     = ft_connectivityanalysis(cfg, freq);

Now we plot the results of the original and the flipped version of the same data.

    cfg = [];
    cfg.parameter = 'grangerspctrm';
    cfg.xlim      = [0 40];
    figure; ft_connectivityplot(cfg,granger,grangerflip);

{% include image src="/assets/img/tutorial/salzburg/figure19.png" %}

## Summary and conclusion
