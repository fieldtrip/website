---
title: Why is FieldTrip developed separately from EEGLAB?
tags: [faq, eeglab]
---

# Why is FieldTrip developed separately from EEGLAB?

The motivation behind FieldTrip is twofold: first to make advanced methods available to end-users, second to get interaction with the end-users in order to improve the methods. The software design underlying FieldTrip was made with the FC Donders setting in mind, where a large research focus is on studying oscillatory brain dynamics using MEG. An important feature in FieldTrip is source analysis of oscillatory activity. Most FieldTrip users at the Donders Centre can be considered advanced users. Furthermore, it is very easy for them to ask advice to any of the advanced users.

EEGLAB clearly has a different audience, i.e. it has a graphical interface and aims at a much wider audience with more of a black-box approach to data analysis. EEGLAB is primarily aimed at EEG and at users that are more naive from a technical/methodological point of view. We consider this black-box approach not optimal for the type of research done here at the FC Donders Centre. The main FieldTrip developer (Robert Oostenveld) is also contributing to the source analysis part of EEGLAB, and initially we did also look at EEGLAB to see whether that could fulfill the needs of the FC Donders Centre. We decided that it would be more efficient and scientifically rewarding for us to design and implement an analysis package completely according to our own ideas. A few important differences between the two packages ar

- EEGLAB does not have a strict separation between data and graphical interface, which makes it difficult to extend the package for people who do not understand how the graphical interface is implemented.

- EEGLAB does not allow for data segments/trials to have a variable length. That is an important feature built into FieldTrip, and we use it to study only data segments up to, but not including, an unpredictable stimulus change or response.

- In EEGLAB the whole dataset should be loaded into memory before it can be processed. This can complicate things when the epochs of interest are only small fraction of the whole recording. FieldTrip allows selectively reading the raw data according to pre-defined trial borders.

- EEGLAB was built around the notion that data consists of matrices, whereas FieldTrip also allows for volume data (anatomical/functional) and other data types (geometry data for the head model and sensors).

- We considered it too much work to extend all parts of EEGLAB to fully support MEG data. The representation of MEG data is more complex than EEG data and although ICA is the same for EEG and MEG, topoplotting can for example be quite different (if you have data from a planar gradiometer system such as Neuromag).

It could not be avoided to re-implement some stuff in FieldTrip that was already available in EEGLAB, but it also means that we could implement it in a better way. We do not want to position FieldTrip as a competitor to EEGLAB. Both are Open Source packages and therefore can borrow code from each other. There is also an active collaboration to provide an interface between the two packages, to allow EEGLAB users to use some of the source modeling methods implemented in FieldTrip. And people who want to use the available advanced features, will find that these are available as a nicely structured set of low-level routines in FieldTrip.
