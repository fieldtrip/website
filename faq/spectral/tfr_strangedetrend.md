---
title: Why does my TFR look strange (part II, detrending)?
category: faq
tags: [mtmconvol, freq, preprocessing, artifact, filter]
redirect_from:
    - /faq/why_does_my_tfr_look_strange_part_ii/
    - /faq/tfr_strangedetrend/
---

If you use 'mtmconvol' as a method for frequency analysis it could happen that the Time-Frequency Representation of your data looks like this:

{% include image src="/assets/img/faq/tfr_strangedetrend/strangetfr3.png" width="400" %}

This phenomenon is caused by the time domain data having a slow low-frequency drift. This low-frequency component leaks into the estimates of all time-frequency points in a variable (but patterned) way. The reason why this actually happens is related to the fact that none of the tapered basis functions (i.e. windowed sine and cosine waves of increasing frequency) are exactly orthogonal to this slow drift.

The solution to this problem is to detrend or high-pass filter your data prior to calling ft_freqanalysis:

    cfg = [];
    cfg.detrend = 'yes';
    data = ft_preprocessing(cfg, data);

The following code shows the effect of a large amplitude low-frequency drift on the TFR:

    % create some data
    data = [];
    data.time{1}  = [-1749:1750]./1000;
    data.trial{1} = -3499:2:3499;
    data.fsample  = 1000;
    data.label    = {'chan01'};
    figure;plot(data.time{1}, data.trial{1});

    % do spectral analysis
    cfg        = [];
    cfg.method = 'mtmconvol';
    cfg.toi    = -1.5:0.005:1.5;
    cfg.foi    = 4:4:80;
    cfg.t_ftimwin = ones(1,numel(cfg.foi)).*0.5;
    cfg.taper  = 'hanning';
    cfg.polyremoval = -1; %see below
    freq       = ft_freqanalysis(cfg, data);

    % plot
    cfg = [];
    cfg.baseline = [-1.5 -0.5];
    cfg.baselinetype = 'relchange';
    figure; ft_singleplotTFR(cfg, freq);

## Figure: Example data with a large amplitude low-frequency drift (1st) and its TFR (2nd)

{% include image src="/assets/img/faq/tfr_strangedetrend/strangetfr4.png" width="300" %}
{% include image src="/assets/img/faq/tfr_strangedetrend/strangetfr3.png" width="300" %}

## cfg.polyremoval

**Note,** in the above code `cfg.polyremoval = -1`. This option has been introduced in July 2011 (see [this email thread](http://mailman.science.ru.nl/pipermail/fieldtrip/2012-January/004666.html)). The default behavior is cfg.polyremoval = 0, which means that the zero-order polynomial is removed, which is equal to demeaning. So if you're just using the default in ft_freqanalysis, your data will NOT be automatically detrended, thus you do have to specify `cfg.detrend = 'yes'` separately in ft_preprocessing to avoid these surprising effects. Alternatively, you can call ft_freqanalysis with `cfg.polyremoval = 1`, which removes BOTH the zero-order (demeaning) and first-order (detrending) polynomial. Also see [Why does my TFR look strange (part I, demeaning)?](/faq/spectral/tfr_strangedemean).

FYI, you can also specify a higher value (removing higher order polynomials), a value of 0 (only removing the mean), or -1 (no removal at all).
