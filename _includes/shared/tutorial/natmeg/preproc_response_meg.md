## Preprocessing MEG

The first step is to read the data using the function **[ft_preprocessing](/reference/ft_preprocessing)**. With the aim to reduce boundary effects occurring at the start and the end of the trials, it is recommended to read larger time intervals than the time period of interest. In this example, the time of interest is from -1.0 s to 1.5 s (t = 0 s defines the time of response); however, the script reads the data from -1.5 s to 2.0 s.

As with the previous preprocessing tutorial, we will preprocess the MEG and EEG data separately. We will start with MEG magnetometers, then move to EEG before looking at the planar gradiometers in MEG.

The MEG dataset that we use in this tutorial is available as  [oddball1_mc_downsampled.fif](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/natmeg/oddball1_mc_downsampled.fif) from our ftp server. Furthermore, you should download and save the custom trial function [trialfun_oddball_responselocked.m](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/natmeg/trialfun_oddball_responselocked.m) to a directory that is on your MATLAB path.

### Read trials

    cfg = [];
    cfg.dataset = 'oddball1_mc_downsampled.fif';
    cfg.channel = 'MEG';

    % define trials based on responses
    cfg.trialdef.prestim       = 1.5;
    cfg.trialdef.poststim      = 2.0;
    cfg.trialdef.stim_triggers = [1 2];
    cfg.trialdef.rsp_triggers  = [256 4096];
    cfg.trialfun               = 'trialfun_oddball_responselocked';
    cfg                        = ft_definetrial(cfg);

    % preprocess MEG data
    cfg.continuous             = 'yes';
    cfg.demean                 = 'yes';
    cfg.dftfilter              = 'yes';
    cfg.dftfreq                = [50 100];

    data_MEG_responselocked    = ft_preprocessing(cfg);

    % write data to disk
    save data_MEG_responselocked data_MEG_responselocked -v7.3

### Clean data

At this stage in the processing pipeline you could remove bad trials using, for example, [ft_rejectvisual](/reference/ft_rejectvisual). We are going to skip this for now as we do not have a lot of trials for this part of the analysis and the data is relatively clean. Furthermore, be aware that removing trials in this way could create a bias towards removing more trials in one condition than in the other due to differences in variance between the conditions.
