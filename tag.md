---
title: Tags
---

<ul>
{% for item in site.data.tags %}
<li><a href="/tag/{{ item[0] }}">{{ item[0] }}</a></li>
{% endfor %}
</ul>
