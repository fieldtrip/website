---
title: How can I use the databrowser?
category: faq
tags: [databrowser, plotting, artifact]
---

# How can I use the databrowser?

The databrowser can be used to look at your raw or preprocessed data and annotate time periods at which specific events happen. Originally designed to identify sleep spindles, it's current main purpose is manual artifact detection. You can call the databrowser in an interactive mode by storing the output in a cfg like this:

    cfg = ft_databrowser(cfg, data);

Note that the second argument, data, is optional. You can also read in data from your harddrive instead, see **[ft_databrowser](/reference/ft_databrowser)**. Note that you need to specify whether your data is continuous or not by setting cfg.continuous to 'yes' or 'no'. If your data is trial based, then continuous is 'no', if you have one long continuous recordings without breaks, you can set continuous to 'yes'.

{% include markup/yellow %}
If you call the databrowser without an output argument like this:

    ft_databrowser(cfg, data)

then whatever you do, it will **not** be saved! Be sure to specify an output argument if you want it to be saved!
{% include markup/end %}

The databrowser supports three viewmodes: butterfly, vertical or component. In 'butterfly' viewmode, all signal traces will be plotted on top of each other, in 'vertical' viewmode, the traces will be below each other. The 'component' viewmode is made specifically if you provide data decomposed into individual components, see **[ft_componentanalysis](/reference/ft_componentanalysis)**. The data will be plotted as in vertical viewmode, but including a topographic map of the component to the left of the time trace. As an alternative to these three viewmodes, if you provide a cfg.layout, then the function will try to plot your data according to the sensor positions specified in the layout.

When the databrowser opens, you will see buttons to navigate at the bottom and artifact annotation buttons on the right. Note that also artifacts that were marked in automatic artifact detection methods will be displayed here, see the [automatic artifact rejection tutorial](/tutorial/automatic_artifact_rejection). You can click on one of the artifact types, select the start and the end of the artifact and then double click into the selected area to mark this artifact. To remove such an artifact, simply repeat the same procedure.

{% include markup/yellow %}
The databrowser will **not** change your data in any way, it will just store your selected or de-selected artifacts in your cfg.
{% include markup/end %}
