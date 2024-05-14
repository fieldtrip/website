---
title: Symmetric dipole pairs for beamforming
tags: [example, source]
---

# Symmetric dipole pairs for beamforming

When you expect symmetric activity in an ERP analysis, it makes sense to use a symmetric dipole pair in **[ft_dipolefitting](/reference/ft_dipolefitting)** by specifying the `cfg.symmetry` option. For the scanning methods that are implemented in **[ft_sourceanalysis](/reference/ft_sourceanalysis)**, and notably for the beamformer methods, you can also make use of symmetric dipole pairs.

This is especially beneficial when the source activity in left and right hemisphere is expected to be highly correlated, as the beamformer expects sources to be (reasonably) uncorrelated. By extending the sourcemodel, the source activity that you are simultaneously estimating while scanning includes both left and right hemisphere activity and the correlation _inside_ that sourcemodel is not a problem.

{% include markup/yellow %}
This is explained for Steady State Auditory Potentials (SSAEPs) in the paper by Tzvetan Popov, Robert Oostenveld, Jan M. Schoffelen (2018) [FieldTrip Made Easy: An Analysis Protocol for Group Analysis of the Auditory Steady State Brain Response in Time, Frequency, and Space](https://doi.org/10.3389/fnins.2018.00711). Supporting material, including all data and scripts can be found on the [Radboud Data Repository](https://doi.org/10.34973/fkgz-8d22).

{% include badge doi="10.3389/fnins.2018.00711" pmid="30356712" pmcid="PMC6189392" %}
{% include markup/end %}


    mri = ft_read_mri('Subject01.mri');

    % just to check that it is in CTF coordinates and that the y axis is from right (-y) to left (+y)
    ft_determine_coordsys(mri, 'interactive', false)

    % we only need the brain surface, as we'll use a singleshell MEG volume conductor
    cfg = [];
    cfg.output = {'brain'};
    cfg.spmmethod = 'new';
    cfg.spmversion = 'spm12';
    mri_segmented = ft_volumesegment(cfg, mri);

    cfg = [];
    cfg.method = 'singleshell';
    headmodel = ft_prepare_headmodel(cfg, mri_segmented);

    % just to be sure, since we'll specify numbers further down
    headmodel = ft_convert_units(headmodel, 'mm');

    cfg = [];
    cfg.headmodel = headmodel;
    cfg.symmetry = 'y';
    cfg.xgrid = -150:10:150; % in mm
    cfg.ygrid =    5:10:150; % in mm, one hemisphere, offset to the midline
    cfg.zgrid = -150:10:150; % in mm
    sourcemodel = ft_prepare_sourcemodel(cfg);

    % the source position is specified as 1547x6
    % corresponding to 1547 dipole pairs
    
    % using the sensor description from the corresponding MEG data
    % we can now compute the leadfields
    grad = ft_read_sens('Subject01.ds', 'senstype', 'meg');

    cfg = [];
    cfg.grad = grad;
    cfg.channel = {'MEGGRAD'};
    cfg.headmodel = headmodel;
    cfg.sourcemodel = sourcemodel;
    leadfield = ft_prepare_leadfield(cfg);

    % each leadfield matrix is 6x151, where 6 corresponds to 3 orientations for
    % the dipole in left and 3 orientations for the dipole in the right hemisphere

    figure
    ft_plot_mesh(leadfield.pos(leadfield.inside, 1:3), 'vertexcolor', 'r')
    ft_plot_mesh(leadfield.pos(leadfield.inside, 4:6), 'vertexcolor', 'b')
