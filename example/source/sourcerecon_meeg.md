---
title: Combined EEG and MEG source reconstruction
category: example
tags: [eeg, meg, headmodel, source]
redirect_from:
    - /example/combined_eeg_and_meg_source_reconstruction/
    - /example/sourcerecon_meeg/
---

## Description

This example script shows how to do combined EEG and MEG source reconstruction. It is sofar only supported by the low-level code in [forwinv](/development/forwinv) and not by the high-level FieldTrip functions such as **[ft_dipolesimulation](/reference/ft_dipolesimulation)**, **[ft_dipolefitting](/reference/ft_dipolefitting)** and **[ft_sourceanalysis](/reference/ft_sourceanalysis)**.

Below is an example that demonstrates how forward computations can be done. Inverse source reconstructions using the low-level code should work similar, i.e. by combining the eeg and meg sensor definitions and volume conduction models into a cell-array.

Note that the same approach can also be used for combined EEG and invasive EEG, or combined MEG and invasive EEG, or any other data fusion. Furthermore note that the combination of volume conduction models can contain more realistically and accurate forward models than those used below.

## MATLAB script

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % create a set of electrodes, randomly placed on the sphere
    elec = [];
    elec.elecpos = randn(32,3);
    dum = sqrt(sum(elec.elecpos.^2,2));                  % compute the distance to the origin
    elec.elecpos = elec.elecpos ./ [dum dum dum] * 0.10; % scale them to a 0.1 meter sphere
    for i=1:32
      elec.label{i} = sprintf('eeg%03d', i);
    end

    % create a concentric 3-sphere volume conductor for the EEG, the radius is the same as for the electrodes
    headmodel_eeg   = [];
    headmodel_eeg.r = [0.088 0.092 0.100]; % radii of spheres
    headmodel_eeg.c = [1 1/80 1];          % conductivity
    headmodel_eeg.o = [0 0 0];             % center of sphere

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % create a set of magnetometers, randomly placed around the sphere
    grad = [];
    grad.coilpos = randn(64,3);
    dum = sqrt(sum(grad.coilpos.^2,2));
    grad.coilpos = grad.coilpos ./ [dum dum dum] * 0.12; % scale them to a 0.12 meter sphere, shifted outward from the head surface
    grad.coilori = grad.coilpos ./ [dum dum dum];        % unit length
    for i=1:64
      grad.label{i} = sprintf('meg%03d', i);
    end
    grad.tra = eye(64,64);

    % create a single-sphere volume conductor for the MEG
    headmodel_meg   = [];
    headmodel_meg.r = 0.1;             % radius of sphere
    headmodel_meg.c = 1;                % conductivity
    headmodel_meg.o = [0 0 0];          % center of sphere

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % combine the EEG and MEG sensor definitions and volume conductor models
    % and do a forward computation
    combined_headmodel = {headmodel_eeg, headmodel_meg};
    combined_sens = {elec, grad};

    pos = [0 0 0.8];
    mom = [1 0 0]';

    [combined_headmodel{1}, combined_sens{1}] = ft_prepare_vol_sens(combined_headmodel{1}, combined_sens{1});
    [combined_headmodel{2}, combined_sens{2}] = ft_prepare_vol_sens(combined_headmodel{2}, combined_sens{2});
    leadfield  = ft_compute_leadfield(pos, combined_sens, combined_headmodel);

    assert(size(leadfield,1)==96);
    assert(size(leadfield,2)==3);

    eeg = leadfield(1:32,:)*mom;
    meg = leadfield(33:end,:)*mom;

    figure; plot(eeg); title('eeg');
    figure; plot(meg); title('meg');

You can plot the EEG and MEG topography in 3D, but note that that the EEG/MEG sensors are randomly distributed on a 10/12 cm sphere. The 3D topography is plotted interpolated on flat triangles that connect the sensors, so that is not exactly following the spherical surface. Especially for the EEG you will see that the electrodes are on the sphere representing the scalp, but that the triangles with the colorcoded topography fall inside the sphere. To fix this, you should interpolate the topography onto a triangulation of the sphere with a much higher resolution.

    figure
    ft_plot_topo3d(elec.elecpos, eeg)
    ft_plot_sens(elec, 'axes', true)
    ft_plot_headmodel(headmodel_eeg, 'facecolor', 'skin', 'facealpha', 0.5)

    figure
    ft_plot_topo3d(grad.coilpos, meg)
    ft_plot_sens(grad, 'axes', true)
    ft_plot_headmodel(headmodel_meg, 'facecolor', 'skin', 'facealpha', 0.5)

You can explore the variables that were created.

    >> whos leadfield eeg meg

      Name            Size            Bytes  Class     Attributes
      eeg            32x1               256  double              
      leadfield      96x3              2304  double              
      meg            64x1               512  double              

    >> ft_senstype(combined_sens)

      ans =
        'electrode'    'meg'

    >> ft_headmodeltype(combined_headmodel)

      ans =
        'concentric'    'singlesphere'
