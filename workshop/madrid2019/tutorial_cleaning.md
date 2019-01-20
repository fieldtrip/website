---
title: Cleaning and processing resting-state EEG
tags: [eeg-chennu, madrid2019]
---

# Cleaning and processing resting-state EEG

## Introduction
This tutorial has been created for the FieldTrip workshop in Madrid 2019.
It shows how to preprocess and analyse resting state EEG data using the
example of an open access dataset shared by University of Cambridge. You
can click [here for details on the dataset](/workshop/madrid2019/eeg_chennu).
In this tutorial you will learn how to load and inspect this dataset
using FieldTrip. You will perform some basic preprocessing such as
repairing broken channels, visual artifact rejection and artifact
correction using ICA

## Background

Here we will adapt the pipeline described in de Cheveigne & Arzounian
(2018). They propose different algorithms to preprocess MEG or EEG
data and importantly they propose rules of thumb on the order of the
application of the algorithms.

The following is taken from the paper Cheveigne & Arzounian (2018) [Robust detrending, rereferencing, outlier
detection, and inpainting for multichannel data](https://doi.org/10.1016/j.neuroimage.2018.01.035).

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

For this tutorial you will require data from one example subject. Furthermore the original open dataset, some intermediate steps have been
computed for you already, for efficiency. You can download both raw and processed data of the example subject [here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/workshop/madrid2019/tutorial_cleaning/).
If you are interested in the raw data from all subjects, you can download it from our [FTP Server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/workshop/madrid2019/extra/). Please note that you **do not** have to download all subjects for this tutorial.

For this tutorial we will lead you through the preprocessing pipeline with
the example of one subject and on one acquisition run (sedation level).

    subj = 'sub-22';

We will start with minimal preprocessing. Be aware that using
the average reference on data with artifacts can spread contamination
but it definitely enhances the interpretability of the data when
using **[ft_databrowser](/reference/ft_databrowser)** (i.e. topoplots)

    cfg = [];
    cfg.dataset    = ['single_subject_resting/' subj '_task-rest_run-3_eeg.vhdr'];
    cfg.channel    = 'all';
    cfg.demean     = 'yes';
    cfg.detrend    = 'no';
    cfg.reref      = 'yes';
    cfg.refchannel = 'all';
    cfg.refmethod  = 'avg';
    data = ft_preprocessing(cfg);

If preprocessing was done as described, the data will have the following
fields

	data =

		hdr: [1x1 struct]
	      label: {91x1 cell}
	       time: {[1x90000 double]}
	      trial: {[91x90000 double]}
	    fsample: 250
         sampleinfo: [1 90000]
		cfg: [1x1 struct]


add the electrode description. For this we will use a custom script which was included in the downloads folder with the data.

    data.elec = prepare_elec_chennu2016(data.label);

Using the **[ft_databrowser](/reference/ft_databrowser)** we will now visually inspect our data and mark
samples as either blink, bad channel or muscle artifacts. If you haven't
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
    artif = ft_databrowser(cfg,data);

{% include image src="/assets/img/workshop/madrid2019/tutorial_cleaning/fig1_databrowser_init.png" width="800" %}

{% include markup/info %}
Exercise 1: Browse through the segments to get a feel for the data. Do you
see any obvious artifacts? There is one channel carrying several artifacts throughout
the recording, can you find it? Use the identify button to see the channel
name
{% include markup/end %}

{% include image src="/assets/img/workshop/madrid2019/tutorial_cleaning/fig2_databrowser_badchan.png" width="800" %}

We manually add to the artifact structure the names of those channels that
we have identified as bad or missing throughout the entire recording.
Many FieldTrip functions, ie **[ft_channelselection](/reference/ft_channelselection)** or **[ft_channelrepair](/reference/ft_channelrepair)**,
which we will use further down take channel names input. For this specify
channel names as strings in a cell array such as {'E7';'Oz'}

    artif.badchannel  = input('write badchannels: ');
    artif.misschannel = input('write missed channels: ');

to save disk space, it is advisable to save the minimal information
and run again the pipeline to reconstruct the data. Here we have already
saved the artifacts we identified but not the cleaned eeg data. You can
either load the preselected artifact file 'sub-22_run-03_eeg_artif' or continue with your own
selection.

    load('sub-22_run-03_eeg_artif')

## Interpolating bad channels
We will now see two different ways of dealing with noisy channels. One is
to interpolate entire channels. The other way is to interpolate only
segments that contain artifacts.

A definition of neighbouring channels is needed when repairing missing
channels (they will be reconstructed by a weighted average of the
neighbours). FieldTrip already comes with a variety of **[templates for
defining neighbouring channels](/template/neighbours)**. For this dataset we provide this information for you.

    load('cfg_neighbours','neighbours');

1.- interpolate channels with artifacts during the whole experiment

    cfg = [];
    cfg.badchannel     = artif.badchannel;
    cfg.method         = 'weighted';
    cfg.neighbours     = neighbours;
    data_fixed = ft_channelrepair(cfg,data);

For this subject the noisy channel only has a handful of artifacts, so
instead of interpolating an entire channel, we will only interpolate the
noisy segments.

2.- select EEG artifacted manual selections with **[ft_redefinetrial](/reference/ft_redefinetrial)**

    artpadding  = 0.1;
    begart      = artif.artfctdef.badchannel.artifact(:,1)-round(artpadding.*data.fsample);
    endart      = artif.artfctdef.badchannel.artifact(:,2)+round(artpadding.*data.fsample);
    begart(begart<1) = 1;
    endart(endart>max(data.sampleinfo(:,2))) = max(data.sampleinfo(:,2));

    cfg     = [];
    cfg.trl = [begart endart zeros(size(endart,1),1)];
    data_bad   = ft_redefinetrial(cfg,data);

You should now have a data structure data_bad, that contains the segments of data
you have identified as artifact in the trial field. Each trial will be of
different length. Inspect the fields in your datastructure and compare to
the data structure after reading in with **[ft_preprocessing](/reference/ft_preprocessing)**.

	data_bad =

		hdr: [1x1 struct]
	      trial: {[91x395 double]  [91x333 double]}
	       time: {[1x395 double]  [1x333 double]}
	       elec: [1x1 struct]
	    fsample: 250
	      label: {91x1 cell}
         sampleinfo: [2x2 double]
		cfg: [1x1 struct]

3.- identify the channels with the artifacts

parameters to detect artifacts

    proportion = 0.4; % criterion proportion of bad samples
    thresh1 = 3; % threshold in units of median absolute value over all data
    data_fixed = {};
    for k=1:size(data_bad.trial,2)
        % This is de Cheveigne algorithm to detect bad channels. See nt_find_bad_channels.m in Noisetools
        w       = ones(size(data_bad.trial{1,k}));
        md      = median(abs(data_bad.trial{1,k}(:)));
        w(find( abs( data_bad.trial{1,k}) > thresh1 * md ) )=0;
        iBad    = find(mean(1-w,2)>proportion);
        [val iBad_a] = max(max(abs(data_bad.trial{1,k}.*(1-w)),[],2));
        if isempty(iBad)
            iBad=find(mean(1-w,2)==max(mean(1-w,2)));
            warning(['decreasing threshold to: ' num2str(max(mean(1-w,2)))]);
        end

        % 4.- use **[ft_channelrepair](/reference/ft_channelrepair)** to interpolate these brief selected artifacts
        cfg = [];
        cfg.badchannel = data_bad.label([iBad;iBad_a]);
        cfg.method = 'weighted';
        cfg.neighbours = neighbours;
        cfg.trials = k;
        data_fixed{1,k} = ft_channelrepair(cfg,data_bad);
    end

After correcting each artifactual trial we can use **[ft_appenddata](/reference/ft_appenddata)** to
combine trials into one structure again.

    data_fixed = ft_appenddata([],data_fixed{:});

{% include markup/info %}
Exercise 2: Visualize the selected artifacts in data_bad with **[ft_databrowser](/reference/ft_databrowser)**
and compare to data_fixed. You can also just plot the bad channel by
specifying its name in cfg.channel. Or you can use the matlab plot
function. For this you need to find the index of the channel using the
data.label field. Try it!
{% include markup/end %}

    clear data_bad

now delete the badchannel artifacts and append the interpolated data

    cfg                               = [];
    cfg.artfctdef.minaccepttim        = 0.010;
    cfg.artfctdef.reject              = 'partial';
    cfg.artfctdef.badchannel.artifact = [begart endart];
    data_clean = ft_rejectartifact(cfg,data);

    data = ft_appenddata([],data_clean,data_fixed);
    clear data_clean data_fixed;

{% include markup/info %}
Exercise 3: inspect the new data structure. What has changed?
{% include markup/end %}

In order keep the data as one continous trial we use **[ft_redefinetrial](/reference/ft_redefinetrial)** and
the sample information

    cfg = [];
    cfg.trl = [min(data.sampleinfo(:,1)) max(data.sampleinfo(:,2)) 0];
    data = ft_redefinetrial(cfg,data);

5.- check the interpolation results using **[ft_databrowser](/reference/ft_databrowser)**

    cfg = [];
    cfg.viewmode      = 'vertical';
    cfg.artifactalpha = 0.8;
    cfg.blocksize    = 5;

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
note we do not want to reject blinks because we want to model them
using independent component analysis
If you have marked muscular or visual artifacts, you can cut the noisy
segments out like this:

    cfg = [];
    cfg.artfctdef.minaccepttim = 0.010;
    cfg.artfctdef.reject       = 'partial';
    if isfield(artif.artfctdef,'visual')
        cfg.artfctdef.visual.artifact = artif.artfctdef.visual.artifact;
    end
    if isfield(artif.artfctdef,'muscle')
        cfg.artfctdef.muscle.artifact = artif.artfctdef.muscle.artifact;
    end
    data = ft_rejectartifact(cfg,data);

once all is cleaned, we can re-reference the data

    cfg            = [];
    cfg.channel    = 'all';
    cfg.demean     = 'yes';
    cfg.reref      = 'yes';
    cfg.refchannel = 'all';
    cfg.refmethod  = 'avg';
    data = ft_preprocessing(cfg,data);

## Eye blink removal with ICA
For the ICA it is best to use as much data as possible. Therefore at this stage
you should combine data from different runs/conditions etc.

concatenate all trials to compute the rank of the data and constrain
the number of independent components

    dat = [];
    for k=1:size(data.trial,2)
        dat = [dat data.trial{1,k}];
    end
    dat(isnan(dat)) = 0;
    n_ic = rank(dat);

    cfg        = [];
    cfg.method = 'runica';
    cfg.numcomponent = n_ic;
    comp = ft_componentanalysis(cfg, data);

Because computing the independent components can be time consuming, it is
efficient to save the result. In order to reduce disk space we delete
the 'time' & 'trial' fields because with the topo and unmixing matrix we
can reconstruct everything.

    comp = rmfield(comp,{'time','trial'});
    save([subj 'run-03_comp.mat'],'-struct','comp');

You can load the pre-computed topo and unmixing matrix if you don't want to wait for
the ICA to finish. Those have been computed on all four runs (sedation
levels) combined

    comp = load([subj,'_comp']);

    cfg = [];
    cfg.demean    = 'no'; % This has to be explicitly stated as the default is to demean.
    cfg.unmixing  = comp.unmixing; % Supply the matrix necessay to 'unmix' the channel-series data into components
    cfg.topolabel = comp.topolabel; % Supply the original channel label information
    comp = ft_componentanalysis(cfg, data);

we add the visually indentified artifacts to check which ICs are
sensitive to them

    data.elec = prepare_elec_chennu2016(data.label);
    cfg = [];
    cfg.layout        = ft_prepare_layout([],data);
    cfg.viewmode      = 'component';
    cfg.zlim          = 'maxmin';
    cfg.compscale     = 'local'; % maxmin normalization for each component separately
    cfg.contournum    = 6;
    cfg.artifactalpha = 0.8;
    cfg.artfctdef     = artif.artfctdef;
    ft_databrowser(cfg,comp);

{% include image src="/assets/img/workshop/madrid2019/tutorial_cleaning/fig3_ica.png" width="800" %}


    ic.selected = input('ICs to keep (i.e. [1 5]): ');
    ic.artifact = input('ICs to reject (i.e. [8]): ');

    save([subj '_ic_selection.mat'],'-struct','ic');

    cfg = [];
    cfg.component = ic.artifact;
    data = ft_rejectcomponent(cfg,comp,data);

{% include markup/info %}
Exercise 4: Use **[ft_databrowser](/reference/ft_databrowser)** one last time to view the cleaned data. Did
the ICA successfully correct all eye blinks?
{% include markup/end %}
