---
title: ft_defaults
---
```
 FT_DEFAULTS (ending with "s") sets some general settings in the global variable
 ft_default (without the "s") and takes care of the required path settings. You can
 call this function in your startup.m script. This function is also called at the
 begin of all FieldTrip functions.

 The global configuration defaults are stored in the global "ft_default" structure.
 The ft_checkconfig function that is called by many FieldTrip functions will merge
 these global configuration defaults with the cfg ctructure that you pass to
 the FieldTrip function that you are calling.

 The global options and their default values are
   ft_default.checkconfig       = string, can be 'pedantic', 'loose', 'silent' (default = 'loose')
   ft_default.checkpath         = string, can be 'pedantic', 'once', 'no' (default = 'pedantic')
   ft_default.checksize         = number in bytes, can be inf (default = 1e5)
   ft_default.showcallinfo      = string, can be 'yes' or 'no' (default = 'yes')
   ft_default.trackconfig       = string, can be 'cleanup', 'report', 'off' (default = 'off')
   ft_default.trackusage        = false, or string with salt for one-way encryption of identifying information (by default this is enabled and an automatic salt is created)
   ft_default.trackdatainfo     = string, can be 'yes' or 'no' (default = 'no')
   ft_default.trackcallinfo     = string, can be 'yes' or 'no' (default = 'yes')
   ft_default.outputfilepresent = string, can be 'keep', 'overwrite', 'error' (default = 'overwrite')
   ft_default.debug             = string, can be 'display', 'displayonerror', 'displayonsuccess', 'save', 'saveonerror', saveonsuccess' or 'no' (default = 'no')
   ft_default.toolbox.signal    = string, can be 'compat' or 'matlab' (default = 'compat')
   ft_default.toolbox.stats     = string, can be 'compat' or 'matlab' (default = 'compat')
   ft_default.toolbox.images    = string, can be 'compat' or 'matlab' (default = 'compat')
   ft_default.reproducescript   = string, directory to which the script and intermediate data are written (default = [])

 If you want to overrule these default settings, you can add something like this in your startup.m script
   ft_defaults
   global ft_default
   ft_default.option1 = value1
   ft_default.option2 = value2

 The toolbox option for signal, stats and images allows you to specify whether you
 want to use a compatible drop-in to be used for these MathWorks toolboxes, or the
 original version from MathWorks.  The default is 'compat', which has the advantage
 that you do not need a license for these toolboxes.

 See also FT_HASTOOLBOX, FT_CHECKCONFIG, FT_TRACKUSAGE
```
