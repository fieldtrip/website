---
title: How can I check whether the grid that I have is aligned to the segmented volume and to the sensor gradiometer?
tags: [faq, source, headmodel, seg]
---

# How can I check whether the grid that I have is aligned to the segmented volume and to the sensor gradiometer?

Having 'grid' (i.e., source model), 'vol' (i.e., volume conduction model, or head model), and 'grad' (i.e., information of the gradiometer, or 'elec' for EEG/IEEG systems) you can use the following:

    Hold on
    plot3(grid.pos(:,1),grid.pos(:,2),grid.pos(:,3),'.');
    ft_plot_headmodel(vol);
    ft_plot_sens(grad);
