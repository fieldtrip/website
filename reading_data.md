---
title: Importing your data
layout: default
tags: [meg, eeg, lfp, spike, raw, dataformat]
---

# Importing your data

FieldTrip has a generic mechanism for reading data from a file. Within FieldTrip there is no difference in how the data from one file format is treated, compared to another file format. Many [EEG, MEG and electrophysiology file formats](/dataformat) are supported. There is a small difference between EEG and MEG data, because in MEG data the sensor positions are usually represented in the raw data files. Therefore the MEG sensor information is kept with the data while processing, whereas in EEG the sensor information is usually processed separately. For animal electrophysiology data there is also a difference in the representation of local field potentials (c.f. EEG) and in spike timestamps and spike waveforms.

Although FieldTrip represents all data in a similar way, for some acquisition systems and/or file formats it may help if you understand how the peculiarities of that file format are related to the FieldTrip implementation. The following pages serve as a starting point for particular data acquisition systems. Note that not all [supported data formats](/dataformat) are listed here, only the ones with peculiarities that you might want to be aware of.
tags: [meg, eeg, lfp, spike, raw, dataformat]
---

# Importing your data

FieldTrip has a generic mechanism for reading data from a file. Within FieldTrip there is no difference in how the data from one file format is treated, compared to another file format. Many [EEG, MEG and electrophysiology file formats](/dataformat) are supported. There is a small difference between EEG and MEG data, because in MEG data the sensor positions are usually represented in the raw data files. Therefore the MEG sensor information is kept with the data while processing, whereas in EEG the sensor information is usually processed separately. For animal electrophysiology data there is also a difference in the representation of local field potentials (c.f. EEG) and in spike timestamps and spike waveforms.

Although FieldTrip represents all data in a similar way, for some acquisition systems and/or file formats it may help if you understand how the peculiarities of that file format are related to the FieldTrip implementation. The following pages serve as a starting point for particular data acquisition systems. Note that not all [supported data formats](/dataformat) are listed here, only the ones with peculiarities that you might want to be aware of.

Finally, you might have data already analysed using other software, and would like to start by reading their output. Or the other way around, and process FieldTrip data further. For some common software packages we provide functions and examples.

{{page>:getting_started:shared}}
