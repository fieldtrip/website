---
title: How does the filter padding in preprocessing work?
tags: [faq, preprocessing, artifact, filter]
---

# How does the filter padding in preprocessing work?

The preprocessing parameter _cfg.padding_ defines the duration to which the data in the trial will be padded: not only the segment of data that corresponds to the trial is read from the file, but also some extra data around it. After filtering this padding is removed from the data and preprocessing only returns the segment of interest.

Padding the data can be beneficial, since the edge artifacts that are typically seen after filtering will be in the padding and not in the segment of interest. Padding is also relevant for DFT filtering of the 50Hz line noise artifact: long padding ensures a higher frequency resolution for the DFT filter, causing a narrower notch to be removed from the data. This is especially relevant for multi-taper frequency analyses.

See also this [FAQ](/faq/how_can_i_interpret_the_different_types_of_padding_that_i_find_when_dealing_with_artifacts) on how the different types of padding are to be interpreted in relation to artifact detection.
