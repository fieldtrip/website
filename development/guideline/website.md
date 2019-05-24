---
title: Website syntax and formatting
tags: [website, syntax, guidelines, development]
---

# Website syntax and formatting

This page describes the syntax and formatting for the Markdown pages that comprise this FieldTrip website. The Markdown pages are converted into html using [Jekyll](https://jekyllrb.com), and includes sections in the [Liquid](https://shopify.github.io/liquid/) makeup language. The resulting html pages and style sheets make use of [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/).

This Markdown [cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is a very good place to start. It is also helpful to check the formatting in an online Markdown editor like <https://stackedit.io> or <https://dillinger.io>.

Since Markdown is limited in its layout options, we use some custom code implemented in Liquid for specific formatting details. A good way to learn the formatting is by looking at the **raw format** of pages on <http://github.com/fieldtrip/website>.

Note that if you look at the raw code of this page, you will also see some [html symbols](https://www.toptal.com/designers/htmlarrows/) in the code: these are required to show the raw code rather that it being rendered.

## Page header

The Markdown document should start with a short header between lined with exactly three minus symbols `---`, including the title and the tags (formatted in a comma-separated) like this

```markdown
---
title: Event related averaging and MEG planar gradient
tags: [tutorial, meg, timelock, preprocessing, plot, meg-language]
---
```

## Tags

Tags that are defined in the page header will automatically appear at the top of the page, where they will link to an overview page with all pages containing the specific tag. Please be restrictive in creating new tags and assigning tags. Tags are meant to search and link **relevant** pages. If you add too many tags, they become less useful.

Workshop tutorials in general should only contain two tags: one for the workshop like `oslo2019`, and one for the dataset that is used like `eeg-audodd`.

## Datasets

Each dataset that is used in the tutorials or examples has an identifier which should be included as a tag. This helps readers to find all documentation that pertains to that dataset. All datasets must also be listed in [this FAQ](faq/what_types_of_datasets_and_their_respective_analyses_are_used_on_fieldtrip).

## Menu

The first and only section with a single `#` corresponds to the page title and is not shown in the page-specific table of content on the right. All subsequent `##` and `###` sections are shown the table of content.

Please ensure that the page title in the header and the first `#` section title are identical.

## Highlighting

This is implemented with small snippets of html code that are contained in the `_includes/markup` directory. Most of them directly correspond to Bootstrap [alerts](https://getbootstrap.com/docs/4.0/components/alerts/#examples). The syntax is like this

{% raw %}
```liquid
{% include markup/info %}
info
{% include markup/end %}
```
{% endraw %}

and it would show up like this

{% include markup/info %}
info
{% include markup/end %}

{% include markup/success %}
success
{% include markup/end %}

{% include markup/warning %}
warning
{% include markup/end %}

{% include markup/danger %}
danger
{% include markup/end %}

{% include markup/exercise %}
exercise
{% include markup/end %}

## Tags

Tags are included at the top of the page.

## See also

## Images

Since images can only be displayed inline in a Markdown document with the size (width and height) determined by the actual bitmap, we are using a piece of Liquid code to insert resizable images. Whereas in Markdown you would to

```markdown
Inline-style:
![alt text](path/to/image.png "Logo Title Text 1")

Reference-style:
![alt text][logo]

[logo]: path/to/image "Logo Title Text 2"
```

where the image is either local or a http link.

For the FieldTrip website you have to do

{% raw %}
```liquid
{% include image src="/assets/img/filename.png" width="300" %}
```
{% endraw %}

Please keep images in `assets/img` with subdirectories according to the place where the image appears.

The preferred format for screenshots is png. The preferred format for photo's is jpg.

## Pdf documents

Pdf documents can be used on the website, but are not managed in github. Since they are binary files and often very large (e.g. slides of presentations), storing them in git would be inefficient. Please send pdf file that you want on the website to Robert.

## Videos

This is implemented with some small snippets of html code contained in the `includes` directory.

You can include a Youtube video like This

{% raw %}
```liquid
{% include youtube id="S8l8Cw7ysis" %}
```
{% endraw %}

and a Vimeo video like this

{% raw %}
```liquid
{% include vimeo id="21604990" %}
```
{% endraw %}
