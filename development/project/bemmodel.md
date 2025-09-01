---
title: An alternative algorithm for constructing triangulated EEG-BEM head models
---

{% include /shared/development/warning.md %}


This page presents the outline of an algorithm (or set of algorithms) that allow the robust creation of single-subject triangulations of the skin/skull/brain boundaries to be used in EEG-BEM volume conduction modeling. The algorithm described here is not implemented in FieldTrip, but an improved version could be considered for implementation

## A short description of the algorithm

### The skin

- Determine which voxels belong to head using simple thresholding, smoothing and region growing
- Project triangulated sphere at center of mass brain onto boundary

{% include image src="/assets/img/development/project/bemmodel/bemmodel2.png" %}

### The brain

- Determine which voxels belong to brain using volumesegment
- Project triangulated sphere at center of mass brain onto boundary
- Optional: use laplacian smoothing on the triangulated surface

{% include image src="/assets/img/development/project/bemmodel/bemmodel1.png" %}

### The skull

- Draw lines from triangulated sphere at center of mass brain
- “Top half”: determine boundary along lines in MR images by trying several algorithms (see below)
- “Bottom half”: define vertices along lines based on average skull thickness

A potential problem in the bottom half is that the skull and brain triangulation intersect. To avoid this one can use the same number of vertices for skull as in brain. An alternative solution is to base the lower half of the triangulation on an "imdilated" brain segmentation.

A known problem in the top half is that the algorithms for determining the skull-skin boundary are not 100% robust. They are based on the MRI intensity countour along the radial lines through the skull and skin.

{% include image src="/assets/img/development/project/bemmodel/bemmodel3.png" %}

This results in outliers.

{% include image src="/assets/img/development/project/bemmodel/bemmodel4.png" %}

### Optimizing the skull triangulation

This requires the computation of the surface laplacial (i.e. smoothness) of the radius of the skull surface. Subsequently the following steps are take

{% include image src="/assets/img/development/project/bemmodel/bemmodel5.png" %}

1.  Detect suspicious vertices in the skull triangulation
    - Any vertex less than 2.5 mm from the brain
    - Any vertex less than 3.5 mm from the scalp
    - Any vertex where the surface laplacian is not sufficiently smooth
2.  Remove suspicious vertices and replace them by interpolation (using minimum laplacian)
3.  Check that the 2.5 and 3.5 criteria are optimally met
4.  Go back to step 1 and repeat until it converges

{% include image src="/assets/img/development/project/bemmodel/bemmodel6.png" %}

## Additional ideas

It is possible to use the skull laplacian smoothness criterium and interpolation also on the brain surface.

It is possible to replace the initial triangulation of the brain surface using the intensity profiles by a triangulation of a segmentation resulting from an dilated brain and eroded skin (using XOR).
