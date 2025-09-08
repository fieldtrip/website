---
title: Getting started with audio data
tags: [dataformat, audio]
category: getting_started
redirect_from:
    - /getting_started/audio/
---

You can read, preprocess and analyze audio files in the same way as EEG or MEG files. This can for example be handy to determine the spectrogram (e.g., using a time-frequency analysis) or to determine the onset of speech.

The following reads the continuous audio data, in this case from a 4-channel WAV file. Most other audio file formats are also supported.

  cfg = [];
  cfg.dataset = '4ch.wav';
  data = ft_preprocessing(cfg)

The following information will be printed on screen:

    processing channel { '4ch channel 1' '4ch channel 2' '4ch channel 3' '4ch channel 4' }
    reading and preprocessing
    reading and preprocessing trial 1 from 1

    the call to "ft_preprocessing" took 1 seconds and required the additional allocation of an estimated 55 MB
    data =
    struct with fields:

             hdr: [1x1 struct]
           label: {4x1 cell}
            time: {[1x211355 double]}
           trial: {[4x211355 double]}
         fsample: 44100
      sampleinfo: [1 211355]
             cfg: [1x1 struct]

Also useful can be to use **[ft_databrowser](/reference/ft_databrowser)** to have a quick look at the time series.

    cfg = [];
    cfg.dataset = '4ch.wav';
    ft_databrowser(cfg);
