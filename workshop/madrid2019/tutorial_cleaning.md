---
title: Cleaning and processing resting-state EEG
tags: [madrid2019, eeg-chennu]
---

# Cleaning and processing resting-state EEG

## Introduction

This tutorial shows how to preprocess and analyze resting state EEG data using
an open access resting state EEG dataset that is shared by the University of
Cambridge. You can click [here](/workshop/madrid2019/eeg_chennu) for details on
the dataset. In this tutorial you will learn how to load and inspect this
dataset using FieldTrip. You will perform some basic preprocessing such as
repairing broken channels, visual artifact rejection and artifact correction
using ICA.

## Background

We will adapt the pipeline described in de Cheveigne & Arzounian (2018). They
discuss different algorithms to preprocess MEG or EEG data and - importantly -
they propose rules of thumb regarding the order which which these preprocessing
steps are applied.

The following is taken directly from the paper Cheveigne & Arzounian (2018)
[Robust detrending, rereferencing, outlier detection, and inpainting for
multichannel data](https://doi.org/10.1016/j.neuroimage.2018.01.035).

*As a rule of thumb, if algorithm B is sensitive to an artifact that
algorithm A can remove, then A should be applied before B. A difficulty
arises of course if A is also sensitive to artifacts that B can remove.*

A likely sequence might be:

1. discard pathological channels for which there is no useful signal,
2. apply robust detrending to each channel,
3. detect and interpolate temporally-local channel-specific glitches,
4. robust re-reference,
5. project out eye artifacts (e.g. using ICA or DSS),
6. fit and remove, or project out, 50 Hz and harmonics,
7. project out alpha activity, etc.,
8. apply linear analysis techniques (ICA, CSP, etc.) to further isolate activity of interest.


## Procedure

In this tutorial the following steps will be taken:

- Read the data into MATLAB using **[ft_preprocessing](/reference/ft_preprocessing)** and visualize the data in between processsing steps with **[ft_databrowser](/reference/ft_databrowser)**
- Interpolate broken channels or noisy data segments with **[ft_channelrepair](/reference/ft_channelrepair)**, removing artifacts with **[ft_rejectartifact](/reference/ft_rejectartifact)**
- Select relevant segments of data using **[ft_redefinetrial](/reference/ft_redefinetrial)** as well as concatenating data using **[ft_appenddata](/reference/ft_appenddata)**
- Once all data is cleaned, correct for eye movement artifacts by running independent component analysis using **[ft_componentanalysis](/reference/ft_componentanalysis)**

## Reading in data

For this tutorial we will use data from one example subject. The dataset that has been shared does not consist of the original recordings; the data has been imported and some preprocessing steps have been performed already. You can download both raw and processed data of the example subject [here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/workshop/madrid2019/tutorial_cleaning/).
If you are interested in the raw data from all subjects, you can download it from our [FTP Server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/workshop/madrid2019/extra/). Please note that you **do not** have to download all subjects for this tutorial.

For this tutorial we will lead you through the preprocessing pipeline with
the example of one subject and for one experimental block (i.e. level of sedation).

    subj = 'sub-22';

We will start with some minimal preprocessing. Be aware that using the average
reference on data that still has artifactual channels can spread the
contamination of those channels to all other channels. The average reference
does enhance the interpretability of the data when using
**[ft_databrowser](/reference/ft_databrowser)** (i.e. topoplots)

    cfg = [];
    cfg.dataset    = ['single_subject_resting/' subj '_task-rest_run-3_eeg.vhdr'];
    cfg.channel    = 'all';
    cfg.demean     = 'yes';
    cfg.detrend    = 'no';
    cfg.reref      = 'yes';
    cfg.refchannel = 'all';
    cfg.refmethod  = 'avg';
    data = ft_preprocessing(cfg);

Following preprocessing, the data will have the following fields

    data =

           hdr: [1x1 struct]
         label: {91x1 cell}
          time: {[1x90000 double]}
         trial: {[91x90000 double]}
       fsample: 250
    sampleinfo: [1 90000]
           cfg: [1x1 struct]


Subsequently we will add the electrode description. For this we will use a custom script which is included with the data on the FTP server.

    data.elec = prepare_elec_chennu2016(data.label);

Using the **[ft_databrowser](/reference/ft_databrowser)** we will now visually inspect our data and mark
samples as either blinks, bad channel or muscle artifacts. If you haven't
used the databrowser before, read [here how to use it](/faq/how_can_i_use_the_databrowser).

    cfg = [];
    cfg.channel       = 'all';
    cfg.layout        = ft_prepare_layout([],data);
    cfg.viewmode      = 'vertical';
    cfg.blocksize     = 5;
    cfg.artifactalpha = 0.8;  % this make the colors less transparent and thus more vibrant
    cfg.artfctdef.blinks.artifact     = [];
    cfg.artfctdef.badchannel.artifact = [];
    cfg.artfctdef.muscle.artifact     = [];
    artif = ft_databrowser(cfg, data);

{% include image src="/assets/img/workshop/madrid2019/tutorial_cleaning/fig1_databrowser_init.png" width="800" %}

##### Exercise 1

{% include markup/info %}
Browse through the segments to get a feel for the data. Do you see any obvious
artifacts? There is one channel carrying several artifacts throughout the
recording, can you find it? Use the identify button to see the channel name.
{% include markup/end %}

{% include image src="/assets/img/workshop/madrid2019/tutorial_cleaning/fig2_databrowser_badchan.png" width="800" %}

We manually add the names of channels that are bad throughout the entire
recording to the artifact structure. Many FieldTrip functions, ie
**[ft_channelselection](/reference/ft_channelselection)** or
**[ft_channelrepair](/reference/ft_channelrepair)**, which we will use further
down take channel names input. For this specify channel names as strings in a
cell array such as {'E7';'Oz'}

    artif.badchannel  = input('write badchannels: ');
    artif.misschannel = input('write missed channels: ');

to save disk space and to prevent doing the same interactive work twice, it is
advisable to save the minimal information and run the pipeline again to
reconstruct the data. Here we have already saved the artifacts we identified but
not the cleaned EEG data. You can either load the preselected artifact file
'sub-22_run-03_eeg_artif' or continue with your own selection.

    load('sub-22_run-03_eeg_artif')

## Interpolating bad channels

We will now explore two different ways of dealing with noisy channels. One is
to interpolate entire channels. The other way is to interpolate only
segments that contain artifacts.

We repair channels by interpolation, or more precisely: by replacing the bad
channel with the average of the neighbouring channels. This requires a
definition of neighbouring channels. FieldTrip comes with a variety of
**[templates for defining neighbouring channels](/template/neighbours)**. For
this dataset we provide this information for you, but in general you know your
own EEG system and your own data the best and you should therefore think about
your own neighbours structure. See also the
**[ft_prepare_neighbours](/reference/ft_prepare_neighbours)** function.

    load('cfg_neighbours', 'neighbours');

### Interpolate channels that are bad during the whole experiment

    cfg = [];
    cfg.badchannel     = artif.badchannel;
    cfg.method         = 'weighted';
    cfg.neighbours     = neighbours;
    data_fixed = ft_channelrepair(cfg,data);

For this subject the noisy channel only has a handful of artifacts, so
instead of interpolating an entire channel, we will only interpolate the
noisy segments.

### Interpolate bad channels for for specific segments

We can make a selection of the segments in which one of the channels was bad.

    artpadding  = 0.1;
    begart      = artif.artfctdef.badchannel.artifact(:,1)-round(artpadding.*data.fsample);
    endart      = artif.artfctdef.badchannel.artifact(:,2)+round(artpadding.*data.fsample);
    offset      = zeros(size(endart));
    % do not go before the start of the recording or the end
    begart(begart<1) = 1;
    endart(endart>max(data.sampleinfo(:,2))) = max(data.sampleinfo(:,2));

    cfg      = [];
    cfg.trl  = [begart endart offset];
    data_bad = ft_redefinetrial(cfg, data);

You should now have a data structure data_bad, that contains the segments of
data you have identified as artifact in the trial field. Note that each bad
segment and hence each trial will be of different length. Inspect the fields in
your data structure and compare them to the original data structure.

    data_bad =

           hdr: [1x1 struct]
         trial: {[91x395 double]  [91x333 double]}
          time: {[1x395 double]  [1x333 double]}
          elec: [1x1 struct]
       fsample: 250
         label: {91x1 cell}
    sampleinfo: [2x2 double]
           cfg: [1x1 struct]

Subsequently we identify the channels with the artifacts using the algorithm by de Cheveigne (see nt_find_bad_channels.m in Noisetools). The parameters to detect artifacts are

{% include markup/danger %}
The following (rather complicated) piece of code is a mix of regular MATLAB code
with FieldTrip functions. If it is useful, we might add it to one of the
FieldTrip functions later to make it easier to use.
{}% include markup/end %}

    proportion  = 0.4; % criterion proportion of bad samples
    thresh1     = 3;   % threshold in units of median absolute value over all data
    data_fixed  = {};
    for k=1:size(data_bad.trial,2)
        w            = ones(size(data_bad.trial{1,k}));
        md           = median(abs(data_bad.trial{1,k}(:)));
        w(find(abs(data_bad.trial{1,k}) > thresh1*md)) = 0;
        iBad         = find(mean(1-w,2)>proportion);
        [val iBad_a] = max(max(abs(data_bad.trial{1,k}.*(1-w)),[],2));
        if isempty(iBad)
            iBad     = find(mean(1-w,2)==max(mean(1-w,2)));
            warning(['decreasing threshold to: ' num2str(max(mean(1-w,2)))]);
        end

        % we use ft_channelrepair to interpolate these short selected artifacts
        cfg = [];
        cfg.badchannel = data_bad.label([iBad;iBad_a]);
        cfg.method     = 'weighted';
        cfg.neighbours = neighbours;
        cfg.trials     = k;
        data_fixed{1,k} = ft_channelrepair(cfg, data_bad);
    end

