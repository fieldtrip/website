---
title: Compute forward simulated data with the low-level ft_compute_leadfield
parent: Source reconstruction
grand_parent: Examples
category: example
tags: [eeg, source, headmodel, dipole, simulation]
redirect_from:
    - /example/compute_leadfield/
---

# Compute forward simulated data with the low-level ft_compute_leadfield

Rather than using the high-level **[ft_dipolesimulation](/reference/ft_dipolesimulation)**, this uses the low-level **[ft_compute_leadfield](/reference/forward/ft_compute_leadfield)**. Note that this makes you responsible of more bookkeeping.

    % create a set of electrodes, randomly placed on a sphere
    elec = [];
    elec.pnt = randn(128,3);
    radius = sqrt(sum(elec.pnt.^2,2));
    elec.pnt = elec.pnt ./ [radius radius radius];  % scale them to a unit sphere
    for i=1:128
     elec.label{i} = sprintf('%03d', i);
    end
    elec.elecpos = elec.pnt;

    % create a concentric 3-sphere volume conductor, the radius is the same as for the electrodes
    vol = [];
    vol.r = [0.88 0.92 1.00]; % radii of spheres
    vol.cond = [1 1/80 1];       % conductivity
    vol.o = [0 0 0];          % center of sphere

    % compute the leadfield for a dipole at position [0 0 0.5]
    pos = [0 0 0.5];
    lf = ft_compute_leadfield(pos, elec, vol);

    % compute the potential distribution for a dipole with x-orientation
    mom = [1 0 0]';
    pot = lf * mom;

    % plot the 3-D distribution of the potential over the sphere surface
    elec.tri = convhulln(elec.pnt)
    figure
    patch('faces', elec.tri, 'vertices', elec.pnt, 'FaceVertexCData', pot, 'FaceColor', 'interp')
    axis equal; axis vis3d
