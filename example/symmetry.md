---
title: Symmetric dipole pairs for beamforming
tags: [example, source]
---

# Symmetric dipole pairs for beamforming

When you expect symmetric activity in an ERP analysis, it makes sense to use a symmetric dipole pair in **[ft_dipolefitting](/reference/ft_dipolefitting)** by specifying the `cfg.symmetry` option. For the scanning methods that are implemented in **[ft_sourceanalysis](/reference/ft_sourceanalysis)**, and notably for the beamformer methods, you can also make use of symmetric dipole pairs.

This is especially beneficial when the source activity in left and right hemisphere is expected to be highly correlated, as the beamformer expects sources to be (reasonably) uncorrelated. By extending the sourcemodel, the source activity that you are simultaneously estimating while scanning includes both left and right hemisphere activity and the correlation _inside_ that sourcemodel is not a problem.

## Simulation of correlated and un-correlated symmetric dipole pairs

To investigate the effects of applying a symmetry constraint to the beamformer analysis, we will simulate two scenarios of symmetric dipoles; correlated and un-correlated. We will then attempt to estimate them with and without symmetry constraints.
First, the symmetric dipoles and a spherical volume conducter model are defined:

    % Define two dipole positions and two directions of moment
    dippos = [-4 -4 4; 4 -4 4];
    dipmom = [1 0 .5; -1 0 .5]';

    % Create an array with some magnetometers at 12cm distance from the origin
    [X, Y, Z] = sphere(10);
    pos = unique([X(:) Y(:) Z(:)], 'rows');
    pos = pos(pos(:,3)>=0,:);
    grad = [];
    grad.coilpos = 12*pos;
    grad.coilori = pos; % in the outward direction

    for i=1:length(pos)
    grad.label{i} = sprintf('chan%03d', i);
    end

    % Create a spherical volume conductor with 10cm radius
    vol.r = 10;
    vol.o = [0 0 0];

Then, two source models are defined; a 'normal' non-symmetric model and one with the symmetry constraint defined for the x-axis (which in this case defines the 'midline'):

    % Source models are defined with x-axis normal to the midline.
    % Non-symmetric 'normal' source model
    cfg = [];
    cfg.headmodel = vol; % use the spherical volume conducter as head model
    cfg.grad = grad;
    cfg.xgrid = -9.5:9.5; % ensure that the midline is not included
    cfg.ygrid = -10:10;
    cfg.zgrid = 0:10;
    sourcemodel_normal = ft_prepare_leadfield(cfg);

    % Source model with symmetry constraint over the midline.
    cfg = [];
    cfg.headmodel = vol;
    cfg.grad = grad;
    cfg.xgrid = -9.5:0; % ensure that the midline is not included
    cfg.ygrid = -10:10;
    cfg.zgrid = 0:10;
    cfg.symmetry = 'x';
    sourcemodel_double = ft_prepare_leadfield(cfg);

    % Plot the grids of the two models
    figure
    ft_plot_mesh(sourcemodel_normal.pos(sourcemodel_normal.inside,:))
    ft_plot_sens(grad)

    figure
    ft_plot_mesh(sourcemodel_double.pos(sourcemodel_double.inside,1:3), 'vertexcolor', 'r')
    ft_plot_mesh(sourcemodel_double.pos(sourcemodel_double.inside,4:6), 'vertexcolor', 'b')
    ft_plot_sens(grad)

{% include image src="/assets/img/example/symmetry/sourcemodel_normal.png" width="300" %}
{% include image src="/assets/img/example/symmetry/sourcemodel_double.png" width="300" %}

In the symmetric sourcemodel, the `.pos` field is evidently a `N/2x6` matrix (where `N` is the number of vertices in the grid), rather than the usual `Nx3`, where the xyz-coordinates of the vertices are given in pairs of triplets.

### Un-correlated symmetric sources with non-symmetric source model

We now define two conditions with uncorrelated (i.e. phase shifted) symmetric 40~Hz signals of varying amplitude emulating a left and right lateral attention modulation:

    cfg.sourcemodel.pos = dippos(:,:);
    cfg.sourcemodel.mom = dipmom(:,:);
    % create some left-right amplitude imbalance, emulating lateral attention modulation
    cfg.sourcemodel.signal = repmat({[1.1*sin(40*2*pi*(0:999)/1000); 0.9*cos(40*2*pi*(0:999)/1000)]}, 1, 10);
    dataLR_attL = ft_dipolesimulation(cfg);
    cfg.sourcemodel.signal = repmat({[0.9*sin(40*2*pi*(0:999)/1000); 1.1*cos(40*2*pi*(0:999)/1000)]}, 1, 10);
    dataLR_attR = ft_dipolesimulation(cfg);


Compute the data covariance matrix, which will capture the activity of each simulated dipole and is needed for the beamformer source estimation:

    cfg = [];
    cfg.covariance = 'yes';
    timelockLR_attL  = ft_timelockanalysis(cfg, dataLR_attL);
    timelockLR_attR  = ft_timelockanalysis(cfg, dataLR_attR);

Now, apply the beamformer based on the non-symmetric 'normal' source model, calculate the lateral contrast, and plot the result:

    cfg = [];
    cfg.headmodel = vol;
    cfg.grad = grad;
    cfg.sourcemodel = sourcemodel_normal;
    cfg.method = 'lcmv';
    singleLR_attL = ft_sourceanalysis(cfg, timelockLR_attL);
    singleLR_attR = ft_sourceanalysis(cfg, timelockLR_attR);

    cfg           = [];
    cfg.operation = '(x2-x1)/(x1+x2)'; % right minus left
    cfg.parameter = 'pow';
    contrastLR_attL_attR = ft_math(cfg, singleLR_attL, singleLR_attR);

    cfg = [];
    cfg.method = 'slice';
    cfg.funparameter = 'pow';
    figure; ft_sourceplot(cfg, contrastLR_attL_attR);

{% include image src="/assets/img/example/symmetry/contrastLR_attL_attR.png" width="300" %}

### Correlated symmetric sources with non-symmetric source model

### Un-correlated symmetric sources with symmetric source model

### Correlated symmetric sources with non-symmetric source model

## Example auditory steady state response

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