After correcting each artifactual trial we can use **[ft_appenddata](/reference/ft_appenddata)** to
combine trials into one structure again.

    data_fixed = ft_appenddata([], data_fixed{:});

##### Exercise 2

{% include markup/info %}
Visualize the selected artifacts in data_bad with
**[ft_databrowser](/reference/ft_databrowser)** and compare it to data_fixed.
You can also just plot the bad channel by specifying its name in cfg.channel. Or
you can use the standard MATLAB plot function. For this you need to find the
index of the channel using the `data.label` field.
{% include markup/end %}

    clear data_bad

Returning to the original data, we now delete the segments that contain
artifacts and append the fixed data.

    cfg                               = [];
    cfg.artfctdef.minaccepttim        = 0.010;
    cfg.artfctdef.reject              = 'partial';
    cfg.artfctdef.badchannel.artifact = [begart endart];
    data_rejected = ft_rejectartifact(cfg, data);

    data = ft_appenddata([], data_rejected, data_fixed);

    % clear these variables from memory to avoid confusion later on
    clear data_rejected data_fixed

##### Exercise 3

{% include markup/info %}
Inspect the new data structure. What has changed?
{% include markup/end %}

In order keep the data as one continous trial we use **[ft_redefinetrial](/reference/ft_redefinetrial)** and
the sample information

    cfg = [];
    cfg.trl = [min(data.sampleinfo(:,1)) max(data.sampleinfo(:,2)) 0];
    data = ft_redefinetrial(cfg,data);

