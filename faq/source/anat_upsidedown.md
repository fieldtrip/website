---
title: My MRI is upside down, is this a problem?
tags: [mri, volume, coordinate]
category: faq
redirect_from:
    - /faq/my_mri_is_upside_down_is_this_a_problem/
    - /faq/anat_upsidedown/
---

No, it isn't. The anatomical image is represented as a cube in which a bunch of numbers are stored. Each of these numbers represent a voxel and have a specific physical dimension. The interpretation of these voxels in 3-dimensional space can be done in two ways. We can attach an (uninteresting) voxel-based coordinate system to the cube of numbers, where we start in the lower left corner, and call this the origin. (Note: this can be (0,0,0), or (1,1,1) depending on whether you use the convention to start counting voxels with 0 or with 1). The other (interesting) coordinate system relates to a set of Cartesian axes which make sense relative to a reference object. In our case, this is typically the brain. In this case, there may be different conventions that can be used. See this Frequently Asked Question about [the definition of coordinate systems](/faq/source/coordsys) for more information.

The bottom line is now, that **if your anatomical volume is registered to a meaningful coordinate system**, it doesn't really matter whether the anatomy appears upside down, or not. The figure tries to illustrate this, where the green axes represent the axes of the interesting coordinate system, that is defined relative to the potato, whereas the pink axes represent the voxel coordinate axes. FieldTrip works with the coordinate system defined by the green axes, which are stored in the transformation matrix that is attached to the MRI structure.

If you still find the upside-down issue problematic, you can use **[ft_volumereslice](/reference/ft_volumereslice)**. See this Frequently Asked Question about [reslicing of an MRI ](/faq/source/anat_reslice) for more information.

{% include image src="/assets/img/faq/anat_upsidedown/potatomen.png" width="600" %}

_Figure; The interpretation of the axes in the voxel coordinate system (pink) depends on how the anatomy is stored in the 'box', but the interpretation of the axes in the potato-related coordinate system (green) stays the same. This is irrespective of how the anatomy is stored in the box._
