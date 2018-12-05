---
title: Reading the FIC data
---

### Reading the FIC data

The **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)** functions require the original MEG dataset, which is available from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).
    
    % find the interesting segments of data
    cfg = [];                                           % empty configuration
    cfg.dataset                 = 'Subject01.ds';       % name of CTF dataset  
    cfg.trialdef.eventtype      = 'backpanel trigger';
    cfg.trialdef.prestim        = 1;
    cfg.trialdef.poststim       = 2;
    cfg.trialdef.eventvalue     = 3;                    % trigger value for fully incongruent (FIC)
    cfg = ft_definetrial(cfg);            
    
    % remove the trials that have artifacts from the trl
    cfg.trl([15, 36, 39, 42, 43, 49, 50, 81, 82, 84],:) = []; 
    
    % preprocess the data
    cfg.channel    = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
    cfg.demean     = 'yes';
    cfg.baselinewindow  = [-0.2 0];
    cfg.lpfilter   = 'yes';                              % apply lowpass filter
    cfg.lpfreq     = 35;                                 % lowpass at 35 Hz.
    
    dataFIC_LP = ft_preprocessing(cfg);                      

These data have been cleaned from artifacts by removing several trials and two sensors; see the [visual artifact rejection tutorial](/tutorial/visual_artifact_rejection).

Subsequently you can save the data to disk. 

    save dataFIC_LP dataFIC_LP

