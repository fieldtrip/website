---
title: MVPA analysis
tags: [practicalmeeg2025, meg, timelock, statistics, plotting, mmfaces]
---


```
Famous      = [5 6 7];
Unfamiliar  = [13 14 15];
Scrambled   = [17 18 19];

%%

subj = datainfo_subject(15);
filename = fullfile(subj.outputpath, 'raw2erp', subj.name, sprintf('%s_data.mat', subj.name));
load(filename)

%%

cfg = [];
cfg.keeptrials = 'yes';
timelock = ft_timelockanalysis(cfg, data);

%%

classlabel = zeros(size(timelock.trial,1),1);
classlabel(ismember(timelock.trialinfo, Famous))     = 1;
classlabel(ismember(timelock.trialinfo, Unfamiliar)) = 2;
classlabel(ismember(timelock.trialinfo, Scrambled))  = 3;

%%

cfg = [];
% cfg.elec = timelock.elec;
cfg.grad = timelock.grad;
layout = ft_prepare_layout(cfg);

ft_plot_layout(layout)

%%

cfg = [];
cfg.method          = 'mvpa';
cfg.channel         = 'megmag';
cfg.avgoverchan     = 'no';
% cfg.latency       = [0.2 0.4];
cfg.avgovertime     = 'no';
cfg.design          = classlabel;
cfg.features        = 'chan';
cfg.mvpa            = [];
cfg.mvpa.k          = 3;
cfg.mvpa.metric     = 'accuracy';
% cfg.mvpa.metric      = 'confusion';
% cfg.mvpa.classifier  = 'lda';
cfg.mvpa.classifier = 'multiclass_lda';
stat = ft_timelockstatistics(cfg, timelock);

plot(stat.time, stat.accuracy)

%%

cfg = [];
cfg.method          = 'mvpa';
cfg.channel         = 'megmag';
cfg.avgoverchan     = 'no';
cfg.latency         = [0.2 0.4];
cfg.avgovertime     = 'no';
cfg.design          = classlabel;
cfg.features        = 'time';
cfg.mvpa            = [];
cfg.mvpa.k          = 3;
cfg.mvpa.metric     = 'accuracy';
% cfg.mvpa.metric      = 'confusion';
% cfg.mvpa.classifier  = 'lda';
cfg.mvpa.classifier = 'multiclass_lda';
stat = ft_timelockstatistics(cfg, timelock);

cfg              = [];
cfg.parameter    = 'accuracy';
cfg.layout       = layout;
cfg.colorbar     = 'yes';
ft_topoplotER(cfg, stat);

%%

cfg = [];
cfg.method          = 'mvpa';
cfg.channel         = 'megmag';
cfg.avgoverchan     = 'no';
cfg.latency         = 'all';
cfg.avgovertime     = 'no';
cfg.design          = classlabel;
cfg.features        = []; % both time and chan
cfg.mvpa            = [];
cfg.mvpa.k          = 3;
cfg.mvpa.metric     = 'accuracy';
% cfg.mvpa.metric      = 'confusion';
% cfg.mvpa.classifier  = 'lda';
cfg.mvpa.classifier = 'multiclass_lda';
stat = ft_timelockstatistics(cfg, timelock);

cfg              = [];
cfg.parameter    = 'accuracy';
cfg.layout       = layout;
cfg.colorbar     = 'yes';
ft_multiplotER(cfg, stat);
```