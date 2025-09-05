---
title: Website syntax and formatting
tags: [website, syntax, guidelines, development]
---

This page describes the syntax and formatting for the FieldTrip website. The content of the website is maintained on <https://github.com/fieldtrip/website> and we have a complete [tutorial](/development/git) that explains how to contribute. You can also use the GitHub web interface by opening a specific page page and clicking on the pen symbol ("Edit this file") in the upper right corner.

The website pages are written in Markdown format, which are converted into html using [Jekyll](https://jekyllrb.com). The resulting html pages and css style sheets make use of [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/).

This Markdown [cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is a good place to start. It is also helpful to check the formatting in an online Markdown editor like <https://stackedit.io> or <https://dillinger.io>.

For more complex content and formatting, the Markdown pages includes sections in the [Liquid](https://shopify.github.io/liquid/) makeup language. The Shopify [Liquid cheat sheet](http://cheat.markdunkley.com) is a good resource and the online editor <https://liquidjs.com/playground.htm> helps to develop and test code.

## Frontmatter

The Markdown document should start with some so-called frontmatter, i.e., a short header between two lines with three minus characters each (not more and not less), including the title, tags, etc.

```markdown
---
title: Website syntax and formatting
tags: [website, syntax, guidelines, development]
category:
tags: []
weight:
---
```

## Title and headings

The page title as defined in the frontmatter is automatically used as the top-level (H1) heading. The Markdown document should therefore not start with a header using `# ...`.

Each page should only have a single top-level H1 heading, and since that is automatically added, you should not use H1 level headers with `# ...` on any page yourself. You can and should use subsequent heading levels (`## ...`, `### ...`), which will appear in the table of contents in the right column.

You should not use sub-headings if the corresponding higher level heading is not also present, i.e., it is fine to use headings at the levels H3, H2 and H1 (which is automatically added with the page title), but not H4 and H2, skipping H3 in between.

### Table of content

The first (and only) H1 level header with a single `#` is automatically added based on the title in the frontmatter and is _not_ shown in the table of content on the right. All subsequent headers _are_ shown in the table of content on the right.

## Tags

Tags that are defined in the frontmatter will automatically appear at the top of the page, where they will link to an overview page with all pages containing the specific tag. Tags should be formatted as a list, even if there is one. Please be restrictive in creating new tags and assigning tags. Tags are meant to search and link **relevant** pages. If you add too many tags, they become less useful.

Tags for a page are displayed in the right column under the table of content. If you click on a tag, you are brought to an overview page with all pages that share the same tag. Those tag overview pages are automatically built on the web server after every change. The tag can be used together with the category to make a "See also" list (see below).

Posts and news items should not have any tags. Workshop tutorials in general should only contain two tags: one for the workshop identifier like `oslo2019`, and one for the dataset that is used like `eeg-audodd`.

### Datasets

Each dataset that is used in the tutorials or examples has an identifier which should be included as a tag. This helps readers to find all documentation that pertains to that dataset. All datasets must also be listed in [this FAQ](/faq/other/datasets).

## Category

You should specify the category under which the page falls in the frontmatter. This should be a single word, not a list. The following categories are currently in use: `tutorial`, `example`, `faq`, `getting_started`.

The category can be used together with the tags to make a "See also" list (see below).

## See also

You can include an automatically generated list of pages with specific tags and/or a specific category like this

{% raw %}

```liquid
{% include seealso category="example" tag="plotting" %}
```

{% endraw %}

which results in the following list

{% include seealso category="example" tag="plotting" %}

The page category can be indicated using a single word. Tags are indicated with `tag`, or when multiple are specified with `tag1`, `tag2`, etcetera. Multiple tags are logically combined with **and**, not with **or**.

## Weights

In the frontmatter you can specify a weigth between 10 and 99 (i.e., it should consist of two digits) that is used to determine how pages are sorted in lists. Low weights appear at the top, high weights at the bottom. If a page does not have a weight, it will go all the way to the bottom. Pages that have the same weight will be sorted alphabetically.

## Redirection

If you rename a page, the URL (i.e. the link on the web) that points to it will not be valid any more. That is problematic if that link is for example used in other documentation, on other websites, or in the email archive. To prevent broken links, you can redirect from the old page to the new page; this requires that you including `redirect_from` in the frontmatter of the new page. You can also use it to redirect links to multiple old pages to a new single page in which the documentation has been merged.

```plaintext
---
title: New page title
redirect_from:
  - /olddir/oldname/
---
```

## Text block highlighting

This is implemented with small snippets of html code that are contained in the `_includes/markup` directory. They correspond to Bootstrap [alerts](https://getbootstrap.com/docs/4.0/components/alerts/#examples). The syntax is like this

{% raw %}

```liquid
{% include markup/yellow %}
yellow
{% include markup/end %}
```

{% endraw %}

and it would show up like this

{% include markup/blue %}
blue
{% include markup/end %}

{% include markup/gray %}
gray
{% include markup/end %}

{% include markup/green %}
green
{% include markup/end %}

{% include markup/red %}
red
{% include markup/end %}

{% include markup/yellow %}
yellow
{% include markup/end %}

{% include markup/skyblue %}
skyblue
{% include markup/end %}

{% include markup/white %}
white
{% include markup/end %}

{% include markup/darkgray %}
darkgray
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

## Line breaks

If you have a short piece of text, such as an address, that you want to appear over multiple lines _without_ converting it into a list, you can add two spaces to the end of the line. This will cause explicit line breaks to be inserted.

## Images

Since bitmap images can only be displayed inline in a Markdown document with the size (width and height) determined by the actual bitmap images, we are using a piece of Liquid code to insert resizable images. Whereas in Markdown you would to

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

Please keep images in `assets/img` with subdirectories according to the place where the image appears. The preferred filename is `figureXX.png`, with XX being the sequential number of the image appearing on the page. The preferred format for screenshots is png. The preferred format for photos is jpg. Do not cross-link to figures from another tutorial or example, but copy that figure over (otherwise changes to the original page with the figure might break the page that cross-links to the figure).

## Pdf documents

Pdf documents can be used on the FieldTrip website, but are not managed in git on GitHub. Since they are binary files and often very large (e.g., slides of presentations), storing them in git would be inefficient. Please send pdf files that you want to appear on the website to Robert, he will copy it to the server.

## Videos

This is implemented with some small snippets of html code contained in the `_includes` directory.

You can include a Youtube video like this

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

To show a news item on the front page, you have to add the news item as a Markdown page to `_posts` with the name `YYYY-MM-DD-short-description.md`. See the other examples in that directory.

Posts should not have any tags.

Recent posts that have the category 'news' are automatically shown on the front page.
