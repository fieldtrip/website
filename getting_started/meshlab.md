---
title: Getting started with MeshLab
tags: [mesh, headmodel, meshlab]
---

# Getting started with MeshLab

[MeshLab](https://www.meshlab.net) is open source software for processing and editing 3D triangular meshes. It provides a set of tools for editing, cleaning, healing, inspecting, rendering, texturing and converting meshes. It offers features for processing raw data produced by 3D digitization tools/devices and for preparing models, among others for 3D printing. MeshLab is available for Windows, macOS, and Linux.

## Example use

The following segments an anatomical MRI in 5 tissue types

    cfg           = [];
    cfg.output    = {'csf', 'gray', 'scalp', 'skull', 'white'};
    % cfg.output    = {'brain', 'skull', 'scalp'}; % this is what you need for BEM
    segmentedmri  = ft_volumesegment(cfg, mri);

From the segmentation, you can make triangulated surface meshes with

    cfg             = [];
    cfg.method      = 'projectmesh';
    cfg.numvertices = [3000 2000 1000];
    cfg.tissue      = {'brain', 'skull', 'scalp'};
    mesh = ft_prepare_mesh(cfg, segmentedmri);

For a BEM model, we want the innermost mesh (the brain) to be the most detailed. The potential distribution varies the most on that surface, whereas on the scalp it does not vay that much.

You can also make more detailed meshes for visualisation and coregistration purposes.

    cfg             = [];
    cfg.method      = 'isosurface';
    cfg.numvertices = [inf inf inf];
    cfg.tissue      = {'brain', 'skull', 'scalp'};
    mesh = ft_prepare_mesh(cfg, segmentedmri);

One of the fileformats supported by MeshLab and many other softwares is [STL](https://en.wikipedia.org/wiki/STL_(file_format)).

    % write one surface per file
    ft_write_headshape('surface_brain.stl', mesh(1), 'format', 'stl')
    ft_write_headshape('surface_skull.stl', mesh(2), 'format', 'stl')
    ft_write_headshape('surface_scalp.stl', mesh(3), 'format', 'stl')

If the meshes appear inside-out, you can flip the triangle orientation like this

    mesh(1).tri = fliplr(mesh(1).tri);
    mesh(2).tri = fliplr(mesh(2).tri);
    mesh(3).tri = fliplr(mesh(3).tri);
