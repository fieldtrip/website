---
title: Why do I need to run ft_freqanalysis before ft_combineplanar?
tags: [freq]
category: faq
redirect_from:
    - /faq/freq_before_combine/
---

The reason for this is that when you square a sine wave, its frequency will be doubled. If you use ft_combineplanar with the default combination method, 'Pythagoras' will be performed on the horizontal and vertical components of the planar gradient, which involves squaring the signals. As a consequence, periodic components in the original spectrum will shift their peaks to higher frequencies. Moreover, if there is more than a single peak in the spectrum, multiplicative effects might occur, which leads to additional spectral peaks at sum (and difference) frequencies of the original signal components. Also, if some of the peaks are at a frequency higher than half the Nyquist frequency, aliasing may occur (since doubling the frequency after squaring moves the peak beyond Nyquist). These things are demonstrated by the code below. The correct order for the computation of spectral quantities on synthetic planar gradient data is to execute ft_freqanalysis first, and ft_combineplanar second.

```
timeaxis = (0:999)./1000;
freqaxis = 0:500;

data = randn(2,1000);
data = data + [1;1]*sin(2*pi*timeaxis*20); % add a 20 Hz sine wave
data = data + [1;1]*sin(2*pi*timeaxis*320); % add a 300 Hz sine wave
data = data - mean(data,2); % subtract mean before FFT to avoid DC leak

data_combined = sqrt(sum(data.^2));
data_combined = data_combined - mean(data_combined,2); % subtract mean before FFT to avoid DC leak

fdata = sum(abs(fft(data,[],2)).^2, 1);
fdata_combined = abs(fft(data_combined,[],2)).^2;

fdata = fdata./sum(fdata); %normalise to sum 1
fdata_combined = fdata_combined./sum(fdata_combined);

figure;
hold on;
plot(freqaxis, fdata(1:501));
plot(freqaxis, fdata_combined(1:501));
legend({'first fft, then combine' 'first combine, then fft'});
```

