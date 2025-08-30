---
title: Use an MNI-aligned grid with a FEM headmodel in individual head coordinates
category: example
tags: [source, sourcemodel, fem]
---

# Use an MNI-aligned grid with a FEM headmodel in individual head coordinates

When using a FEM head model in forward and inverse computations, for numerical reasons the dipoles are ideally placed well within the geometric elements of the FEM mesh and not on the element boundaries, i.e., at the center of the hexahedra or tetrahedra. To support this, the **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)** function supports for `cfg.method` the `basedoncentroids` method. Alternatively, it has the `cfg.movetocentroids` option.

With the `basedoncentroids` method, a dipole is placed at the center of each hexahedron or tetrahedron. If the FEM mesh is based on a segmentation of an anatomical MRI at 1 mm, the geometric elements of the FEM mesh are also about 1 mm large, which means that the grid of dipoles will also have 1 mm spacing. That is a very dense (most likely irregular) grid, and the computational time fo the forward and inverse method will be very long.

With the `cfg.movetocentroids` option, you can use any of the other methods to construct the initial source model, for example the `basedongrid` or the `basedonresultion` method. The resulting grid of dipoles subsequently undergoes some postprocessing (sill inside the ft_prepare_sourcemodel function) where each dipole is moved to the center of the nearest hexahedral or tetrahedral element. The tissue type of that hexahedral or tetrahedral element is subsequently copied and retained alongside the dipoles, allowing you yourself (outside the function) to make an inside selection of only the dipoles in the grey matter of the FEM mesh. This approach allows you to make a grid with a resolution according to your own choice that results in a more appropriate computational time.

Regardless of which of the two approaches you use, the number of dipoles "inside" the gray matter and their position will correspond to the individual's FEM model, and hence will differ over subjects, thereby complicating group-level statistics. For MEG (using singleshell and BEM headmodels) we have adopted the practice of using an [MNI-aligned grid of dipoles](/tutorial/source/sourcemodel/#subject-specific-grids-that-are-equivalent-across-subjects-in-normalized-space) that is equivalent across subjects. The following example demonstrates how to use the same procedure for FEM headmodels, regardless whether for EEG or MEG.

To demonstrate it, we will start with a headmodel for the example Subject01 that was constructed in the tutorial on [creating a FEM volume conduction model for EEG](/tutorial/source/headmodel_eeg_fem). Furthermore, we will use the MNI-aligned template grid at 3 mm that was created in the [corresponding example](/example/source/sourcemodel_mnitemplate).

The required input files are available from our [download server](https://download.fieldtriptoolbox.org/example/sourcemodel_fem_centroids/).

    % we start with loading the FEM head model
    load('headmodel.mat')

    %% we prepare an individual sourcemodel based on the centroids

    % this places dipoles at centers of the hexahedral or tetrahedral FEM mesh
    % elements, but only for the grey matter. This results in a high resolution
    % mesh with dipoles approximately every 1 mm - assuming the segmented MRI on
    % which the mesh is based had a 1 mm resolution.

    cfg = [];
    cfg.method = 'basedoncentroids';
    cfg.headmodel = headmodel; % has gray matter
    cfg.tight = 'no';
    sourcemodel_individual = ft_prepare_sourcemodel(cfg);

    %% we prepare the MNI-warped sourcemodel

    % load the individual subject's MRI that was used for the segmentation and for creating the FEM mesh
    load('mri_resliced.mat')

    % load the MNI-based template grid with the preferred resolution 
    % the inside dipoles must be gray matter only, see https://www.fieldtriptoolbox.org/example/source/sourcemodel_mnitemplate/
    load('sourcemodel_template3mm.mat')

    % plot the dipole positions that are inside the MNI template sourcemodel,
    % this shows a regular grid that is also nicely aligned with the x, y, and z axes
    figure
    ft_plot_mesh(sourcemodel_template.pos(sourcemodel_template.inside,:))
    ft_plot_axes(sourcemodel_template)

    % warp the MNI-based template grid to the individual head
    cfg = [];
    cfg.mri = mri_resliced; % same MRI as used for segmentation and mesh 
    cfg.template = sourcemodel_template; % MNI template grid, defines resolution of output
    cfg.method = 'basedonmni'; % uses template source positions inversely warped from MNI to native space (subject MRI)
    cfg.nonlinear = 'yes';  % we warp non-linearly
    sourcemodel_mni = ft_prepare_sourcemodel(cfg); % has same resolution as template grid

    % plot the dipole positions with respect to the individual head
    % note that it is in CTF coordinates and not nicely aligned with the x, y, and z axes any more
    figure
    ft_plot_mesh(sourcemodel_mni.pos(sourcemodel_mni.inside,:))
    ft_plot_axes(sourcemodel_mni)

    % the MNI coordinate system has the origin at the AC and the x-axis towards
    % the right, whereas the individual head is in CTF coordinates with the
    % origin between the ears and the x-axis towards the noise.
    % 
    % See https://www.fieldtriptoolbox.org/faq/coordsys/

    %% move the dipoles from the individually aligned MNI source model to the 
    % closest centroids of the hexahedral or tetrahedral FEM mesh

    % this takes a couple of minutes
    tic 
    [idx,~] = dsearchn(sourcemodel_individual.pos(sourcemodel_individual.inside,:), sourcemodel_mni.pos(sourcemodel_mni.inside,:)); % dsearchn(A, B)
    toc

     % get all "inside" grid points (= grey matter)
    insidepos = sourcemodel_individual.pos(sourcemodel_individual.inside,:);
    
    % replace the inside grid points with the positions of the closest centroids
    sourcemodel_mni.pos(sourcemodel_mni.inside,:) = insidepos(idx,:);

    figure
    ft_plot_mesh(sourcemodel_mni.pos(sourcemodel_mni.inside,:))
    ft_plot_axes(sourcemodel_mni)

    % The dipoles are now still in CTF coordinates, consistent with the individual
    % MRI, headmodel and electrodes, and are also one-by-one comparable to
    % their matching locations in MNI space. However, in individual space they
    % have all moved a little bit, so that they align with the nearest
    % grey-matter centroids. Consequently, they are not nicely aligned any more,
    % regardless how you turn the figure.
