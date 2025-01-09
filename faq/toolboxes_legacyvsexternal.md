---
title: Can I prevent "external" toolboxes from being added to my MATLAB path?
parent: MATLAB questions
category: faq
tags: [matlab, toolbox, path]
redirect_from:
    - /faq/can_i_prevent_external_toolboxes_from_being_added_to_my_matlab_path/
---

# Can I prevent "external" toolboxes from being added to my MATLAB path?

The recommended path settings are explained in this [frequently asked question](/faq/installation).

The code in the **[ft_defaults](/reference/ft_defaults)** function will execute only once and should preferably be executed in your `startup.m` file. The main FieldTrip functions will also call **[ft_defaults](/reference/ft_defaults)** to ensure that the required subdirectories are on the path.

The **[ft_defaults](/reference/ft_defaults)** will also add some toolboxes from external to your path, such as external/signal, external/stats and external/image. These contain drop-in [replacements for some MATLAB functions](/faq/matlab_replacements) to reduce the requirements on the (network) licenses, which are often available in a limited number.

If you don't want these replacement functions on your path, you can do the following in your `startup.m` file.

    global ft_default
    ft_default.toolbox.signal = 'matlab';  % can be 'compat' or 'matlab'
    ft_default.toolbox.stats  = 'matlab';
    ft_default.toolbox.image  = 'matlab';
    ft_defaults % this sets up the FieldTrip path

Alternatively, to remove them at a later stage you can do the following

    [ftver, ftpath] = ft_version;
    rmpath(fullfile(ftpath, 'external', 'signal'))
    rmpath(fullfile(ftpath, 'external', 'stats'))
    rmpath(fullfile(ftpath, 'external', 'image'))
