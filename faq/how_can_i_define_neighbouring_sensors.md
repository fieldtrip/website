---
title: How can I define neighbouring sensors?
category: faq
tags: [statistics, cluster, plotting]
redirect_from:
  - /faq/how_can_i_define_my_own_neighbourhood_template/
---

# How can I define neighbouring sensors?

Certain functions require knowledge what sensors are near other sensors and should be considered as neighbours. As an example, a classical cluster-based permutation test on event-related fields (in which clustering happens in both the spatial and time domain) needs to be informed which sensors are allowed to form a cluster. From August 2011 on, you as the user are obliged to define and verify the neighbours manually rather than relying on FieldTrip's internal standard. Here we explain what possibilities there are to achieve this.

In FieldTrip, the function **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)** is computing information about what sensors are neighbours of which other sensors. Neighbourhood should be a symmetric property (if A is a neighbour of B, then B is a neighbour of A). You can get neighbours from your data as following

    cfg.neighbours = ft_prepare_neighbours(cfg, data);

You can verify the neighbour selection by calling **[ft_neighbourplot](/reference/ft_neighbourplot)**

    ft_neighbourplot(cfg, data);

or by simply asking for feedback when calling ft_prepare_neighbours

    cfg.feedback = 'yes';
    cfg.neighbours = ft_prepare_neighbours(cfg, data);

There are three methods how ft_prepare_neighbours can define the neighbour structure for your data: 'distance', 'triangulation' and 'template'.

{% include markup/yellow %}
We recommend that you check with ft_neighbourplot whether the 'template' method looks suitable to you.

Note that we do not take responsibility for any wrongly drawn conclusions. The choice how to select neighbours has to be made by you!

Also note that ft_prepare_neighbours will first try to deduce the neighbours from the configuration (e.g., from the optional cfg.layout field) before it will try searching your data for sensor position information.
{% include markup/end %}

You can of course also manually define a neighbourhood struct-array, or manually adjust an existing neighbourhood structure. Currently, each entry of the neighbour-structure array needs to have two fields: 'label' and 'neighblabel', see below. the 'label' is a string that contains the label of the current channel, the neighblabel is a cell array of strings that defines the direct neighbours for that given channel.

    cfg.neighbours = struct;
    cfg.neighbours(1).label = 'Fp1';
    cfg.neighbours(1).neighblabel = {'Fpz'; 'AFz'};
