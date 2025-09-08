---
title: Making a synchronous movie of EEG or NIRS combined with video recordings
tags: [video, eeg, nirs, plotting]
category: example
redirect_from:
    - /example/video_eeg/
---

Inspecting your data is important to get a better understanding of it. You might have video recordings of your participant or the experimental setting. Playing the video recordings synchronously with the EEG or NIRS data can provide a lot of insight, for example to detect possible motion artifacts or to detect clear effects of the experimental stimuli.
 
This example script shows how to make a movie of your data with the help of **[ft_databrowser](/reference/ft_databrowser)** and MATLAB's Videowriter function. Subsequently, you synchronize this movie with your actual video data with video editing software like Adobe Premiere Pro or using  annotation software like [ELAN](https://archive.mpi.nl/tla/elan).

EEG and fNIRS are often used in freely moving subjects and in motion research. The following is a movie of fNIRS signals and artifacts during walking, turning, frowning, head movements and jumping. The example video shown here below was edited with Premiere Pro.

{% include youtube id="k1OB-vTWCys" %}

## MATLAB script

```
% read the continuous data in memory, this results in one long segment (trial)
cfg = [];
cfg.dataset = 'motioncapture.snirf';
data_continuous = ft_preprocessing(cfg);

% we also want to plot the events (if present)
event = ft_read_event('motioncapture.snirf');

%%

begtime = 0;
endtime = 60 - 1/data_continuous.fsample; % 60 seconds minus one sample
increment = 1; % stepwise in seconds

% make a figure with the desired size, see https://en.wikipedia.org/wiki/Display_resolution
close all
figh = figure;

set(figh, 'position', [10 10 1280 720]);
% set(figh, 'WindowState', 'maximized');

% prepare the video file
vidObj = VideoWriter('databrowser', 'MPEG-4');
vidObj.FrameRate = 1/increment;
vidObj.Quality = 100;
open(vidObj);

% prevent too much feedback info to be printed on screen
ft_debug off
ft_info off
ft_notice off

%%

while (endtime < data_continuous.time{1}(end)) && ishandle(figh)
  
  % cut a short piece of data from the continuous recording
  cfg = [];
  cfg.toilim = [begtime endtime];
  cfg.trackcallinfo = 'no';
  cfg.showcallinfo = 'no';
  data_piece = ft_redefinetrial(cfg, data_continuous);
  
  cfg = [];
  cfg.figure = figh;            % IMPORTANT: reuse the existing figure
  cfg.trackcallinfo = 'no';     % prevent too much feedback info to be printed on screen
  cfg.showcallinfo = 'no';      % prevent too much feedback info to be printed on screen
  cfg.viewmode = 'vertical';
  cfg.event = event;
  cfg.ploteventlabels = 'value';
  cfg.plotlabels = 'yes';
  cfg.fontsize = 5;
  cfg.continuous = 'yes';
  cfg.blocksize = round(endtime-begtime);
  cfg.nirsscale = 15;
  cfg.preproc.demean = 'yes';
  cfg.linecolor = [0.9290 0.6940 0.1250;0.8500 0.3250 0.0980; 0.6350 0.0780 0.1840; 0.4660 0.6740 0.1880; 0 0 0];
  cfg.colorgroups = [ones(1,4), 5*ones(1,2), ones(1,4), 5*ones(1,2), 2*ones(1,8), 5*ones(1,2), 2*ones(1,2), 5*ones(1,2),...
    ones(1,4), 5*ones(1,2), ones(1,4), 5*ones(1,2), 2*ones(1,8), 5*ones(1,2), 2*ones(1,2), 5*ones(1,2),...
    3*ones(1,4), 5*ones(1,2), 3*ones(1,4), 5*ones(1,2), 4*ones(1,2), 5*ones(1,2), 4*ones(1,4), 5*ones(1,2),...
    3*ones(1,4), 5*ones(1,2), 3*ones(1,4), 5*ones(1,2), 4*ones(1,2), 5*ones(1,2), 4*ones(1,4), 5*ones(1,2)];

  ft_databrowser(cfg, data_piece);
  
  set(gca, 'XGrid', 'on');
  currFrame = getframe(gcf);
  writeVideo(vidObj,currFrame);

  % go to the next segment of data
  begtime = begtime + increment;
  endtime = endtime + increment;
end

%%

% close the file
close(vidObj);
```

## See also

- <https://archive.mpi.nl/tla/elan>
- <https://datavyu.org>
- <https://cmu-perceptual-computing-lab.github.io/openpose>
