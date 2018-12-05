---
title: Use DSS to remove ECG/BCG artifacts within ft_componentanalysis
---

{% include /shared/development/warning.md %}

## Use DSS to remove ECG/BCG artifacts within ft_componentanalysis

### Description

This script demonstrates how you can use DSS for cleaning the BCG artifacts from your EEG data. It consists of three step
 1.  performing optimal peak detection on the independent ECG channel
 2.  selecting number of components to remove from EEG data
 3.  removing those components and backprojecting the data

You may download the external [DSS toolbox here](http://www.cis.hut.fi/projects/dss).   

How does DSS work to find the components to remove?  You give it the time points of the peaks, and time windows of set length before/after this peak (you can obtain these easily by calling ft_artifact_zvalue).  After concatenating trials into one vector (hence matrix of channels x time) the data is sphered.  For each component, it initializes by projecting the sphered data onto a random basis [randn(1,Nchan)*sphered_data]. If it is solving for the second or later component, this weight is orthogonalized with respect to all previously found weights for previously computed components. The average template of the artifact in the time windows around the peaks is computed, with zeros elsewhere. (This step was modified to respect trial boundaries, i.e. if a time window around a peak goes off the edge of a trial).  The weighting of sphered data to obtain this repeated template is computed (and re-orthogonalized if component 2 or greater) and normed. Iterate until weights not change much and save.

### Example dataset

You can run the code below on your own data. Alternatively, try with the example EEG dataset [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/callmesomething.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/callmesomething.zip). All figures in this example script are based on these data.   (Note*** just a placeholder at the moment, this data does not exist yet.***)

To load this dataset into matlab and preprocess with FieldTrip, us


	% ft_preprocessing of example dataset
	cfg = [];
	cfg.dataset = 'ArtifactRemoval.ds';
	cfg.trialdef.eventtype = 'trial';
	cfg = ft_definetrial(cfg);

### ECG peak detection

We can use ft_artifact_zvalue.  Apply preproc to the ECG channel, and use some cfg options to obtain the peak time point above threshold within a certain time range (rather than all values above threshold), and furthermore, set a fixed time-range around this peak.
Filter the ECG channel to optimize separation of a single peak per heartbeat relative to other waves.  This will be different per subject.  One possible/recommended way for BCG is a combination of drift-removal (bandpass 5-30Hz) and then the Hilbert envelope of this.


	cfg=[];
	cfg.artfctdef.zvalue.channel='ECG';
	cfg.artfctdef.zvalue.cutoff=2;
	cfg.artfctdef.zvalue.interactive = 'yes';
	cfg.artfctdef.zvalue.bpfilter='yes';
	cfg.artfctdef.zvalue.bpfreq=[5 30];
	cfg.artfctdef.zvalue.hilbert='yes';
	cfg.artfctdef.zvalue.artfctpeak='yes';
	cfg.artfctdef.zvalue.artfctpeakrange=[-.25 .5]; % save out 250ms prior and 500ms post ECG peak
	cfg=ft_artifact_zvalue(cfg,rawcleanrere);

The DSS code wants a 'params' structure which contains peak time points, as well as the range around the peak that you think is relevant.  Note that the subfield 'dssartifact' is different from 'artifact' in 2 ways: 1) beginning/end points based on cfg.artfctdef.zvalue.artfctpeakrange rather than where the channel exceeded the threshold, and 2) the sample counts between trial end to the start of next trial have been subtracted.


	params.tr=cfg.artfctdef.zvalue.peaks;
	params.tr_begin=cfg.artfctdef.zvalue.dssartifact(:,1);
	params.tr_end=cfg.artfctdef.zvalue.dssartifact(:,2);

### DSS component rejection


	addpath ~/mfiles/dss_1-0

	cfg                   = [];
	cfg.method            = 'dss';
	cfg.dss.denf.function = 'denoise_avgJM';
	cfg.dss.denf.params   = params;
	cfg.numcomponent      = 15; % choose here optimal for your dataset!!
	% cfg.channel           = {'all', '-ECG'};
	cfg.channel           = {'all'}; % Is it better to include ECG in DSS or not??
	compdss               = ft_componentanalysis(cfg, rawcleanrere);

The output compdss contains the components to reject.  Use ft_databrowser to plot all components at once and decide if you have selected the correct scfg.numcomp to reject.  Iterate if needed until it appears that all components rejected are heartbeat related.   Usually 10-15 is the right range for 64 channel EEG data in the MRI.


	cfg = [];
	cfg.layout = 'EEG1010.lay'; % specify the layout file that should be used for plotting
	cfg.showcallinfo='no';
	ft_databrowser(cfg,compdss);

Once you are happy with the number of components to reject, then actually remove them from the data.


	cfg           = [];
	cfg.component = 1:size(compdss.topo,2);
	cfg.feedback  = 'textbar';
	rawdssrej     = ft_rejectcomponent(cfg, compdss, rawcleanrere);
