---
title: Categories
nav_exclude: true
---

## Categories

<ul>
{% for item in site.data.category %}
<li><a href="/category/{{ item[0] }}">{{ item[0] }}</a></li>
{% endfor %}
</ul>