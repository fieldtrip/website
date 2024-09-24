---
title: How can I visualize a localspheres volume conductor model?
category: faq
tags: [headmodel, localspheres]
---

# How can I visualize a localspheres volume conductor model?

Typically, one would use **[ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)** for the visualization of a headmodel. This function will not allow you right away to visualize a localspheres headmodel in a meaningful way. The reason for this is that a meaningful interpretation of the localspheres headmodel is only possible in combination with a specification of the sensor-array that was used to construct the headmodel. Namely, in the specification of the headmodel, for each of the sensors a sphere has been specified that best describes the local surface of the boundary closest to that sensor. ft_plot_headmodel does not know anything about the sensors, and will not be able to plot an interpretable figure. The following snippet of code can be used to visualize the surface that is described by the localspheres headmodel. For this code to work it is assumed that you have the headmodel and corresponding sensor description (here named grad) in MATLAB working memory.

    [a,b] = match_str(headmodel.label, grad.label);

    % get the corresponding elements from both data structures
    R     = headmodel.r(a);
    O     = headmodel.o(a,:);
    chanpos = grad.chanpos(b,:);

    vec = chanpos-O;
    for k = 1:size(vec,1)
    vec(k,:) = vec(k,:)./norm(vec(k,:));
    end
    headshape.pnt = O+diag(R)*vec;

    cfg = [];
    cfg.method = 'headshape';
    cfg.headshape = headshape;
    bnd = ft_prepare_mesh(cfg);

    figure;hold on;
    ft_plot_sens(grad);
    ft_plot_mesh(bnd, 'facecolor', 'w');
