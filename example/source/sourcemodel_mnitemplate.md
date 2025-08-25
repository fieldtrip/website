---
title: Create a template source model aligned to MNI space
category: example
tags: [meg, mri, headmodel, source]
---

# Create template source models aligned to MNI space

On the [template sourcemodel](/template/sourcemodel) page we describe that we have a number of 3D grid
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
Both are correct, but for computers the difference matters. FieldTrip **[ft_volumesegment](/reference/ft_volumesegment)** uses the American spelling, whereas SPM uses the British spelling.
{% include markup/end %}

    % read the 1 mm resolution canonical MNI template MRI
    [ftver, ftpath] = ft_version
    mri = ft_read_mri(fullfile(ftpath, 'template/anatomy/single_subj_T1_1mm.nii'));
    mri.coordsys = 'mni';
    
    % make a tissue probability map segmentation of CSF, white and gray matter
    cfg = [];
    cfg.output = 'tpm';
    cfg.spmmethod = 'old';
    seg = ft_volumesegment(cfg,mri);
    
    % there are also voxels that are neither CSF, white or gray matter
    seg.otherwise = ones(seg.dim)-seg.gray-seg.white-seg.csf;
    
    % make a matrix with 4 columns, each row is a voxel
    % the probabilistic sum of all tissue types adds up to 1, or 100%
    prob = [seg.gray(:) seg.white(:) seg.csf(:) seg.otherwise(:)];
    
    % identify which voxels have the highest probability of being gray matter
    % these are considered to be inside the (binary) grey matter compartment
    inside = zeros(seg.dim);
    for voxel = 1:prod(seg.dim)
    [m,tissue] = max(prob(voxel,:)); % tissue = column, m = number
    inside(voxel) = tissue == 1;
    end
    
    % these are not needed any more
    seg = rmfield(seg,'gray');
    seg = rmfield(seg,'white');
    seg = rmfield(seg,'csf');
    seg = rmfield(seg,'otherwise');
    
    % add the inside-gray-matter mask
    seg.inside = inside;
    
    %% prepare a source model for gray matter
    
    cfg = [];
    cfg.method = 'basedongrid';
    cfg.xgrid = -90:3:90;
    cfg.ygrid = -120:3:90;
    cfg.zgrid = -90:3:90;
    cfg.unit = 'mm';
    
    % you want the xgrid/ygrid/zgrid numbers to be such, that they cover the entire brain
    % and that they are nicely symmetric around the origin. In this case they are chosen
    % such that there is also a dipole exactly at [0, 0, 0].
    
    sourcemodel_template = ft_prepare_sourcemodel(cfg);
    
    % the resulting source model consists of a 3D grid of dipoles that spans the brain,
    % but does not specify which ones are inside the grey matter (or the brain) or outside
    
    figure
    ft_plot_mesh(sourcemodel_template.pos)
    
    % you should rotate the figure, you will see that it is a square block with many dipoles
    
    % we now determine for each dipole what tissue type it is in
    sourcemodel_template.inside = zeros(prod(sourcemodel_template.dim),1);
    
    % the following uses the inverse homogenous transformation to go from head to voxel coordinates
    
    for dipole = 1:prod(sourcemodel_template.dim)       % loop over all dipoles
        thispos = sourcemodel_template.pos(dipole,:);   % the position of this dipole in head coordinates
        thispos = [thispos 1]';
        thisvox = round(inv(seg.transform)*thispos);    % the indices of the nearest voxel in the segmented MRI
        if thisvox(1) < 1 || thisvox(1) > seg.dim(1)
            % it falls outside the segmented volume
            sourcemodel_template.inside(dipole) = 0;
        elseif thisvox(2) < 1 || thisvox(2) > seg.dim(2)
            % it falls outside the segmented volume
            sourcemodel_template.inside(dipole) = 0;
        elseif thisvox(3) < 1 || thisvox(3) > seg.dim(3)
            % it falls outside the segmented volume
            sourcemodel_template.inside(dipole) = 0;
        else
            % look up in the segmented volume whether the nearest voxel is gray matter
            sourcemodel_template.inside(dipole) = seg.inside(thisvox(1), thisvox(2), thisvox(3));
        end
    end
    
    % convert it into a logical array with true/false values
    sourcemodel_template.inside = logical(sourcemodel_template.inside);
    
    % make a plot of the dipoles that are inside the gray matter
    figure
    ft_plot_mesh(sourcemodel_template.pos(sourcemodel_template.inside,:))
    
    % you should rotate the figure, you will see that it is a brain-shaped cloud of dipoles, only in gray matter
    
