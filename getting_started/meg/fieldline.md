---
title: Getting started with FieldLine OPM data
category: getting_started
tags: [dataformat, meg, opm, opm-mediannerve, fieldline]
redirect_from:
    - /getting_started/fieldline/
---

[FieldLine](https://fieldlineinc.com/) is a company located in Boulder, Colorado that develops OPM sensors and complete OPM-based MEG systems. The data from their current systems is stored in the \*.fif format, which is developed and used by [Neuromag/Elekta/Megin](/getting_started/meg/neuromag). The \*.fif file format is already supported by FieldTrip, which means that no special functions are needed for reading the data.

    cfg = [];
    cfg.dataset = 'MedianNerve_RestingStateEyesClosed.fif';
    data = ft_preprocessing(cfg);
    
    cfg = [];
    cfg.preproc.demean = 'yes';
    cfg.ylim = [-1 1] * 1e-11;
    cfg.blocksize = 30; % seconds
    ft_databrowser(cfg, data);

There are a number of differences though, which are relevant for processing FieldLine data in more detail. One difference is how events or triggers are represented and detected. Another difference is in the procedure used to record the position of the OPM sensors relative to the head, which is relevant for topographic plotting and for the coregistration between MEG and MRI. Furthermore, it can be the case that you have multiple recordings with a small number of OPM sensors on different locations, and that you want to merge those recordings.

## Reading and processing triggers

Depending on the generation of the FieldLine OPM system that you are working with, the triggers may be represented as an analog channel (with voltages) or as a digital channel.

In this case the recording is from a FieldLine v2 system and the experiment consisted of a median nerve stimulation on the right wrist. Each stimulus is coded with an analog trigger represented in the `Input-1` channel.

    filename = 'MedianNerve_StimBreakStim2min_Pos1.fif';
    hdr = ft_read_header(filename);

    disp(hdr.label)
        {'Input-1'    }
        {'00:01-BZ_OL'}
        {'00:02-BZ_OL'}
        {'00:03-BZ_OL'}
        {'00:04-BZ_OL'}
        {'00:05-BZ_OL'}
        {'00:06-BZ_OL'}
        {'00:07-BZ_OL'}
        {'00:08-BZ_OL'}

    % determine the segments of interest around the triggers (aka the trials)
    cfg = [];
    cfg.dataset = filename;
    cfg.trialdef.eventtype = 'Input-1';
    cfg.trialdef.prestim = 0.1;
    cfg.trialdef.poststim = 0.3;
    cfg = ft_definetrial(cfg);

    % read the segments of interest (aka the trials)
    cfg.channel = '00*';
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

As there is quite some drift in the signal, it is better to apply a filter to the continuous data prior to segmenting. That results in the following alternate preprocessing script, similar to the [tutorial on processing continuous EEG or MEG data](/tutorial/continuous/).

    % read the continuous data
    cfg = [];
    cfg.dataset = filename;
    cfg.channel = '00*';
    cfg.demean = 'yes';
    cfg.baselinewindow = [-inf inf];
    cfg.hpfilter = 'yes';
    cfg.hpfreq = 1;
    data_continuous = ft_preprocessing(cfg);

    % determine the segments of interest around the triggers (aka the trials)
    cfg = [];
    cfg.dataset = filename;
    cfg.trialdef.eventtype = 'Input-1';
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

When we look at this FieldLine v2 recording, we see channel names like `00:01-BZ_OL` and `00:02-BZ_OL`. These channels correspond to the hardware sensors, i.e. the OPMs, and in this case each OPM has only one channel in the axial (or normal) direction, indicated by "BZ".

The data structure returned by **[ft_preprocessing](/reference/ft_preprocessing)** or the header from **[ft_read_header](/reference/fileio/ft_read_header)** include the `grad` field, which describes the sensor positions (see also [this FAQ](/faq/source/sensors_definition)). However, in this case the recording software did not know in which slots of the 3D-printed helmet the OPMs were placed. The `data.grad.coilpos` and `data.grad.coilori` fields that are obtained from the fif file also don't make sense.

In this specific recording the OPM sensors were placed in an early version of the FieldLine smart helmet that the company refers to as the "Alpha1" version. The specific helmet has 107 slots for OPM sensors, but of course not all slots need to be filled. The FieldTrip [templates](/template/gradiometer) includes a detailed description of this helmet, and there is a [layout](/template/layout/#fieldline-opm-system) for 2D topographic plotting.

During acquisition of the data, an Excel table was maintained to map the channel numbers in the electronics chassis, to the OPM sensors, and to the corresponding slots in the 3D-printed helmet.

| channel | OPM sensor | helmet position |
|---------|------------|-----------------|
| 1       | 338        | FL30            |
| 2       | 119        | FL21            |
| 3       | 323        | FL20            |
| 4       | 111        | FL23            |
| 5       | 62         | FL36            |
| 6       | 336        | FL35            |
| 7       | 22         | FL34            |
| 8       | 246        | FL84            |

{% include markup/skyblue %}
Note that the OPM sensor number is not used here, but it might be relevant if you want to apply fine calibration, or if you want to account for the different noise characteristics of the different OPMs.
{% include markup/end %}

For topographic plotting the channel names (in `data.label`) should match the locations on the head. To keep the script clean and reproducible, we will **not** go in the data structure and manually rename the channels to match, but we will use a [montage](/example/rereference/#montage), similar to how EEG and iEEG channels can be renamed, combined, added, and subtracted.

    montage = [];
    montage.labelold = {
      '00:01-BZ_OL'
      '00:02-BZ_OL'
      '00:03-BZ_OL'
      '00:04-BZ_OL'
      '00:05-BZ_OL'
      '00:06-BZ_OL'
      '00:07-BZ_OL'
      '00:08-BZ_OL'
      }';
    montage.labelnew = {
      'FL30'
      'FL21'
      'FL20'
      'FL23'
      'FL36'
      'FL35'
      'FL34'
      'FL84'
    };
    montage.tra = eye(8); % the data is simply copied one-to-one

    % rename the channels in the raw data
    cfg = [];
    cfg.montage = montage;
    data_helmetpos = ft_preprocessing(cfg, data);

    % or rename the channels in the timelocked ERF data
    timelock_helmetpos = ft_preprocessing(cfg, timelock)

    % plot the ERFs on the corresponding position in the helmet
    cfg = [];
    cfg.layout = 'fieldlinealpha1_helmet.mat';
    cfg.showoutline = 'yes';
    ft_multiplotER(cfg, timelock_helmetpos)

## Merging multiple recordings

In this experiment three subsequent recordings were performed on the same participant in which the 8 OPM sensors were moved to different positions in the Alpha1 helmet. Each recording is stored in a different fif file. Using the example above, we can construct three raw data structures with the trials. After removing the noisy trials in each of the three recordings, we can average each of the recordings.  

Since channels in a FieldTrip data structure are required have a unique channel name, we cannot immediately use **[ft_appenddata](/reference/ft_appenddata)** or **[ft_appendtimelock](/reference/ft_appendtimelock)** to concatenate the data along the channel direction; we first have to rename the channels to make them unique. Using three separate montages to map (rename) the channels in each recording onto the corresponding names of the slots in the 3D printed helmet, we get raw data (or timelock) structures with unique channel names that can be appended.

## Coregistration

There is a dedicated [tutorial](/tutorial/source/coregistration_opm) that deals with various ways to coregister the OPM sensors with the head and the anatomical MRI. 

## See also

{% include seealso tag="fieldline" %}