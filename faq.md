---
title: Frequently asked questions
category: faq
---

On this page you can find answers to a variety of FieldTrip and MATLAB related questions.

We invite you to [add your own](/development/contribute) tutorials to the website, considering the [documentation guidelines](/development/guideline/documentation). Whenever you explain somebody in person or over email how to do something with FieldTrip, please consider whether you could use the website for this, allowing others to learn from it as well.

See also the [tutorials](/tutorial) and [example scripts](/example).

## Reading and preprocessing data

- [How can I inspect the electrode impedances of my data?](/faq/preproc/impedancecheck)
- [How can I use the databrowser?](/faq/preproc/databrowser)
- [I used to work with trl-matrices that have more than 3 columns. Why is this not supported anymore?](/faq/preproc/trialinfo_trl)
- [Should I rereference my EEG data prior to, or after ICA?](/faq/preproc/ica_rereference)
- [Why should I set continuous to yes for CTF data?](/faq/preproc/continuous)
- [Why should I start with rereferencing for BioSemi EEG data?](/faq/preproc/biosemi_reference)

### Specific data formats

{% include pagelist section="faq/preproc/dataformat" %}

### Data handling

{% include pagelist section="faq/preproc/datahandling" %}

### Trials, triggers and events

{% include pagelist section="faq/preproc/events" %}

### Artifacts

{% include pagelist section="faq/preproc/artifact" %}

## Spectral analysis

{% include pagelist section="faq/spectral" %}

## Source reconstruction

{% include pagelist section="faq/source" %}

## Statistical analysis

{% include pagelist section="faq/stats" %}

- [How can I define neighbouring sensors?](/faq/stats/sensors_neighbours)
- [How can I determine the onset of an effect?](/faq/stats/effectonset)
- [How can I test an interaction effect using cluster-based permutation tests?](/faq/stats/clusterstats_interaction)
- [How can I test for correlations between neuronal data and quantitative stimulus and behavioural variables?](/faq/stats/behavior_signalcorrelation)
- [How can I test whether a behavioral measure is phasic?](/faq/stats/behavior_cosinefit)
- [How can I use the ivar, uvar, wvar and cvar options to precisely control the permutations?](/faq/stats/clusterstats_iuwcvar)
- [How does ft_prepare_neighbours work?](/faq/stats/neighbours_prepare)
- [How NOT to interpret results from a cluster-based permutation test?](/faq/stats/clusterstats_interpretation)
- [Should I use t or F values for cluster-based permutation tests?](/faq/stats/clusterstats_teststatistic)
- [What is the idea behind statistical inference at the second-level?](/faq/stats/statistics_secondlevel)
- [Why are there multiple neighbour templates for the NeuroMag306 system?](/faq/stats/neighbours_neuromag)
- [Why should I use the cfg.correcttail option when using statistics_montecarlo?](/faq/stats/clusterstats_correcttail)

## Plotting and visualization

{% include pagelist section="faq/plotting" %}

## Experimental questions

{% include pagelist section="faq/experiment" %}

## Realtime data streaming and analysis

{% include pagelist section="faq/realtime" %}

## Distributed computing

- [What are the different approaches I can take for distributed computing?](/faq/distcomp/distributed_computing)

### Distributed computing with the MATLAB distributed computing toolbox

- [How to get started with the MATLAB distributed computing toolbox?](/faq/distcomp/distributed_matlab)

### Distributed computing with fieldtrip/qsub on a HPC cluster

- [How to compile MATLAB code into stand-alone executables?](/faq/distcomp/matlab_compile)
- [How to get started with distributed computing using qsub?](/faq/distcomp/distributed_qsub)

## MATLAB questions

- [Can I prevent "external" toolboxes from being added to my MATLAB path?](/faq/matlab/toolboxes_legacyvsexternal)
- [Can I use FieldTrip without MATLAB license?](/faq/matlab/compiled)
- [Can I use Octave instead of MATLAB?](/faq/matlab/octave)
- [How can I compile the mex files and command-line programs?](/faq/matlab/compile)
- [How can I compile the mex files on 64-bit Windows?](/faq/matlab/compile_windows)
- [How can I compile the mex files on macOS?](/faq/matlab/compile_osx)
- [How many lines of code does FieldTrip consist of?](/faq/matlab/fieldtrip_codelines)
- [How to select the correct SPM toolbox?](/faq/matlab/spmversion)
- [Installation and setting up the path](/faq/matlab/installation)
- [MATLAB complains about a missing or invalid MEX file, what should I do?](/faq/matlab/matlab_mexinvalid)
- [MATLAB complains that mexmaci64 cannot be opened because the developer cannot be verified](/faq/matlab/mex_osx)
- [MATLAB does not see the functions in the "private" directory](/faq/matlab/matlab_privatefunctions)
- [MATLAB version 7.3 (2006b)_crashes_when_I_try_to_do_...](/faq/matlab/matlab_crash73)
- [The databrowser crashes and destroys the whole MATLAB session, how can I resolve this?](/faq/matlab/databrowser_crash)
- [What are the MATLAB requirements for using FieldTrip?](/faq/matlab/requirements)
- [Which external toolboxes are used by FieldTrip?](/faq/matlab/external)
- [Why are so many of the interesting functions in the private directories?](/faq/matlab/privatefunctions_why)

## Code and development questions

{% include pagelist section="faq/development" %}

## Organizational questions

{% include pagelist section="faq/organization" %}

## Various other questions

- [Are the FieldTrip lectures available on video?](/faq/other/video)
- [Can I map different electrode position layouts?](/faq/other/capmapping)
- [Can I organize my own FieldTrip workshop?](/faq/other/workshop)
- [How can I anonymize a BrainVision dataset?](/faq/other/anonymization_brainvision)
- [How can I anonymize a CTF dataset?](/faq/other/anonymization_ctf)
- [How can I anonymize data processed in FieldTrip?](/faq/other/anonymization_fieldtripdata)
- [How can I anonymize DICOM files?](/faq/other/anonymization_dicom)
- [How can I anonymize or deidentify an anatomical MRI?](/faq/other/anonymization_anatomical)
- [How can I share my MEG data?](/faq/other/data_sharing)
- [How do I prevent FieldTrip from printing the time and memory after each function call?](/faq/other/showcallinfo)
- [How should I prepare for the upcoming FieldTrip workshop?](/faq/other/workshop_preparation)
- [How should I specify the coordinate systems in a BIDS dataset?](/faq/other/bids_coordsystem)
- [What are the units of the data and of the derived results?](/faq/other/units)
- [Where can I find open access MEG/EEG data?](/faq/other/open_data)
- [Which datasets are used in the documentation and where are they used?](/faq/other/datasets)
- [Which methodological details should I report in an EEG/MEG manuscript?](/faq/other/checklist)
