---
title: How can I keep track of changes to the code?
category: faq
tags: [download, development, cvs, svn, git]
---

# How can I keep track of changes to the code?

The FieldTrip code is accessible using [git](https://git-scm.com/) at [github.com](https://github.com). To quickly get access to the code, you would do the following from the command line or the equivalent in a graphical git interface, such as the [GitHub desktop](https://desktop.github.com).

    git clone https://github.com/fieldtrip/fieldtrip

To update automatically, you could schedule a job (e.g., using cron) to run "git pull" every night.

Please see our [git and GitHub](/development/git) tutorial for details.

## Downloading as zip file

You can also download the latest ("master") version as a [zip file](https://github.com/fieldtrip/fieldtrip/archive/master.zip).

## Related documentation

{% include seealso tag="git" %}
{% include seealso tag="svn" %}
{% include seealso tag="cvs" %}
