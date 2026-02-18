---
title: Citations to the FieldTrip reference paper
tags: [literature]
---

_These are open-access papers on [Pubmed](https://pubmed.ncbi.nlm.nih.gov/21253357) that cite FieldTrip, you can find a more complete list incluiding restricted-access papers on [Google Scholar](https://scholar.google.com/scholar?cites=3328911510682538425&scisbd=1)._

{% assign years = "2026,2025,2024,2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011" | split: "," %}
{% for year in years %}

{% assign counter = 0 %}
{% for item in site.data.citedby %}
  {% assign pubyear = item[1].pubdate | split: " " | first %}
  {% if pubyear == year %}
    {% assign counter = counter | plus: 1 %}
  {% endif %}
{% endfor %}

## {{ year }} - {{counter}} papers

<ul>
{% for item in site.data.citedby %}
  {% assign pubyear = item[1].pubdate | split: " " | first %}
  {% if pubyear == year %}
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
  {% endif %}
{% endfor %}
</ul>
{% endfor %}
