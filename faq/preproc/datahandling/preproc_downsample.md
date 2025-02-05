---
title: How can I preprocess a dataset that is too large to fit into memory?
category: faq
tags: [preprocessing, memory]
redirect_from:
    - /faq/how_can_i_preprocess_a_dataset_that_is_too_large_to_fit_into_memory/
    - /faq/preproc_downsample/
---

# How can I preprocess a dataset that is too large to fit into memory?

If your dataset is too large to fit into memory at once, you can preprocess one channel at a time With **[ft_preprocessing](/reference/ft_preprocessing)**, immediately combined with **[ft_resampledata](/reference/ft_resampledata)**. After gathering all downsampled channels, you can combine them again into a normal multi-channel data structure.

In summary, the code would look like this:

    for i=1:nchans
    cfgp         = [];
    cfgp.dataset = 'yourfile.dat';
    % instead of specifying channel names, you are allowed to use channel numbers
    cfgp.channel = i;
    datp         = ft_preprocessing(cfgp);

    cfgr            = [];
    cfgr.resamplefs = 250;
    datr{i}         = ft_resampledata(cfgr, datp);

    clear datp
    end

    cfg = [];
    datall = ft_appenddata(cfg, datr{:}); % this expands all cells into input variables
