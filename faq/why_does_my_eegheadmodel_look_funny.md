
    % load an anatomical mri
    [ftver, ftpath] = ft_version;
    mri = ft_read_mri(fullfile(ftpath, 'template/anatomy', 'single_subj_T1_1mm.nii'));
    mri.coordsys = 'acpc';

The image on disk has an ugly aliasing artifact at the top, causing the
standard settings to create an ugly segmentation. increasing the
threshold for the scalp segmentation, and switching off the smoothing is
sufficient to fix it in this case. But let's first show that it leads to
a segmentation problem, and a funky scalp surface.

    cfg          = [];
    cfg.output   = {'brain','skull','scalp'};
    segmentedmri0 = ft_volumesegment(cfg, mri);

    cfg             = [];
    cfg.tissue      = {'brain','skull','scalp'};
    cfg.numvertices = [3000 2000 1000];
    bnd0            = ft_prepare_mesh(cfg, segmentedmri0);

    figure;
    ft_plot_mesh(bnd0(3), 'facecolor',[0.4 0.4 0.4]);
    view([90 0]);

adjusting the settings for the segmentation is helpful in this case, but
will not always work.
    cfg          = [];
    cfg.output   = {'brain','skull','scalp'};
    cfg.scalpthreshold = 0.2;
    cfg.scalpsmooth  = 'no';
    segmentedmri = ft_volumesegment(cfg, mri);

    cfg             = [];
    cfg.tissue      = {'brain','skull','scalp'};
    cfg.numvertices = [3000 2000 1000];
    bnd             = ft_prepare_mesh(cfg, segmentedmri);

    figure;
    ft_plot_mesh(bnd(3), 'facecolor',[0.4 0.4 0.4]);
    view([90 0]);

the chunk of code below is intended to create a mask for the relevant
anatomical data, so that the aliasing artifact can be zero'ed out, so
that we don't need to account for that anymore
    scalpmask = double(segmentedmri.scalp);

fill the bottom
    scalpmask(50:130,50:130,1) = 1;
    pw_dir = pwd;
    cd(fullfile(ftpath, 'private'));
    scalpmask = volumefillholes(scalpmask);
    cd(pw_dir);

    mri2 = mri;
    mri2.anatomy(~scalpmask) = 0; % avoid the strange aliasing effect

change the homogeneity of the image
    krn  = gausswin(181,2)*gausswin(201,2)';
    K    = repmat(krn, [1 1 180]);
    for k = 1:180
      K(:,:,k) = K(:,:,k).*(k./150);
    end
    blob = ones(mri2.dim);
    blob(91+[-90:90], 101+[-100:100], 2:end) = max(1-K,0);

    mri2.anatomy = mri2.anatomy.*blob;
    ft_sourceplot([], mri2);

    cfg          = [];
    cfg.output   = {'brain','skull','scalp'};
    segmentedmri2 = ft_volumesegment(cfg, mri2);

    cfg             = [];
    cfg.tissue      = {'brain','skull','scalp'};
    cfg.numvertices = [3000 2000 1000];
    bnd2            = ft_prepare_mesh(cfg, segmentedmri2);
the above already throws a warning that the segmentation is not
star-shaped

    figure;
    ft_plot_mesh(bnd2(3), 'facecolor',[0.4 0.4 0.4]);
    view([90 0]);

estimate the inhomogeneity and remove this bias
    mri3 = ft_volumebiascorrect([], mri2);

    cfg          = [];
    cfg.output   = {'brain','skull','scalp'};
    segmentedmri3 = ft_volumesegment(cfg, mri3);

    cfg             = [];
    cfg.tissue      = {'brain','skull','scalp'};
    cfg.numvertices = [3000 2000 1000];
    bnd3            = ft_prepare_mesh(cfg, segmentedmri3);

    figure;
    ft_plot_mesh(bnd3(3), 'facecolor',[0.4 0.4 0.4]);
    view([90 0]);
