---
title: Why is there a residual 50Hz line-noise component after applying a DFT filter?
category: faq
tags: [artifact, filter, noise, preprocessing]
---

# Why is there a residual 50Hz line-noise component after applying a DFT filter?

The residual line noise at 50 or 60 Hz is due to its non-stationarity. Imagine a trial in which the 50Hz line noise increases in amplitude over time (e.g., trial #3 in the first figure).

{% include image src="/assets/img/faq/why_is_there_a_residual_50hz_line-noise_component_after_applying_a_dft_filter/linenoise.png" width="600" %}

With `cfg.dftfilter` we fit the amplitude and phase of a constant-amplitude sine wave to the data. The fitted amplitude will correspond to the mean over the whole trial, i.e. at the begin of the trial it will be larger than the actual amplitude, and towards the end it will be smaller (second figure, using a 5 Hz example sine).

    % sampling rate
    fs = 1000;
    % time
    t = (1:10000)/fs;
    % frequency (Hz)
    f = 5;
    % increasing amplitude
    amp = (1:10000)/fs;

    % 5 Hz sine with increasing amplitude
    s1 = amp.*sin(2*pi*f*t);
    plot(t, s1, 'b');

    % dftfilter: fit 5 Hz sine (with constant amplitude)
    avgamp = mean(amp);
    s2 = avgamp.*sin(2*pi*f*t);
    hold on; plot(t, s2, 'r');

{% include image src="/assets/img/faq/why_is_there_a_residual_50hz_line-noise_component_after_applying_a_dft_filter/dftfilter1.png" width="500" %}

Imagine that you then subtracting the estimated 5 Hz component. At the begin of the trial you subtract too much, causing a negative (sign-flipped) 5 Hz signal to remain in the data, and towards the end of the trial you are not subtracting enough, causing a positive (non sign-flipped) 5 Hz signal to remain (black line in third figure).

So computed over the whole time interval of the cleaned data, the 5 Hz amplitude is zero. However, for a short time interval at the begin, there is non-zero amplitude at 5 Hz. In the middle the amplitude dips, and towards the end of the trial the amplitude increases and is again non-zero. I.e., the time-varying amplitude is V-shaped: large at the edges, small in the middle. Similarly, if you were to look at the power, it would be U-shaped.

    % subtract the 5 Hz fit
    s3 = s1-s2;
    figure; plot(t, s3, 'k');

    % bandstopfilter: remove 4.9 to 5.1 Hz
    s4 = ft_preproc_bandstopfilter(s1, fs, [4.9 5.1], 2);
    hold on; plot(t, s4, 'm');

{% include image src="/assets/img/faq/why_is_there_a_residual_50hz_line-noise_component_after_applying_a_dft_filter/dftfilter2.png" width="500" %}

After spectral estimation this would lead to a consistent decrease in the line noise towards the middle of the trials. Note that it depends on the spectral estimation technique and the data padding during filtering whether and how the residual line noise will express itself.

One way to get rid of this residual line noise is to use a DFT filter at multiple frequencies that are close to the line noise frequency. Another is to use a bandstop filter (see the magenta line in the third figure).
