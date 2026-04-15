---
title: Categories
---

<ul>
{% for item in site.data.categories %}
<li><a href="/category/{{ item[0] }}">{{ item[0] }}</a></li>
{% endfor %}
</ul>
