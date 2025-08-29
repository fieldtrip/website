---
title: Create a template source model aligned to MNI space
category: example
tags: [meg, mri, headmodel, source]
---

# Create a template source model aligned to MNI space

On the [template sourcemodel](/template/sourcemodel) page we describe a number of regular 3D grid 
source models defined in MNI space. These models can be used as templates for individual subject data,
allowing for more accurate and consistent source reconstruction across subjects. The procedure for this
is described in the [source model tutorial](/tutorial/sourcemodel).

These source models are only available at a few resolutions, and have dipoles throughout the whole brain
compartment, including CSF, white matter and gray matter. That is convenient for beamformer source
reconstruction of MEG and EEG data with a BEM or single shell head model, but not so for minimum
norm source reconstruction or for source estimates using a FEM model.

The following script describes how to create your own template source model in MNI space, at 3mm
resolution, and only with dipoles in gray matter.

{% include markup/yellow %}
Note that "gray" is the American English spelling, while "grey" is the British English spelling.
Both are correct but when the computer is comparing strings, the difference matters. With
FieldTrip**[ft_volumesegment](/reference/ft_volumesegment)** we try to stick to the American
spelling, whereas SPM uses the British spelling.
{% include markup/end %}

    % read the 1 mm resolution canonical MNI template MRI
    [ftver, ftpath] = ft_version;
    mri = ft_read_mri(fullfile(ftpath, 'template/anatomy/single_subj_T1_1mm.nii'));
    mri.coordsys = 'mni';

    % make a tissue probability map segmentation of CSF, white and gray matter
    cfg = [];
    cfg.output = 'tpm';
    cfg.spmmethod = 'old';
    mri_segmented = ft_volumesegment(cfg,mri);

    % there are also voxels that are neither CSF, white or gray matter
    mri_segmented.otherwise = ones(mri_segmented.dim)-mri_segmented.gray-mri_segmented.white-mri_segmented.csf;

    % make a matrix with 4 columns, each row is a voxel
    % the probabilistic sum of all tissue types adds up to 1, or 100%
    prob = [mri_segmented.gray(:) mri_segmented.white(:) mri_segmented.csf(:) mri_segmented.otherwise(:)];

    % identify which voxels have the highest probability of being gray matter
    % these are considered to be inside the (binary) grey matter compartment
    inside = zeros(mri_segmented.dim);
    for voxel = 1:prod(mri_segmented.dim)
    [m,tissue] = max(prob(voxel,:)); % tissue = column, m = number
    inside(voxel) = (tissue == 1);
    end

    % add the inside-gray-matter mask
    mri_segmented.inside = inside;

    % these are not needed any more
    mri_segmented = rmfield(mri_segmented, 'gray');
    mri_segmented = rmfield(mri_segmented, 'white');
    mri_segmented = rmfield(mri_segmented, 'csf');
    mri_segmented = rmfield(mri_segmented, 'otherwise');

    %% prepare a source model for gray matter

    cfg = [];
    cfg.method = 'basedongrid';
    cfg.xgrid = -120:3:120;
    cfg.ygrid = -120:3:120;
    cfg.zgrid =  -50:3:120;
    cfg.unit = 'mm';

    % you want the xgrid/ygrid/zgrid numbers to be such, that they cover the entire brain
    % and that they are nicely symmetric around the origin. In this case they are chosen
    % such that there is also a dipole exactly at [0, 0, 0].

    sourcemodel_template = ft_prepare_sourcemodel(cfg);
    sourcemodel_template.coordsys = 'mni'; 

    % the resulting source model consists of a 3D grid of dipoles that spans the brain,
    % but does not specify which ones are inside the grey matter (or the brain) or outside

    figure
    ft_plot_mesh(sourcemodel_template.pos)
    ft_plot_axes(sourcemodel_template) % this shows the axes, including the correct labels along the axes

    % you should rotate the figure, you will see that it is a square block with many dipoles

    % we now determine for each dipole what tissue type it is in
    sourcemodel_template.inside = zeros(prod(sourcemodel_template.dim),1);

    % the following uses the inverse homogenous transformation to go from head to voxel coordinates

    for dipole = 1:prod(sourcemodel_template.dim)       % loop over all dipoles
        thispos = sourcemodel_template.pos(dipole,:);   % the position of this dipole in head coordinates
        thispos = [thispos 1]';
        thisvox = round(inv(mri_segmented.transform)*thispos);    % the indices of the nearest voxel in the segmented MRI
        if thisvox(1) < 1 || thisvox(1) > mri_segmented.dim(1)
            % it falls outside the segmented volume
            sourcemodel_template.inside(dipole) = 0;
        elseif thisvox(2) < 1 || thisvox(2) > mri_segmented.dim(2)
            % it falls outside the segmented volume
            sourcemodel_template.inside(dipole) = 0;
        elseif thisvox(3) < 1 || thisvox(3) > mri_segmented.dim(3)
            % it falls outside the segmented volume
            sourcemodel_template.inside(dipole) = 0;
        else
            % look up in the segmented volume whether the nearest voxel is gray matter
            sourcemodel_template.inside(dipole) = mri_segmented.inside(thisvox(1), thisvox(2), thisvox(3));
        end
    end

    % convert it into a logical array with true/false values
    sourcemodel_template.inside = logical(sourcemodel_template.inside);

    % make a plot of the dipoles that are inside the gray matter
    figure
    ft_plot_mesh(sourcemodel_template.pos(sourcemodel_template.inside,:))
    ft_plot_axes(sourcemodel_template) % this shows the axes, including the correct labels along the axes

    % you should rotate the figure, you will see that it is a brain-shaped cloud of dipoles, only in gray matter

    % save the 3mm MNI-aligned template grid with only gray matter dipoles to a file
    save sourcemodel_template3mm.mat sourcemodel_template

This template source model can be used just as the other templates to create MNI-aligned individual source 
models, as explained in the tutorial on contructing a [source model](/tutorial/source/sourcemodel/#subject-specific-grids-that-are-equivalent-across-subjects-in-normalized-space).

This template sourcemodel is also used in [another example script](/example/source/sourcemodel_fem_centroids)
that shows how to use an individually aligned MNI template grid with a FEM headmodel.