# Visualize the results of channel interpolation

We can use **[ft_databrowser](/reference/ft_databrowser)** to check the results of the interpolation.

    cfg = [];
    cfg.viewmode      = 'vertical';
    cfg.artifactalpha = 0.8;
    cfg.blocksize     = 5;

    if isfield(artif.artfctdef,'badchannel')
        cfg.artfctdef.badchannel.artifact = artif.artfctdef.badchannel.artifact;
    end
    if isfield(artif.artfctdef,'visual')
        cfg.artfctdef.visual.artifact     = artif.artfctdef.visual.artifact;
    end
    if isfield(artif.artfctdef,'muscle')
        cfg.artfctdef.muscle.artifact     = artif.artfctdef.muscle.artifact;
    end
    ft_databrowser(cfg,data);

## Reject the muscular and visual artifacts

Eye movements and blinks cause artifacts in the EEG data because the retina
(which is electrically charged) moves when the subject blinks. The contribution
of eye artifacts to the EEG data can be estimated and removed with independent
component analysis (ICA). If you have marked muscular or visual artifacts, you
can cut the noisy segments out like this:

    cfg = [];
    cfg.artfctdef.minaccepttim = 0.010;
    cfg.artfctdef.reject       = 'partial';
    if isfield(artif.artfctdef,'visual')
        cfg.artfctdef.visual.artifact = artif.artfctdef.visual.artifact;
    end
    if isfield(artif.artfctdef,'muscle')
        cfg.artfctdef.muscle.artifact = artif.artfctdef.muscle.artifact;
    end
    data = ft_rejectartifact(cfg, data);

