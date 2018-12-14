# FieldTrip website

This repository contains the content that is hosted on http://www.fieldtriptoolbox.org

Feel free to contribute to the Fieldtrip documentation by doing edits here and sending a pull request.

## Technical notes

* Pages that contain tags must have a title.
* Variables passed in an include must be specified in quotes.
* Code blocks should have an empty line before and after them.
* Shared pages should go in _include/shared.
* MarkDown documentation can be found on https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet.
* Liquid documentation can be found on https://help.shopify.com/en/themes/liquid and https://shopify.github.io/liquid.

## Checking for broken links and missing images

  wget --spider -r -nd -nv -o spider.log http://localhost:4000
  grep -B1 'broken link!' spider.log  | grep http > broken.log

## Ideas

* For image resizing we might consider a service like https://www.imgix.com or https://images.weserv.nl.
* Use code highlighting from https://jekyllrb.com/docs/liquid/tags/#code-snippet-highlighting.
