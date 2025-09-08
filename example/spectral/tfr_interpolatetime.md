---
title: Interpolate the time axis of single-trial TFRs
tags: [tfr]
category: example
redirect_from:
    - /example/tfr_interpolatetime/
---

If you're interested in quantifying the time-frequency response during an underlying slower (pseudo-)periodicity, e.g. during the gait cycle, it may be useful to adjust the time axes of the TFR on a cycle-by-cycle basis. This example script demonstrates a way to achieve this.

```matlab
%% generate some data 
% this consists of a bunch of signals, with a periodically modulated
% beta oscillation. The period varies from trial to trial, and has a range
% of [0.5 - 2] seconds.
ntrl = 500;
T = 1.5.*rand(1,ntrl) + 0.5;
F = 1./T;

fsample = 1000;
nsample = 2500;
nsamplepre = 1000;
for k = 1:ntrl
  tim = (-nsamplepre:(nsample-1))./fsample;
  mod = sin(2.*pi.*tim.*F(k)) + 1.5;
  dat = mod.*ft_preproc_bandpassfilter(randn(1,nsample+nsamplepre), fsample, [15 25], [], 'firws') + randn(1,nsample+nsamplepre);
  trial{1,k} = dat;
  time{1,k}  = tim;
end
data.trial = trial;
data.time  = time;
data.label = {'chan01'};
data.fsample = fsample;
data.trialinfo = T(:);

%% spectral transformation
cfg = [];
cfg.method = 'mtmconvol';
cfg.pad    = 5;
cfg.foi    = 2:2:40;
cfg.t_ftimwin = ones(1, numel(cfg.foi))./2;
cfg.toi    = -0.75:0.025:1.75;
cfg.keeptrials = 'yes';
cfg.taper = 'hanning';
freq = ft_freqanalysis(cfg, data);

%% old-fashioned way for averaging
fd = ft_freqdescriptives([], freq);

cfg = [];
cfg.baseline = [-inf inf];
cfg.baselinetype = 'relchange';
ft_singleplotTFR(cfg, fd);

%% now interpolate the powspctrm, based on the information in the trialinfo
pin = freq.powspctrm;
siz = size(pin);
siz(end) = nsteps+11;
pout = nan(siz);

timin = freq.time;
nsteps = 30; % this is the number of steps per interpolated cycle
for k = 1:size(pin,1)
  tstepout = freq.trialinfo(k,1)./nsteps;

  timout = [flip(-(tstepout.*(1:10)),2) tstepout.*(0:nsteps)];

  dim2  = 1:numel(freq.freq);
  [x,y] = ndgrid(dim2, timin);
  [xout,yout] = ndgrid(dim2, timout);

  for kk = 1:numel(freq.label)
    dat = shiftdim(pin(k,kk,:,:));
    pout(k,kk,:,:) = interpn(x, y, dat, xout, yout, 'spline');
  end
end

freq_int = freq;
freq_int.powspctrm = pout;
freq_int.time = timout./freq.trialinfo(end);
fd_int = ft_freqdescriptives([], freq_int);

cfg = [];
cfg.baseline = [-inf inf];
cfg.baselinetype = 'relchange';
ft_singleplotTFR(cfg, fd_int);
```
