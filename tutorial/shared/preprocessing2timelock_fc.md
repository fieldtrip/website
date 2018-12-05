---
title: Reading the data
---

### Reading the data

Definetrial and preprocessing require the original MEG dataset, which is available from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).
    
    % find the interesting segments of data
    cfg = [];                                                  % empty configuration
    cfg.dataset                 = 'Subject01.ds';              % name of CTF dataset  
    cfg.trialdef.eventtype      = 'backpanel trigger';
    cfg.trialdef.prestim        = 1;
    cfg.trialdef.poststim       = 2;
    cfg.trialdef.eventvalue     = 9;                     
    cfg = definetrial(cfg);            
    
    % preprocess the data
    trl = cfg.trl
    trl([2,3,4,30,39,40,41,45,46,47,51,53,59,77,85],:) = [];           
   % remove the segments that have artifacts
    cfg.channel    = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
    cfg.lpfilter   = 'yes';                              % apply lowpass filter
    cfg.lpfreq     = 35;   
    dataFC2timelock    = preprocessing(cfg);                      

These data have been cleaned from artifacts by removing several trials and two sensors; see [tutorial:visual_artifact_rejection](/tutorial/visual_artifact_rejection). For event related averaging data it is recommended to lowpass de data at 35 Hz (and NOT to detrend!).

Subsequently you can save the data to disk. 

    save dataFC2timelock dataFC2timelock