Once all is cleaned, we can re-reference the data

    cfg            = [];
    cfg.channel    = 'all';
    cfg.demean     = 'yes';
    cfg.reref      = 'yes';
    cfg.refchannel = 'all';
    cfg.refmethod  = 'avg';
    data = ft_preprocessing(cfg, data);

## Eye artifact removal with ICA

For estimating the ICA components it is best to use as much data as possible.
Also, the spatial distribution of the eye artifacts will not be different in the
different experimental conditions. To improve the estimate and to make sure that
you are removing the same eye activity in all conditions,  you should combine
data from the different runs/conditions.

We concatenate all trials into one matrix to compute the rank of the data, this
helps to constrain the number of independent components.

    dat = cat(2, data.trial{:});
    dat(isnan(dat)) = 0;
    n_ic = rank(dat);

    cfg = [];
    cfg.method       = 'runica';
    cfg.numcomponent = n_ic;
    comp = ft_componentanalysis(cfg, data);

Because computing the independent components can be time consuming, it is
efficient to save the result. To reduce disk space we delete the 'time' &
'trial' fields because with the topo and unmixing matrix we can reconstruct
everything.

{% include markup/danger %}
In general we recommend to **not** change the FieldTrip structures. It increases
the chances of accidental data corruption and errors later in your analysis
pipeline.
{% include markup/end %}

    comp = rmfield(comp, 'time');
    comp = rmfield(comp, 'trial');
    save([subj 'run-03_comp.mat'], '-struct', 'comp');

You can load the pre-computed topo and unmixing matrix if you do not want to
wait for the ICA to finish. Those have been computed on all four runs (sedation
levels) combined. Using the pre-computed topo and unmixing matrix, we can
quickly reconstruct the effect of the ICA unmixing.

    comp = load([subj,'_comp']);

    cfg = [];
    cfg.demean    = 'no';           % This has to be explicitly stated, as the default is to demean.
    cfg.unmixing  = comp.unmixing;  % Supply the matrix necessay to 'unmix' the channel-series data into components
    cfg.topolabel = comp.topolabel; % Supply the original channel label information
    comp = ft_componentanalysis(cfg, data);

We add the visually indentified artifacts to check which ICs are sensitive to
them.

    data.elec = prepare_elec_chennu2016(data.label);

    cfg = [];
    cfg.layout        = ft_prepare_layout([],data);
    cfg.viewmode      = 'component';
    cfg.zlim          = 'maxmin';
    cfg.compscale     = 'local'; % scale each component separately
    cfg.contournum    = 6;
    cfg.artifactalpha = 0.8;
    cfg.artfctdef     = artif.artfctdef;
    ft_databrowser(cfg, comp);

{% include image src="/assets/img/workshop/madrid2019/tutorial_cleaning/fig3_ica.png" width="800" %}

    ic.selected = input('ICs to keep (i.e. [1 5]): ');
    ic.artifact = input('ICs to reject (i.e. [8]): ');

    save([subj '_ic_selection.mat'],'-struct','ic');

    cfg = [];
    cfg.component = ic.artifact;
    data = ft_rejectcomponent(cfg, comp, data);

##### Exercise 4

{% include markup/info %}
Use **[ft_databrowser](/reference/ft_databrowser)** one last time to view the
cleaned data. Did the ICA successfully correct all eye blinks?
{% include markup/end %}

## See also

A more general overview of dealing with artifacts is provided in the [artifact tutorial](/tutorial/artifacts).
