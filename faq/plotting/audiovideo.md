---
title: How can I play back EEG/MEG and synchronous audio or video?
parent: Plotting and visualization
grand_parent: Frequently asked questions
category: faq
tags: [audio, video]
redirect_from:
    - /faq/audiovideo/
---

# How can I play back EEG/MEG and synchronous audio or video?

In epilepsy recordings it is common to record video along with the EEG. Also for some cognitive tasks, e.g., involving communicative expressions or spoken feedback, it is possible to record video and/or audio along with the EEG or MEG.

FieldTrip has two functions to facilitate the exploration of EEG/MEG recorded in synchrony with audio/video: **[ft_databrowser](/reference/ft_databrowser)** and **[ft_audiovideobrowser](/reference/ft_audiovideobrowser)**.

For both functions you should consider that:

- the moment at which the recordings started will in general be different,
- the sampling rate of the two recordings will be different (e.g., much higher for audio, but much lower for video).

The synchronization between the two recordings is realized by specifying both in _timestamps_ that are expressed relative a common temporal reference (e.g., the time on an external clock) using the offset and slope, where _timestamp=offset+slope\*sample_.

{% include markup/skyblue %}
This functionality has been implemented specifically for the [VideoMEG](https://github.com/andreyzhd/VideoMEG) software, but also works with audio and video recordings stored in another format as demonstrated above. For the VideoMEG system the synchronization between audio/video and MEG is realized by triggers that are sent by the VideoMEG to the MEG data stream.
{% include markup/end %}

## ft_databrowser

The **[ft_databrowser](/reference/ft_databrowser)** function has the focus on the EEG/MEG data and allows you to select a fragment of the EEG/MEG and playback the corresponding audio and/or video.

## ft_audiovideobrowser

The **[ft_audiovideobrowser](/reference/ft_audiovideobrowser)** function has the focus on the audio/video data and allows you to segment it in trials in the same way that the EEG/MEG data is segmented. This allows you to review the audio/video in the experimental trials. The trial definition that is based on the triggers/events coded in the EEG/MEG file are used to read the corresponding audio/video fragments.

## Example

Here is a demonstration of **[ft_databrowser](/reference/ft_databrowser)**. You specify the EEG dataset and the function that is to be executed upon selecting a piece of EEG data. The _browse_audiovideo_ is a small helper function located in the `fieldtrip/private` directory; similar functions exist for a quick spectral analysis or topographic plotting of a selected piece of EEG data.

In `cfg.selcfg` you specify the details needed by _browse_audiovideo_: the audio file, and the header of both data and audio. The header of the data and the audio are extended with the **FirstTimeStamp** and **TimeStampPerSample** fields. You should define the timestamps the same for synchronous samples in both recordings.

In this case the EEG starts at timestamp 0 and the audio recording was started a bit earlier at timestamp -19.865. In both recordings the timestamps correspond to seconds. The number of timestamps per second is different for the two recordings due to their different sampling rates. Both for the EEG and for the audio the relation _timestamp=FirstTimeStamp+TimeStampPerSample\*sample_ holds, not only for the first sample in the respective recording, but also for all subsequent samples.

    cfg = [];
    cfg.dataset = 'bitalino_2018.05.27_09.46.14.edf';

    cfg.selfun = 'browse_audiovideo';

    cfg.selcfg.audiofile = 'bitalino_2018.05.27_09.46.14_log.m4a';

    cfg.selcfg.audiohdr = ft_read_header(cfg.selcfg.audiofile);
    cfg.selcfg.audiohdr.FirstTimeStamp = -19.865;
    cfg.selcfg.audiohdr.TimeStampPerSample = 1/cfg.selcfg.audiohdr.Fs;

    cfg.selcfg.datahdr = ft_read_header(cfg.dataset);
    cfg.selcfg.datahdr.FirstTimeStamp = 0;
    cfg.selcfg.datahdr.TimeStampPerSample = 1/cfg.selcfg.datahdr.Fs;

    ft_databrowser(cfg);

When the ft_databrowser window shows, you make a selection with your left-mouse button. Subsequently you click with your right mouse-button in that window and select from the context-sensitive menu the option _browse_audiovideo_. A new window will popup that shows the audio and/or video corresponding to that selection.
