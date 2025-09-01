---
title: How can I visualize the different geometrical objects that are needed for forward and inverse computations?
category: faq
tags: [source, headmodel, inverse, warning]
redirect_from:
    - /faq/how_can_i_visualize_the_different_geometrical_objects_that_are_needed_for_forward_and_inverse_computations/
    - /faq/inspect_geometries/
---

# How can I visualize the different geometrical objects that are needed for forward and inverse computations?

For forward and inverse computations several geometrical objects need to be correctly coregistered. It's good practice to verify this coregistration before proceeding with the next steps of the analysis. The simplest way of verification is obviously visual inspection. FieldTrip allows for the plotting of various geometrical objects by means of the functions in the [plotting module](/development/module/plotting). The following describes how you can use the lower-level plotting functions for the visualization.

{% include markup/red %}
Nice visualization of MEG multisphere volume conductor models is not supported by the low-level plotting functions, but see this [frequently asked question](/faq/plotting/headmodel_localspheres).
{% include markup/end %}

{% include markup/red %}
In general, we advise to use the singleshell as a volume conductor model for MEG, rather than the multisphere model.
{% include markup/end %}

The following code shows how to visualize the gradiometer positions in combination with the subject's headshape and the single sphere volume conductor model. We use the example data [Subject01.zip](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip).

    % read in single sphere volume conductor model
    vol  = ft_read_headmodel('Subject01.hdm');

    % read in the gradiometer description
    hdr  = ft_read_header('Subject01.ds');
    grad = hdr.grad;

    % read in the headshape
    shape = ft_read_headshape('Subject01.shape');
    shape = rmfield(shape, 'fid'); % remove the fiducials -> these are stored in MRI-voxel coords

    % plot
    ft_plot_sens(grad);
    ft_plot_headmodel(vol, 'facecolor', 'none');
    ft_plot_headshape(shape);
