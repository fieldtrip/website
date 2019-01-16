---
title: Cleaning and processing resting-state EEG
tags: [eeg-chennu, madrid2019]
---

# Cleaning and processing resting-state EEG

# Introduction
This tutorial has been created for the FieldTrip workshop in Madrid 2019.
It shows how to preprocess and analyse resting state EEG data using the
example of an open access dataset shared by University of Cambridge. You
can click here for details on the dataset.

In this tutorial you will learn how to load and inspect this dataset
using FieldTrip. You will perform some basic preprocessing and finally
you will do a time frequency analysis on the resting state data including
group-level statistics

# Background
Here we will adapt the pipeline described in de Cheveigne & Arzounian
(2018). In there they propose different algorithms to preprocess MEEG
data and importantly they propose rules of thumb on the order of the
application of the algorithms. The following section is taken literally
from the paper:

As a rule of thumb, if algorithm B is sensitive to an artifact that
algorithm A can remove, then A should be applied before B.

A difficulty arises of course if A is also sensitive to artifacts
that B can remove.

A likely sequence might be:
(a) discard pathological channels for which there is no useful signal,
(b) apply robust detrending to each channel,
(c) detect and interpolate temporally-local channel-specific glitches,
(d) robust re-reference,
(e) project out eye artifacts (e.g. using ICA or DSS),
(f) fit and remove, or project out, 50 Hz and harmonics,
(g) project out alpha activity, etc.,
(f) apply linear analysis techniques (ICA, CSP, etc.) to further isolate
activity of interest."

Reference:
Cheveigne & Arzounian(2018) Robust detrending, rereferencing, outlier
detection, and inpainting for multichannel data. Neuroimage 172 (2018)
903-912 https://doi.org/10.1016/j.neuroimage.2018.01.035

# Procedure

In this tutorial the following steps will be taken:

- Read the data into MATLAB using ft_preprocessing and visualize the data in between processsing steps with ft_databrowser
- Interpolate broken channels or noisy data segments with ft_channelrepair, removing artifacts with ft_rejectartifact
- Select relevant segments of data using ft_redefinetrial as well as concatenating data using ft_appenddata
- Once all data is cleaned, correct for eye movement artifacts by running independent component analysis using ft_componentanalysis

# Reading in data

For this tutorial you will require the original open dataset, which you
can download here. Furthermore, some intermediate steps have been
computed for you already, for efficiency. You can download both original
and processed data here: link-to-file

For this tutorial we will lead you through the preprocessing pipelne with
the exsample of one subject.

    subj = 'sub-28';

We will start with minimal preprocessing. Be aware that using
the average reference on data with artifacts can spread contamination
but it definitely enhances the interpretability of the data when
using ft_databrowser (i.e. topoplots)

    cfg = [];
    cfg.dataset    = fullfile('raw_bids',subj,'eeg',[subj '_task-rest_run-1_eeg.vhdr']);
    cfg.channel    = 'all';
    cfg.demean     = 'yes';
    cfg.detrend    = 'no';
    cfg.reref      = 'yes';
    cfg.refchannel = 'all';
    cfg.refmethod  = 'avg';
    data = ft_preprocessing(cfg);

If preprocessing was done as described, the data will have the following
fields

	eeg =
		hdr: [1ÔøΩ1 struct]
	  label: {91ÔøΩ1 cell}
	   time: {[1ÔøΩ102500 double]}
	  trial: {[91ÔøΩ102500 double]}
	fsample: 250
 sampleinfo: [1 102500]
	    cfg: [1ÔøΩ1 struct]

add the electrode description

    data.elec = prepare_elec_chennu2016(data.label);

Using the ft_databrowser we will now visually inspect our data and mark
samples as either blink, bad channel or muscle artifacts. If you haven't
used the databrowser before, read here how to use it
ref:faq/how_can_i_use_the_databrowser

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

{Figure of databrowser}

