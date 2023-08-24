---
title: Check the consistency between the documentation and the implementations
---

{% include /shared/development/warning.md %}

# Check the consistency between the documentation and the implementations

## Objectives

- the reference documentation should be included in the m-files (i.e. "help function_name")
- the documentation should be complete w.r.t. the underlying implementation
- the documentation should be up-to-date, and should be easily kept up-to-date
- the structure between the functions should become more transparent

The help of any function could look like this

    % FUNNAME does something useful
    %
    % Use as
    %    output = funname(cfg, input)
    % where the input is the result from OTHER_FUNNAME
    %
    % The cfg contains
    %   cfg.xxx =
    %   cfg.xxx =
    %   cfg.xxx =
    %   cfg.xxx =
    %
    % See also OTHER_FUNNAME, and other related functions

The second commented block in each file (i.e. which is not visible when you type help, but which is visible if you edit the file) can contain the more advanced and obscure options. Furthermore, it can contain a description of the dependencies of the reference documentation of this function on the documentation in other (private) functions.

    % Undocumented local options
    %   cfg.yyy
    %   cfg.yyy
    %   cfg.yyy
    %   cfg.yyy
    %   cfg.yyy
    %
    % This function depends on prepare_zzz, which has the following options
    %   cfg.zzz
    %   cfg.zzz
    %   cfg.zzz
    %   cfg.zzz
    %   cfg.zzz
    %
    % This function depends on prepare_aaa, which has the following options
    %   cfg.aaa
    %   cfg.aaa
    %   cfg.aaa
    %
    % ...

## Step 1: get an overview of all undocumented options

All 0th order (local options) and 1st order (direct dependency on a private function) dependencies are now included in the "undocumented options" section in each m-file. Status: done.

## Step 2: ensure consistency between the documentation of cfg options in different functions

Status: done.

## Step 3: automatize the creation of the html documentation for the FieldTrip site

The documentation should consist of an overview of the main commands with the complete help similar as in MATLAB ([reference](/reference)) and an index with all [cfg options](/configuration). Status: done.

These should be cross-linked. Status: no attempts yet.

## Appendix: some useful unix commands

Finding all configuration option

```bash
grep -o 'cfg\.[a-zA-Z0-9]_' function_name.m
grep -o 'cfg\.[a-zA-Z0-9]_' _.m
grep -o 'cfg\.[a-zA-Z0-9]_' function_name.m | sort | uniq
grep -o 'cfg\.[a-zA-Z0-9]_' _.m | sort | uniq
```

Getting the Nth paragraphs of a text file (the N below should be changed into a number)

```bash
cat function_name.m | awk "BEGIN {t=1}; /^$/ {t=t+1}; !/^$/ {if ((t-N)==0) print}"
```

Get a set of files that describe all configuration options in the help and in the code, and determine the configuration options that are missing from either the help or the code:

```bash
for file in _.m ; do grep -v '^%' \$file | grep -o 'cfg\.[a-zA-Z0-9]_' | sort | uniq > $file.cfg_code ; done
for file in *.m ; do grep    '^%' $file | grep -o 'cfg\.[a-zA-Z0-9]_' | sort | uniq > \$file.cfg_help ; done
for file in _.m ; do diff $file.cfg_* > $file.diff ; done
for file in _.diff ; do grep '^`<' $file | tr '<' '%' >` \$file.missing_help ; done
for file in _.diff ; do grep '^>' $file | tr '>' '%' > $file.missing_code ; done
```
