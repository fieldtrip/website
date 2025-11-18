---
title: Getting started
category: getting_started
redirect_from:
    - /reading_data/
---

FieldTrip is a MATLAB toolbox that contains a set of separate (high-level) functions, it does **not** have a graphical user interface. The toolbox functions can be combined into an analysis pipeline, i.e. a MATLAB script containing all steps of your analysis. For this reason, if you are new to MATLAB scripting or EEG/MEG/iEEG/NIRS analysis, FieldTrip might not be the most efficient for you. If you are persistent and eager to learn, the list of [review papers and teaching material](/references_to_review_papers_and_teaching_material) can help you on your way.

For a general overview of how FieldTrip is designed, please have a look at the [reference paper](http://www.hindawi.com/journals/cin/2011/156869). The best way to get hands-on experience is by following the [tutorials](/tutorial), the [walkthrough](/walkthrough) and through the other [documentation](/documentation). If you have questions that are not answered by the documentation or in the [frequently asked questions](/faq), you can register on the [email list](/discussion_list) and ask the other users and the developers for help. Also, FieldTripping is not something you do alone; inform yourself about colleagues that use (or want to use) FieldTrip.

We organize [FieldTrip workshops](/workshop) with lectures and hands-on training. Attending one of these will probably benefit your understanding and analysis skills. You can also watch [online video lectures](/video) that were recorded at previous workshops.

## Getting started with particular data

FieldTrip has a generic mechanism for reading data with little to no difference from one file format to another. Many [EEG, MEG and electrophysiology file formats](/faq/preproc/datahandling/dataformat) are supported. There are some differences between MEG and EEG, since for MEG data the sensor positions are often represented in the raw data files whereas EEG raw data files usually do not contain the electrode positions. For animal electrophysiology data there is also a difference in the representation of local field potentials (c.f. EEG) and in spike timestamps and spike waveform snippets.

Although FieldTrip represents all data in a similar way, for some acquisition systems and/or file formats it may help if you understand how the peculiarities of that file format are related to the FieldTrip implementation. The following pages serve as a starting point for particular data acquisition systems. Note that not all [supported data formats](/faq/preproc/datahandling/dataformat) are listed here, only those with peculiarities that you should be aware of.

{% include markup/red %}
In general you should get started with the [tutorials](/tutorial). The pages listed below only serve to explain system specific details and peculiarities, but lack the complete overview that the tutorials provide.
{% include markup/end %}

## Getting started with MEG data

{% include pagelist section="getting_started/meg" %}

## Getting started with EEG data

{% include pagelist section="getting_started/eeg" %}

## Getting started with intracranial data

{% include pagelist section="getting_started/intracranial" %}

## Getting started with NIRS data

{% include pagelist section="getting_started/nirs" %}

## Getting started with eyetracker data

{% include pagelist section="getting_started/eyetracker" %}

## Getting started with motion capture data

{% include pagelist section="getting_started/motion" %}

## Getting started with other types of data

{% include pagelist section="getting_started/otherdata" %}

## Getting started with (data from) other software

{% include pagelist section="getting_started/othersoftware" %}

## Getting started with real-time data analysis

{% include pagelist section="getting_started/realtime" %}
