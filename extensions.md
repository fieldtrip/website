---
title: Extensions
tags: [development]
---

The FieldTrip toolbox is part of a larger, collaborative ecosystem. We encourage researchers and developers to open-source and share their own extensions, plugins, algorithms, graphical user interfaces, and analysis pipelines that extend, build upon, or interface with FieldTrip. To support community-driven development, we collect and list known contributions on this page.

{% include markup/yellow %}
⚠️ Please note that these extensions are maintained by their respective authors. The FieldTrip team does not endorse them or provide support. Contact the respective authors for assistance.
{% include markup/end %}

To have your own extension listed here, please contact the FieldTrip maintainers by email or send a [pull request](https://github.com/fieldtrip/website/tree/master/_data/extensions).

{% assign extensions = site.data.extensions | sort %}
{% for item in extensions %}
<h2>{{ item[1].name }}</h2>
<p>{{ item[1].description }}</p>
<p>This extension was authored by {{ item[1].authors }}.</p>
<p>For more info see <a href="{{ item[1].url }}">here</a >.</p>
{% endfor %}
