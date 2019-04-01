---
title: How can I anonymize or deidentify a CTF dataset?
tags: [faq, ctf, raw, anonymize, sharing]
---

# How can I anonymize or deidentify a CTF dataset?

Using the CTF command line tool "newDs" with the "-anon" option. To keep all other aspects of the dataset as it is, you should specify some option

    newDs -anon -includeBadChannels -includeBadSegments -includeBad `<dataset>` `<savePath>`

Otherwise, bad channels, bad segments (in the continuous data) and bad trials (in segmented data) will be thrown away.

Make sure the savePath has an unambiguous name, so that you don't mix up your data.

Fields that are blanked out: purpose, site, institute, operator name, run title and description, collection description. The subject ID is set to Anon-1. The collection date and time are changed to 11/11/1911, 11:11.

{% include markup/danger %}
newDd version 5.4.0-linux-20061212 is known to have a bug that causes the collection date and time not to be cleared. To remove these from your recording, you can use the remove_ctf_datetime script available [here](https://github.com/robertoostenveld/bids-tools).
{% include markup/end %}

It is advisable to also convert the headlocalizer datasets, which are inside the SubjectXX.ds and are named hz.ds, hz2.ds, etc.

{% include markup/warning %}
After creating the anonymous dataset, you should delete the **defaults.de** ASCII file that is present in the `<savePath>`, because that contains some information that can be traced back to the original file location on disk (which may include your name or the name of the subject).
{% include markup/end %}

An example use is (note that this should all be on a single line)

    newDs -anon -includeBadChannels -includeBadSegments -includeBad /home/common/matlab/fieldtrip/data/Subject01.ds ~/anon/Subject01.ds

    newDs -anon -includeBadChannels -includeBadSegments -includeBad /home/common/matlab/fieldtrip/data/Subject01.ds/hz.ds ~/anon/Subject01.ds/hz.ds

    newDs -anon -includeBadChannels -includeBadSegments -includeBad /home/common/matlab/fieldtrip/data/Subject01.ds/hz2.ds ~/anon/Subject01.ds/hz2.ds

    rm ~/anon/Subject01.ds/defaults.de
    rm ~/anon/Subject01.ds/hz.ds/defaults.de
    rm ~/anon/Subject01.ds/hz2.ds/defaults.de

See also this frequently asked question on [how to anonymize an anatomical MRI](/faq/how_can_i_anonymize_an_anatomical_mri).
