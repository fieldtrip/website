---
title: Website menu
---


{% assign menu = site.data.menu %}
{% if menu %}
<ul>
{% for item in menu %}
{% if item.link %}
<li><a href="{{ item.link }}">{{ item.title }}</a></li>
{% else %}
<li>{{ item.title }}</li>
{% endif %}

{% assign menu = item.menu %}
{% if menu %}
<ul>
{% for item in menu %}
{% if item.link %}
<li><a href="{{ item.link }}">{{ item.title }}</a></li>
{% else %}
<li>{{ item.title }}</li>
{% endif %}

{% assign menu = item.menu %}
{% if menu %}
<ul>
{% for item in menu %}
{% if item.link %}
<li><a href="{{ item.link }}">{{ item.title }}</a></li>
{% else %}
<li>{{ item.title }}</li>
{% endif %}

{% assign menu = item.menu %}
{% if menu %}
<ul>
{% for item in menu %}
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

