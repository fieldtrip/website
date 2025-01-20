---
title: Getting started with video data
parent: Other data
grand_parent: Getting started
category: getting_started
tags: [dataformat, video]
nav_order: 2
redirect_from:
    - /getting_started/video/
---

# Getting started with video data

You can read, preprocess and analyze video files in a similar way as and [fMRI timeseries data](/getting_started/fmri), as if they were a bunch of timeseries, one for each pixel. This can be handy to determine changes in a specific region of interest in the video, for example if you recorded the stimulus presentation screen, or to track mnotion of your subject. You can also take the temporal derivative over time (i.e. subsequent frames) to determine moments of large variance and hence motion.

To read video and represent it as a bunch of timeseries channels, you use

    cfg = [];
    cfg.dataset = 'Untitled.mov';
    data = ft_preprocessing(cfg);

The low-level functions can also be handy, especially if you plan to do your own custom processing on the data. Using the low-level functions has the advantage that it skips the data bookkeeping of the ft_preprocessing function, which is very time-consuming for so many channels.

    hdr = ft_read_header('Untitled.mov');
    disp(hdr)
    struct with fields:

               Fs: 30
           nChans: 2764800
            label: {2764800x1 cell}
         chantype: {2764800x1 cell}
         chanunit: {2764800x1 cell}
         nSamples: 240
          nTrials: 1
      nSamplesPre: 0
             orig: [1x1 struct]

    dat = ft_read_data('Untitled.mov', 'header', hdr); % pass the previously read header to speed it up

You can take one frame out of the video recording and convert it back to an RGB image.

    frame = dat(:,100);

    h = hdr.orig.Height;
    w = hdr.orig.Width
    frame = reshape(frame, h, w, 3);

    figure
    image(frame)
    axis equal
