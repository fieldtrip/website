---
title: How does ft_prepare_neighbours work?
tags: [statistics, cluster]
---

# How does ft_prepare_neighbours work?

There are three methods how **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)** can define the neighbour structure for your data: '**distance**', '**triangulation**' and '**template**'.

Usually, neighbouring sensors can be defined as sensors that are close by. The '**distance**' method simply draws a circle of certain size around each sensor-position. Each other sensor included in this circle is defined to be a neighbouring sensor. The radius of the circle is defined by cfg.neighbourdist. If not given a value, the function will try to be smart and 'guess' a good value. From experience we know, however, that this default is not always a good choice. Choosing 'distance' as the defining property of neighbour might not always be useful. It might introduce superfluous information, thereby reducing sensitivity of your analyses. It will lead to some central sensor having way more neighbours than outer sensors, which, depending on the choice of cfg.neighbourdist, might even be neglected.

The problem of defining neighbouring nodes in a network is known from graph theory. A particular succesful approach to solve this problem is '**triangulation**' - this option can also be used by ft_prepare_neighbours. A triangulation algorithm tries to build triangles between nearby nodes, thereby being independent of distance of sensors. Even in a network with different clusters of nodes, the algorithm tries to build as many triangles until the whole area filled up by the nodes is covered. Although this sounds quite optimal, it of course also has downsides. For our particular purpose of selecting neighbouring sensors, especially the constraint that vertices may not cross constitutes a problem. For example, in a network of four nodes, a triangulation approach will never connect all four sensors equally, because of the disallowance of crossing-vertices. Although we implemented a workaround for this particular problem, there are also other problems. An optimal triangulation algorithm is only known for two-dimensional networks. In order to maintain compatibility with older MATLAB versions, FieldTrip projects any three-dimensional sensor positions to a two-dimensional plane and applies the triangulation on this 2D plane. This can also lead to slightly ill-defined or missing neighbourpairs.
[TODO: a picture may be nice to illustrate the crossing vertices problem]

To circumvent all the above mentioned problems, we introduced a ['**template**'-based approach](/template/neighbours) for neighbourselection in summer 2011. The rationale behind this approach is simply that systems across the world are equal, therefore any neighbourselection once made should be valid for other systems of the same kind. However, selection of neighbours still is highly subjective. All templates in FieldTrip can and will probably updated and optimized, without you as the user realizing this. Please make sure to verify the template-defined neighbourselection by ft_neighbourplot.

For more information how to call and use this, see **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)** and **[ft_neighbourplot](/reference/ft_neighbourplot)**.
