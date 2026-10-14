---
title: Getting started with Cerca OPM data
tags: [dataformat, meg, opm, cerca, bids]
category: getting_started
redirect_from:
    - /getting_started/cerca/
---

[Cerca Magnetics](https://www.cercamagnetics.com) is a joint-venture spin-out company from the University of Nottingham and Magnetic Shields Limited that develops full wearable OPM-MEG systems. The data from their current systems is stored in the `.cMEG` format, but a converter is supplied with each system to turn the data into the `.fif` format for post-processing. The `.fif` format is already supported by FieldTrip, which means that no special functions are needed for reading the data. A separate function can be used to read the data straight from `.cMEG` into FieldTrip – this is currently being developed.

There are some differences which are relevant for processing Cerca data - and OPM data as a whole. One difference is how events or triggers are represented and detected. Another difference is in the procedure used to record the position of the OPM sensors relative to the head, which is relevant for topographic plotting and for the co-registration between MEG and MRI. Furthermore, Cerca OPM systems use either dual axis or triaxial systems, and so displaying data at a sensor-level requires some further considerations.

The example data provided on the our [download server](https://download.fieldtriptoolbox.org/getting_started/cerca/) includes a self-contained version of the data in the `.fif` format organized according to the [BIDS standard](https://www.bids-standard.org). This includes sensor locations that are already co-registered to a 3D digitization of the participant. An additional folder includes the raw files in the original `.cMEG` if you wish to develop a co-registration pipeline separately from what is provided. All files are detailed in the `README.txt`.

## Read and visualize the continuous data

    % this starts with the fif data organized according to BIDS
    filename = 'bids/ses-001/meg/sub-004_ses-001_task-braille_run-001_meg.fif'; 

    cfg = [];
    cfg.dataset = filename;
    cfg.coilaccuracy = 0; % to read the sensor positions properly
    data = ft_preprocessing(cfg);

    cfg = [];
    cfg.preproc.demean = 'yes';
    cfg.ylim = [-1 1] * 1e-11;
    cfg.blocksize = 5; % seconds
    ft_databrowser(cfg, data);

## Reading and processing triggers

The Cerca OPM system uses triggers that are represented as voltages in an analogue channel.

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

When we look at this recording, we see channel names like “A1X” and “F4Y”. These names correspond to the hardware sensors, i.e. the OPMs, as they are named in the DAQ recording, with the sensitive axis indicated by the last letter (either X, Y, or Z).

The data structure returned by **[ft_preprocessing](/reference/ft_preprocessing)** or the header from **[ft_read_header](/reference/fileio/ft_read_header)** include the "grad" field, which describes the sensor positions (see also [this FAQ](/faq/how_are_electrodes_magnetometers_or_gradiometers_described/#the-definition-of-meg-sensors)). The recording software itself does not know the relative locations of sensors to each other in the helmet, but it requires you to select a `_HelmConfig.tsv` file that lists which slot each sensor is in, as well as their positions and orientations for each sensitive axis. In this specific recording the OPM sensors were placed in the generic purple adult large helmet supplied by Cerca.

For topographic plotting, the channel names in `data.label` should be mapped to the corresponding locations on the head. To keep the script clean and reproducible, we will not go in the data structure and manually rename the channels, but use a montage as explained [here](/faq/preproc/datahandling/rename_channels).

The `_HelmConfig.tsv` file specifies the channel names (based on the name of the hardware sensors) and their placements in the helmet. If we know which OPM sensor is in which slot, we can make a montage that allows for renaming the channels in the data, so that we can (consistently over participants) use the same helmet slot names and locatios for the plotting and for source reconstruction.

    tsv = ft_read_tsv('11766_054_braille1/20240129_101236_cMEG_Data/20240129_101236_HelmConfig.tsv');
    tsv = tsv(1:end-1,:); % drop the last line

    helmetlab  = tsv{:,1};   % labels for the helmet slots
    pos        = tsv{:,2:4};
    ori        = tsv{:,5:7};
    xy         = tsv{:,8:9};
    channellab = tsv{:,10};  % labels for the OPM sensor channels

    % remove spaces from the helmet slot and OPM channel names
    for i=1:numel(lab)
      lab{i}(isspace(lab{i})) = [];
    end
    for i=1:numel(chan)
      chan{i}(isspace(chan{i})) = [];
    end

    % make a montage to rename the channels
    montage = [];
    montage.labelold = helmetlab;
    montage.labelnew = helmetlab;
    montage.tra = eye(length(helmetlab));

The `_HelmConfig.tsv` file also contains 2D projection coordinates of the helmet slot positions in `Layx` and `Layy` which can be used for 2D plotting. Using the `_HelmConfig.tsv` file, we can create a [layout](/tutorial/plotting/layout) for the topographic plotting.

    % make a general purpose layout, we will refine it further down 
    layout = [];
    layout.label  = lab; % we could also use "chan" here
    layout.pos    = xy;
    layout.width  = ones(192,1) * 0.1;
    layout.height = ones(192,1) * 0.05;

    % add the location for the scale indicator in the upper right corner
    layout.label{end+1}  = 'SCALE';
    layout.pos(end+1,:)  = [0.5 0.5];
    layout.width(end+1)  = 0.1;
    layout.height(end+1) = 0.05;

    % add the location for the comment field in the upper left corner
    layout.label{end+1}  = 'COMNT';
    layout.pos(end+1,:)  = [-0.5 0.5];
    layout.width(end+1)  = 0.1;
    layout.height(end+1) = 0.05;

    % we can add an outline, which we reuse from the CTF helmet
    cfg = [];
    cfg.layout = 'CTF151_helmet';
    ctf151_helmet = ft_prepare_layout(cfg);

    layout.mask = ctf151_helmet.mask;
    layout.outline = ctf151_helmet.outline;

    % slightly increase the size of the outline and mask 
    for i=1:numel(layout.mask)
      layout.mask{i} = 1.1 * layout.mask{i};
    end
    for i=1:numel(layout.outline)
      layout.outline{i} = 1.1 * layout.outline{i};
    end

    figure; ft_plot_layout(layout);

The layout that we just created has the three (x, y, z) channels of each OPM sensor at the same position. Since we don't want to plot them on top of each other, we make a subset of the x, y, and z channels.  

    selx = endsWith(layout.label, 'X') | strcmp(layout.label, 'SCALE') | strcmp(layout.label, 'COMNT');
    sely = endsWith(layout.label, 'Y') | strcmp(layout.label, 'SCALE') | strcmp(layout.label, 'COMNT');
    selz = endsWith(layout.label, 'Z') | strcmp(layout.label, 'SCALE') | strcmp(layout.label, 'COMNT');

    cerca192x = [];
    cerca192x.label   = layout.label(selx);
    cerca192x.pos     = layout.pos(selx,:);
    cerca192x.width   = layout.width(selx);
    cerca192x.height  = layout.height(selx);
    cerca192x.outline = layout.outline;
    cerca192x.mask    = layout.mask;

    cerca192y = [];
    cerca192y.label   = layout.label(sely);
    cerca192y.pos     = layout.pos(sely,:);
    cerca192y.width   = layout.width(sely);
    cerca192y.height  = layout.height(sely);
    cerca192y.outline = layout.outline;
    cerca192y.mask    = layout.mask;

    cerca192z = [];
    cerca192z.label   = layout.label(selz);
    cerca192z.pos     = layout.pos(selz,:);
    cerca192z.width   = layout.width(selz);
    cerca192z.height  = layout.height(selz);
    cerca192z.outline = layout.outline;
    cerca192z.mask    = layout.mask;

    % figure; ft_plot_layout(cerca192x);   % tangential component
    % figure; ft_plot_layout(cerca192y);   % tangential component
    figure; ft_plot_layout(cerca192z);   % radial component

It can also be usefull to make a multiplot with the ERPs, power spectra, or TFRs for each of the channels with the three channels shown as a triplet next to each other.

    selx = endsWith(layout.label, 'X');
    sely = endsWith(layout.label, 'Y');
    selz = endsWith(layout.label, 'Z');

    cerca192all = layout;
    cerca192all.pos(selx,2) = cerca192all.pos(selx,2) + 0.011; % move a little up
    cerca192all.pos(sely,2) = cerca192all.pos(sely,2) + 0.011; % move a little up
    cerca192all.pos(selz,2) = cerca192all.pos(selz,2) - 0.011; % move a little down

    cerca192all.pos(selx,1) = cerca192all.pos(selx,1) - 0.0205; % move a little to the left
    cerca192all.pos(sely,1) = cerca192all.pos(sely,1) + 0.0205; % move a little to the right

    cerca192all.width(selx) = 0.035;
    cerca192all.width(sely) = 0.035;
    cerca192all.width(selz) = 0.035;

    cerca192all.height(selx) = 0.02;
    cerca192all.height(sely) = 0.02;
    cerca192all.height(selz) = 0.02;

    figure; ft_plot_layout(cerca192all)

## Renaming the OPM channels to the corresponding helmet locations

To use the layouts that we just created, we have to rename the channels in the data from their "OPM sensor" names to the "helmet slot" names using the montage. It is actually recommended to do this as the first step in the processing pipeline upon reading the raw data ft_preprocessing.

    % rename the channels in the raw data
    cfg = [];
    cfg.montage = montage;
    data_helmet = ft_preprocessing(cfg, data);
    
    % also rename the channels in the timelocked ERF data (not needed if the raw data channels had been renamed earlier on)
    timelock_helmet = ft_preprocessing(cfg, timelock);
    
    % plot the ERFs on the corresponding position in the helmet
    cfg = [];
    cfg.layout = layout;
    cfg.showoutline = 'yes';
    ft_multiplotER(cfg, timelock_helmet)

## Construct the gradiometer definition

The `_HelmConfig.tsv` file also contains the 3D positions and orientations which we can use to construct a gradiometer definition. This can be used for denoising using HFC or AMM, or for source reconstruction. This is an alternative to using the grad structure that you can read from the fif file using ft_preprocessing or ft_read_sens.

    grad = [];
    grad.label    = helmetlab;
    grad.coilpos  = pos;
    grad.coilori  = ori;
    grad.tra      = eye(192);
    grad.coordsys = 'RAS';
    grad.unit     = 'm';

    ft_plot_sens(grad, 'coil', true, 'orientation', true, 'axes', true)

The grad structure is specific for the helmet, so you don't have to make it again and again for different recordings with that helmet, but you can just save it to disk and reuse it. In this specific recording the OPM sensors were placed in the purple adult large helmet supplied by Cerca. You would have to make separate grad structures for each of the Cerca helmet sizes that you use.

## Co-registration

There is a dedicated tutorial elsewhere that deals with various ways to co-register the OPM sensors with the head and the anatomical MRI. In this demonstration, the .fif file already contains a digitization that the sensors have been co-registered to (using the dev2head transform `hdr.orig.dev_head_t`). However, the raw digitization files and CAD file for the helmet have also been provided on the [download server](https://download.fieldtriptoolbox.org/getting_started/cerca/) (see README.txt). The co-registration of the sensors to the digitization was performed as described in Figure 2b in [Hill et al. 2020](https://doi.org/10.1016/j.neuroimage.2020.116995).

## See also

{% include seealso tag="cerca" %}
