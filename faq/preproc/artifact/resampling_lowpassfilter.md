---
title: Do I need to resample my data, and if so, how is this to be done?
category: faq
tags: [preprocessing]
redirect_from:
    - /faq/resampling_lowpassfilter/
---

## When is resampling required?
In principle, if your computing hardware is sufficient, there is hardly ever a need to resample the data in order to represent the time series at a sampling rate that is different from the sampling rate that was used upon data acquisition. Specifically, if you have enough compute power (and patience), storage space, and RAM, then **not** resampling the data may even be recommended, because it avoids potential unforeseen side effects (to be discussed below).

There can be specific cases that do require resampling. For instance, when to simultaneously recorded signals were digitized at different sampling rates. Also, if storage space, RAM or compute power are limiting factors, you may decide to resample the data to a lower sampling rate. In FieldTrip the resampling is performed by **[ft_resampledata](/reference/ft_resampledata)**.

## How is the resampling done?

The help documentation of **[ft_resampledata](/reference/ft_resampledata)** provides some more details. It implements several resampling methods. The most important thing to be aware of, when resampling to a lower sampling rate, is the phenomenon of [aliasing](https://en.wikipedia.org/wiki/Aliasing). Signal components present in the original signal that cannot be anymore represented by the new discrete sampling rate (i.e., signal components that are present in the original signal's bandwidth that is beyond the new signal's Nyquist frequency) wrap around to the lower frequencies, and thus may artificially inflate the noise at lower frequencies, which is undesired.

## Do I need to worry about this aliasing, and can it be avoided?

When you use **[ft_resampledata](/reference/ft_resampledata)** on typical data, i.e. using sufficiently clean data with a typical 1/f spectral characteristic + some band-limited neuronal signal components, the default method `resample` implements a sufficiently good anti-aliasing filter by default. However, the cutoff frequency is right on top of the new signal's Nyquist frequency and the filter does not have a very steep roll-off. This is problematic if there is substantially signal (or noise) just above the new signal's Nyquist frequency. The other methods implemented in **[ft_resampledata](/reference/ft_resampledata)** do not by default apply an low-pass filter, so in that case it is recommended to pre-filter the data before resampling using **[ft_preprocessing](/reference/ft_preprocessing)**, or to use the `cfg.lpfilter` option in **[ft_resampledata](/reference/ft_resampledata)**, which has been implemented as of May 2022.

## Example code to illustrate some of the methods and the aliasing

The below code can be used to explore the different methods and to illustrate the effect of aliasing using simulated signals that prove problematic for the default filtering.

```
fs = 500;
nchan = 1;
nrpt  = 32;
start_time = -1; % seconds
end_time = 2.5; % seconds
nsamples = (end_time - start_time) * fs + 1;

data = [];
for k = 1:nrpt
  data.time{k} = linspace(start_time, end_time, nsamples);
  data.trial{k} = randn(nchan,nsamples);
end
data.label = cellstr(num2str((1:nchan).'));

% the default functionality in ft_resampledata applies a firls
% anti-aliasing filter that has its cutoff at the new Nyquist frequency
cfg = [];
cfg.resamplefs = 200;
dataout1 = ft_resampledata(cfg, data);

cfg.lpfilter = 'yes';
cfg.lpfilttype = 'firws';
cfg.lpfreq   = 100;
dataout2 = ft_resampledata(cfg, data);

cfg.lpfreq = 90;
dataout3 = ft_resampledata(cfg, data);

cfg = [];
cfg.time = dataout1.time;
dataout4 = ft_resampledata(cfg, data);

cfg.lpfilter = 'yes';
cfg.lpfilttype = 'firws';
cfg.lpfreq = 100;
dataout5 = ft_resampledata(cfg, data);

cfg = [];
cfg.resamplefs = 250;
cfg.method = 'downsample';
dataout6 = ft_resampledata(cfg, data);

cfg.lpfilter = 'yes';
cfg.lpfilttype = 'firws';
cfg.lpfreq = 100;
dataout7 = ft_resampledata(cfg, data);

cfg = [];
cfg.method = 'mtmfft';
cfg.tapsmofrq = 1;
cfg.pad = 4;
freq = ft_freqanalysis(cfg, data);
freq1 = ft_freqanalysis(cfg, dataout1);
freq2 = ft_freqanalysis(cfg, dataout2);
freq3 = ft_freqanalysis(cfg, dataout3);
freq4 = ft_freqanalysis(cfg, dataout4);
freq5 = ft_freqanalysis(cfg, dataout5);
freq6 = ft_freqanalysis(cfg, dataout6);
freq7 = ft_freqanalysis(cfg, dataout7);

cmap = ft_colormap('Set1');

figure; hold on;
plot(freq1.freq, (log10(freq1.powspctrm)), 'color', cmap(2,:), 'linewidth', 2);
plot(freq2.freq, (log10(freq2.powspctrm)), 'color', cmap(3,:), 'linewidth', 2);
plot(freq3.freq, (log10(freq3.powspctrm)), 'color', cmap(4,:), 'linewidth', 2);
plot(freq4.freq, (log10(freq4.powspctrm)), 'color', cmap(5,:), 'linewidth', 2);
plot(freq5.freq, (log10(freq5.powspctrm)), 'color', cmap(7,:), 'linewidth', 2);
plot(freq6.freq, (log10(freq6.powspctrm)), 'color', cmap(8,:), 'linewidth', 2);
plot(freq7.freq, (log10(freq7.powspctrm)), 'color', cmap(9,:), 'linewidth', 2);
plot(freq.freq,  (log10(freq.powspctrm)), 'color', cmap(1,:), 'linewidth', 2);
legend({'rs_native', 'rs_firws100', 'rs_firws090', 'interp1', 'interp1_firws100', 'downsample', 'downsample_firws100', 'original'}, 'interpreter', 'none');
xlabel('frequency (Hz)');
ylabel('power');
```
{% include image src="/assets/img/faq/resampling/resampling1.png" width="600" %}

If the signal has a flat spectrum in the original bandwidth (red line, 'original'), the default `resample` method works well enough (blue line, 'rs_native'). The `interp1` and `downsample` resampled spectra (orange and pink lines) show an increase in power that is due to the aliasing. This aliasing can be avoided by an explicit lowpass filtering step prior to the resampling.

```
% add a very high amplitude broad-band component
data_hf_broad = data;
for k = 1:nchan
  data_hf_broad.trial{k}(1,:) = data_hf_broad.trial{k}(1,:) + ft_preproc_highpassfilter(randn(1,nsamples), fs, 110, [], 'firws').*50;
  data_hf_broad.time{k} = data_hf_broad.time{1};
end
data_hf_broad.trial{1} = data_hf_broad.trial{1}(1,:);
data_hf_broad.label    = data_hf_broad.label(1);

% the default functionality in ft_resampledata applies a firls
% anti-aliasing filter that has its cutoff at the new Nyquist frequency
cfg = [];
cfg.resamplefs = 200;
dataout1 = ft_resampledata(cfg, data_hf_broad);

cfg.lpfilter = 'yes';
cfg.lpfilttype = 'firws';
cfg.lpfreq = 100;
dataout2 = ft_resampledata(cfg, data_hf_broad);

cfg.lpfreq = 90;
dataout3 = ft_resampledata(cfg, data_hf_broad);

cfg = [];
cfg.time = dataout1.time;
dataout4 = ft_resampledata(cfg, data_hf_broad);

cfg.lpfilter = 'yes';
cfg.lpfilttype = 'firws';
cfg.lpfreq = 100;
dataout5 = ft_resampledata(cfg, data_hf_broad);

cfg = [];
cfg.resamplefs = 250;
cfg.method = 'downsample';
dataout6 = ft_resampledata(cfg, data_hf_broad);

cfg.lpfilter = 'yes';
cfg.lpfilttype = 'firws';
cfg.lpfreq = 100;
dataout7 = ft_resampledata(cfg, data_hf_broad);

cfg = [];
cfg.method = 'mtmfft';
cfg.tapsmofrq = 1;
cfg.pad = 4;
freq = ft_freqanalysis(cfg, data_hf_broad);
freq1 = ft_freqanalysis(cfg, dataout1);
freq2 = ft_freqanalysis(cfg, dataout2);
freq3 = ft_freqanalysis(cfg, dataout3);
freq4 = ft_freqanalysis(cfg, dataout4);
freq5 = ft_freqanalysis(cfg, dataout5);
freq6 = ft_freqanalysis(cfg, dataout6);
freq7 = ft_freqanalysis(cfg, dataout7);

figure; hold on;
plot(freq1.freq, (log10(freq1.powspctrm)), 'color', cmap(2,:), 'linewidth', 2);
plot(freq2.freq, (log10(freq2.powspctrm)), 'color', cmap(3,:), 'linewidth', 2);
plot(freq3.freq, (log10(freq3.powspctrm)), 'color', cmap(4,:), 'linewidth', 2);
plot(freq4.freq, (log10(freq4.powspctrm)), 'color', cmap(5,:), 'linewidth', 2);
plot(freq5.freq, (log10(freq5.powspctrm)), 'color', cmap(7,:), 'linewidth', 2);
plot(freq6.freq, (log10(freq6.powspctrm)), 'color', cmap(8,:), 'linewidth', 2);
plot(freq7.freq, (log10(freq7.powspctrm)), 'color', cmap(9,:), 'linewidth', 2);
plot(freq.freq,  (log10(freq.powspctrm)), 'color', cmap(1,:), 'linewidth', 2);
legend({'rs_native', 'rs_firws100', 'rs_firws090', 'interp1', 'interp1_firws100', 'downsample', 'downsample_firws100', 'original'}, 'interpreter', 'none');
xlabel('frequency (Hz)');
ylabel('power');
```

{% include image src="/assets/img/faq/resampling/resampling2.png" width="600" %}

The above example is an extreme case that illustrates the need of applying a bit more 'aggressive' lowpass filtering for the `rs_native` (blue) line. Although the applied lowpass filter is sufficient for the `resample` method, this filter is still not good enough to get rid of all aliasing for the `interp1` method.

```
% add a very high amplitude narrowband component
data_hf_narrow = data;
for k = 1:nchan
  data_hf_narrow.trial{k}(1,:) = data_hf_narrow.trial{k}(1,:) + ft_preproc_bandpassfilter(randn(1,nsamples), fs, [110 120], [], 'firws').*50;
  data_hf_narrow.time{k} = data_hf_narrow.time{1};
end
data_hf_narrow.trial{1} = data_hf_narrow.trial{1}(1,:);
data_hf_narrow.label    = data_hf_narrow.label(1);

% the default functionality in ft_resampledata applies a firls
% anti-aliasing filter that has its cutoff at the new Nyquist frequency
cfg = [];
cfg.resamplefs = 200;
dataout1 = ft_resampledata(cfg, data_hf_narrow);

cfg.lpfilter = 'yes';
cfg.lpfilttype = 'firws';
cfg.lpfreq   = 100;
dataout2 = ft_resampledata(cfg, data_hf_narrow);

cfg.lpfreq = 90;
dataout3 = ft_resampledata(cfg, data_hf_narrow);

cfg = [];
cfg.time = dataout1.time;
dataout4 = ft_resampledata(cfg, data_hf_narrow);

cfg.lpfilter = 'yes';
cfg.lpfilttype = 'firws';
cfg.lpfreq = 100;
dataout5 = ft_resampledata(cfg, data_hf_narrow);

cfg = [];
cfg.resamplefs = 250;
cfg.method = 'downsample';
dataout6 = ft_resampledata(cfg, data_hf_narrow);

cfg.lpfilter = 'yes';
cfg.lpfilttype = 'firws';
cfg.lpfreq = 100;
dataout7 = ft_resampledata(cfg, data_hf_broad);

cfg = [];
cfg.method = 'mtmfft';
cfg.tapsmofrq = 1;
cfg.pad = 4;
freq = ft_freqanalysis(cfg, data_hf_narrow);
freq1 = ft_freqanalysis(cfg, dataout1);
freq2 = ft_freqanalysis(cfg, dataout2);
freq3 = ft_freqanalysis(cfg, dataout3);
freq4 = ft_freqanalysis(cfg, dataout4);
freq5 = ft_freqanalysis(cfg, dataout5);
freq6 = ft_freqanalysis(cfg, dataout6);
freq7 = ft_freqanalysis(cfg, dataout7);

figure; hold on;
plot(freq1.freq, (log10(freq1.powspctrm)), 'color', cmap(2,:), 'linewidth', 2);
plot(freq2.freq, (log10(freq2.powspctrm)), 'color', cmap(3,:), 'linewidth', 2);
plot(freq3.freq, (log10(freq3.powspctrm)), 'color', cmap(4,:), 'linewidth', 2);
plot(freq4.freq, (log10(freq4.powspctrm)), 'color', cmap(5,:), 'linewidth', 2);
plot(freq5.freq, (log10(freq5.powspctrm)), 'color', cmap(7,:), 'linewidth', 2);
plot(freq6.freq, (log10(freq6.powspctrm)), 'color', cmap(8,:), 'linewidth', 2);
plot(freq7.freq, (log10(freq7.powspctrm)), 'color', cmap(9,:), 'linewidth', 2);
plot(freq.freq,  (log10(freq.powspctrm)), 'color', cmap(1,:), 'linewidth', 2);
legend({'rs_native', 'rs_firws100', 'rs_firws090', 'interp1', 'interp1_firws100', 'downsample', 'downsample_firws100', 'original'}, 'interpreter', 'none');
xlabel('frequency (Hz)');
ylabel('power');
```

{% include image src="/assets/img/faq/resampling/resampling3.png" width="600" %}

In the above example, the strong band limited component shows a method specific aliasing, with the contamination of the unfiltered `interp1` method being the most prominent. Note that the aliasing in the `rs_native` spectrum is also non-negligible.
