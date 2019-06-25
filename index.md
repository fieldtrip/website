---
title: Welcome to the FieldTrip website
---

# Welcome to the FieldTrip website

FieldTrip is the MATLAB software toolbox for MEG, EEG, iEEG and NIRS analysis. It offers preprocessing and advanced analysis methods, such as time-frequency analysis, source reconstruction using dipoles, distributed sources and beamformers and non-parametric statistical testing. It supports the [data formats](/faq/dataformat) of all major MEG systems and of the most popular EEG, iEEG and NIRS systems. New data formats can be [added easily](/faq/how_can_i_import_my_own_dataformat). FieldTrip contains high-level functions that you can use to construct your own analysis protocols as a MATLAB script.

The FieldTrip software is released free of charge as [open source software](http://en.wikipedia.org/wiki/Open_source) under the GNU [general public license](http://www.gnu.org/copyleft/gpl.html).

{% include markup/warning %}
Please cite the FieldTrip reference paper when you have used FieldTrip in your study.

Robert Oostenveld, Pascal Fries, Eric Maris, and Jan-Mathijs Schoffelen. **[FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data.](http://www.hindawi.com/journals/cin/2011/156869)** Computational Intelligence and Neuroscience, vol. 2011, Article ID 156869, 9 pages, 2011. doi:10.1155/2011/156869.
{% include markup/end %}

To get started with FieldTrip, please continue reading the [getting started](/getting_started) documentation.

{% include facebook %}

## News and announcements

{% for post in site.posts %}
{% if post.categories contains 'news' %}
{{ post.excerpt }}
{% endif %}
{% endfor %}

## Recent improvements to the code

All changes to the code can be tracked on [Twitter](http://twitter.com/fieldtriptoolbx) and [GitHub](/development/git).
