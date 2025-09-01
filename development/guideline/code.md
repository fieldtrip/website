---
title: Code guidelines
tags: [guidelines, development, fixme]
---

# Code guidelines

A recent paper "Best Practices for Scientific Computing" which can be found [here](http://arxiv.org/pdf/1210.0530v1.pdf) provides a very accessible account of things you should consider when developing software such as FieldTrip. It is recommended reading material for all contributors.

When you contribute new code or make changes to existing code, please consider the following guidelines.

## Implementing a new high-level function

A high-level FieldTrip function always should behave like this

    [outputargs] = ft_functionname(cfg, inputargs)

where some functions might not need _inputargs_ and some functions might not return _outputargs_.

The function should always start with a help section, that explains the purpose of the function, the type of input data that it expects, the type of output data that it will produce and the configurable options that the user has to control the behavior of the function.

### The best-practice example function

The easiest way to get started with writing a new high-level FieldTrip function is to take a close look at [ft_examplefunction](/reference/ft_examplefunction), which is located in FT's core (root) directory. (Note: this is true as of Feb 11, 2011.) It shows the best practices that one should adhere to concerning input and output structure and data handling. Also, it demonstrates how one should document the function according to FT standard guidelines.

## Provide reference documentation in the function help

The help of all FieldTrip functions is listed in the [reference](/reference) documentation. To allow for cross-linking, please use the "See also" section at the bottom of the function help.

To explain what the input and output data structures of the function are, please document it as

    Use as

[output] = ft_xxxxxx(cfg, input)
[output] = ft_xxxxxx(cfg, input1, input2)

where output and input, input1, input2 are the standard names of data types, such as raw, timelock, freq, source, volume, spike. Pleae look in **[ft_datatype](/reference/utilities/ft_datatype)** for a complete list and pointers to the detailed documentation on the standard datatypes.

## Provide the appropriate level of feedback to the user

It is important to provide appropriate feedback to the user when the code is running or when its execution is terminated because of an error.

There are 5 different ways of doing this.

- **silent**: It is not communicated what happens during running the script. For example, details of computations that the user does not need to know are not communicated.
- **print**: Notifications are printed on screen. E.g.: “processing trials”, "5 trials rejected with artifacts". Via these prints the user is informed that the expected operations are taking place. These are really important when it is not obvious in the output whether an operation has really occurred. When such prints appear on screen the user also knows the processing of the input started and where it is at the moment. This is important when the functions do time-consuming computations.
- **warning once**: A warning printed on screen (i.e. a short text message starting with "Warning: ...") when it occurs _first_. This was implemented to avoid many warnings when a function is executed more times after each other.
- **warning**: A warning printed on screen. E.g.: “Warning: no baseline correction”. Warnings are used when the user's input is not erroneous in certain context but it could lead to an error or sub-optimal analysis in another context. The user can re-consider whether the right input was used.
- **error**: Error printed on screen and the process is terminated. This happens when the input does not make sense or is obviously wrong. A short text message is provided with the error to point out why it has occurred.

When a new function is written in FieldTrip, it is important to include these feedbacks. Each warning and error should have an **identifier**. By using identifiers, the individual warnings can be switched off by the user in MATLAB. Hence, `warning_once` should be used cautiously.

The short text messages which accompany errors and warnings on the screen are often not enough to provide insight for the users. The text message on screen should be kept short, but a [Frequently Asked Question](/faq) should explain the warning and why an error occurred. The identifiers should help the user to find the relevant FAQ. The FAQ
should also have the same 'warning' or 'error' tag (e.g., `FieldTrip:fileio:fileNotExisting`).

## Use the dimord field to describe or decipher the data

In general (although some exceptions apply, see below) the specification of the dimensions in the data structure is like this

    datastructure.aaa = 2-D array
    datastructure.aaadimord = 'xxx_yyy'
    datastructure.xxx = scalar vector or cell-array that describes the 1st dimension
    datastructure.yyy = scalar vector or cell-array that describes the 2st dimension

This can be extended like

    datastructure.aaa
    datastructure.aaadimord = 'xxx_yyy'
    datastructure.bbb
    datastructure.bbbdimord = 'yyy_zzz'
    datastructure.xxx
    datastructure.yyy
    datastructure.zzz

In case multiple fields in a structure have the same dimord, it is allowed to specify

    datastructure.aaa
    datastructure.bbb
    datastructure.dimord = 'xxx_yyy' % applies to aaa and bbb
    datastructure.xxx
    datastructure.yyy

And furthermore

    datastructure.aaa
    datastructure.bbb
    datastructure.dimord = 'xxx_yyy' % applies to all fields that do not specify their own dimord
    datastructure.ccc
    datastructure.cccdimord = 'yyy_zzz' % applies only to ccc
    datastructure.xxx
    datastructure.yyy
    datastructure.zzz

If a structure only contains a single data field, all fields (i.e. the only one) have the same dimensions and therefore a general dimord can be used instead of a field-specific one. So the structure would be

    datastructure.aaa = 2-D array
    datastructure.dimord = 'xxx_yyy'
    datastructure.xxx = scalar vector or cell-array that describes the 1st dimension
    datastructure.yyy = scalar vector or cell-array that describes the 2st dimension

Some high-level FieldTrip functions allow or require the specification of the parameter on which to perform their algorithm, whereas other functions do not require or allow the parameter to be specified. If the parameter is not specified, and if the non-specific “dimord” only refers to a single data field, that field is considered to be the main data and will be used as input for the algorithm.

The known exceptions are

- the dimension 'chan' is described with the cell-array vector 'label'
- the dimension 'chancmb' is described with the cell-array 'labelcmb', which is a Nx2 array
- if the dimension is indicated as '{xxx}', then it refers to a cell-array description. An example is '{pos}\_ori_time' for vector dipole moments as a function of time, that are estimated for multiple dipole positions. The positions are here represented in a cell-array to allow for positions (from a 3-D regular grid) outside the brain where the computation is not done. The alternative would be to use a 3D array with pos_ori_time with NaNs to indicate that the data at some positions does not apply, but that is memory-wise inefficient.
- if the dimension is indicated as '(xxx)', then it refers to a struct-array description. We don't have this worked out in detail and we don't use it.
- some fields contain supportive information and not actual data, and therefore are not described with a dimord. Examples are cumtapcnt, sampleinfo, trialinfo.
- some dimensions do not have an explicit description and are only implicitly numbered. examples are “comp” and “rpt”.
- rpt is used for repetitions, which are usually trials, but in timelock (ERP) structures we use “rpt" and “subj” interchangeably. The dimord “subj_chan_time" is used to represent an ERP that cas been concatenated over subjects.

To determine the dimord, you should use the **fieldtrip/private/getdimord** function. The **getdimord** function can be followed by **tokenize**. To determine the length (number of elements) along each dimension, you should use the **fieldtrip/private/getdimsiz** function. If the length of the vector returned by **getdimsiz** is smaller than the number of dimensions, you should assume that it has trailing singleton dimensions.

## Adding new configuration options

Any new configuration option should have a default set at the beginning of the function. If you don't know a good default value, you should specify the default value as empty, i.e. `cfg.newoption = ft_getopt(cfg, 'newoption');`.

If you add a configuration option, you should check in the [configuration index](/configuration) whether a cfg option with similar functionality already exists in another function. Use identical names for identical functionality and try to keep the help similar if possible.

In general, for the default handling of cfg options, one should not use `if isfield(cfg, 'newoption')`, but always use `if isempty(cfg.newoption)`, given that the default option should always be defined at the top of the function.

## Renaming configuration options or values

Whenever you rename a configuration option, you have to ensure backward compatibility with the end-users' scripts that they have carefully crafted. Forcing the users to update the scripts every time we change something will scare them away. That is why you should use

    cfg = ft_checkconfig(cfg, 'renamed', {'oldoption', 'newoption'})

or

    cfg = ft_checkconfig(cfg, 'renamedval', {'option', 'oldval', 'newval'})

This will ensure that the user script will continue to work. Furthermore, he/she will get warning or error (depending on whether cfg.checkconfig is 'silent', 'loose' or 'pedantic').

## Removing configuration options

If you remove a configuration option from a function, you should ensure that the user of that function becomes aware of it. Sending an email to the mailing list is one option (and in general good), but it might be that he/she is not subscribed to the mailing list. That is why you should also add the following to the function

    cfg = ft_checkconfig(cfg, 'forbidden', 'oldoption')

In case the user still specifies the option, he/she will get warning or error (depending on whether cfg.checkconfig is 'loose' or 'pedantic').

## Document deprecated source code

Sometimes it is necessary to rename or remove a function, an option or a piece of code. We should try to keep FieldTrip backward compatible whenever we replace a function or an option with something else. However, it is not possible to maintain backward compatibility for ever and sometimes the requirements for the deprecated functionality interferes with other maintenance to the code or the implementation of new functionality. Therefore we should accommodate the possibility to remove deprecated functionality, i.e. make the functionality unsupported.

Sections of code or functions that are deprecated should be documented in the code as such, including the name of the person who deprecated it, the date at which it was deprecated, and possibly also a link to some background (e.g., link to GitHub Issues) and an estimate of when the support for the deprecated functionality can be removed altogether (i.e. an "expiration date"). Deprecated functions and options should also be added to [this list](/development/deprecated).

An example is

    % DEPRECATED by roboos on 17 May 2013
    % see <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=2171> for more details
    % support for this functionality can be removed at the end of 2013

## Graphics

### Graphical-User Interfaces (GUI)

If you want to add a user interface (ui) to a figure, use the functions uicontrol and ft_uilayout for setting it up. This helps to manage the different components. Try to keep ui-definitions at one place in the code to make the code more manageable for other developers. Please make yourself familiar with other functions with a GUI before programming one your own, e.g., ft_databrowser.

Some practical issue

- Use tags to identify components. Tags should have a sensible name to facilitate code readability. Tags should be named according to function (e.g., 'channelui') or according to type ('buttonui') or position in the ui ('leftui').
- If it makes sense to group ui elements together, do it as early as possible – it makes life easier. Do not retag otherwise!

Example of good ui code:

    % define sensible tag-descriptions
    uicontrol('tag', 'channelui', ...);
    uicontrol('tag', 'trialui', ...)

    % do tag-specific stuff, e.g.
    ft_uilayout(h, 'tag', 'channelui', 'width', 0.10, 'height', 0.05);
    ft_uilayout(h, 'tag', 'trialui',   'width', 0.05, 'height', 0.05);

    % retag
    ft_uilayout(h, 'tag', 'channelui', 'retag', 'viewui');
    ft_uilayout(h, 'tag', 'trialui',   'retag', 'viewui');

    % do common stuff, e.g.
    ft_uilayout(h, 'tag', 'viewui', 'hpos', 'auto', 'vpos', 0);

Example of bad ui code (please avoid this):

    % uninformative tags
    uicontrol('tag', 'group1', ...);
    uicontrol('tag', 'group2', ...);

    % stuff that could have been done together if retagged earlier
    ft_uilayout(h, 'tag', 'group1',  'width', 0.10, 'height', 0.05);
    ft_uilayout(h, 'tag', 'group2',  'width', 0.10, 'height', 0.05);

    % retag when it's too late
    ft_uilayout(h, 'tag', 'group2', 'visible', 'on', 'retag', 'group1');

### Figure handles and Handle Graphics 2

From MATLAB 2014b onwards, MathWorks introduced a new way of figure handling as a standard called Handle Graphics 2 (HG2). While in former MATLAB versions, a figure handle could be treated as a double variable, this is not the case for HG2 anymore, where figure handles are objects. These figure handle objects can, however, be casted to double. Thus, an initialization of a graphics handle cannot be done by setting it to \[], 0 or 1 anymore.

It is good practice in FieldTrip to name a figure according to the function that created it and the data that was put in. Due to HG2, a proper (i.e. compatible) code for this is

    set(gcf, 'Name', sprintf('%d: %s: %s', double(gcf), funcname, dataname));

gcf refers to the current figure handle. There are number of additional consequences of HG2, which are too numerous to list here. See [Bugzilla bug 2461](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=2461) for FieldTrip relevant issues. While this bug is being solved, the most prominent issues and their fixes will be listed there.

## Git commit log messages

Git commit messages should describe the change to the file or files. The log message should allow an end-user to realize that a recent change in the code may relate to the changed behavior that he/she observes. The log message should also allow another developer that is familiar with the particular code to understand why the code was changed, and what part of the code was changed.

Log messages don't have to be long, but they have to be clear to the intended audience: end-users and colleague developers. Log messages should also be clear for yourself, because sometimes you'll have to go back in a function to fix problems that were introduced by your own previous change.

To allow better human and machine readable changelogs, please start your log message with a single descriptive word and a hyphen to separate it from the actual description. Whenever applicable you should use the description "bugfix", "enhancement", "documentation", or "restructuring".

Examples of good and useful log messages are

    documentation - changed the documentation, no change to the code

    enhancement - added support for the new cfg.whatever option

    restructuring - changed the structure of the code, instead of .... it now works like ...

    bugfix - fixed a problem in xxx, in case of ... it did ..., whereas it should be doing ...

    bugfix - fixed the problem described in <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=50>

Examples of bad log messages are

    <empty>

    made a change in this function

    lot of small changes

    fixed a bug

## Public and private functions

In FieldTrip the interface towards the user is controlled by making only those functions publicly available that the end-user is supposed to call from the command-line or from a MATLAB script. Those functions are **public** and should be in the main directory or in one of the module directories.

Low-level functions that are only supposed to be called by other FieldTrip functions but not by the end-user should be in the private directories.

## Calling functions that are located elsewhere

Functions in a module, i.e. sub-directory, should **not** be calling any FieldTrip functions at a higher level. e.g., a function like fileio/xxx.m should only call other functions in fileio, in fileio/private or in an external toolbox.

This requirement on the dependencies ensures the [modular design](/development/architecture#modular-organization).

## Varargin arguments

Generally functions (e.g., in the plotting directory) have optional arguments as a pair
of inputs describing the name of one property and its value.
These arguments have to be handled at the very beginning inside the function, by setting a default value,
like this:

    function ft_plot_mesh(bnd, varargin)
    ...
    % get the optional input arguments
    facecolor   = ft_getopt(varargin, 'facecolor',   'white');
    vertexcolor = ft_getopt(varargin, 'vertexcolor', 'none');

The function ft_getopt is specific to check syntactic consistency of the arguments, and the
optional third input arguments specifies the default value for the option in the function. If this optional input argument is not specified, it defaults to \[].
In this way the variables which are used in the function are always correctly initialized.

## File names for executable/compiled binaries

Since we support FieldTrip on most currently popular platforms regarding hardware and software, we have to create executables for all platforms that we can. If an executable cannot be compiled on a particular platform, e.g., because it depends on Windows-specific DLLs, then you of course don't have to bother.

Ensuring that all executables can co-exist on all platforms (and especially on the Unix base platforms) means that they should have unique file names. The choice for that is based on the specification according to the MATLAB function "computer", i.e.

    >> help computer
    computer Computer type.
      C = computer returns character vector C denoting the type of computer
      on which MATLAB is executing. Possibilities are:

                                                ISPC ISUNIX ISMAC ARCHSTR
      64-Bit Platforms
        PCWIN64  - Microsoft Windows on x64       1     0     0   win64
        GLNXA64  - Linux on x86_64                0     1     0   glnxa64
        MACI64   - Apple Mac OS X on x86_64       0     1     1   maci64

      ARCHSTR = computer('arch') returns character vector ARCHSTR which is
      used by the MEX command -arch switch.

      [C,MAXSIZE] = computer returns integer MAXSIZE which
      contains the maximum number of elements allowed in a matrix
      on this version of MATLAB.

      [C,MAXSIZE,ENDIAN] = computer returns either 'L' for
      little endian byte ordering or 'B' for big endian byte ordering.

      See also ispc, isunix, ismac.

The binaries for the different versions of the unix platforms (Linux, macOS) should have an extension corresponding to the computer type, e.g., the buffer executable would be named

- buffer.exe for Microsoft Windows
- buffer.glnx86 for 32-bit Linux
- buffer.glnxa64 for 64-bit Linux
- buffer.mac for 32-bit macOS on PPC hardware
- buffer.maci for 32-bit macOS on Intel hardware
- buffer.maci64 for 64-bit macOS on Intel hardware

Note that on Windows the executable is required to have the file extension "exe". In general it is sufficient to only provide a 32-bit version of the executable. For 64-bit Windows there is no convention yet.

## Check the requirements

FieldTrip of course depends on MATLAB, but there are additional requirements, such as operating systems (for mex files) and external toolboxes. We want to develop FieldTrip such that it can be used by as many people as possible, which means that we want to control and minimize the additional requirements.

Please consider the general [requirements](/faq/matlab/requirements) when extending or changing the FieldTrip code. Keep in mind that FieldTrip should not only run on the latest and greatest MATLAB version that you happen to have installed on your personal "supercomputer", but also on the more modest computers of many other people with other (older or newer) MATLAB versions and operating systems.

## Ensure that it runs on older MATLAB versions

Although you may be developing FieldTrip on the latest MATLAB version, we try to support it for previous MATLAB versions up to five years old. As of the end of 2020, this means supporting MATLAB version R2015b and newer.

Here is a list of MATLAB release dates; a complete list can be found on [Wikipedia](https://en.wikipedia.org/wiki/MATLAB#Release_history).

| version number | release name | release date |
| -------------- | ------------ | ------------ |
| MATLAB 9.9     | R2020b       | 17 Sep 2020 |
| MATLAB 9.8     | R2020a       | 19 Mar 2020 |
| MATLAB 9.6     | R2019a       | 20 Mar 2019  |
| MATLAB 9.5     | R2018b       | 12 Sep 2018  |
| MATLAB 9.4     | R2018a       | 15 Mar 2018  |
| MATLAB 9.3     | R2017b       | 14 Sep 2017  |
| MATLAB 9.2     | R2017a       | 09 Mar 2017  |
| MATLAB 9.1     | R2016b       | 15 Sep 2016  |
| MATLAB 9.0     | R2016a       | 03 Mar 2016  |
| MATLAB 8.6     | R2015b       | 03 Sep 2015  |
| MATLAB 8.5     | R2015a       | 05 Mar 2015  |
| MATLAB 8.4     | R2014b       | 03 Oct 2014  |
| MATLAB 8.3     | R2014a       | 07 Mar 2014  |
| MATLAB 8.2     | R2013b       | 06 Sep 2013  |
| MATLAB 8.1     | R2013a       | 07 Mar 2013  |
| MATLAB 8.0     | R2012b       | 11 Sep 2012  |
| MATLAB 7.14    | R2012a       | 01 Mar 2012  |
| MATLAB 7.13    | R2011b       | 13 Aug 2011  |
| MATLAB 7.12    | R2011a       | 08 Apr 2011  |
| MATLAB 7.11    | R2010b       | 03 Sep 2010  |
| MATLAB 7.10    | R2010a       | 05 Mar 2010  |
| MATLAB 7.9     | R2009b       | 04 Sep 2009  |
| MATLAB 7.8     | R2009a       | 06 Mar 2009  |
| MATLAB 7.7     | R2008b       | 09 Oct 2008  |
| MATLAB 7.6     | R2008a       | 01 Mar 2008  |
| MATLAB 7.5     | R2007b       | 01 Sep 2007  |
| MATLAB 7.4     | R2007a       | 01 Mar 2007  |

To facilitate supporting older MATLAB versions, below we list some known incompatibilities:

- the nargout function in MATLAB 6.5 and older does not work on function handles
- the "try ... catch me ..." statement fails in MATLAB 7.4, see [this bug](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=541)
- the ~ output argument is not supported in MATLAB versions &lt; 2009b and should be avoided
- nan with multiple input arguments to create a nan-matrix does not work for MATLAB versions &lt; R14

## Compiling MEX files

FieldTrip has to run on a large variety of platforms, with different operating systems and MATLAB versions. Therefore, we try to keep the compiled mex files reasonably consistent. Since mex files are added in the course of the development, and we don't want to recompile them too often, we cannot be too strict on the compile environment. If possible you should compile the mex files with a MATLAB version that is two years old, i.e. not the latest, but also not a version that is very old.

In most cases the mex file source code should be located in fieldtrip/src. The `ft_compile_mex` function is used to compile the mex files and the `synchronize-private.sh` Bash script is used to copy the updated mex files to all required (private) directories.

If the mex file is part of a collection of related mex files and only present on a single location (e.g., fieldtrip/@config/private), the mex file source code should be present in _that_ specific directory together with a compilation script.

For Unix-like platforms (Linux and macOS), it it also possible to compile all mex files from the Unix shell command line interface (on macOS called ''Terminal.app'') using ''make'' with target ''mex'', which uses the ''Makefile'' in FieldTrip's root directory. This approach is supported with Matlab and Octave, and requires providing the path to the MATLAB or octave binary. For example,

    make mex MATLAB=/usr/bin/matlab

would build for MATLAB using the binary in ''/usr/bin/matlab'' (a typical location on Linux platforms),

    make mex MATLAB=/Applications/MATLAB_R2015a.app/bin/matlab

would use MATLAB 2015a on macOS, and

    make mex OCTAVE=/Applications/Octave.app/Contents/Resources/usr/bin/octave

would build for Octave on OSX.
If the binary is already in the search path (for example, ''which matlab'' prints the location of MATLAB), a shortened form with only the binary name itself can be used as in

    make mex MATLAB=matlab

Different platforms have different extensions; for example, ''.mexmaci64'' for MATLAB macOS 64-bit intel, ''.mexw32'' for MATLAB Windows 32-bit, and ''.mex'' for all Octave platforms. The "Makefile" determines the correct extension based on the ''MATLAB'' or ''OCTAVE'' binary provided.

Below are more details on the compilation guidelines on different platforms.

### Windows 32-bit

You should use the LCC compiler that is included with MATLAB.

### Windows 64-bit

The 64-bit versions of MATLAB do not come with a compiler (see for example [here](http://www.mathworks.com/support/compilers/R2012a/win64.html) and [here](http://www.mathworks.nl/support/sysreq/previous_releases.html)). Furthermore, a C/C++ compiler is by default not available on Windows systems, therefore you are required to install a compiler to (re)compile the mex files.

You should use the Microsoft Visual C++ 2008 compiler. This compiler is available for free in the [MSVC 2008 Express Edition](http://www.microsoft.com/visualstudio/en-us/products/2008-editions/express) and is supported in MATLAB2012a and older versions (going back to 2008).

### Linux 32-bit

You should use gcc, but further details are not known at the moment.

### Linux 64-bit

Most development at the Donders is done on CentOS release 5.2 and the default gcc version 4.1.2. Further details are not known at the moment.

### Apple macOS 32-bit

MATLAB is not supported on 32-bit macOS any more.

### Apple macOS 64-bit

You should use the gcc compiler that is included in the Xcode package. Further details are not known at the moment.

## Avoid using nested functions

Although a nested function has certain advantages, it makes maintaining the code more difficult. Furthermore, ft_preamble and eval are not fully compatible with nested functions.

## Use a consistent spacing

It is annoying to get large git diffs just because of changes in the whitespace. That is why all developers are encouraged to work with two spaces instead of tabs. In the MATLAB editor you can specify this in Preferences->Editor/Debugger->Tab, where you can specify "2" and "tab key inserts spaces".

With Ctrl-A, Ctrl-I you can auto-indent the whole m-file and ensure that the horizontal whitespaces are consistent.

## Avoid changing the order of the channels in the data, if possible

FieldTrip functions should not rely on the channels being represented in a particular order, but should always explicitly look into the list with the channel labels in order to determine on which elements in the numeric data a particular computation is required. Functions may operate on several data-arguments that have information that pertains to channels, e.g., electrode positions, coil-to-channel mappings for MEG gradiometer arrays, time series of electrophysiological data, parameters of a sphere fitted to the headsurface directly underlying a particular channel, a set of neighbours relative to a particular channel, etc.

In this case we aim at imposing the following behavior of the function:

1.  The order of the channels in the first data argument will be the one that determines the order of the channels in the output: it will always override the order specified in the cfg (in cfg.channel).
2.  The order of the channels in the data overrides the order in the auxiliary information (such as sensor definitions).
3.  When multiple data structures of equivalent type are present in the input: the order of the channels in the N'th data argument is more important than the order of the channels in the (N+1)'th data argument.

## Add copyrights

You should add something like this to code that you have written yourself, or together with your colleagues. If you borrow code from elsewhere, you should include the original copyright statement.

    % Copyright (C) 2012, Donders Centre for Cognitive Neuroimaging, Nijmegen, NL
    %
    % This file is part of FieldTrip, see http://fieldtriptoolbox.org
    % for the documentation and details.
    %
    %    FieldTrip is free software: you can redistribute it and/or modify
    %    it under the terms of the GNU General Public License as published by
    %    the Free Software Foundation, either version 3 of the License, or
    %    (at your option) any later version.
    %
    %    FieldTrip is distributed in the hope that it will be useful,
    %    but WITHOUT ANY WARRANTY; without even the implied warranty of
    %    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    %    GNU General Public License for more details.
    %
    %    You should have received a copy of the GNU General Public License
    %    along with FieldTrip. If not, see <https://www.gnu.org/licenses/>.


## Ask for help

If you are unsure about the choices that you should make in developing new code or contributing to existing code, please ask one of the experienced developers for help. Robert, Jan-Mathijs, Eelke and Joern all have a good understanding of the FieldTrip programming philosophy.

## Suggested further reading

Please also consider the [documentation guidelines](/development/guideline/documentation) when making contributions to the FieldTrip project.
