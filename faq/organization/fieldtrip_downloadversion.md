---
title: Which version of FieldTrip should I download?
category: faq
tags: [download, release]
redirect_from:
  - /faq/which_version_of_fieldtrip_should_i_download_from_the_ftp_server/
  - /faq/which_version_of_fieldtrip_should_i_download/
    - /faq/fieldtrip_downloadversion/
---

# Which version of FieldTrip should I download?

Although initially we considered to use [semantic versioning](https://semver.org) with version 1.0, 1.1, 2.0, etc., we decided against it. We don't have clear development milestones that would warrant a version increment, and we don't want to break backward compatibility. Instead, we have a smooth development path and make changes from day to day. The latest version of the toolbox will generally work with your older scripts (and if not, please report it as a [bug](/development/issues)). When we add or change functionality in the code, we always test it using the [dashboard](/development/testing) prior to releasing it. There is a limited number of people that can directly change the code, and they take their responsibility to the other users very seriously.

We release regular versions of FieldTrip, with the name fieldtrip-YYYYMMDD, where YYYY, MM and DD are the year, month and day. These are generated following the development, test and release cycle described [here](/development/releasing) and contain the tested and most up-to-date code.

Besides the normal release, there is also a "lite" version that does not contain the binary *.mat files. These mat files contain templates used for plotting source reconstructions and they do not change very often. The lite version is only approximately 80 MiB, whereas the normal version (which includes the anatomical templates) is around 400 MiB.

In general, you should download the most recent daily release version. It contains the most features and all known bugs will be fixed in that version. If you encounter a problem and think that that is caused by a bug in the code, you should download the latest version at that moment. If the problem still persists, please inform us about it through the [email discussion list](/discussion_list) or report it as a [bug](/development/issues).

If you want to control in detail which version of FieldTrip you have, if you want to do frequent updates, or if you want to contribute, you should use the [GitHub](/development/git) version.
