The **[ft_definetrial](https://github.com/fieldtrip/fieldtrip/blob/release/ft_definetrial.m)** and **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)** functions require the original MEG dataset, which is available at [ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip)

Do the trial definition for the all conditions together:

    cfg                         = [];
    cfg.dataset                 = 'Subject01.ds';
    cfg.trialfun                = 'ft_trialfun_general'; % this is the default
    cfg.trialdef.eventtype      = 'backpanel trigger';
    cfg.trialdef.eventvalue     = [3 5 9]; % the values of the stimulus trigger for the three conditions
    % 3 = fully incongruent (FIC), 5 = initially congruent (IC), 9 = fully congruent (FC)
    cfg.trialdef.prestim        = 1; % in seconds
    cfg.trialdef.poststim       = 2; % in seconds

    cfg = ft_definetrial(cfg);