We manually add to the artifact structure the names of those channels that
we have identified as bad or missing throughout the entire recording.
Many FieldTrip functions, ie ft_channelselection or ft_channelrepair,
which we will use further down take channel names input. For this specify
channel names as strings in a cell array such as {'E7';'Oz'}

    artif.badchannel  = input('write badchannels: ');
    artif.misschannel = input('write missed channels: ');

to save disk space, it is advisable to save the minimal information
and run again the pipeline to reconstruct the data. Here we only will
save the artifacts we identified but not the cleaned eeg data

    save([subj '_task' int2str(f) '_artif.mat'],'artif');

# Interpolating bad channels
    load('sub-28_artif')
    load neighbours

1.- interpolate channels with artifacts during the whole experiment

    cfg = [];
    cfg.badchannel     = artif.badchannel;
    cfg.method         = 'weighted';
    cfg.neighbours     = neighbours;
    data = ft_channelrepair(cfg,data);

{% include markup/info %}
Exercise 1: plot the broken channel before and after interpolation to see
how ft_channelrepair affects the data! Tip: Find the index of the channel
in the eeg.label field and match it to the data in the eeg.trial field.
{% include markup/end %}

2.- select EEG artifacted manual selections with ft_redefinetrial

    artpadding  = 0.1;
    begart      = artif.artfctdef.badchannel.artifact(:,1)-round(artpadding.*data.fsample);
    endart      = artif.artfctdef.badchannel.artifact(:,2)+round(artpadding.*data.fsample);
    begart(begart<1) = 1;
    endart(endart>max(data.sampleinfo(:,2))) = max(data.sampleinfo(:,2));

    cfg     = [];
    cfg.trl = [begart endart zeros(size(endart,1),1)];
    data_bad   = ft_redefinetrial(cfg,data);

You should now have a data structure, that contains the segments of data
you have identified as artifact in the trial field. Each trial will be of
different length. Inspect the fields in your datastructure and compare to
the data structure after reading in with ft_preprocessing.

	data_bad =
		hdr: [1ÔøΩ1 struct]
	  trial: {[91ÔøΩ151 double]  [91ÔøΩ132 double]  [91ÔøΩ135 double]  [91ÔøΩ116 double]  [91ÔøΩ139 double]  [91ÔøΩ230 double]}
	   time: {[1ÔøΩ151 double]  [1ÔøΩ132 double]  [1ÔøΩ135 double]  [1ÔøΩ116 double]  [1ÔøΩ139 double]  [1ÔøΩ230 double]}
	   elec: [1ÔøΩ1 struct]
	fsample: 250
	  label: {91ÔøΩ1 cell}
 sampleinfo: [6ÔøΩ2 double]
	    cfg: [1ÔøΩ1 struct]

3.- identify the channels with the artifacts

parameters to detect artifacts

    proportion	= 0.4; 	% criterion proportion of bad samples
    thresh1		= 3; 		% threshold in units of median absolute value over all data

	data_fixed  = {};
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

        % 4.- use ft_channelrepair to interpolate these brief selected artifacts
        cfg = [];
        cfg.badchannel = data_bad.label([iBad;iBad_a]);
        cfg.method = 'weighted';
        cfg.neighbours = neighbours;
        cfg.trials = k;
        data_fixed{1,k} = ft_channelrepair(cfg,data_bad);
    end
    clear data_bad

After correcting each artifactual trial we can use ft_appenddata to combine trials into one structure again.

	data_fixed = ft_appenddata([],data_fixed{:});

{% include markup/info %}
Exercise 2: Visualize the selected artifacts in data_bad with ft_databrowser
and compare to data_fixed.
{% include markup/end %}

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

In order keep the data as one continous trial we use ft_redefinetrial and the sample information

    cfg = [];
    cfg.trl = [min(data.sampleinfo(:,1)) max(data.sampleinfo(:,2)) 0];
    data = ft_redefinetrial(cfg,data);

