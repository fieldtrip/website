---
layout: default
---

# Bugzilla bug tracking system

For the FieldTrip project we are using the [bugzilla](http://www.bugzilla.org) bug tracking system. Bugzilla is open source software that helps to manage the workflow related to bug reports, code enhancements and feature requests. It works by storing all these requests as a TODO list in a database, which allows all collaborators to assign and distribute the responsibilities and keep track of everything.

Our Bugzilla server is located at http://bugzilla.fieldtriptoolbox.org. 

{{buggie.png}}

## Use bugzilla to report or to get updates

To contribute a new issue to bugzilla or to add yourself to one of the existing bugs, you have to create a bugzilla account with your email address as user name. Your email address will not be visible to external visitors, but only to other contributors to the FieldTrip project after they have logged in. The reason for using the email address as login is that bugzilla uses it to keep you automatically updated on the status of your request. I.e., you get an automatic mail whenever someone works on your request. 

Note that the easier it is for one of the developers to reproduce the bug, the more likely it is that we can fix the problem. 

`<note>`
You will have to register on the bugzilla server with your email address. Your address will not be visible to external visitors and will only be used to report back to you when the bug is resolved or to ask for additional information that we might need from you. 
`</note>`

Good bug reports include a small test script and the data (i.e. mat file) required to reproduce the bug. Please create a test script and a piece of data that are both as small as possible to reproduce the problem. For example: a *.mat file containing a data structure and a cfg structure, and an instruction like *"load the cfg and data from the mat file and run ft_freqanalysis(cfg, data)"*.

If there is a chance to the bug being platform dependent, please also specify the platform (Windows, OS X, Linux), the version of your operating system (WinXP, Vista, Redhat 7.2, ...), the version of MATLAB that you are using and whether you are using a 32 bit or 64 bit operating system and MATLAB.

Example data (e.g. your MATLAB workspace) that helps to pinpoint a specific issue can be uploaded to the bugzilla server as attachment. This only works for relatively small files. If the data that you want to share is too large, please consider using one of the methods for sharing files that is listed in this frequently asked questio

{{page>faq:how_should_i_send_example_data_to_the_developers}}

