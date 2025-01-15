---
title: Tags
---

## Tags

{% for item in site.data.tag %}
- <a href="/tag/{{ item[0] }}">{{ item[0] }}</a>
{% endfor %}
