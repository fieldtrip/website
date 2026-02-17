---
title: Citations to the FieldTrip reference paper
tags: [literature]
---

_These are open-access papers on [Pubmed](https://pubmed.ncbi.nlm.nih.gov/21253357) that cite FieldTrip, you can find a more complete list on [Google Scholar](https://scholar.google.com/scholar?cites=3328911510682538425&scisbd=1)._

{% assign years = "2011, 2012, 2013" | split: "," %}
{% for year in years %}
{{ year }}
{% endfor %}

<ul>

{% for item in site.data.citedby %}
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

  <li>
  {% if issue.size == 0 %}
    {{ authors }}. <a href="https://doi.org/{{ doi }}">{{ title }}</a> <em>{{ fulljournalname }} {{ pubdate }}; {{volume}}:{{ pages }}.</em> {% include badge doi=doi pmid=pmid %}
  {% else %}
    {{ authors }}. <a href="https://doi.org/{{ doi }}">{{ title }}</a> <em>{{ fulljournalname }} {{ pubdate }}; {{volume}}({{ issue }}):{{ pages }}.</em> {% include badge doi=doi pmid=pmid %}
  {% endif %}
  </li>
{% endfor %}
</ul>
