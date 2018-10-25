---
title: Why are there multiple neighbour templates for the NeuroMag306 system?
layout: default
tags: [faq, neuromag, template, warning]
---

## Why are there multiple neighbour templates for the NeuroMag306 system?

The neuromag306 system has two kind of sensors, planar gradiometers and magnetometers. These two kind of sensors are recording in different units (fT/cm vs. fT). A proper combination of signals from these two sensors is therefore difficult and would involve unit conversion. Hence, for defining neighbours we decided to split them apart and have two neighbour templates, a neuromag306mag for the magnetometers and a neuromag306plan for the gradiometers. The third template, neuromag306, is a simple concatenation of the two mentioned templates, i.e. magnetometers and gradiometers are still separated.
