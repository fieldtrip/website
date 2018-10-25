---
title: What usage information is FieldTrip tracking?
layout: default
tags: [faq]
---

## What usage information is FieldTrip tracking?

The FieldTrip software includes the **[/reference/ft_trackusage](/reference/ft_trackusage)** function for usage tracking. This function is called once in every MATLAB session from within **[/reference/ft_defaults](/reference/ft_defaults)** at the moment that you start using the first high-level FieldTrip function. Furthermore, this function could be called at the start of each high-level FieldTrip function or could be called at specific events, such as errors.
 
We track the details of the software usage to gather information about the number of users, how often the software is used, which MATLAB versions are being used, about popular use cases, about potential frequent problems, etc. This information helps us in deciding where to focus our attention in continued development. Furthermore, this information is used to inform our funding sources about the success of the toolbox. 

We also track the downloads from our ftp server and we monitor the usage of this website using Google Analytics. 
