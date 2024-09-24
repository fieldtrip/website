---
title: How can I change the head localization in a CTF dataset?
category: faq
tags: [ctf]
---

# How can I change the head localization in a CTF dataset?

## Introduction

The res4 file in a CTF dataset contains information about the location of each gradiometer with respect to the head. This information is computed and stored using the localizer measurements prior to, and after the real experiment. It is important to know the location of the gradiometers exactly if you want to do source analysis (in fieldtrip, CTF or Curry), or if you want to realign the data to a template head location.

If you only want to analyze the data on the channel level, the location of the gradiometers is not used. If you want to use channel-level statistics on the channel-level data, you do need the channel locations, but it is not important that they are accurate.

## Computing the head position from additional localizers

This is done using the CTF command line utility `calcHeadPos`. You can get additional information from the file /opt/ctf/doc/readme.calcheadPos. Furthermore, CTF gave us this additional explanation by e-mail.
To understand, some background information is likely needed. A specific collection protocol (.rp) is required to collect head localization data (e.g., to drive the coils at specified frequencies). Besides collecting this data, Acq utilizes the coil moments that are also saved in this `.rp` file to do the head localization and save the results with the datasets. This file is stored in your 'hardware' directory and is given a `.hz.rp` extension (it is most easily located by viewing the 'List resources' option under Acq).
To change or re-compute the head localization results the software must have the frequency and moment calibration results that are stored within the '.hz.rp' file and thus it is this file calcHeadPos needs. However it is imperative to use the `hz.rp` file that was used at the time of the original collection (i.e. the `hz.rp` file is updated after each coil calibration and thus one should not rely on the copy in the 'hardware' directory).

With all this said the good news is that within each dataset the `.rp` file used for the collection is saved as a separate file but with a `.acq` extension. As the head localization datasets are saved within the main dataset directories (e.g., as `hz.ds` and `hz2.ds` for the pre and post run head localizations) the required `.hz.rp` are readily available. In short, to use calcHeadPos I recommend just executin

    calcHeadPos [options] mydataset.ds mydataset.ds/hz.ds/hz.rp

This assumes a pre-run head localization was performed but, if not, just specify any head localization dataset collected.

## Changing the head localization

Using the CTF command line utility `changeHeadPos`, you can change the head coil positions in the dataset. The default behavior is to read the dataset's `.hc` file and update its sensor resources using the values in the `.hc` file. There are also options to swap or modify the head coil positions. For instance, when you want to swap the positions of the left ear coil with the right ear head coil, this can be achieved with:

    changeHeadPos -swap N R L dataset.ds

where N L R would be the normal order. It is noteworthy that execution of this command is preferably done at the acquisition computer. A computer not supporting this operation, may yield a 'Segmentation fault (core dumped)' error.
