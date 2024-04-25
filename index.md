---
title: Welcome to the FieldTrip website
redirect_from:
  - /start/
---

# Welcome to the FieldTrip website

FieldTrip is the MATLAB software toolbox for MEG, EEG and iEEG analysis, which is released free of charge as [open source software](https://en.wikipedia.org/wiki/Open_source) under the GNU [general public license](https://www.gnu.org/copyleft/gpl.html). FieldTrip is developed by members and collaborators of the [Donders Institute for Brain, Cognition and Behaviour](https://www.ru.nl/donders/) at [Radboud University](https://www.ru.nl), Nijmegen, the Netherlands.

{% include markup/yellow %}
Please cite the reference paper when you have used FieldTrip in your study.

Robert Oostenveld, Pascal Fries, Eric Maris, and Jan-Mathijs Schoffelen. **[FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data.](https://doi.org/10.1155/2011/156869)** _Computational Intelligence and Neuroscience, 2011; 2011:156869._

{% include badge doi="10.1155/2011/156869" pmid="21253357" pmcid="PMC3021840" %}
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

## Recent citations

_These are recent citations on [Pubmed](https://pubmed.ncbi.nlm.nih.gov/21253357), you can find a more complete list on [Google Scholar](https://scholar.google.com/scholar?cites=3328911510682538425&scisbd=1)._


{% assign sortlist = "" %}
{% for item in site.data.citedby %}
{% assign this = item[1].sortdate | replace: "/" | replace: ":" | replace: " " | append: "-" | append: forloop.index0 %}
{% assign sortlist = sortlist | append: " " | append: this %}
{% endfor %}
{% assign sortlist = sortlist | split: " " | sort | reverse | slice: 0,5 %}

{% assign sortindex = "" %}
{% for item in sortlist %}
{% assign this = item | split: "-" %}
{% assign sortindex = sortindex | append: " " | append: this[1] %}
{% endfor %}
{% assign sortindex = sortindex | split: " " %}

<div class="post-excerpt" markdown="1">

{% for index in sortindex %}
  {% for item in site.data.citedby %}
    {% assign numericindex = index | times: 1 %}
    {% if numericindex == forloop.index0 %}
      {% assign title = item[1].title %}
      {% assign authors = item[1].authors | map: "name"  | join: ", " %}
      {% assign pubdate = item[1].pubdate %}
      {% assign fulljournalname = item[1].fulljournalname %}
      {% assign volume = item[1].volume %}
      {% assign issue = item[1].issue %}
      {% assign pages = item[1].pages %}

      {% assign doi = item[1].articleids | where: "idtype", "doi" %}
      {% assign doi = doi[0].value %}

      {% assign pmid = item[1].articleids | where: "idtype", "pmid" %}
      {% assign pmid = pmid[0].value %}

      {% assign pmcid = item[1].articleids | where: "idtype", "pmcid" %}
      {% assign pmcid = pmcid[0].value %}
  
<h3>{{ title }}</h3>

{%- if issue.size == 0 -%}
{{ authors }} <em>{{ fulljournalname }}, {{ pubdate }}; {{ volume }}:{{ pages }}.</em>
{%- else -%}
{{ authors }} <em>{{ fulljournalname }}, {{ pubdate }}; {{ volume }}({{ issue }}):{{ pages }}.</em>
{%- endif -%}
{% include badge doi=doi %}

    {% endif %}
  {% endfor %}
{% endfor %}

</div>

<section id="sec-news" markdown="1">

## News and announcements

_You can also follow us on [Mastodon](https://fosstodon.org/@fieldtriptoolbox)._

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
