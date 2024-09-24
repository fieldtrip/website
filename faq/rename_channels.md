---
title: How can I rename channels in my data structure?
category: faq
tags: [preprocessing, montage]
---

# How can I rename channels in my data structure?

You may have a data file that includes channel names that don't match the proper name, or in which the channel names don't match the sensor positions (for example with OPM sensors). The **[ft_preprocessing](/reference/ft_preprocessing)** will return that data with the original channel names. One way to rename the channel names is by doing it by hand using standard MATLAB code. However, the preferred way of doing it is by using a montage.

    montage = [];
    montage.labelold = {'1', '2', '3', ...};        % cell-array with N labels
    montage.labelnew = {'Cz', 'Pz', 'AFz', ...};    % cell-array with N labels
    montage.tra = eye(length(montage.labelold));    % N-by-N identity matrix 

Subsequently you can use the **[ft_preprocessing](/reference/ft_preprocessing)** function to apply the montage to the existing data to change the old into the new labels.

    cfg = [];
    cfg.montage = montage;
    datanew = ft_preprocessing(cfg, dataold);

Channels in the input data that are _not_ in the montage will be retained with the same label in the output data, so you can also use this to rename a single channel.

To do the renaming as early as possible, you can already include the `cfg.montage` option in the initial preprocessing.

    cfg = [];
    cfg.dataset = 'filename.ext'
    cfg.montage = montage;
    data = ft_preprocessing(cfg);

Montages can be used for more complex tasks, such as re-referencing EEG and iEEG data as explained in [this example page](/example/rereference/#montage). See also the help of **[ft_apply_montage](/reference/forward/ft_apply_montage)**, which is the low-level function that implements the montage.
