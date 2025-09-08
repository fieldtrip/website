---
title: Create atlas-based MNI-aligned grids in individual head coordinates
tags: [meg, mri, atlas, headmodel, source]
category: example
redirect_from:
    - /example/create_single-subject_grids_in_individual_head_space_that_are_all_aligned_in_brain_atlas_based_mni_space/
    - /example/sourcemodel_aligned2mni_atlas/
---

When combining the source-level data of multiple subjects this data is typically first interpolated (e.g., using **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)**) and then spatially normalized to a template brain (e.g., using **[ft_volumenormalise](/reference/ft_volumenormalise)**). However it is also possible to define the source reconstruction grid for each individual subject in such a way that all these grids are already aligned in MNI-space. The combination or statistic of source-level data across subjects can then directly be computed within the source-structure without the need to interpolate and normalize each volume. In addition, the position of the grid points can be chosen in a way that only locations corresponding to particular brain areas (parcels) are included.

The procedure is as follows. First, a template grid is computed on the basis of the standard head model located in the FieldTrip template directory. Subsequently, a brain atlas is loaded using **[ft_read_atlas](/reference/fileio/ft_read_atlas)**. On the basis on the brain atlas and the template grid it is possible to create a binary mask of all locations in the template grid that match atlas locations using **[ft_volumelookup](/reference/ft_volumelookup)**. Finally the mask is used to determine which location shall be defined as 'inside' the head model.

    % first you read the MEG single shell headmodel for the MNI template brain
    [ftver, ftpath] = ft_version;
    load(fullfile(ftpath, 'template/headmodel/standard_singleshell.mat'), 'vol');
    vol = ft_convert_units(vol, 'cm');

    cfg = [];
    cfg.xgrid  = -12:1:12;
    cfg.ygrid  = -12:1:12;
    cfg.zgrid  =  -5:1:12;
    cfg.unit   = 'cm';
    cfg.tight  = 'yes';
    cfg.inwardshift = -1.5;
    cfg.headmodel   = vol;
    template_grid   = ft_prepare_sourcemodel(cfg);
    template_grid.coordsys = 'mni';

    figure
    hold on
    ft_plot_mesh(template_grid.pos(template_grid.inside,:));
    ft_plot_headmodel(vol, 'facecolor', 'cortex', 'edgecolor', 'none');
    ft_plot_axes(vol);
    alpha 0.5
    camlight

Read the atlas, ensure it is in cm just like the source model and create the binary mask.

    atlas = ft_read_atlas(fullfile(ftpath, 'template/atlas/aal/ROI_MNI_V4.nii'));
    atlas = ft_convert_units(atlas, 'cm');

    cfg = [];
    cfg.atlas = atlas;
    cfg.roi   = atlas.tissuelabel;  % here you can also specify a single label, i.e. single ROI
    mask      = ft_volumelookup(cfg, template_grid);

Now we determine all indices of the binary mask to be considered as inside the head model. And plot the result. Note the missing dipole locations for example in the vicinity of the ventricles.

    template_grid.inside = false(template_grid.dim);
    template_grid.inside(mask==1) = true;

    figure
    ft_plot_mesh(template_grid.pos(template_grid.inside,:));

{% include image src="/assets/img/example/sourcemodel_aligned2mni_atlas/atlasbasedmnigrid.png" width="600" %}

Download the subject-specific MRI from [our download server](https://download.fieldtriptoolbox.org/tutorial/connectivity_aef/mri.mat) and inverse-warp the subject-specific grid to the template grid.

    mri = ft_read_mri('mri.mat'));

    cfg           = [];
    cfg.warpmni   = 'yes';
    cfg.template  = template_grid;
    cfg.nonlinear = 'yes'; % use non-linear normalization
    cfg.mri       = mri; % this is the individual MRI
    sourcemodel   = ft_prepare_sourcemodel(cfg);

Finally, you can load the subject-specific headmodel from [our download server](https://download.fieldtriptoolbox.org/tutorial/connectivity_aef/hdm.mat) and check the result.

    hdm = ft_read_mri('hdm.mat');

    % put everything in SI units
    hdm         = ft_convert_units(hdm, 'm');
    sourcemodel = ft_convert_units(sourcemodel, 'm');

    figure
    hold on
    ft_plot_headmodel(hdm, 'facecolor', 'cortex', 'edgecolor', 'none');
    ft_plot_axes(hdm);
    alpha 0.4  % make the surface slightly transparent
    ft_plot_mesh(sourcemodel.pos(sourcemodel.inside,:));
    view ([0 -90 0])
