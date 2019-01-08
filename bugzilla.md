---
title: Bugzilla and Github issue tracking
---

# Bugzilla and Github issue tracking

For a long time we used own own [bugzilla](http://bugzilla.fieldtriptoolbox.org) server for tracking issues, but recently we started moving over to [Github issues](http://github.com/fieldtrip/fieldtrip/issues). Both Bugzilla and Github help us to manage the workflow: by having all bugs/issues/requests in a sort of TODO list, we can more easily collaborate,  distribute the responsibilities and keep track of things.

## Use github to report an issue (recommended)

To report an issue on Github you have to [sign up for an account](https://github.com/join).  This allows us to follow up on reported issues and keep you automatically updated on the status. I.e., you will get an automatic mail whenever someone works on your request.

## Use bugzilla to report an issue (old)

To report an issue on Bugzilla or to add yourself to one of the existing bugs, you have to create a bugzilla account with your email address as user name. You will have to register on the bugzilla server with your email address. Your address will not be visible to external visitors and will only be used to report back to you when the bug is resolved or to ask for additional information that we might need from you.

## Provide informative reports of your issue

The easier it is for one of the developers to reproduce your bug, the more likely it is that we'll fix the problem.

Good bug reports include a small test script and the data (i.e. mat file) required to reproduce the bug. Please create a test script and a piece of data that are both as small and simple as possible to reproduce the problem. For example: a .mat file containing a data structure and a cfg structure, and an instruction like *"load the cfg and data from the mat file and run ft_freqanalysis(cfg, data)"*.

If there is a chance to the bug being platform dependent, please also specify the platform (Windows, OS X, Linux), the version of your operating system (WinXP, Vista, Redhat 7.2, ...), the version of MATLAB that you are using and whether you are using a 32 bit or 64 bit operating system and MATLAB.

Example data (e.g. your MATLAB workspace) that helps to pinpoint a specific issue can be uploaded to the bugzilla server as attachment. This only works for relatively small files. If the data that you want to share is too large, please consider using one of the methods for sharing files that is listed in this frequently asked question:

## See also

{% include seealso tag="bugzilla" %}
