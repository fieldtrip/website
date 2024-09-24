---
title: I have problems reading in neuroscan .cnt files. How can I fix this?
category: faq
tags: [raw, neuroscan, eeg, dataformat, preprocessing]
---

# I have problems reading in neuroscan .cnt files. How can I fix this?

Neuroscan .cnt files can have the data stored with 16 or 32-bit resolution. It is not straightforward to extract this from the file's header. By default the data are assumed to be 16 bit. The result of this is that if in reality your data are stored with 32-bit resolution, it looks as if the data are corrupt. Moreover there will be a factor of 2 discrepancy between the number of expected data samples based on total measurement time, and the number of data samples which are returned by the reading function. If you suspect that this may be causing your problems, you can explicitly specify cfg.dataformat, cfg.headerformat and cfg.eventformat to be 'ns_cnt16' or 'ns_cnt32', for a bit resolution of 16 or 32, respectively.
