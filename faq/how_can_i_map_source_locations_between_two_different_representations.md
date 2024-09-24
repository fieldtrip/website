---
title: How can I map source locations onto an anatomical label in an atlas?
category: faq
tags: [source, interpolate, atlas, label]
---

# How can I map source locations onto an anatomical label in an atlas?

After doing your source reconstruction, you may want to interpolate an atlas onto your sourcemodel, for example to be able to find peaks of activity within an anatomical ROI.

The best way to go about is to do your beamformer source reconstruction on a subject-specific grid, which is inverse-warped from a regular grid defined on the MNI-template. You can read more about it in the example script [create a grid in individual head space from a template grid in MNI space](/example/sourcemodel_aligned2mni).

Then, you can interpolate the atlas of your choice onto this sourcemodel using **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)**.

    % read the atlas
    atlas = ft_read_atlas('~/fieldtrip/template/atlas/aal/ROI_MNI_V4.nii');

    % load the template sourcemodel with the resolution you need (i.e. the resolution you used in your beamformer grid)
    load('~/fieldtrip/template/sourcemodel/standard_sourcemodel3d10mm.mat')

    % and call ft_sourceinterpolate:
    cfg = [];
    cfg.interpmethod = 'nearest';
    cfg.parameter = 'tissue';
    sourcemodel2 = ft_sourceinterpolate(cfg, atlas, sourcemodel);

_Some useful tips:_

- Ensure that the units are consistent in atlas and sourcemodel. If that's not the case, use **[ft_convert_units](/reference/forward/ft_convert_units)**.
- When using **[ft_read_atlas](/reference/fileio/ft_read_atlas)**, it is better to use an atlas defined in MNI space, like the AAL atlas, in order to avoid too much distortion when converting between MNI and Talairach space. The figure below exemplifies this issue.
  {% include image src="/assets/img/faq/how_can_i_map_source_locations_between_two_different_representations/atlas_afni_brainweb_sourcespace.png" width="600" %}
  _Comparing grey matter tagging using atlases AFNI (all labels; blue) and Brainweb (tissue grey_matter; red). Note how the AFNI version does not fill the volume conductor model completely, probably due to TAL to MNI transformation issues._

From the previous step, a field 'tissue' should be created in sourcemodel2: 'tissue' represents the anatomical labels, according to the corresponding atlas. 'atlas.tissuelabel' gives the labels that correspond to the numbers in the tissue field.
Now without the need to call **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)** or **[ft_volumenormalise](/reference/ft_volumenormalise)** on your source-reconstructed data, you can get the indices of the source positions that have this particular anatomical label in your source variable.

    indx = find(sourcemodel2.tissue==x); % where x is the number of your choice
