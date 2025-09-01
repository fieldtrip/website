---
title: Neighbour templates
---

{% include /shared/development/warning.md %}


This project has been completed and it's result can be found here:

- <http://fieldtrip.fieldtriptoolbox.org/faq/how_can_i_define_neighbouring_sensors>
- <http://fieldtrip.fieldtriptoolbox.org/faq/how_does_ft_prepare_neighbours_work>
- <http://fieldtrip.fieldtriptoolbox.org/faq/how_can_i_define_my_own_neighbourhood_template>

Related bugzilla bugs:

- <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=800>
- <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=983>
- <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=984>
- <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=1929>

Find below the old project notes

#### Goals

1. Provide functionality for supporting neighbour templates [check]
2. Provide information how to create own neighbour templates and check using ft_neighbourplot [check]
3. Update the community on this functionality
4. Make user obliged to call neighbourselection
5. Update community about this functionality change
6. Make a FAQ: How can I select neighbouring sensors? This can incorporate information from (2) [check]

#### How can I define neighbouring sensors?

Certain functions require knowledge what sensors are near other sensors and should be considered as neighbours. As an example, any cluster-statistic needs to be informed which sensors are allowed to form a cluster. From August 2011 on, you as the user are obliged to define and verify the neighbours manually rather than relying on FieldTrip's internal standard. In the following will be explained what possibilities there are to achieve this.

In FieldTrip, the function ft_neighbourselection is computing information about what sensors are neighbours of which other sensors. Neighbourhood should be a symmetric property (if A is a neighbour of B, then B is a neighbour of A). You can get neighbours from your data as follows:

    cfg.neighbours = ft_neighbourselection(cfg, data);

You can verify the neighbourselection by calling ft_neighbourplot

    ft_neighbourplot(cfg, data);

or by simply asking for feedback when calling ft_neighbourselection

    cfg.feedback = 'yes';
    cfg.neighbours = ft_neighbourselection(cfg, data);

There are three methods how ft_neighbourselection can define the neighbour structure for your data: 'distance', 'triangulation' and 'template'. We recommend check whether the 'template' method looks suitable for you using ft_neighbourplot. However, note that we do not take responsibility for any wrongly drawn conclusions. The choice how to select neighbours has to be made by you!
**Also note that ft_neighbourselection will first try to deduce the neighbours from the configuration(e.g., from the optional cfg.layout field) before it will try searching your data for sensor position information.**

#### In depth information: How to ft_neighbourselection work?

There are three methods how ft_neighbourselection can define the neighbour structure for your data: 'distance', 'triangulation' and 'template'.

Usually, neighbouring sensors can be defined as sensors that are close by. The 'distance' method simply draws a circle of certain size around each sensor-position. Each other sensor included in this circle is defined to be a neighbouring sensor. The radius of the circle is defined by cfg.neighbourdist. If not given a value, the function will try to be smart and 'guess' a good value. From experience is know, however, that this default is not always a good choice. Choosing 'distance' as the defining property of neighbour might not always be useful. It might introduce superfluous information, thereby reducing sensitivity of your analyses. It will lead to some central sensor having way more neighbours than outer sensors, which, depending on the choice of cfg.neighbourdist, might even be neglected.

The problem of defining neighbouring nodes in a network is known from graph theory. A particular successful approach to solve this problem is 'triangulation' - this option can also be used by ft_neighbourselection. A triangulation algorithm tries to build triangles between nearby nodes, thereby being independent of distance of sensors. Even in a network with different clusters of nodes, the algorithm tries to build as many triangles until the whole area filled up by the nodes is covered. Although this sounds quite optimal, it of course also has downsides. For our particular purpose of selecting neighbouring sensors, especially the constraint that vertices may not cross constitutes a problem. For example, in a network of four nodes, a triangulation approach will never connect all four sensors equally, because of the disallowance of crossing-vertices. Although there are workarounds for this particular problem, there are other problems. An optimal triangulation algorithm is only known for two-dimensional networks. In order to keep maximal compatibility with older MATLAB versions, FieldTrip projects any three-dimensional sensor positions to a two-dimensional plane and applies the triangulation on this 2D plane. This can also lead to slightly ill-defined or missing neighbourpairs.
[TODO: a picture may be nice to illustrate the crossing vertices problem]

To circumvent all the above mentioned problems, we introduced a 'template'-based approach for neighbourselection in summer 2011. The rationale behind this approach is simply that systems across the world are equal, therefore any neighbourselection once made should be valid for other systems of the same kind. However, selection of neighbours still is highly subjective. All templates in FieldTrip can and will probably updated and optimized, without you as the user realizing this. Please make sure to verify the template-defined neighbourselection by ft_neighbourplot.

For more information how to call and use this ft_neighbourselection, please see the function reference [TODO: add].

#### Creating templates or updating an already existing template

Currently, each entry of the neighbour-structure needs to have two fields: 'label' and 'neighblabel'. cfg.neighbours must be a cell-array, with each entry having these two fields. You can then define the structure as follows:

    cfg.neighbours = {};
    cfg.neighbours{1}.label = 'Fp1';
    cfg.neighbours{1}.neighblabel = {'Fpz'; 'AFz'};

Similarly, you can load a template and then change the neighbour definition. Note, although repeating this over and over again: verify your choice using ft_neighbourplot.

If you feel that a template is representing a suboptimal neighbour definition, feel free to contact Jörn Horschig jm.horschig@donders.ru.nl - he is administrating the FieldTrip template directory. Please let him know what data you use and optimally send him the figures from ft_neighbourplot with the old and with the updated template.
