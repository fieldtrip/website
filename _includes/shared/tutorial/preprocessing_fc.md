### Reading the FC data

**[Ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)** require the original MEG dataset, which is available from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).

    % find the interesting segments of data
    cfg = [];                                           % empty configuration
    cfg.dataset                 = 'Subject01.ds';       % name of CTF dataset  
    cfg.trialdef.eventtype      = 'backpanel trigger';
    cfg.trialdef.prestim        = 1;
    cfg.trialdef.poststim       = 2;
    cfg.trialdef.eventvalue     = 9;                    % event value of FC
    cfg = ft_definetrial(cfg);            

    % remove the trials that have artifacts from the trl
    cfg.trl([2, 3, 4, 30, 39, 40, 41, 45, 46, 47, 51, 53, 59, 77, 85],:) = [];

    % preprocess the data
    cfg.channel   = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
    cfg.demean    = 'yes';                              % do baseline correction with the complete trial

    dataFC = ft_preprocessing(cfg);

These data have been cleaned from artifacts by removing several trials and two sensors; see the [visual artifact rejection tutorial](/tutorial/visual_artifact_rejection).

Subsequently you can save the data to disk.

    save dataFC dataFC
