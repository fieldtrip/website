### Reading the IC data

The **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)** functions require the original MEG dataset, which is available from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).
    
    % find the interesting segments of data
    cfg = [];                                           % empty configuration
    cfg.dataset                 = 'Subject01.ds';       % name of CTF dataset  
    cfg.trialdef.eventtype      = 'backpanel trigger';
    cfg.trialdef.prestim        = 1;
    cfg.trialdef.poststim       = 2;
    cfg.trialdef.eventvalue     = 5;                    % trigger value for initially congruent (IC)
    cfg = ft_definetrial(cfg);            
    
    % remove the trials that have artifacts from the trl
    cfg.trl([1, 2, 3, 4, 14, 15, 16, 17, 20, 35, 39, 40, 47, 78, 79, 80, 86],:) = []; 
    
    % preprocess the data
    cfg.channel    = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
    cfg.demean     = 'yes';
    cfg.baselinewindow  = [-0.2 0];
    cfg.lpfilter   = 'yes';                              % apply lowpass filter
    cfg.lpfreq     = 35;                                 % lowpass at 35 Hz.
    
    dataIC_LP = ft_preprocessing(cfg);                      

These data have been cleaned from artifacts by removing several trials and two sensors; see the [visual artifact rejection tutorial](/tutorial/visual_artifact_rejection).

Subsequently you can save the data to disk. 

    save dataIC_LP dataIC_LP

