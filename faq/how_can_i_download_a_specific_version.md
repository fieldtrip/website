---
title: Which version of FieldTrip should I download?
category: faq
tags: [download, release]
---

Our [download server](https://download.fieldtriptoolbox.org/) holds recent versions of the FieldTrip toolbox code, corresponding to [tagged versions](https://github.com/fieldtrip/fieldtrip/tags) on GitHub. In general we also archive the latest released version of every year on <https://download.fieldtriptoolbox.org/historical/>, which correspond to the persistently archived versions on [Zenodo](https://zenodo.org/records/10495308). 

If you are looking for a specific version not listed here, you can look at the tagged versions at <https://github.com/fieldtrip/fieldtrip/tags>. These tagged versions are generated following the development, test and release cycle described [here](/development/releasing).

Alternatively, you can also check out a specific version using the git software like this:

    git clone https://github.com/fieldtrip/fieldtrip.git
    git rev-list master -n 1 --first-parent --before=2018-03-07
    git checkout ee0774ac2374a2f696e1e373d59435de17bbf3e3  # using the SHA identifier that the previous command returned

To go back from the detached HEAD to the master branch with the latest development version, you would do:

    git checkout master
