---
title: Which version of FieldTrip should I download from the ftp server?
tags: [faq, download]
---

# Which version of FieldTrip should I download from the ftp server?

Although initially we considered to have version 1.0, 1.1, 2.0, etc., eventually we decided against it. We have a smooth development path and so far we have been able to maintain backward compatibility quite well. The latest version of the toolbox will generally work with your older scripts. There is a limited number of people that can directly change the code, and they take their responsibility to the other users very seriously. When we add or change functionality in the code, we always test it prior to committing it to the code repository.

We release a daily version of FieldTrip, with the name fieldtrip-YYYYMMDD, where YYYY, MM and DD are the year, month and day. These are automatically generated every day, and contain the most up-to-date code. Besides the normal daily release, there is also a _lite_ version that does not contain the binary .mat files. These mat files contain templates used for plotting source reconstructions and they do not change very often. The lite version is only approximately 70 MiB, whereas the normal version (which includes the anatomical templates) is around 400 MiB.

In general, you should download the most recent daily release version. It contains the most features and all known bugs will be fixed in that version. If you encounter a problem and think that that is caused by a bug in the code, you should download the latest version of that moment. If the problem still persists, please inform us about it through the [email discussion list](/discussion_list).

If you want to control in detail which version of FieldTrip you have, if you want to do frequent updates, or if you want to change or conontribute code, you can use the [GitHub](/development/git) version.
