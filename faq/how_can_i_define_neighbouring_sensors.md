---
title: How can I define neighbouring sensors?
layout: default
tags: [faq, statistics, cluster, plot]
---

## How can I define neighbouring sensors?

Certain functions require knowledge what sensors are near other sensors and should be considered as neighbours. As an example, any cluster-statistic needs to be informed which sensors are allowed to form a cluster. From August 2011 on, you as the user are obliged to define and verify the neighbours manually rather than relying on FieldTrip's internal standard. In the following will be explained what possibilities there are to achieve this.

In FieldTrip, the function **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)** is computing information about what sensors are neighbours of which other sensors. Neighbourhood should be a symmetric property (if A is a neighbour of B, then B is a neighbour of A). You can get neighbours from your data as followin

	  cfg.neighbours = ft_prepare_neighbours(cfg, data);

You can verify the neighbourselection by calling **[ft_neighbourplot](/reference/ft_neighbourplot)**

	  ft_neighbourplot(cfg, data);

or by simply asking for feedback when calling ft_prepare_neighbours

	  cfg.feedback = 'yes';
	  cfg.neighbours = ft_prepare_neighbours(cfg, data);

    
There are three methods how ft_neighbourselection can define the neighbour structure for your data: 'distance', 'triangulation' and 'template'. 

<div class="alert-warning">
We recommend that you check with ft_neighbourplot whether the 'template' method looks suitable for you. 

Note that we do not take responsibility for any wrongly drawn conclusions. The choice how to select neighbours has to be made by you!

Also note that ft_prepare_neighbours will first try to deduce the neighbours from the config (e.g. from the optional cfg.layout field) before it will try searching your data for sensor position information
</div>
