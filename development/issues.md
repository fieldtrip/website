---
title: Reporting issues
tags: [development, support]
redirect_from:
  - /bugzilla/
---

# Reporting issues

You first have to [sign up for an account](https://github.com/join) or log in on GitHub, subsequently you can report the issue [here](https://github.com/fieldtrip/fieldtrip/issues). We automatically will receive an email and will follow up and keep you updated; i.e., you will get an email through GitHub whenever someone works on your issue.

## Bug reporting

1. Please search on both the [FieldTrip discussion list](/discussion_list)
   and the [GitHub issue list](https://github.com/fieldtrip/fieldtrip/issues)
   to see if anybody else has lodged a similar observation.

2. How confident are you that the behaviour you have observed is in fact a
   genuine bug, and not a misunderstanding?

   -  *Confident*: Please [open a new GitHub issue](https://github.com/fieldtrip/fieldtrip/issues/new/choose);
      select the "bug report" issue template to get started.

   -  *Not so confident*: That's fine! Consider instead creating a new topic
      on the [FieldTrip discussion list](/discussion_list);
      others can then comment on your observation and determine the
      appropriate level of escalation.

## Requesting a new feature

Please search the [GitHub issue list](https://github.com/fieldtrip/fieldtrip/issues)
to see if anybody else has made a comparable request:

   -  If a corresponding issue already exists, please add a comment to that
      issue to escalate the request. Additionally, describe any
      aspect of that feature not yet described in the existing issue.

   -  If no such listing exists, then you are welcome to create a [new
      issue](https://github.com/fieldtrip/fieldtrip/issues/new) outlining the
      request. Be sure to select the "feature request" option to get started
      with writing the issue.

## Provide informative details about your issue

{% include markup/skyblue %}
The easier it is for one of the developers to reproduce your bug, the more likely it is that we'll fix the problem. Good bug reports include a small test script and the data (i.e. mat file) required to reproduce the bug.
{% include markup/end %}

Please create a small test script and a piece of data that are both as small and simple as possible to reproduce the problem. For example: a .mat file containing a data structure and a cfg structure, and an instruction like _"load the cfg and data from the mat file and run ft_freqanalysis(cfg, data)"_.

If there is a chance of the bug being platform dependent, please also specify the platform (Windows, macOS, Linux), the version of your operating system (Windows 10, Redhat 7.2, High Sierra, ...) and the version of MATLAB that you are using.

Example data (e.g., your MATLAB workspace) that helps to pinpoint a specific issue can be uploaded to the GitHub server as an attachment. This only works for relatively small files. If the data that you want to share is too large, please use a file hosting service as explained [here](/faq/how_should_i_send_example_data_to_the_developers).
