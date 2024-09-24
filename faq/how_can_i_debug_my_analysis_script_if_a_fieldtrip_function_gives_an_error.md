---
title: How can I debug my analysis script if a FieldTrip function gives an error?
category: faq
tags: [debug]
---

# How can I debug my analysis script if a FieldTrip function gives an error?

You may write an elaborate data analysis pipeline in a script, which calls other data analysis scripts. If you get an error in such a nested combination of scripts, it might be difficult to debug because reaching the error takes a long time and MATLAB bails out as soon as the error happens.

## Standard MATLAB debugging

One standard way available in MATLAB is to use the built-in [debugger](http://www.mathworks.com/help/matlab/debugging-code.html). Most frequently, you will want to do

    dbstop if error

which will stop the debugger in case an error is detected. The presently running function will be loaded into the editor and the debugger will point to the line at which the error was detected.

## FieldTrip specific debugging

Another way of debugging an analysis pipeline is by using the FieldTrip debugging functionality. If you add

    cfg.debug = 'saveonerror'

to your high-level FieldTrip function calls, the function that detects the error will save its input arguments to a temporary mat file. There are multiple options for the cfg.debug field: 'display', 'displayonerror', 'displayonsuccess', 'save', 'saveonerror', saveonsuccess' or 'no' (which is the default).

For example, the following will result in an error because of the invalid input data structure:

    >> cfg = [];
    >> cfg.debug = 'saveonerror'
    >> ft_timelockanalysis(cfg, [])

---

    An error was detected while executing ft_timelockanalysis
    Saving debug information to /private/tmp/ft_timelockanalysis_20140719T103549.mat

---

    Error using ft_checkdata (line 442)
    This function requires raw+comp or raw data as input.

    Error in ft_timelockanalysis (line 105)
    data = ft_checkdata(data, 'datatype', {'raw+comp', 'raw'}, 'feedback', 'yes', 'hassampleinfo', 'yes');

Although the error is not resolved, you can load the file from disk and directly zoom in on the problematic piece of code. It might be that your configuration is inconsistent with the data, that the data is incompatible with the function (as above), or that there is a bug in the FieldTrip code (see [issues](/development/issues)).

You can load the input variables to the function (and some extra information from the file).

    >> load /private/tmp/ft_timelockanalysis_20140719T103549.mat
    >> whos
    Name              Size            Bytes  Class     Attributes

    cfg               1x1             17670  struct
    data              0x0                 0  double
    funname           1x19               38  char
    last_err          1x89              178  char
    last_error        1x1              2396  struct
    last_warning      0x0                 0  char

This allows you to replicate the same error very quickly, but now with "dbstop on error" to look into the details of the problem. Even without knowing the function name, you can do

    feval(funname, cfg, data)

to replicate the error.

## Use FieldTrip debugging everywhere

It is likely that you don't want to edit all of your analysis scripts to add

    cfg.debug = 'saveonerror'

to each individual function call. It is possible to enable this behavior globally, using the `ft_default` global variable.

    global ft_default
    ft_default.debug = 'saveonerror'

The fields in `ft_default` are merged with the input cfg structure to all FieldTrip functions. This is explained in more detail in **[ft_defaults](/reference/ft_defaults)**.
