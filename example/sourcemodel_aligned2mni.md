---
title: Create MNI-aligned grids in individual head-space
tags: [example, meg, mri, headmodel, source]
redirect_from:
   - /example/create_single-subject_grids_in_individual_head_space_that_are_all_aligned_in_mni_space/
---

# Create MNI-aligned grids in individual head-space

When combining the source-level estimates of activity in multiple subjects, the activity can first be interpolated on the individuals MRI (using **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)**) and then spatially normalized to a template brain (using **[ft_volumenormalise](/reference/ft_volumenormalise)**).

It is also possible to define the source reconstruction grid for each individual subject in such a way that all these grids are already aligned in MNI-space. The combination or statistic of source-level data across subjects can then directly be computed within the source-structure _without the need_ to interpolate and normalize each volume.

{% include markup/blue %}
The content of this page has moved to another location, and is dealt with **in context** in the tutorial about [the construction of different types of source models](/tutorial/sourcemodel#subject-specific_grids_that_are_equivalent_across_subjects_in_normalized_space).
{% include markup/end %}
