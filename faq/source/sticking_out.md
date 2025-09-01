---
title: Is it OK for vertices/dipoles to stick out of the volume conductor?
category: faq
tags: [sourcemodel, bem]
redirect_from:
    - /faq/sticking_out/
---

# Is it OK for vertices/dipoles to stick out of the volume conductor?

It is relatively common to use a triangulated cortical sheet - e.g., from FreeSurfer - as the basis for a source model. In that case dipoles are placed on all vertices of the cortical sheet. Sometimes the orientation of the triangles is also used to determine the orientation of the neighboring vertices/dipoles.

Dipoles sticking out of the inner surface of the volume conductor can indeed be a problem. The inner surface the describes the interface between brain and skull tissues, and defines the compartment in which all sources have to be.

## In the case of EEG

For the singlesphere, concentricspheres, BEM and FEM models available for EEG it is crucial that the dipoles are in the actual source compartment, i.e. in the brain. That means that in the model they should **not** stick out of the innermost surface.

Furthermore, to ensure that BEM (which interpolates potential over the triangles) does not get too inaccurate, the dipoles also need to be sufficiently far away from the surface triangles. Each dipole should be at least at a distance from the surface that is on the order of FIXME times the triangle edge length. This applies both to EEG-BEM and MEG-BEM.

## In the case of MEG

When using a BEM volume conductor with MEG, you should ensure that your dipoles are well inside the brain compartment.

For the singleshell, singlesphere or localspheres models for MEG it is not a problem to have dipoles outside the innermost surface. For these, the actual location of the skull surface does not influence the MEG field distribution, i.e. a dipole at [0 0 70] mm in a spherical volume conductor will have the same field distribution for a sphere with a radius of 80 mm, or 120 mm, or 50 mm, since only the radial symmetry is relevant

## Solution

If you are working with regularly spaced 3D grids as source model, you don't have to do anything. FieldTrip will check for every source whether it is inside or outside the innermost compartment of the volume conductor, and all sources outside will be flagged and not used in the source reconstruction. FieldTrip will actually do the same check for source models based on a triangulated cortical sheets. You can use the `cfg.inwardshift` option to ensure that sources that are on the inside - but too close to the surface for BEM - are also flagged as outside.

If you do not want to flag any of your dipoles as outside and exclude them from the source estimation, you have to modify your source model. First of all, you should ensure that your cortical sheet is properly aligned with your volume conduction model of the head. The `cfg.moveinward` option in **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)** takes all dipoles that are outside, and projects then on an inward-shifted surface of the inside-skull. I.e. it deforms the cortical sheet by pushing some vertices inward. This should work both for spherical models (i.e. concentric spheres) and BEM models. In the case of spherical models, it will result in a cortical mesh that is squeezed in to a sphere shape.

{% include markup/skyblue %}
Since for MEG singleshell, singlesphere and localspheres models it does not matter that they stick out, we often specify a negative value for `cfg.inwardshift`. This causes dipoles that are just outside the brain still to be flagged as inside. This results in nicer interpolations and deals with the issue that is discussed in [this faq](/faq/source/sourcerecon_rim).
{% include markup/end %}
