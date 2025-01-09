---
title: What kind of filters can I apply to my data?
parent: Artifacts
category: faq
tags: [preprocessing, timelock, freq, artifact, filter]
redirect_from:
    - /faq/what_kind_of_filters_can_i_apply_to_my_data/
---

# What kind of filters can I apply to my data?

The **[ft_preprocessing](/reference/ft_preprocessing)** function in FieldTrip implements a Butterworth and a FIR filter, for low-pass, high-pass and band-pass filtering (cfg.lpfilter/hpfilter/bpfilter). Furthermore, you can specify the filter order and the filter direction. Default is to apply a two-pass filter (forward and reverse), which results in a zero-phase shift of your ERP components.

Besides these "conventional" filters, during preprocessing you can also apply a very sharp discrete Fourier transform filter (cfg.dftfilter). To make this dft filter very sharp, you have to pad the data to a large amount (cfg.padding), e.g., to 5 or 10 seconds. The DFT filter is effective in removing the 50 Hz line noise (and the harmonics at 100 and 150 Hz). After DFT filtering and multitaper frequency analysis, you will not notice any line noise in the power spectra any more.
