---
title: Getting started with Biosemi BDF data
category: getting_started
tags: [dataformat, eeg, biosemi, bdf]
redirect_from:
    - /getting_started/biosemi/
---

# Getting started with Biosemi BDF data

[Biosemi](http://www.biosemi.com) makes EEG amplifiers for EEG that have active electrodes, i.e the signal is already pre-amplified at the scalp before it is sent to the amplifier box where it is further amplified and digitized. The active electrodes make the recorded signals less sensitive for environmental noise (e.g., electronics noise in the lab) and for movements of the electrode cables. These Biosemi amplifiers are especially popular in applications with high channel density.

The Biosemi system has a few special characteristics

- it uses a non-standard referencing scheme (with the DRL and CMS electrode, rather than GND and REF)
- it stores the data in a 24 bit format
- it uses a sampling rate that is much higher (from 2 kHz upwards) than most EEG systems (commonly around 512 Hz)
- the active electrodes are only useable with electrode caps from Biosemi.

The [24 bit file format](http://www.biosemi.com/faq/file_format.htm) has the practical consequence that files are slightly smaller than they would have been when stored with 32-bits, but also that reading and converting the 24 bit numerical representation is very slow because 24 bit is not a standard numerical representation on Intel computers. MATLAB allows to read single bits or 8-bit values from a file, which can be used to construct the 24 bit value, but which is very slow. To speed up the reading, FieldTrip uses a mex file that reads the 24 bit values and converts them to a 32-bit representation on the fly.

The [high sampling rate](http://www.biosemi.com/faq/adjust_samplerate.htm) (minimally 2kHz, i.e. 2000 Hz) has the consequence that files are much larger than with most acquisition systems. e.g., when compared to a BrainAmp data file sampled at 512 Hz with the same number of electrodes, the Biosemi data file will be approximately 3x as large on disk and 4x as large after having read it in memory. That means that for processing bdf files you typically will want to have a computer with more than the standard amount of RAM. After reading the data in MATLAB memory, a common procedure is to downsample it to reduce the sampling rate to 500 Hz using **[ft_resampledata](/reference/ft_resampledata)**. This will make all subsequent analyses run much faster and will facilitate doing the analysis with less RAM.

Most Biosemi [electrode caps](http://www.biosemi.com/headcap.htm) have a unique channel naming scheme. Also the exact number and positions is different from those in other EEG systems. Consequently, when plotting the channel-level data with a topographic arrangement of the channels, or when plotting the topographies (see the [plotting tutorial](/tutorial/plotting#plotting_data_at_the_channel_level) and the [channel layout tutorial](/tutorial/layout)), you will have to use a layout that is specific to your Biosemi electrode cap. FieldTrip includes the following template 2D layout files in the `fieldtrip/template/layout` directory, but you might want to construct your own layout.

- biosemi16.lay
- biosemi32.lay
- biosemi64.lay
- biosemi128.lay
- biosemi160.lay
- biosemi256.lay

Please note that the use of these layout files requires that the channel labeling in the data is consistent with the channel labeling in the layout file. You might want to check the following

    cfg = [];
    cfg.layout = 'biosemi160.lay'
    ft_layoutplot(cfg)

{% include image src="/assets/img/getting_started/biosemi/biosemi160.png" width="400" %}

## Referencing Biosemi EEG data

The Biosemi system uses a common-sense (CMS) and a driven-right-leg (DRL) electrode, which injects a small amount of current to minimize the effect of external noise sources. When recording data to disk and when reading it into FieldTrip, it is expressed as potential difference relative to the CMS. With this type of amplifier systems you should **always** reference after reading the data from disk, i.e. change the reference from CMS to another electrode, and you should **not** add the CMS electrode as implicit reference channel to the data.

For channel-level analysis you may want to use linked mastoids, or linked T7 and T8. For source analysis you would (as with other systems) best reference to the average of all electrodes (minus CMS).

See also [this](http://www.biosemi.com/faq/cms&drl.htm) explanation on the Biosemi website.

## Preprocessing and analyzing BDF data

Except for the required referencing, BDF data is processed just like other EEG and MEG data. A simple analysis script would look like this

    filename 'yourfile.bdf';

    cfg = [];
    cfg.dataset = filename;
    cfg.trialdef.eventtype  = 'STATUS'
    cfg.trialdef.eventvalue = [1 2];
    cfg.trialdef.prestim    = 0.2;
    cfg.trialdef.poststim   = 0.8;
    cfg = ft_definetrial(cfg);

    cfg.reref = 'yes';
    cfg.refchannel = 'A1';
    cfg.demean = 'yes';
    cfg.baselinewindow = [-0.2 0];
    data = ft_preprocessing(cfg);

    cfg = [];
    timelock = ft_timelockanalysis(cfg, data);

To find out what the trigger codes are in your BDF file, you can use the following code snippet

    event = ft_read_event(filename);

    % select only the trigger codes, not the battery and CMS status
    sel = find(strcmp({event.type}, 'STATUS'));
    event = event(sel);

    plot([event.sample], [event.value], '.')

## See also

The BDF file format is documented on the [Biosemi website](https://www.biosemi.com/faq/file_format.htm).

The BDF+ file format is not used by the Biosemi acquisition software, but you can find its documentation [here](https://www.teuniz.net/edfbrowser/bdfplus%20format%20description.html) for reference.

The EDF and EDF+ file formats are documented [here](https://www.edfplus.info).

Other pages on this website that relate to Biosemi:

{% include seealso tag="biosemi" %}