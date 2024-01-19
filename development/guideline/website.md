---
title: Website syntax and formatting
tags: [website, syntax, guidelines, development]
---

# Website syntax and formatting

This page describes the syntax and formatting for the FieldTrip website. The content of the website is maintained on <https://github.com/fieldtrip/website> and we have a complete [tutorial](/development/git) that explains how to contribute. You can also use the GitHub web interface by opening a specific page page and clicking on the pen symbol ("Edit this file") in the upper right corner.

The website pages are written in Markdown format, which are converted into html using [Jekyll](https://jekyllrb.com). The Markdown pages includes sections in the [Liquid](https://shopify.github.io/liquid/) makeup language for more detailed formatting, for which the Shopify [Liquid cheat sheet](http://cheat.markdunkley.com) is a good resource. The resulting static html pages and style sheets also make use of [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/).

This Markdown [cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is a very good place to start. It is also helpful to check the formatting in an online Markdown editor like <https://stackedit.io> or <https://dillinger.io>.

Since Markdown is limited in its layout options, we use some custom code implemented in Liquid for specific formatting details. A good way to learn the formatting is by looking at the **raw format** of pages on <https://github.com/fieldtrip/website>.

## Page header

The Markdown document should start with a short header between two lines with three minus characters (not more and not less), including the title and the tags (formatted in a comma-separated) like this

```markdown
---
title: Website syntax and formatting
tags: [website, syntax, guidelines, development]
---
```

## Tags

Tags that are defined in the page header will automatically appear at the top of the page, where they will link to an overview page with all pages containing the specific tag. Please be restrictive in creating new tags and assigning tags. Tags are meant to search and link **relevant** pages. If you add too many tags, they become less useful.

Workshop tutorials in general should only contain two tags: one for the workshop like `oslo2019`, and one for the dataset that is used like `eeg-audodd`.

## Datasets

Each dataset that is used in the tutorials or examples has an identifier which should be included as a tag. This helps readers to find all documentation that pertains to that dataset. All datasets must also be listed in [this FAQ](/faq/datasets).

## Menu

The first and only section with a single `#` corresponds to the page title and is not shown in the page-specific table of content on the right. All subsequent `##` and `###` sections are shown the table of content.

Please ensure that the page title in the header and the first `#` section title are identical.

## Text block highlighting

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

## Code syntax highlighting

You can indent a single word in a sentence using three back-tics at the start and end. You can highlight a block with multiple lines by indenting the whole block with 4 spaces. You can also highlight a multi-line block by starting with three back-tics.

````plaintext
```
This would be formatted as MATLAB code.
```
````

The default syntax highlighter is for MATLAB. You can use other highlighting options as explained [here](https://frankindev.com/2017/03/18/syntax-highlight-with-rouge-in-jekyll/).

````plaintext
```python
This would be formatted as Python code.
```
````

````plaintext
```bash
This would be formatteded as Bash command-line code.
```
````

and

````plaintext
```plaintext
This is formatted with a fixed-width font, but without color highlighting.
```
````

The last option is useful for MATLAB command window output, which in itself is not executable code, and for displaying sections of MATLAB help.

## Tags

Tags are displayed at the top of the page. If you click on a tag, you are brought to an overview page with all pages that share the same tag. Those overview pages are automatically build on the web server after every change.

## Redirection

If you rename a page, the URL (i.e. the link on the web) that points to it will not be valid any more. That is problematic if that link is for example used in other documentation, on other websites, or in the email archive. To prevent broken links, you can redirect from the old page to the new page; this requires that you including `redirect_from` in the page header of the new page. You can also use it to redirect links to multiple old pages to a new single page in which the documentation has been merged.

```plaintext
---
title: New page title
redirect_from:
  - /olddir/oldname/
---
```

## See also

You can include an automatically generated list of pages with specific tags like this

{% raw %}

```liquid
{% include seealso tag1="guidelines" %}
```

{% endraw %}

which results in the following list

{% include seealso tag1="guidelines" %}

Tags are indicated with `tag`, `tag1`, `tag2` etcetera, and multiple tags are logically combined with **and**, not with **or**.

## Line breaks

If you have a short piece of text, such as an address, that you want to appear over multiple lines _without_ converting it into a list, you can add two spaces to the end of each line. This will cause explicit line breaks to be inserted.

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

Pdf documents can be used on the FieldTrip website, but are not managed in git on GitHub. Since they are binary files and often very large (e.g., slides of presentations), storing them in git would be inefficient. Please send pdf file that you want on the website to Robert, he will copy it to .

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

## News items

To show a news item on the front page, you have to add the news item as a Markdown page to `_posts` with the name `YYYY-MM-DD-short-description.md`. See the other examples in that directory. Posts that have the category `news` are shown on the front page, for older posts you should remove the `news` category.
