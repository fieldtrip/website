---
title: Why are there multiple neighbour templates for the Neuromag306 system?
category: faq
tags: [neuromag, template, warning]
---

# Why are there multiple neighbour templates for the Neuromag306 system?

The 306-channel Neuromag system has two kind of sensors, planar gradiometers and magnetometers. These two kind of sensors are recording in different units (fT/cm vs. fT). A proper combination of signals from these two sensors is therefore difficult and would involve unit conversion. Hence, for defining neighbours we decided to split them apart and have two neighbour templates, a neuromag306mag for the magnetometers and a neuromag306planar for the planar gradiometers. The third template, neuromag306cmb is for combined planar channels following **[ft_combineplanar](/reference/ft_combineplanar)**.
