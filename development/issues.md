---
title: Reporting issues
tags: [development, support]
redirect_from:
  - /bugzilla/
---

# Reporting issues

You first have to [sign up for an account](https://github.com/join) or log in on GitHub, subsequently you can report the issue [here](https://github.com/fieldtrip/fieldtrip/issues). We automatically will receive an email and will follow up and keep you updated; i.e., you will get an email through GitHub whenever someone works on your issue.

## Provide informative details about your issue

{% include markup/info %}
The easier it is for one of the developers to reproduce your bug, the more likely it is that we'll fix the problem. Good bug reports include a small test script and the data (i.e. mat file) required to reproduce the bug.
{% include markup/end %}

Please create a small test script and a piece of data that are both as small and simple as possible to reproduce the problem. For example: a .mat file containing a data structure and a cfg structure, and an instruction like _"load the cfg and data from the mat file and run ft_freqanalysis(cfg, data)"_.

If there is a chance of the bug being platform dependent, please also specify the platform (Windows, macOS, Linux), the version of your operating system (Windows 10, Redhat 7.2, High Sierra, ...) and the version of MATLAB that you are using.

Example data (e.g. your MATLAB workspace) that helps to pinpoint a specific issue can be uploaded to the GitHub server as an attachment. This only works for relatively small files. If the data that you want to share is too large, please use a file hosting service as explained [here](/faq/how_should_i_send_example_data_to_the_developers).

## Issues on bugzilla

In the past we used our own [Bugzilla](http://bugzilla.fieldtriptoolbox.org) server for tracking the development and issues, but we have moved over to [GitHub issues](http://github.com/fieldtrip/fieldtrip/issues). The bugzilla server is still available at <http://bugzilla.fieldtriptoolbox.org> for reference to documentation of previous issues.
