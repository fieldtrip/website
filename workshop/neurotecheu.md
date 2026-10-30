---
title: NeurotechEU hackathon - wearable neurotechnology with fNIRS and EEG 
tags: [neurotecheu, eeg-audodd]
---

As part of the NeurotechEU hackathon, we will do an online workshop on the processing of EEG data. Participants will learn how to do offline processing of EEG data. We will ill start with a short discussion on common EEG file formats, followed by importing the data in MATLAB or Python, quality assurance, bad channel and segment removal, re-referencing, filtering, ICA cleaning, event detection, segmenting, and estimation of event-related responses and/or oscillatory activity. Participants will learn the characteristics of raw EEG signals, recognize and deal with common artifacts, and extract interpretable brain signals.

- When: Friday, October 30 from 11:45 – 13:00
- Where: online on Teams
- Who: Robert Oostenveld will present this part of the hackathon

This page serves to provide the links to the documentation, datasets, and software used.

## Download and install FieldTrip

To get a recent copy of FieldTrip, you can follow this [link](https://github.com/fieldtrip/fieldtrip/releases/tag/20261022), download the zip-file, and unzip it at a convenient location on your laptop's hard drive. Alternatively, you could do the following in the MATLAB command window.

    % create a folder that will contain the code and the data, and change directory
    mkdir('neurotecheu');
    cd('neurotecheu');

    % download and unzip fieldtrip into the newly created folder
    url_fieldtrip = 'https://github.com/fieldtrip/fieldtrip/archive/refs/tags/20261022.zip';
    unzip(url_fieldtrip);

Upon completion of this step, the folder structure should look something like this:

```bash
fieldtrip-20261022/
|-- bin
|-- compat
|-- connectivity
|-- contrib
|-- external
|-- fileio
|-- forward
|-- inverse
|-- plotting
|-- preproc
|-- private
|-- qsub
|-- realtime
|-- specest
|-- src
|-- statfun
|-- template
|-- test
|-- trialfun
`-- utilities
```

{% include markup/red %}
If you have downloaded and unzipped by hand, it could be that there's an 'extra folder layer' in your directory structure. We recommend that you remove this extra layer, i.e. move all content one level up.
{% include markup/end %}

## Set up MATLAB and FieldTrip

If you from now on - that is for the duration of the hackathon - *ALWAYS* execute the following steps after starting a fresh MATLAB session, you should be all good to go:

    % change into the 'neurotecheu' folder and then do the following
    restoredefaultpath
    addpath('fieldtrip-20261022')
    ft_defaults

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath` statement adds the `fieldtrip-20261022` directory, i.e. the directory containing the FieldTrip main functions. The other `addpath` statement tells MATLAB where to find the relevant data, and the `ft_defaults` command ensures that all of FieldTrip's required subdirectories are added to the path.

{% include markup/red %}
In general, please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using a startup.m file than the path GUI. You can find more information about startup files in the MATLAB documentation.

Furthermore, please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/matlab/installation).
{% include markup/end %}

## Download the tutorial data

