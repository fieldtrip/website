---
title: Compute EEG leadfields using a FEM headmodel
category: example
tags: [eeg, fem, leadfield, headmodel]
redirect_from:
    - /example/fem/
---

# Compute EEG leadfields using a FEM headmodel

    [ftver, ftpath] = ft_version;
    
    %% read mri
    mri = ft_read_mri('Subject01.mri');

    %% segmentation
    cfg          = [];
    cfg.output   = {'gray', 'white', 'csf', 'skull', 'scalp'};
    segmentedmri = ft_volumesegment(cfg, mri);

    %% mesh
    cfg        = [];
    cfg.shift  = 0.3;
    cfg.method = 'hexahedral';
    mesh       = ft_prepare_mesh(cfg,segmentedmri);

    %% volume conductor
    cfg              = [];
    cfg.method       = 'simbio';
    cfg.conductivity = [0.33 0.14 1.79 0.01 0.43];
    headmodel        = ft_prepare_headmodel(cfg, mesh);

    %% electrode alignment
    elec = ft_read_sens(fullfile(ftpath,'template/electrode/standard_1020.elc'));

    % the location of the fiducials is specified in the MRI
    fiducials = mri.fid;

    % match the fiducials from the elec structure with those of the MRI
    cfg          = [];
    cfg.method   = 'fiducial';
    cfg.template = fiducials;
    cfg.elec     = elec;
    cfg.fiducial = {'Nz', 'LPA', 'RPA'};
    elec_align   = ft_electroderealign(cfg);

    % add 12 mm to the x-axis, needed due to different definitions of the fiducials
    % the ear points are placed at the ear canals in the MRI, and at the pre-auricular points in the electrodes
    % an interactive realignment is recommendedto check that it all fits
    n = size(elec_align.chanpos, 1);
    for i=1:n
     elec_align.chanpos(i,1) = elec_align.chanpos(i,1) + 12;
     elec_align.elecpos(i,1) = elec_align.elecpos(i,1) + 12;
    end

    figure
    ft_plot_sens(elec_align, 'label', 'label');
    hold on
    ft_plot_mesh(mesh,'edgeonly', 'yes', 'vertexcolor', 'none', 'facecolor', [0.5 0.5 0.5], 'facealpha',1, 'edgealpha', 0.1)

    %% make the sourcemodel/grid
    cfg            = [];
    cfg.mri        = mri;
    sourcemodel    = ft_prepare_sourcemodel(cfg);
    sourcemodel    = ft_convert_units(sourcemodel, headmodel.unit);

    cfg            = [];
    cfg.headmodel  = headmodel;
    cfg.elec       = elec_align;
    cfg.grid       = sourcemodel;
    lf             = ft_prepare_leadfield(cfg);

    % plot the leadfield for a few representative locations: points around z-axis with increasing z values

    plotpos   = [];
    positions = [];
    n = size(lf.pos, 1);
    p = 1;
    for i = 1:n
      if lf.pos(i,1)==-0.1 && lf.pos(i,2)==-0.2
          plotpos(p)=i;
          positions(p,:) = lf.pos(i,:);
          p=p+1;
      end
    end

    figure;
    for i=1:20

      subplot(4,5,i);
      ft_plot_topo3d(lf.cfg.elec.chanpos, lf.leadfield{plotpos(i)}(:,3));
      % view([0 0]);

    end
