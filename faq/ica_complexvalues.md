---
title: Why does my ICA output contain complex numbers?
category: faq
tags: [ica]
redirect_from:
    - /faq/why_does_my_ica_output_contain_complex_numbers
---

# Why does my ICA output contain complex numbers?

Independent component analysis (ICA) can not return more components than the [rank](<https://en.wikipedia.org/wiki/Rank_(linear_algebra)>) of your data. For example, if your data contains 100 linearly independent channels, then the rank of your data would be 100, and you can compute up to 100 independent components. If your data contains 100 channels, of which 99 channels are independent but channel 100 is dependent on channel 99 (e.g., chan100 = -chan99), then the max number of independent components to fully describe your data would be 99. If you try to compute 100 components on this data set, it will fail. Componentanalysis will either return an error, or get into a loop and eventually give you output that contains complex numbers.

This might occur when you have EEG data which is re-referenced using the common average reference, with EEG data that has the reference channel included in the data structure, or with (Neuromag) MEG data that has been MaxFiltered.

The following shows how to exclude the reference channel, before calling ft_componentanalysis:

    cfg = [];
    cfg.channel = {'all', '-refchan'};
    test = ft_componentanalysis(cfg, data);

Or, alternatively, if you want to keep all the channels:

    cfg = [];
    cfg.runica.pca = 99;     % channel number minus the number of dependent channels, in case of the example above 100-1=99
    test = ft_componentanalysis(cfg, data);

This returns 99 components, and after back projection gives you again your 100 channels, which can be useful for plotting/interpretation purposes. The last snippet of code can in general be applied. So, when having Neuromag MaxFiltered data with a rank of 60, the `cfg.runica.pca` argument should be set to 60 (or less).

Note that for independent component analysis with ft_componentanalysis, the EEGlab toolbox is required.
