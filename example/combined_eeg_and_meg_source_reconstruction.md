---
title: Combined EEG and MEG source reconstruction
tags: [example, eeg, meg, headmodel, source]
---

# Combined EEG and MEG source reconstruction

## Description

This example script shows how to do combined EEG and MEG source reconstruction. It is sofar only supported by the low-level code in [forwinv](/development/forwinv) and not by the high-level FieldTrip functions such as **[ft_dipolesimulation](/reference/ft_dipolesimulation)**, **[ft_dipolefitting](/reference/ft_dipolefitting)** and **[ft_sourceanalysis](/reference/ft_sourceanalysis)**.

Below is an example that demonstrates how forward computations can be done. Inverse source reconstructions using the low-level code should work similar, i.e. by combining the eeg and meg sensor definitions and volume conduction models into a cell-array.

Note that the same approach can also be used for combined EEG and invasive EEG, or combined MEG and invasive EEG, or any other data fusion. Furthermore note that the combination of volume conduction models can contain more realistically and accurate forward models than those used below.

## MATLAB script

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % create a set of electrodes, randomly placed on the sphere
    elec = [];
    elec.pnt = randn(32,3);
    dum = sqrt(sum(elec.pnt.^2,2));
    elec.pnt = elec.pnt ./ [dum dum dum];  % scale them to a unit sphere
    for i=1:32
      elec.label{i} = sprintf('eeg%03d', i);
    end

    % create a concentric 3-sphere volume conductor for the EEG, the radius is the same as for the electrodes
    headmodel_eeg   = [];
    headmodel_eeg.r = [0.88 0.92 1.00]; % radii of spheres
    headmodel_eeg.c = [1 1/80 1];       % conductivity
    headmodel_eeg.o = [0 0 0];          % center of sphere

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % create a set of magnetometers, randomly placed around the sphere
    grad = [];
    grad.coilpos = randn(64,3);
    dum = sqrt(sum(grad.coilpos.^2,2));
    grad.coilpos = grad.coilpos ./ [dum dum dum] * 1.2;  % scale them to a unit sphere and shift outward a bit
    grad.coilori = grad.coilpos ./ [dum dum dum];        % unit length
    for i=1:64
      grad.label{i} = sprintf('meg%03d', i);
    end
    grad.tra = eye(64,64);

    % create a single-sphere volume conductor for the MEG
    headmodel_meg   = [];
    headmodel_meg.r = 1.00;             % radius of sphere
    headmodel_meg.c = 1;                % conductivity
    headmodel_meg.o = [0 0 0];          % center of sphere

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % combine the EEG and MEG sensor definitions and volume conductor models
    % and do a forward computation
    combined_headmodel = {headmodel_eeg, headmodel_meg};
    combined_sens = {elec, grad};

    pos = [0 0 0.8];
    mom = [1 0 0]';

    [combined_headmodel{1}, combined_sens{1}] = ft_prepare_headmodel_sens(combined_headmodel{1}, combined_sens{1});
    [combined_headmodel{2}, combined_sens{2}] = ft_prepare_headmodel_sens(combined_headmodel{2}, combined_sens{2});
    leadfield  = ft_compute_leadfield(pos, combined_sens, combined_headmodel) * mom;

    figure; plot(leadfield(1:32)); title('eeg');
    figure; plot(leadfield(33:end)); title('meg');

    whos leadfield

    Name            Size            Bytes  Class     Attributes
    leadfield      96x1               768  double

    >> ft_senstype(combined_sens)

    ans =
      'electrode'    'meg'

    >> ft_headmodeltype(combined_headmodel)

    ans =
      'concentric'    'singlesphere'
