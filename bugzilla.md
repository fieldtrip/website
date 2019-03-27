---
title: Bugzilla and GitHub issue tracking
tags: [development]
---

# Bugzilla and GitHub issue tracking

For a long time we have used our own [Bugzilla](http://bugzilla.fieldtriptoolbox.org) server for tracking issues, but recently we started moving over to [GitHub issues](http://github.com/fieldtrip/fieldtrip/issues). Both Bugzilla and GitHub help us to manage the workflow: by having all bugs/issues/requests in a sort of TODO list, we can more easily collaborate, distribute the responsibilities and keep track of things.

## Use github to report an issue (recommended)

To report an issue on GitHub you have to [sign up for an account](https://github.com/join) on GitHub. This allows us to follow up on reported issues and keep you automatically updated on the status; i.e., you will get an automatic email whenever someone works on your request.

## Use bugzilla to report an issue (not recommended any more)

To report an issue on Bugzilla or to add yourself to one of the existing bugs, you have to create a [Bugzilla account](http://bugzilla.fieldtriptoolbox.org/createaccount.cgi) with your email address as the user name. Your email address will not be visible to external visitors and will only be used to ask for additional information or to report when the bug is resolved.

## Provide informative reports of your issue

{% include markup/info %}
The easier it is for one of the developers to reproduce your bug, the more likely it is that we'll fix the problem. Good bug reports include a small test script and the data (i.e. mat file) required to reproduce the bug.
{% include markup/end %}

Please create a small test script and a piece of data that are both as small and simple as possible to reproduce the problem. For example: a .mat file containing a data structure and a cfg structure, and an instruction like _"load the cfg and data from the mat file and run ft_freqanalysis(cfg, data)"_.

If there is a chance of the bug being platform dependent, please also specify the platform (Windows, OS X, Linux), the version of your operating system (Windows 10, Redhat 7.2, High Sierra, ...) and the version of MATLAB that you are using.

Example data (e.g. your MATLAB workspace) that helps to pinpoint a specific issue can be uploaded to the Bugzilla server as an attachment. This only works for relatively small files. If the data that you want to share is too large, please consider using one of the methods for sharing files that is listed in [this frequently asked question](/faq/how_should_i_send_example_data_to_the_developers).