5.- check the interpolation results using ft_databrowser

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

# Reject the muscular and visual artifacts
note we do not want to reject blinks because we want to model them
using independent component analysis

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

{% include markup/info %}
Exercise 4: Could be to compare different modes of rejecting artifacts like
partial vs nan etc .
{% include markup/end %}

once all is cleaned, we can reference the data

    cfg            = [];
    cfg.channel    = 'all';
    cfg.demean     = 'yes';
    cfg.reref      = 'yes';
    cfg.refchannel = 'all';
    cfg.refmethod  = 'avg';
    data = ft_preprocessing(cfg,data);

# Add missing channel
Now we will pretend to add an electrode channel to show how
one would add a missing channel using ft_channelrepair
we detect the elec data from missing channel

    missingchannel = {'XXX'};
    missingneigh = {'E55','E79','E78','Pz','E61','E54'};

    [sel1,~] = match_str(data.elec.label,missingneigh);

    data.elec.chanpos(end+1,:) = mean(data.elec.chanpos(sel1,:),1);
    data.elec.elecpos(end+1,:) = mean(data.elec.elecpos(sel1,:),1);
    data.elec.label{end+1,:}   = missingchannel{1};
    data.elec.chanunit{end+1}  = 'V';
    data.elec.chantype{end+1}  = 'eeg';
    clear elec;

update the neighbours representation accordingly
    cfg_neigh = [];
    cfg_neigh.elec = data.elec;
    cfg_neigh.neighbours = neighbours;
    cfg_neigh.neighbours(end+1).label = missingchannel{1};
    cfg_neigh.neighbours(end).neighblabel = missingneigh;

    cfg = [];
    cfg.badchannel = missingchannel{1};
    cfg.method = 'weighted';
    cfg.neighbours = cfg_neigh.neighbours;
    data = ft_channelrepair(cfg,data);

# Eye blink removal with ICA
For the ICA it is best to use as much data as possible. We will therefore
combine data from all tasks/different sedation levels. To save time, we
have preprocessed the remaining data segments for you.

    load('alldata');
    data = alldata;
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
trial 'time','trial' fields because with the topo and unmixing matrix we
can reconstruct everything

    comp = rmfield(comp,{'time','trial'});
    save([subj '_comp.mat'],'-struct','comp');

If you want to skip the ICA, simply load in the pre-computed components
and apply to data

    comp = load('sub-28_comp');

small fix: tell FieldTrip that these are different blocks updating sampleinfo

    nsmp = data.sampleinfo(:,2);
    begsample = cat(1, 0, cumsum(nsmp(1:end-1))) + 1;
    endsample = begsample + nsmp - 1;
    data.sampleinfo = [begsample endsample];

    cfg = [];
    cfg.demean    = 'no'; % This has to be explicitly stated as the default is to demean.
    cfg.unmixing  = comp.unmixing; % Supply the matrix necessay to 'unmix' the channel-series data into components
    cfg.topolabel = comp.topolabel; % Supply the original channel label information
    comp = ft_componentanalysis(cfg, data);

we add the visually indentified artifacts to check which ICs are
sensitive to them

    cfg = [];
    cfg.layout        = ft_prepare_layout([],data);
    cfg.viewmode      = 'component';
    cfg.zlim          = 'maxmin';
    cfg.compscale     = 'local'; % maxmin normalization for each component separately
    cfg.contournum    = 6;
    cfg.artifactalpha = 0.8;
    cfg.artfctdef     = artif.artfctdef;
    ft_databrowser(cfg,comp);

    ic.selected = input('ICs to keep (i.e. [1 5]): ');
    ic.artifact = input('ICs to reject (i.e. [8]): ');

    save([subj '_ic_selection.mat'],'-struct','ic');

    cfg = [];
    cfg.component = ic.artifact;
    data = ft_rejectcomponent(cfg,comp,data);
