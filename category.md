---
title: Categories
---

## Categories

{% for item in site.data.category %}
- <a href="/category/{{ item[0] }}">{{ item[0] }}</a>
{% endfor %}
