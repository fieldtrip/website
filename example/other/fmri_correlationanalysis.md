---
title: Correlation analysis of fMRI data
category: example
tags: [fmri, raw, freq, coherence]
redirect_from:
    - /example/correlation_analysis_in_fmri_data/
    - /example/fmri_correlationanalysis/
---

# Correlation analysis of fMRI data

This script demonstrates how FieldTrip can be used for time-series analysis of fMRI data.

## Get the data in a "raw" data structure, similar to preprocessed MEG data

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % contruct the projection matrix for the ROIs
    load aal_new_mat
    aal = ft_read_mri('aal_new.hdr')
    project = zeros(length(ROI), prod(aal.dim));
    for i=1:length(ROI)
      disp(i);
      project(i,:) = double(aal.anatomy(:)==ROI(i).ID);
      project(i,:) = project(i,:)./sum(project(i,:));
    end
    project = sparse(project);

    mri = ft_read_mri('bwamarspr_rs_sess01_vol0001.nii');

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % read the data and put into a FT structure
    session = {
    'sess01'
    'sess02'
    'sess03'
    'sess04'
    'sess05'
    'sess06'
    'sess07'
    'sess08'
    'sess09'
    'sess10'
    'sess11'
    'sess12'
    };

    raw = [];
    raw.fsample  = 1/1.35;
    raw.label    = {ROI.Nom_L}';

    for s=1:length(session)
    path = session{s}
    filename = dir(path);
    filename = {filename(~[filename.isdir]).name}';
    for i=1:length(filename)
      filename{i} = fullfile(path, filename{i});
    end

    dat = zeros(length(ROI), length(filename));
    for i=1:length(filename)
      disp(i);
      tmp = ft_read_mri(filename{i});
      dat(:,i) = project * tmp.anatomy(:);
    end

    raw.time{s}  = (0:(size(dat,2)-1)) ./ raw.fsample;
    raw.trial{s} = dat;
    end % for session

    save project project -v6
    save mri mri -v6
    save raw raw -v6

## Apply frequency analysis, compute frequency specific correlation/coherence

    cfg = [];
    cfg.blc = 'yes';
    cfg.keeptrials = 'yes';
    timelock = ft_timelockanalysis(cfg, raw);

    winsize = 64;
    fr = (256/winsize)./timelock.time(end);

    cfg = [];
    cfg.method     = 'mtmwelch';
    cfg.output     = 'powandcsd';
    cfg.taper      = 'hanning';
    cfg.channel    = 'all';
    cfg.channelcmb = {'all', 'all'};
    cfg.foi        = 0:fr:(raw.fsample/2)
    cfg.toi        = raw.time{1}((winsize/2):winsize:256);
    cfg.tapsmofrq  = nan * ones(size(cfg.foi));
    cfg.t_ftimwin  = winsize/raw.fsample * ones(size(cfg.foi));
    cfg.keeptrials = 'no';
    cfg.keeptapers = 'no';
    cfg.pad        = 'maxperlen';
    freq = ft_freqanalysis(cfg, timelock);

    cfg = [];
    % cfg.complex = 'abs';
    cfg.complex = 'real';
    fd = ft_freqdescriptives(cfg, freq);

    cfg = [];
    cfg.layout = 'ordered';
    lay = ft_prepare_layout(cfg, fd);

    cfg = [];
    cfg.layout = lay;
    cfg.interactive = 'yes';
    cfg.showlabels = 'yes';
    figure; ft_multiplotER(cfg, fd);

    cfg = [];
    cfg.layout = lay;
    cfg.interactive = 'yes';
    cfg.showlabels = 'yes';
    cfg.zparam = 'cohspctrm';
    cfg.zlim = [0 1];
    cfg.cohrefchannel = fd.label{1};
    figure; ft_multiplotER(cfg, fd);
