---
title: source reconstruction using two dipoles
---

{% include /shared/development/warning.md %}

## source reconstruction using two dipoles

## Description

This example script shows you how to work with more advanced source models in case of correlated sources. This can be used to reconstruct the location of activity (power) in case of correlated sources, but also for more accurate reconstruction of coherence with a muscular reference channel (c.f. Schoffelen 2008).

It first creates some simulated channel-level MEG data with two dipoles with varying amounts of correlation.

Subsequently it does a beamformer source reconstruction to localize the activity. For a large amount of correlation between the sources, the source reconstruction will fail to reconstruct the correct source locations.

A double-dipole source model in the beamformer scan can be used to circumvent the problem of correlated sources.

NOTE: the example below uses some low-level functions from the FieldTrip/private directory that will not be found in the default installation of FieldTrip. For the example below to work, you should rename the FieldTrip/private directory and add it explicitly to your path.

## Generate simulated data

FIXME in the following section the simulated data should consist of two dipoles with more appropriate time courses

    % create a gradiometer array with magnetometers at 12cm distance from the origin
    [pnt, tri] = icosahedron162;
    pnt        = pnt(pnt(:,3)>=0,:);
    grad.pnt   = 12*pnt;
    grad.ori   = pnt;
    for i=1:length(pnt)
    grad.label{i} = sprintf('chan%03d', i);
    end

    % create a spherical volume conductor with 10cm radius
    vol.r = 9;
    vol.o = [0 0 2.5];

    % note that beamformer scanning will be done with a 1cm grid, so you should
    % not put the dipole on a position that will not be covered by a grid
    % location later

    % create a dipole simulation with two dipoles and a custom timecourse
    cfg      = [];
    cfg.headmodel = vol; % see above
    cfg.grad = grad;     % see above
    cfg.dip.pos = [
     0  6  3        % dipole 1
     0  -6 3        % dipole 2
     ];
    cfg.dip.mom = [      % each row represents [qx1 qy1 qz1 qx2 qy2 qz2]
     0 1 0 0 0 0       % this is how signal1 contributes to the 6 dipole components
     0 0 0 0 1 0       % this is how signal2 contributes to the 6 dipole components
     ]';               % note, it should be transposed
    time = (1:1000)/1000;
    signal1 = sin(10*time*2*pi);
    signal2 = cos(15*time*2*pi);
    cfg.dip.signal = {[signal1; signal2]}; % one trial only
    cfg.fsample = 1000;                     % Hz
    cfg.relnoise = 10;
    data = ft_dipolesimulation(cfg);

FIXME the following code should do freqanalysis instead of timelockanalysis

    % compute the data covariance matrix, which will capture the activity of
    % the simulated dipole
    cfg = [];
    cfg.covariance = 'yes';
    timelock = ft_timelockanalysis(cfg, data);

## Conventional beamformer source reconstruction fails for correlated sources

The following code demonstrates how to do beamformer source reconstruction with a single-dipole source model, i.e. conventional beamforming.

FIMXE insert figure at the end of the following block of code

    % do the beamformer source reconstuction on a 1 cm grid
    cfg            = [];
    cfg.headmodel  = vol;
    cfg.grad       = grad;
    cfg.resolution = 1;
    cfg.method     = 'lcmv';
    source         = ft_sourceanalysis(cfg, timelock);

    % compute the neural activity index, i.e. projected power divided by
    % projected noise
    cfg = [];
    cfg.powmethod = 'none'; % keep the power as estimated from the data covariance, i.e. the induced power
    source = ft_sourcedescriptives(cfg, source);

    cfg = [];
    cfg.method = 'ortho';
    cfg.funparameter = 'nai';
    cfg.funcolorlim = [1.6 2.2];  % the voxel in the center of the volume conductor messes up the autoscaling
    ft_sourceplot(cfg, source);

## Beamformer source reconstruction with a two-dipole source model

The following code demonstrates how to do beamformer source reconstruction with a two-dipole source model.

FIMXE insert subsequent code, based on prepare_leadfield, sourceanalysis with method=dics/pcc, and sourcedescriptives.

## Beaming cortico-muscular coherence with a two-dipole source model

FIXME extend with refchan, e.g., repeat dipolesimulation and add the timecourse of a nice signal to an additional channel in the data.
