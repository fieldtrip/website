---
title: Welcome to the FieldTrip website
---

# Welcome to the FieldTrip website

FieldTrip is the MATLAB software toolbox for MEG, EEG and iEEG analysis, which is released free of charge as [open source software](http://en.wikipedia.org/wiki/Open_source) under the GNU [general public license](http://www.gnu.org/copyleft/gpl.html). FieldTrip is developed by members and collaborators of the [Donders Institute for Brain, Cognition and Behaviour](https://www.ru.nl/donders/) at [Radboud University](https://www.ru.nl), Nijmegen, the Netherlands.

{% include markup/warning %}
Please cite the FieldTrip reference paper when you have used FieldTrip in your study.

Robert Oostenveld, Pascal Fries, Eric Maris, and Jan-Mathijs Schoffelen. **[FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data.](https://doi.org/10.1155/2011/156869)** Computational Intelligence and Neuroscience, vol. 2011, Article ID 156869, 9 pages, 2011. doi:10.1155/2011/156869.
{% include markup/end %}

To get started, head over to the [getting started](/getting_started) documentation and the [tutorials](/tutorial).

<section id="sec-news" markdown="1">

## Latest release

_The latest code developments can be tracked in detail on [GitHub](/development/git)._

{% assign counter = 0%}
{% for post in site.posts %}
{% if post.categories contains 'release' %}

{% if counter == 0 %}
{% assign counter = counter | plus: 1 %}
<div class="post-excerpt" markdown="1">
{{ post.excerpt }}
</div>
{% endif %}

{% endif %}
{% endfor %}

</section>

<section id="sec-news" markdown="1">

## News and announcements

_You can also follow us on [Twitter](http://twitter.com/fieldtriptoolbx)._

{% assign counter = 0%}
{% for post in site.posts %}
{% if post.categories contains 'news' %}

{% if counter < 7 %}
{% assign counter = counter | plus: 1 %}
<div class="post-excerpt" markdown="1">
{{ post.excerpt }}
</div>
{% endif %}

{% endif %}
{% endfor %}

</section>
