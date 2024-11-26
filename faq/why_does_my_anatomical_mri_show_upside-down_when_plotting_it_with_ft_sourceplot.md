---
title: Why does my anatomical MRI show upside-down when plotting it with ft_sourceplot?
category: faq
tags: [anatomical, mri]
---

# Why does my anatomical MRI show upside-down when plotting it with ft_sourceplot?

When visualizing anatomical MRIs and source reconstructed data with **[ft_sourceplot](/reference/ft_sourceplot)**, it may happen that the image is plotted upside-down. This has to do with the way in which anatomical volumes are plotted in FieldTrip. For more information, see the frequently asked question [What is the plotting convention for anatomical MRIs?](/faq/what_is_the_plotting_convention_for_anatomical_mris).

{% include image src="/assets/img/faq/why_does_my_anatomical_mri_show_upside-down_when_plotting_it_with_ft_sourceplot/upside_down_sourceplot.png" width="400" %}

In itself this is **not a problem**, as explained [here](/faq/my_mri_is_upside_down_is_this_a_problem).

If for aesthetic reasons you do want the figure to be plotted upside-up, you can use the **[ft_volumereslice](/reference/ft_volumereslice)** function to reslice the MRI, i.e. to interpolate the anatomy onto a new 3D grid that is aligned with the axes of the coordinate system. If you use the resliced MRI as input to **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)**, the source reconstructed result will also show up as expected.

{% include image src="/assets/img/faq/why_does_my_anatomical_mri_show_upside-down_when_plotting_it_with_ft_sourceplot/correct_sourceplot.png" width="400" %}
