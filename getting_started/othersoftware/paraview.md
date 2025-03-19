---
title: Getting started with ParaView
category: getting_started
tags: [mesh, segmentation, volume, headmodel, paraview]
redirect_from:
    - /getting_started/paraview/
---

# Getting started with ParaView

[ParaView](https://www.paraview.org) is both an application framework and a turn-key application for advanced data visualization that can be used to inspect anatomical MRI data and segmentations, in combination with triangular, tetrahedral and/or hexahedral meshes. It is useful to check the details of the meshes used in BEM and FEM forward modeling.

## Example use

The following segments an anatomical MRI in 5 tissue types

    cfg           = [];
    cfg.output    = {'csf', 'gray', 'scalp', 'skull', 'white'};
    % cfg.output    = {'brain', 'skull', 'scalp'}; % this is what you need for BEM
    segmentedmri  = ft_volumesegment(cfg, mri);

From the segmentation, you can make meshes with

    cfg             = [];
    cfg.method      = 'isosurface';
    cfg.numvertices = inf;
    cfg.tissue      = {'csf', 'gray', 'scalp', 'skull', 'white'};
    surface = ft_prepare_mesh(cfg, segmentedmri);

    cfg        = [];
    cfg.method = 'tetrahedral';
    tetrahedral = ft_prepare_mesh(cfg, segmentedmri);

    cfg        = [];
    cfg.method = 'hexahedral';
    hexahedral = ft_prepare_mesh(cfg, segmentedmri);

Using the `isosurface` method of **[ft_prepare_mesh](/reference/ft_prepare_mesh)** and the highest number of vertices makes a detailed surface description using the MATLAB [isosurface](https://nl.mathworks.com/help/matlab/ref/isosurface.html) function. The surface meshes created here are not suitable for a BEM model, as that requires nested surfaces that are closed and non-intersecting. To construct BEM meshes you can use the `projectmesh` method on the brain, skull and scalp segmentation.

The tetrahedral and hexahedral meshes can be used for FEM models.

We can write the anatomical MRI and segmentation to a `.vtk` file with **[ft_write_mri](/reference/fileio/ft_write_mri)**

    % write the anatomical MRI, including the coordinate transformation matrix
    ft_write_mri('mri.vtk', mri.anatomy, 'transform', mri.transform, 'dataformat', 'vtk')

    % convert the different boolean/probabilistic volumes into one volume with indices
    segmentedmri = ft_datatype_segmentation(segmentedmri, 'segmentationstyle', 'indexed');

    % write the segmentation with the indices that represent the different issue types
    ft_write_mri('segmentedmri.vtk', segmentedmri.tissue, 'transform', segmentedmri.transform, 'dataformat', 'vtk')

and the meshes with **[ft_write_headshape](/reference/fileio/ft_write_headshape)**

    % one surface per file
    ft_write_headshape('surface_csf.vtk', surface(1), 'format', 'vtk')
    ft_write_headshape('surface_gray.vtk', surface(2), 'format', 'vtk')
    ft_write_headshape('surface_scalp.vtk', surface(3), 'format', 'vtk')
    ft_write_headshape('surface_skull.vtk', surface(4), 'format', 'vtk')
    ft_write_headshape('surface_white.vtk', surface(5), 'format', 'vtk')

    % also write the tissue indices
    ft_write_headshape('tetrahedral.vtk', tetrahedral, 'format', 'vtk', 'data', tetrahedral.tissue)

    % also write the tissue indices
    ft_write_headshape('hexahedral.vtk', hexahedral, 'format', 'vtk', 'data', hexahedral.tissue)

It is possible to split the tetrahedral mesh into the different tissue types and write those to separate files.

    % the tissue and tissuelabel will become invalid
    tetrahedral_csf   = rmfield(tetrahedral, {'tissue', 'tissuelabel'});
    tetrahedral_gray  = rmfield(tetrahedral, {'tissue', 'tissuelabel'});
    tetrahedral_scalp = rmfield(tetrahedral, {'tissue', 'tissuelabel'});
    tetrahedral_skull = rmfield(tetrahedral, {'tissue', 'tissuelabel'});
    tetrahedral_white = rmfield(tetrahedral, {'tissue', 'tissuelabel'});

    % only select one tissue type
    tetrahedral_csf.tet   = tetrahedral.tet(tetrahedral.tissue==1,:);
    tetrahedral_gray.tet  = tetrahedral.tet(tetrahedral.tissue==2,:);
    tetrahedral_scalp.tet = tetrahedral.tet(tetrahedral.tissue==3,:);
    tetrahedral_skull.tet = tetrahedral.tet(tetrahedral.tissue==4,:);
    tetrahedral_white.tet = tetrahedral.tet(tetrahedral.tissue==5,:);

    ft_write_headshape('tetrahedral_csf.vtk', tetrahedral_csf, 'format', 'vtk')
    ft_write_headshape('tetrahedral_gray.vtk', tetrahedral_gray, 'format', 'vtk')
    ft_write_headshape('tetrahedral_scalp.vtk', tetrahedral_scalp, 'format', 'vtk')
    ft_write_headshape('tetrahedral_skull.vtk', tetrahedral_skull, 'format', 'vtk')
    ft_write_headshape('tetrahedral_white.vtk', tetrahedral_white, 'format', 'vtk')

and idem for the hexahedral meshes.

    % the tissue and tissuelabel will become invalid
    hexahedral_csf   = rmfield(hexahedral, {'tissue', 'tissuelabel'});
    hexahedral_gray  = rmfield(hexahedral, {'tissue', 'tissuelabel'});
    hexahedral_scalp = rmfield(hexahedral, {'tissue', 'tissuelabel'});
    hexahedral_skull = rmfield(hexahedral, {'tissue', 'tissuelabel'});
    hexahedral_white = rmfield(hexahedral, {'tissue', 'tissuelabel'});

    % only select one tissue type
    hexahedral_csf.hex   = hexahedral.hex(hexahedral.tissue==1,:);
    hexahedral_gray.hex  = hexahedral.hex(hexahedral.tissue==2,:);
    hexahedral_scalp.hex = hexahedral.hex(hexahedral.tissue==3,:);
    hexahedral_skull.hex = hexahedral.hex(hexahedral.tissue==4,:);
    hexahedral_white.hex = hexahedral.hex(hexahedral.tissue==5,:);

    ft_write_headshape('hexahedral_csf.vtk', hexahedral_csf, 'format', 'vtk')
    ft_write_headshape('hexahedral_gray.vtk', hexahedral_gray, 'format', 'vtk')
    ft_write_headshape('hexahedral_scalp.vtk', hexahedral_scalp, 'format', 'vtk')
    ft_write_headshape('hexahedral_skull.vtk', hexahedral_skull, 'format', 'vtk')
    ft_write_headshape('hexahedral_white.vtk', hexahedral_white, 'format', 'vtk')
