---
title: How is anatomical, functional or statistical "volume data" described?
category: faq
tags: [volume, datatype]
redirect_from:
    - /faq/how_is_anatomical_functional_or_statistical_volume_data_described/
---

# How is anatomical, functional or statistical "volume data" described?

One data object used throughout FieldTrip is that of "volume data", i.e. data that can be described as a regular arrangement of voxels in a 3D volume. For example, the function **[ft_read_mri](/reference/fileio/ft_read_mri)** is used to read anatomical MRI data. The function **[ft_sourceanalysis](/reference/ft_sourceanalysis)** is used to perform a beamformer scan on a regular 3D grid. The function **[ft_sourcestatistics](/reference/ft_sourcestatistics)** can be used to do statistics on the **[ft_sourceanalysis](/reference/ft_sourceanalysis)** output, and therefore also statistical parameters such as t-score and probability are defined on a grid that is the same as the source grid.

All functions that accept volume data as input, or that give volume data as output, work with the same basic data structure. An anatomical or functional volume containing Nx*Ny*Nz voxels at least contains the following field

    volume.dim = [Nx Ny Nz]  % number of voxels along each dimensions
    volume.transform         % 4*4 matrix with homogeneous transformation (optional, see below)

Note that FieldTrip adheres to the MATLAB convention for counting voxels, starting to count from 1 and not from 0. The fields above are only needed for the bookkeeping, the actual content of the volume depends on what the data describes. If the volume describes anatomical (MRI) data, it will have the field

    volume.anatomy            % Nx * Ny * Nz matrix

The anatomical data can be represented as double precision floating point values, but also as uint8 or uint16.

If the volume describes functional data, such as a beamformer source reconstruction, it can contai

    volume.avg.pow    % average power
    volume.avg.noise  % average noise projected through filter
    volume.avg.nai    % neural activity index

If the volume describes statistical data, it can contain

    volume.prob       % probability under the null-hypothesis
    volume.mask       % boolean mask with significance
    volume.tscore
    volume.zscore

Volume data is most easily represented as a Nx*Ny*Nz matrix, but can also be represented as a single vector of length Nx*Ny*Nz, in which case the MATLAB command

    volume.param = reshape(volume.param, volume.dim)

can be used to make a 3D volume out of it. To reshape a 3D matrix into a vector, you can do

    volume.param = volume.param(:)

The coordinate system in which you want to represent the data does not necessarily have to correspond with the direction of the principal axes of the volume. For example you have an anatomical MRI, and you want to represent the data in head-coordinates with the axes going through the nose and ears. The homogeneous transformation matrix is used to transform from the native voxel-coordinate system of the volume (in this case MRI) to the other coordinate system (i.e. head). To compute the position of the voxel indices (i, j, k) in headcoordinates, you should do

    [xh yh zh 1] = volume.transform * [i j k 1]'

and the other way around, to express the position of a point in headcoordinates in your volume, you should do

    [i j k 1] = inv(volume.transform) * [xh yh zh 1]'
    i = round(i)
    j = round(j)
    k = round(k)

If no homogeneous transformation matrix is specified, it is assumed to be equal to the identity matrix (i.e. no coordinate transformation is done).
