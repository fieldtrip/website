---
title: Implement function that checks consistency of cfgs
---

{% include /shared/development/warning.md %}


## Objectives

1.  For the user: input cfgs should be adjusted when necessary and possible, and feedback (warning/error) should be given when **required** options are missing or when **forbidden** or **deprecated** options are used. This should replace the current 'backward compatibility' code.
2.  Internal use: checkconfig should control the relevant cfg options that are being passed on to other functions.
3.  Output: only relevant cfg fields should be contained in the output (data.cfg), e.g., it should not contain unused default settings.

## Relevant functions

Overview of relevant functions where checkconfig should be implemented:

- preprocessing ------step1=done------
- private/preproc (uses cfg.preproc)
- artifact functions ------step1=done------
- timelockanalysis ------step1=done------
- freqanalysis ------step1=done------
- sourceanalysis ------step1=done------
- private/prepare_dipole_grid (uses cfg.grid)
- statistics functions!!
- perhaps also other private functions that take a cfg as input

Overview of existing relevant function

- createsubcfg
- checkconfig
- check_cfg_unused
- check_cfg_required

## Step 1

Add the check (objective 1) to the existing functions.

**Required**: check whether required options are present, give error when missing

- e.g.: sourceanalysis: method; xxxstatistics: method
- ...(perhaps in general search for cfg.method using grep and check whether this is a more common required feature)

**Renamed**: change old options/values into new ones + give warning

- this should replace most of the backward compatibility code regarding renamed options and values

**Deprecated**: give warning when deprecated options are used

- search for that using grep

**Forbidden**: give error when forbidden option is used

- e.g., cfg.trl when calling preprocessing on data that has already been read

## Step 2

Incorporate existing functions in checkconfig:

- createsubcfg - done -
- dataset2files - done -

## Step 3

Control the output cfg:

- report on used/unused fields (trackconfig)
- remove unused fields from output cfg (trackconfig)
- remove large fields from output cfg (checksize)

**trackconfig:**

{% include markup/red %}
In November 2022 the config object and the `cfg.trackconfig` functionality have been removed, see <https://github.com/fieldtrip/fieldtrip/issues/2127>.
{% include markup/end %}

- controlled via ft_defaults or overruled by cfg.trackconfig: 'report', 'cleanup', or 'off'
- start of each FT function: cfg=checkconfig(cfg) >> if user requests report or cleanup, configtracking is turned on
- end of each FT function: cfg=checkconfig(cfg, 'trackconfig', 'off')

**checksize:**

- controlled via ft_defaults or overruled by cfg.checksize: inf or number in bytes
- end of each FT function: cfg=checkconfig(cfg, 'checksize', 'yes')
