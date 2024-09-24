---
title: How do I prevent FieldTrip from printing the time and memory after each function call?
category: faq
tags: [matlab]
---

# How do I prevent FieldTrip from printing the time and memory after each function call?

To inform the user about the requirements of each function call and thereby give him/her a better feeling on how to optimize the analysis using distributed computing, each FieldTrip function estimates the time and memory(\*) it requires. This information about the call is printed at the end of the function, like this

    cfg = [];
    cfg.dataset = 'Subject01.ds';
    data = ft_preprocessing(cfg);

    processing channel { 'STIM' 'SCLK01' ... 'MZO01' 'MZO02' 'MZP01' 'MZP02' 'EOG' }
    reading and preprocessing
    reading and preprocessing trial 1 from 266
    reading and preprocessing trial 2 from 266
    ...
    reading and preprocessing trial 266 from 266
    the call to "ft_preprocessing" took 14 seconds and an estimated 386 MB

If you do not want the time and memory to be printed, you can specify cfg.showcallinfo='no' instead of the default 'yes'. This is something you can do for every function separately, like this:

    cfg = [];
    cfg.dataset = 'Subject01.ds';
    cfg.showcallinfo = 'no';
    data = ft_preprocessing(cfg);

You can also pass it as a general option to all functions like this:

    global ft_default
    ft_default.showcallinfo = 'no';

The configuration options in the `ft_default` global variable are (in general) on startup of each FieldTrip function merged with the configuration options that you pass to that function.

Of course you can add this general setting to your `startup.m` file so that you don't have to type it each time that you start MATLAB.

\*) Note that the memory estimate is currently not yet available on Windows.