Next, we proceed with downloading the tutorial data. We will use a task EEG dataset recorded in an [auditory oddball](/workshop/natmeg2014/meg_audodd) experiment. You can download the data from our [download server](https://download.fieldtriptoolbox.org/workshop/neurotecheu/) or use the MATLAB code below.

    % cd('neurotecheu'); % in case you moved somewhere else

    mkdir('data')
    cd('data')

    filelist = {
        'oddball1_mc_downsampled_aux.eeg'
        'oddball1_mc_downsampled_aux.vhdr'              
        'oddball1_mc_downsampled_aux.vmrk'                
        'oddball1_mc_downsampled_eeg.eeg'            
        'oddball1_mc_downsampled_eeg.vhdr'               
        'oddball1_mc_downsampled_eeg.vmrk'   
    };
    downloadurl = 'https://download.fieldtriptoolbox.org/workshop/neurotecheu/';

    for i=1:length(filelist)
        fprintf('downloading %s\n', filelist{i});
        websave(filelist{i}, fullfile(downloadurl, filelist{i}));
    end

More details on the experiment and recording can be found [here]((/workshop/natmeg2014/meg_audodd), but the most important are the following trigger codes that are used in the analysis:

- Onset of standard stimulus: 1
- Onset of oddball stimulus: 2
- Button-press onset of left hand: 256
- Button-press onset of right hand: 4096

## Example analysis script

### Exploring the raw data

```matlab
cfg = [];
cfg.dataset = 'oddball1_mc_downsampled_eeg.eeg';
cfg.continuous = 'yes';
cfg.viewmode = 'vertical';
cfg.blocksize = 1; % duration of data to display, in seconds
ft_databrowser(cfg);

%%

% zoom out a bit, both horizontal and vertical
% apply demeaning as minimal preprocessing

cfg = [];
cfg.dataset = 'oddball1_mc_downsampled_eeg.eeg';
cfg.continuous = 'yes';
cfg.viewmode = 'vertical';
cfg.blocksize = 30; % duration of data to display, in seconds
cfg.preproc.demean = 'yes';
cfg.layout = 'natmeg_customized_eeg1005.lay';
ft_databrowser(cfg);

% see https://www.fieldtriptoolbox.org/template/layout/

% select the artifact around 16 seconds, right-click and do multiplotER and topoplotER

% select the artifact around 132 seconds, right-click and do multiplotER and movieplotER

%%

cfg = [];
cfg.dataset = 'oddball1_mc_downsampled_eeg.eeg';
cfg.continuous = 'yes';
cfg.demean = 'yes'; % note that it does not go in cfg.preproc here
data_raw = ft_preprocessing(cfg);

cfg.lpfilter = 'no';
cfg.hpfilter = 'no';
cfg.bpfilter = 'no';
cfg.lpfreq = 30;
data_lp = ft_preprocessing(cfg);

cfg.lpfilter = 'no';
cfg.hpfilter = 'yes';
cfg.bpfilter = 'no';
cfg.hpfreq = 1;
data_hp = ft_preprocessing(cfg);

cfg.lpfilter = 'no';
cfg.hpfilter = 'no';
cfg.bpfilter = 'yes';
cfg.bpfreq = [1 30];
data_bp = ft_preprocessing(cfg);

cfg = [];
cfg.blocksize = 30;
cfg.ylim = [-100 100]*1e-6; % plusminus 100 uV
cfg.layout = 'natmeg_customized_eeg1005.lay';
ft_databrowser(cfg, data_hp);

% note how the eye blinks look like in the HP filtered data

%%

cfg = [];
cfg.dataset = 'oddball1_mc_downsampled_aux.eeg';
cfg.continuous = 'yes';
cfg.viewmode = 'vertical';
cfg.blocksize = 30;
cfg.ylim = [-300 300] * 1e-6;
cfg.preproc.demean = 'yes';
cfg.plotevents = 'no';
ft_databrowser(cfg);

% find the HEOG artifact from 134-135 seconds
% in the next section we return to the unfiltered EEG data and plot that artifact

%%

cfg = [];
cfg.dataset = 'oddball1_mc_downsampled_aux.eeg';
cfg.continuous = 'yes';
cfg.demean = 'yes'; % note that it does not go in cfg.preproc here
data_aux = ft_preprocessing(cfg);

cfg = [];
data_all = ft_appenddata(cfg, data_raw, data_aux);

%%

cfg = [];
cfg.blocksize = 30;
cfg.ylim = [-500 500]*1e-6; % plusminus 500 uV
cfg.layout = 'natmeg_customized_eeg1005.lay';
cfg.channel = 'EOG*';
ft_databrowser(cfg, data_all);

% find the HEOG artifact from 134-135 seconds
% select all channels to be displayed, and then multiplotER and topoplotER

%%

event = ft_read_event('oddball1_mc_downsampled_eeg.eeg');

% look at the relation between the eye blinks and the triggers

cfg           = [];
cfg.event     = event;
cfg.blocksize = 60;
cfg.ylim      = [-500 500]*1e-6; % plusminus 0.5 mV
cfg.layout    = 'natmeg_customized_eeg1005.lay';
cfg.channel   = 'EOG*';
ft_databrowser(cfg, data_all);

% what happens in the first 10 seconds?
% what happens from 930 seconds towards the end?

%%

hdr = ft_read_header('oddball1_mc_downsampled_eeg.eeg');

begsample = 10*hdr.Fs;
endsample = 930*hdr.Fs;
offset    = 0;

cfg         = [];
cfg.dataset = 'oddball1_mc_downsampled_eeg.eeg';
cfg.demean  = 'yes';
cfg.trl     = [begsample endsample offset];
data_exp    = ft_preprocessing(cfg);

cfg           = [];
cfg.event     = event;
cfg.blocksize = 60;
cfg.ylim      = [-100 100]*1e-6; % plusminus 100 uV
cfg.layout    = 'natmeg_customized_eeg1005.lay';
ft_databrowser(cfg, data_exp);

% the first sample in the data segment that we read in is now at time=0
```

### Auditory oddball

```matlab
cfg = [];
cfg.dataset             = 'oddball1_mc_downsampled_eeg.vhdr';

cfg.trialdef.eventtype  = 'STI101'; % name of trigger channel
cfg.trialdef.eventvalue = [1, 2]; % 1 is standard, 2 is deviant
cfg.trialdef.prestim    = 0.200; % seconds
cfg.trialdef.poststim   = 0.600; % seconds
cfg.trialfun            = 'ft_trialfun_general';
cfg                     = ft_definetrial(cfg); % this creates a new cfg, including "trl"

% and we add more stuff to it here

cfg.continuous          = 'yes';    % data is continuous
cfg.hpfilter            = 'no';     % we do not apply a high-pass filter
cfg.detrend             = 'no';     % we do not detrend
cfg.demean              = 'yes';    % we demean (baseline correct) ...
cfg.baselinewindow      = [-Inf 0]; % using the mean activity in this window
cfg.dftfilter           = 'yes';    % a notch filter ...
cfg.dftfreq             = [50 100]; % hitting the (European) power frequency (and its first harmonic)
cfg.channel             = 'EEG';

cfg.reref               = 'yes';    % was recorded with left mastoid but is ...
cfg.refchannel          = 'all';    % rereferenced to all (also called common average

data_auditory           = ft_preprocessing(cfg);

%%

cfg             = [];
cfg.continuous  = 'yes';
cfg.event       = event;
cfg.blocksize   = 30;
cfg.ylim        = [-100 100]*1e-6; % plusminus 100 uV
cfg.layout      = 'natmeg_customized_eeg1005.lay';
ft_databrowser(cfg, data_auditory);

%%

cfg          = [];
cfg.trials   = find(data_auditory.trialinfo == 1);
ERP_standard = ft_timelockanalysis(cfg, data_auditory);

cfg         = [];
cfg.trials  = find(data_auditory.trialinfo == 2);
ERP_deviant = ft_timelockanalysis(cfg, data_auditory);

%%

cfg        = [];
cfg.layout = 'natmeg_customized_eeg1005.lay';
cfg.figure = figure;
ft_multiplotER(cfg, ERP_standard, ERP_deviant);

%%

cfg        = [];
cfg.layout = 'natmeg_customized_eeg1005.lay';
cfg.metric = 'std';
data_auditory_cleaned = ft_rejectvisual(cfg, data_auditory);

%%

cfg                = [];
cfg.lpfilter       = 'yes';
cfg.lpfreq         = 30;
cfg.detrend        = 'yes';     % removing linear trends
cfg.baselinewindow = [-Inf 0];  % using the mean activity in this window

data_auditory_filt = ft_preprocessing(cfg, data_auditory_cleaned);

%%

cfg          = [];
cfg.trials   = find(data_auditory_filt.trialinfo == 1);
ERP_filt_standard = ft_timelockanalysis(cfg, data_auditory_filt);

cfg         = [];
cfg.trials  = find(data_auditory_filt.trialinfo == 2);
ERP_filt_deviant = ft_timelockanalysis(cfg, data_auditory_filt);

%%

cfg        = [];
cfg.layout = 'natmeg_customized_eeg1005.lay';
cfg.figure = figure;
ft_multiplotER(cfg, ERP_filt_standard, ERP_filt_deviant);

%%

cfg           = [];
cfg.operation = 'x2-x1';
cfg.parameter = 'avg';
ERP_difference = ft_math(cfg, ERP_filt_standard, ERP_filt_deviant);

cfg        = [];
cfg.layout = 'natmeg_customized_eeg1005.lay';
cfg.figure = figure;
ft_multiplotER(cfg, ERP_difference);
```

### Motor response

```matlab
cfg = [];
cfg.dataset = 'oddball1_mc_downsampled_eeg.vhdr';

% define trials based on motor responses
cfg.trialdef.prestim    = 1.5;
cfg.trialdef.poststim   = 2.0;
cfg.trialdef.eventtype  = 'STI102';     % name of trigger channel
cfg.trialdef.eventvalue = [256, 4096];  % 256 = button press left, 4096 = button press right
cfg.trialfun            = 'ft_trialfun_general';
cfg                     = ft_definetrial(cfg);

% preprocess EEG data
cfg.demean              = 'yes';
cfg.dftfilter           = 'yes';
cfg.dftfreq             = [50 100];
cfg.reref               = 'yes';  % rereferencing
cfg.refchannel          = 'all';

data_motor              = ft_preprocessing(cfg);

%%

cfg        = [];
cfg.layout = 'natmeg_customized_eeg1005.lay';
cfg.metric = 'std';
data_motor_cleaned = ft_rejectvisual(cfg, data_motor);

%%

cfg            = [];
cfg.output     = 'pow';
cfg.channel    = 'all';
cfg.method     = 'mtmconvol';
cfg.taper      = 'hanning';
cfg.toi        = -1 : 0.10 : 1.5;
cfg.foi        = 2:2:40;
cfg.t_ftimwin  = ones(size(cfg.foi)) * 0.5;

cfg.trials     = find(data_motor_cleaned.trialinfo(:,1) == 256);
tfr_left       = ft_freqanalysis(cfg, data_motor_cleaned);

cfg.trials     = find(data_motor_cleaned.trialinfo(:,1) == 4096);
tfr_right      = ft_freqanalysis(cfg, data_motor_cleaned);

%%

cfg              = [];
cfg.baseline     = [-0.5 -0.1];
cfg.baselinetype = 'relative';  % we use a relative baseline
cfg.xlim         = [0.4 0.8];
cfg.ylim         = [16 24];
cfg.zlim         = 'maxabs';
cfg.marker       = 'on';
cfg.colorbar     = 'yes';
cfg.layout       = 'natmeg_customized_eeg1005.lay';

cfg.figure       = figure;
ft_topoplotTFR(cfg, tfr_left);
title('Left hand reaction');

cfg.figure       = figure;
ft_topoplotTFR(cfg, tfr_right);
title('Right hand reaction');

%%

cfg            = [];
cfg.parameter  = 'powspctrm';
cfg.operation  = '(x1-x2)/(x1+x2)';
tfr_difference = ft_math(cfg, tfr_right, tfr_left);

cfg              = [];
cfg.xlim         = [0.4 0.8];
cfg.ylim         = [16 24];
cfg.zlim         = 'maxabs';
cfg.marker       = 'on';
cfg.colorbar     = 'yes';
cfg.layout       = 'natmeg_customized_eeg1005.lay';
cfg.figure       = figure;

ft_topoplotTFR(cfg, tfr_difference);
title('Left vs right hand response');


%%

cfg              = [];
cfg.layout       = 'natmeg_customized_eeg1005.lay';
cfg.zlim         = 'maxabs';
cfg.colorbar     = 'yes';
cfg.figure       = figure;

ft_multiplotTFR(cfg, tfr_difference);
```
