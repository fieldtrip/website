---
layout: default
---

### Reading the data

Definetrial and preprocessing require the original MEG dataset, which is available from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).
    
    % find the interesting segments of data
    cfg = [];                                                  % empty configuration
    cfg.dataset                 = 'Subject01.ds';              % name of CTF dataset  
    cfg.trialdef.eventtype      = 'backpanel trigger';
    cfg.trialdef.prestim        = 1;
    cfg.trialdef.poststim       = 2;
    cfg.trialdef.eventvalue     = 3;                     
    cfg = definetrial(cfg);            
    
    % preprocess the data
    cfg.trl([15, 36, 39, 42, 43, 49, 50, 81, 82, 84],:) = [];  % remove the segments that have artifacts
    cfg.channel = {'MEG', '-MLP31', '-MLO12'};                 % read all MEG channels except MLP31 and MLO12
    cfg.detrend = 'yes';   
    dataFIC = preprocessing(cfg);                      

These data have been cleaned from artifacts by removing several trials and two sensors; see [tutorial:rejectvisual](/tutorial/rejectvisual). For time-frequency analysis of power it is recommended to 'detrend' each trial (removes the DC offset and linear trend).

Subsequently you can save the data to disk. 

    save dataFIC dataFIC

