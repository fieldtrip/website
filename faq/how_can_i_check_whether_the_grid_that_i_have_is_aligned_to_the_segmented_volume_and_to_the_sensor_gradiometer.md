---
title: How can I check whether the grid that I have is aligned to the segmented volume and to the sensor gradiometer?
category: faq
tags: [source, headmodel, seg]
---

# How can I check whether the grid that I have is aligned to the segmented volume and to the sensor gradiometer?

Having a source model (i.e., positions of the dipoles), a head model (i.e., volume conduction model of the head), and the 'grad' structure, (i.e., information of the gradiometers) you can use the following:

    hold on
    plot3(sourcemodel.pos(:,1), sourcemodel.pos(:,2), sourcemodel.pos(:,3),'.');
    ft_plot_headmodel(headmodel);
    ft_plot_sens(grad);
