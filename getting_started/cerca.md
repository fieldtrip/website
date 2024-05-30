---
title: Getting started with Cerca OPM data
tags: [dataformat, meg, opm, cerca, bids]
---

# Getting started with Cerca OPM data

[Cerca Magnetics](https://www.cercamagnetics.com) is a joint-venture spin-out company from the University of Nottingham and Magnetic Shields Limited that develops full wearable OPM-MEG systems. The data from their current systems is stored in the `*.cMEG` format, but a converter is supplied with each system to turn the data into the *.fif format for post-processing. The `*.fif` file format is already supported by FieldTrip, which means that no special functions are needed for reading the data. A separate function can be used to read the data straight from `*.cMEG` into FieldTrip – this is currently being developed.

There are some differences which are relevant for processing Cerca data - and OPM data as a whole. One difference is how events or triggers are represented and detected. Another difference is in the procedure used to record the position of the OPM sensors relative to the head, which is relevant for topographic plotting and for the co-registration between MEG and MRI. Furthermore, Cerca OPM systems use either dual axis or triaxial systems, and so displaying data at a sensor-level requires some further considerations.

The example data provided on the FieldTrip [download server](https://download.fieldtriptoolbox.org/example/cerca/) includes a self-contained version of the data in the `.fif` format organized according to the [BIDS standard](https://www.bids-standard.org). This includes sensor locations that are already co-registered to a 3D digitisation of the participant. An additional folder includes the raw files if you wish to develop a co-registration pipeline separately from what is provided. All files are detailed in the `README.txt`.

## Read and visualize the continuous data

    % this starts with the fif data organized according to BIDS
    filename = 'ses-001/meg/sub-004_ses-001_task-braille_run-001_meg.fif'; 

    cfg = [];
    cfg.dataset = filename;
    data = ft_preprocessing(cfg);

    cfg = [];
    cfg.preproc.demean = 'yes';
    cfg.ylim = [-1 1] * 1e-11;
    cfg.blocksize = 5; % seconds
    ft_databrowser(cfg, data);

## Reading and processing triggers

The Cerca OPM system uses triggers that are represented as an analogue channel (with voltages).

In this case the experiment consisted of a braille pattern stimulation on the left and right index fingers. Each stimulus is coded with an analogue trigger represented in the “Bra” channel (for Braille), and the stimulated finger is represented by the “Lef” or “Rig” channels (Left or Right). Here we will look at both fingers. For ease of visualisation, we will also only look at the Z (radial) channels.

        %% read the triggers and the data segments of interest
        hdr = ft_read_header(filename);

        disp(hdr.label)

        % determine the segments of interest around the triggers (aka the trials)
        cfg = [];
        cfg.dataset = filename;
        cfg.trialdef.eventtype = 'Bra';
        cfg.trialdef.prestim = 0.1;
        cfg.trialdef.poststim = 0.3;
        cfg = ft_definetrial(cfg);

        % read the segments of interest (aka the trials)
        cfg.channel = '*Z'; % Only look at the Z channels
        cfg.demean = 'yes';
        cfg.baselinewindow = [-inf 0];
        data = ft_preprocessing(cfg);

        % remove large variance trials
        cfg = [];
        cfg.method = 'summary';
        data_clean = ft_rejectvisual(cfg, data);

        % average over trials and plot the ERF
        cfg = [];
        timelock = ft_timelockanalysis(cfg, data_clean);

        plot(timelock.time, timelock.avg)

## Reading and filtering

As there is quite some drift in the signal, it is better to apply a filter to the continuous data prior to segmenting. That results in the following alternate preprocessing script, similar to the tutorial on processing continuous EEG or MEG data. Here, we apply a highpass filter of 1 Hz and a lowpass filter of 40 Hz.

    %% read and filter the continuous data
    cfg = [];
    cfg.dataset = filename;
    cfg.channel = '*Z';
    cfg.demean = 'yes';
    cfg.baselinewindow = [-inf inf];
    cfg.hpfilter = 'yes';
    cfg.hpfreq = 2;
    cfg.lpfilter = 'yes';
    cfg.lpfreq = 40;
    data_continuous = ft_preprocessing(cfg);

    % determine the segments of interest around the triggers (aka the trials)
    cfg = [];
    cfg.dataset = filename;
    cfg.trialdef.eventtype = 'Bra';
    cfg.trialdef.prestim = 0.1;
    cfg.trialdef.poststim = 0.3;
    cfg = ft_definetrial(cfg);

    % do the actual segmentation of the data
    data_segmented = ft_redefinetrial(cfg, data_continuous);

    % remove large variance trials
    cfg = [];
    cfg.method = 'summary';
    data_clean = ft_rejectvisual(cfg, data_segmented);

    % average over trials and plot the ERF
    cfg = [];
    timelock = ft_timelockanalysis(cfg, data_clean);

    plot(timelock.time, timelock.avg)

## Topographic plotting

When we look at this recording, we see channel names like “A1X” and “F4Y”. These channels correspond to the hardware sensors, i.e. the OPMs, as they are named in the DAQ recording, with the sensitive axis indicated by the last letter, i.e. either X, Y, or Z.

The data structure returned by **[ft_preprocessing](/reference/ft_preprocessing)** or the header from **[ft_read_header](/reference/fileio/ft_read_header)** include the "grad" field, which describes the sensor positions (see also this FAQ). The recording software itself does not know the relative locations of sensors to each other in the helmet, but it requires you to select a `_HelmConfig.tsv` file that lists which slot each sensor is in, as well as their positions and orientations for each sensitive axis.

In this specific recording the OPM sensors were placed in a generic helmet (the purple adult large helmet supplied by Cerca).

For topographic plotting, the channel names (in data.label) should match the locations on the head. To keep the script clean and reproducible, we will not go in the data structure and manually rename the channels to match, but we will use a montage, similar to how EEG and iEEG channels can be renamed, combined, added, and subtracted. However, the order in which the data is saved in the acquisition is not the same as the order in which the `_HelmConfig.tsv` is made. We therefore also have to match sensor names to their respective slot name. The `_HelmConfig.tsv` file also contains 2D projection coordinates of the helmet positions (Layx and Layy). Using this, we can create a layout for the topographic plotting.


    %% Rename channels
    montage = [];
    montage.labelold = data.label';
    
    % Read helmet layout mapping
    HelmConfig = tdfread(‘Braille_example_data\11766_054_braille1\20240129_101236_cMEG_Data\ 20240129_101236_HelmConfig.tsv');
    last_line_idx = strmatch('Helmet:',HelmConfig.Name);
    field_names = fieldnames(HelmConfig);
    for n = 1:size(field_names,1)
        HelmConfig.(field_names{n})(last_line_idx,:) = [];
        if max(strcmpi(field_names{n},{'Px';'Py';'Pz';'Ox';'Oy';'Oz';'Layx';'Layz'}))
            try
                HelmConfig.(field_names{n}) = str2num(HelmConfig.(field_names{n}));
            end
        end
    end
    HC_sensnames = strrep(cellstr(HelmConfig.Sensor),' ','');
    HC_slotnames = strrep(cellstr(HelmConfig.Name),' ','');
    sensor_slot_mapping = [];
    for n = size(data.label,1):-1:1
        sensor_slot_mapping(n) = find(strcmpi(HC_sensnames,data.label{n}));
    end
    
    montage.labelnew = HC_slotnames(sensor_slot_mapping);
    montage.tra = eye(size(data.label,1)); % the data is simply copied one-to-one
    
    % Create layout from tsv file
    layout = [];
    layout.pos = [HelmConfig.Layx(sensor_slot_mapping),HelmConfig.Layy(sensor_slot_mapping)];
    layout.label = HC_slotnames(sensor_slot_mapping);
    layout.width = repmat(0.02,size(layout.pos,1),1);
    layout.height = repmat(0.02,size(layout.pos,1),1);
    
    % rename the channels in the raw data
    cfg = [];
    cfg.montage = montage;
    data_helmetpos = ft_preprocessing(cfg, data);
    
    % or rename the channels in the timelocked ERF data
    timelock_helmetpos = ft_preprocessing(cfg, timelock);
    
    % plot the ERFs on the corresponding position in the helmet
    cfg = [];
    cfg.layout = layout;
    cfg.showoutline = 'yes';
    ft_multiplotER(cfg, timelock_helmetpos)
    
## Co-registration

There is a dedicated tutorial elsewhere that deals with various ways to co-register the OPM sensors with the head and the anatomical MRI. In this demonstration, the .fif file already contains a digitisation that the sensors have been co-registered to (using the dev2head transform `hdr.orig.dev_head_t`). However, the raw digitisation files and CAD file for the helmet have been provided (see the README.txt). The co-registration of the sensors to the digitisation was performed as described in Figure 2b in [Hill et al. 2020](https://doi.org/10.1016/j.neuroimage.2020.116995). 

## See also

{% include seealso tag="cerca" %}