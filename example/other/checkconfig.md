---
title: How to use ft_checkconfig
category: example
tags: [cfg]
redirect_from:
    - /example/checkconfig/
---

The function **[ft_checkconfig](/reference/utilities/ft_checkconfig)** is used in the main FieldTrip functions and checks the input configuration (cfg). This is similar to what **[ft_checkdata](/reference/utilities/ft_checkdata)** does for the input data. The **[ft_checkconfig](/reference/utilities/ft_checkconfig)** function is automatically called when you use a FieldTrip function. You may not even notice this, unless it gives you feedback about your cfg,m for example with a warning or error message.

This example explains what **[ft_checkconfig](/reference/utilities/ft_checkconfig)** does, and importantly, how you can control it and use it to your advantage!

## Introduction to ft_checkconfig

This function checks whether the cfg contains all the required options, it gives a warning when renamed or deprecated options are used, and it makes sure no forbidden options are used. If necessary and possible, this function will adjust the cfg to the input requirements. If the input cfg does NOT correspond to the requirements, this function gives an elaborate warning message.

Furthermore, it controls the relevant cfg options that are being passed on to other functions, by putting them into substructures or by converting them into the required format.

## How to control the behavior of ft_checkconfig

Any high-level FieldTrip function that you call automatically uses **[ft_checkconfig](/reference/utilities/ft_checkconfig)** to check the cfg you supplied. If necessary, **[ft_checkconfig](/reference/utilities/ft_checkconfig)** will give you feedback. How can you control this feedback? As explained in the help documentation:

    % The behavior of checkconfig can be controlled by the following cfg options,
    % which can be set as global FieldTrip defaults (see FT_DEFAULTS)
    %   cfg.checkconfig = 'pedantic', 'loose' or 'silent' (control the feedback behavior of checkconfig)
    %   cfg.checksize   = number in bytes, can be inf (set max size allowed for output cfg fields)

You can specify these two options yourself in your scripts. However, it is likely that you will always want to have the same behavior.

When you use a FieldTrip function, this automatically calls the function `ft_defaults`, which takes care of path setting, plus it sets defaults to be used throughout FieldTrip. It does this by creating a global variable called `ft_default` (without the 's') that is globally available to all functions everywhere, but not directly visible to the user. You can make it visible by typing `global ft_default`. The variable `ft_default` includes the following fields that you can change.

    ft_default.checkconfig = 'loose'; % or 'pedantic' or 'silent'
    ft_default.checksize   = 1e5;

**cfg.checkconfig: 'pedantic', 'loose' or 'silent'**

This setting determines the type of feedback **[ft_checkconfig](/reference/utilities/ft_checkconfig)** gives about options specified in the cfg that have been renamed, that are unused, deprecated or forbidden. If possible, **[ft_checkconfig](/reference/utilities/ft_checkconfig)** will adjust the cfg to the input requirements and give feedback to the user. You can control the type of feedback given. This can either be **'silent'**, which means no feedback is given at all, or **'loose'** which means warnings are given for all inconsistencies, or **'pedantic'**, which means errors are given for each inconsistency in your input cfg. Note that a missing required field in the cfg will always lead to an error, because FieldTrip simply will not run without it.

To give an example using **[ft_freqdescriptives](/reference/ft_freqdescriptives)**, if your cfg contains the field 'jacknife' (which was used in a previous version of FieldTrip but has since been renamed to 'jackknife'

    cfg = [];
    cfg.jacknife = 'no';
    test = ft_freqdescriptives(cfg, freq)

You will get the following feedback

    Warning: use cfg.jackknife instead of cfg.jacknife

In this case, you don't have to do anything: **[ft_checkconfig](/reference/utilities/ft_checkconfig)** will rename the field for you, and **[ft_freqdescriptives](/reference/ft_freqdescriptives)** can do its job. Of course the idea is, that you will use this feedback to improve your scripts!

_Note: the feedback **[ft_checkconfig](/reference/utilities/ft_checkconfig)** gives on your input cfg is not exhaustive, meaning that not all possible options you could come up with will be taken care of. It mainly ensures backward compatibility of old scripts, and checks some important required and forbidden fields._

**cfg.checksize: number in bytes, can be inf**

This determines the maximum size allowed for output cfg fields (i.e. the outputdata.cfg). Some fields in the output cfg can be very large, e.g., the cfg.sourcemodel field when you do `ft_sourceanalysis` with precomputed leadfields. To avoid that several MBs or even GBs of your memory and disk space are taken up by the outputdata.cfg, you can set a maximum and **[ft_checkconfig](/reference/utilities/ft_checkconfig)** will empty all the cfg fields that are too big, before adding the cfg to the data. Crucial fields such as the cfg.trl and cfg.event will never be removed. Currently, the following fields are ignored: 'checksize', 'trl', 'trlold', 'event', 'artifact', 'artfctdef', 'previous'). The default is set to 1e5 bytes, i.e., 100kB. If you do not want any fields to be removed, set it to `Inf`.

## How to use cfg.checksize to save disk space

As explained above, you can use cfg.checksize to set a limit to the size of fields in the output cfg, **[ft_checkconfig](/reference/utilities/ft_checkconfig)** then empties fields that are too big. Crucial fields such as the trl will never be removed. This all pertains to the output cfg, i.e. the cfg that comes out of the function (depending on the FieldTrip function you are using, this is either cfg or data.cfg). This does _not_ change any data.cfg.previous fields.

However, you may have lots of analysed data on disk, with data.cfgs that might be taking up quite some of your disk space. Especially after doing beamforming (sourceanalysis) the output cfg can be large, since the grid is always kept in the data.cfg. If you would like to free some disk space (and are sure you can do without these fields), the following trick can be applied

    %%% script to downsize cfgs of stored data
    %%% this can free up significant amounts of disk space

    downsizefiles={
      '/mydir/dataset1'
      '/mydir/dataset2'
      '/mydir/etc.'};

    for k=1:length(downsizefiles)
      load(downsizefiles{k}); % here we assume that this contains the variable 'data'

      data.cfg.checksize = 100000;
      data.cfg = ft_checkconfig(data.cfg, 'checksize', 'yes');

      save(downsizefiles{k}, 'data')
    end

This way **[ft_checkconfig](/reference/utilities/ft_checkconfig)** will run recursively through the entire data.cfg, including all the previous fields, and empty the fields that are larger than the specified limit.
