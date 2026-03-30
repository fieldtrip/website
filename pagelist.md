---
title: Pagelist
---

{% assign pagelist = site.data.pagelist %}
{% if pagelist %}
<ul>
{% for item in pagelist %}
{% if item.link %}
<li><a href="{{ item.link }}">{{ item.title }}</a></li>
{% else %}
<li>{{ item.title }}</li>
{% endif %}

{% assign pagelist = item.pagelist %}
{% if pagelist %}
<ul>
{% for item in pagelist %}
{% if item.link %}
<li><a href="{{ item.link }}">{{ item.title }}</a></li>
{% else %}
<li>{{ item.title }}</li>
{% endif %}

{% assign pagelist = item.pagelist %}
{% if pagelist %}
<ul>
{% for item in pagelist %}
{% if item.link %}
<li><a href="{{ item.link }}">{{ item.title }}</a></li>
{% else %}
<li>{{ item.title }}</li>
{% endif %}

{% assign pagelist = item.pagelist %}
{% if pagelist %}
<ul>
{% for item in pagelist %}
{% if item.link %}
<li><a href="{{ item.link }}">{{ item.title }}</a></li>
{% else %}
<li>{{ item.title }}</li>
{% endif %}

{% endfor %}
</ul>
{% endif %}
{% endfor %}
</ul>
{% endif %}
{% endfor %}
</ul>
{% endif %}
{% endfor %}
</ul>
{% endif %}

