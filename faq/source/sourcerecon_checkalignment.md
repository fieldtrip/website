---
title: How can I check whether the grid that I have is aligned to the segmented volume and to the sensor gradiometer?
tags: [source, headmodel, seg]
category: faq
redirect_from:
    - /faq/how_can_i_check_whether_the_grid_that_i_have_is_aligned_to_the_segmented_volume_and_to_the_sensor_gradiometer/
    - /faq/sourcerecon_checkalignment/
---

Having a source model (i.e., positions of the dipoles), a head model (i.e., volume conduction model of the head), and the 'grad' structure, (i.e., information of the gradiometers) you can use the following:

    hold on
    ft_plot_mesh(sourcemodel);
    ft_plot_headmodel(headmodel);
    ft_plot_sens(grad);
