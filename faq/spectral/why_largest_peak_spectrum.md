---
title: Why is the largest peak in the spectrum at the frequency which is 1/segment length?
category: faq
tags: [mtmfft, freq, demean]
redirect_from:
    - /faq/why_largest_peak_spectrum/
    - /faq/why_largest_peak_spectrum/
---

# Why is the largest peak in the spectrum at the frequency which is 1/segment length?

If you use 'mtmfft' as a method for frequency analysis it could happen that apparently the largest peak in the spectrum is invariably at the first non-zero frequency bin. In addition, when changing the epoch length, e.g., by cutting a long data segment into 1-second snippets, rather than into 1-second segments, it seems that this peak is shifting from 0.5 to 1 Hz.

This phenomenon is caused by the discrete nature of the spectral transformation, and by one of the default algorithmic details of the spectral decomposition in FieldTrip. Specifically, FieldTrip removes the DC-component (signal mean) by default, prior to spectral transformation. This brings down the 0 Hz component to have a power of ~0. Next, if there's a 1/f power profile in the underlying data, the first non-zero frequency bin will show the highest power in the spectrum of the DC-corrected signal. The location of this first non-zero bin depends on the spectral resolution, which is determined by the segments' length.

If you don't want the DC-component to be removed prior to spectral transformation, you should specify the option ``cfg.polyremoval = -1`` before calling ``ft_freqanalysis``. The motivation for the DC-component removal is explained in the FAQ: [Why does my TFR look strange (part I)?](/faq/spectral/tfr_strangedemean)

    clear all;
    data.time{1} = (0:99999)./1000;
    data.label{1} = 'chan01';
    data.trial{1} = 1;
    for k = 2:100000
        data.trial{1}(k)=randn(1)+1.*data.trial{1}(k-1);
    end

    cfg2.method = 'mtmfft';
    cfg2.taper  = 'boxcar';

    L = [0.5 1 2 4];
    for k = 1:numel(L)
        cfg1.length = L(k);
        freq{1,k} = ft_freqanalysis(cfg2,ft_redefinetrial(cfg1,data));
    end
    figure;
    subplot(1,2,1); hold on;
    for k = 1:4
        plot(freq{k}.freq,log10(freq{k}.powspctrm));
    end
    xlim([0 10])
    ylim([-2 4]);

    cfg2.polyremoval=-1;
    for k = 1:4
        cfg1.length = L(k);
        freq{1,k}=ft_freqanalysis(cfg2,ft_redefinetrial(cfg1,data));
    end
    subplot(1,2,2);hold on;
    for k = 1:4
        plot(freq{k}.freq,log10(freq{k}.powspctrm));
    end
    xlim([0 10])
    ylim([-2 4])

### Figure: spectra from signal with large DC component with (left) and without (right) demeaning prior to ft_freqanalysis

{% include image src="/assets/img/faq/why_largest_peak_spectrum/spectra.png" width="400" %}
