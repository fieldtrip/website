---
title: Why is FieldTrip developed separately from EEGLAB?
parent: Organizational questions
category: faq
tags: [eeglab]
redirect_from:
    - /faq/why_is_fieldtrip_developed_separately_from_eeglab/
---

# Why is FieldTrip developed separately from EEGLAB?

The motivation for developing FieldTrip is twofold: first to make advanced methods available to end-users, second to get interaction with the end-users in order to improve the methods. The software design underlying FieldTrip was made with the researchers of the FC Donders Centre in mind, where a large focus is on studying oscillatory brain dynamics using MEG. An important feature in FieldTrip is therefore source analysis of oscillatory activity. Most FieldTrip users at the Donders Centre can be considered advanced users. Furthermore, it is relatively easy for them to ask advice to the developers and from other users.

EEGLAB has a wider audience, it has a graphical interface, and supports more of a black-box approach to data analysis. EEGLAB is primarily aimed at EEG and at users with a less strong methodological background. The main FieldTrip developer (Robert Oostenveld) is also a long-time contributor to the source analysis part of EEGLAB. At the start of the Donders Centre we considered whether EEGLAB could fulfill the needs of our researchers, but decided that it would not be an optimal match. Hence, we decided that it would be more efficient and scientifically rewarding to design and implement an analysis package from scratch.

A few important differences between the two packages are:

- EEGLAB does not have a strict separation between data and graphical interface, which makes it difficult to extend the package for people who do not understand how the graphical interface is implemented. However, EEGLAB now has plugins that make extending it easier.

- EEGLAB does not allow for data segments/trials to have a variable length. That is an important feature of FieldTrip; we use it to study only data segments up to, but not including, an unpredictable stimulus change or response.

- In EEGLAB the whole dataset has to be loaded into memory before it can be processed. This can complicate things when the epochs of interest are only small fraction of the whole recording. FieldTrip allows selectively reading the raw data according to pre-defined trial borders, allowing it to be used with MEG datasets that are often very large (10GB on disk, 20GB when full in memory).

- EEGLAB was built around the notion that data consists of matrices, whereas FieldTrip also allows for volume data (anatomical/functional) and other data types (geometry data for the head model and sensors).

- We considered it too much work to extend all parts of EEGLAB to fully support MEG data. The representation of MEG data is more complex than EEG data and although ICA is the same for EEG and MEG, topoplotting can for example be quite different if you have data from a planar gradiometer system, such as Neuromag.

It could not be avoided to re-implement some stuff in FieldTrip that was already available in EEGLAB, but it also means that we could implement it in way that we considered better. We do not want to position FieldTrip as a competitor to EEGLAB. Both are Open Source packages and therefore can and do borrow code from each other. There is also an active collaboration to provide an interface between the two packages, to allow EEGLAB users to use some of the source modeling methods implemented in FieldTrip. And people who want to use the available advanced features, will find that these are available as a nicely structured set of low-level routines in FieldTrip.
