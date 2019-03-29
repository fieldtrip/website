---
title: ft_checkconfig
---
```
 FT_CHECKCONFIG checks the input cfg of the main FieldTrip functions
 in three steps.

 1: It checks whether the cfg contains all the required options, it gives
 a warning when renamed or deprecated options are used, and it makes sure
 no forbidden options are used. If necessary and possible, this function
 will adjust the cfg to the input requirements. If the input cfg does NOT
 correspond to the requirements, this function gives an elaborate warning
 message.

 2: It controls the relevant cfg options that are being passed on to other
 functions, by putting them into substructures or converting them into the
 required format.

 3: It controls the output cfg (data.cfg) such that it only contains
 relevant and used fields. The size of fields in the output cfg is also
 controlled: fields exceeding a certain maximum size are emptied.
 This part of the functionality is still under construction!

 Use as
   [cfg] = ft_checkconfig(cfg, ...)

 The behavior of checkconfig can be controlled by the following cfg options,
 which can be set as global FieldTrip defaults (see FT_DEFAULTS)
   cfg.checkconfig = 'pedantic', 'loose' or 'silent' (control the feedback behavior of checkconfig)
   cfg.trackconfig = 'cleanup', 'report' or 'off'
   cfg.checksize   = number in bytes, can be inf (set max size allowed for output cfg fields)

 Optional input arguments should be specified as key-value pairs and can include
   renamed         = {'old',  'new'}        % list the old and new option
   renamedval      = {'opt',  'old', 'new'} % list option and old and new value
   allowedval      = {'opt', 'allowed1'...} % list of allowed values for a particular option, anything else will throw an error
   required        = {'opt1', 'opt2', etc.} % list the required options
   allowed         = {'opt1', 'opt2', etc.} % list the allowed options, all other options are forbidden
   forbidden       = {'opt1', 'opt2', etc.} % list the forbidden options, these result in an error
   deprecated      = {'opt1', 'opt2', etc.} % list the deprecated options
   unused          = {'opt1', 'opt2', etc.} % list the unused options, these will be removed and a warning is issued
   createsubcfg    = {'subname', etc.}      % list the names of the subcfg
   createtopcfg    = {'subname', etc.}      % list the names of the subcfg
   dataset2files   = 'yes', 'no'            % converts dataset into headerfile and datafile
   inside2logical  = 'yes', 'no'            % converts cfg.inside or cfg.sourcemodel.inside into logical representation
   checksize       = 'yes', 'no'            % remove large fields from the cfg
   trackconfig     = 'on', 'off'            % start/end config tracking

 See also FT_CHECKDATA, FT_DEFAULTS
```
