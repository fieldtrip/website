---
title: What usage information is FieldTrip tracking?
tags: [faq]
---

# What usage information is FieldTrip tracking?

The FieldTrip software includes the **[ft_trackusage](https://github.com/fieldtrip/fieldtrip/blob/release/ft_trackusage.m)** function for usage tracking. This function is called once in every MATLAB session from within **[ft_defaults](https://github.com/fieldtrip/fieldtrip/blob/release/ft_defaults.m)** at the moment that you start using the first high-level FieldTrip function. Furthermore, this function could be called at the start of each high-level FieldTrip function or could be called at specific events, such as errors.

The reason for tracking details of the software usage is to gather information about the number of users, how often the software is used, which MATLAB versions are being used, about popular use cases, about potential frequent problems, etc. This information helps us in deciding where to focus our attention in continued development. Furthermore, this information is used to inform our funding sources about the success of the toolbox.

We also track the downloads from our FTP server and we monitor the usage of this website using Google Analytics.
