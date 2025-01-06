# FieldTrip website

This repository contains the FieldTrip documentation that is hosted on <https://www.fieldtriptoolbox.org>.

Feel free to contribute by doing edits here and sending a pull request. See <https://www.fieldtriptoolbox.org/development/git> for a complete tutorial and <https://www.fieldtriptoolbox.org/development/guideline/website> for formatting instructions.

## House prose style

- UK English spelling
- No Oxford commas
- Spellings
  - "FieldTrip", not "Fieldtrip"
  - "open source", not "open-source"
  - "website", not "web site"
  - "MATLAB", not "Matlab"
- Sentence case (not "Title Case") for section headings
- Use en- or em-dashes where appropriate

## Technical notes

- The website is rebuilt after every merged commit; this can take up to 5 minutes.
- File names should not contain spaces or other special characters.
- Files should be saved in UNIX format, not in DOS format.
- The tags and authors in the front matter should be lists, the category should have a single value.
- Pages that contain tags must have a title.
- Tags should be in lower case.
- All tags should appear on a single line.
- Variables passed in an include must be specified in quotes.
- Code blocks should have an empty line before and after them.
- Shared pages should go in \_include/shared.
- Markdown documentation can be found on <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>.
- Liquid documentation can be found on <https://help.shopify.com/en/themes/liquid> and <https://shopify.github.io/liquid>.
- Jekyll cheatsheet can be found on <https://devhints.io/jekyll>.

## Limitations when viewing on GitHub

Most of the Markdown formatting will show up nicely here on GitHub, but there are some limitations.

- Hyperlinks will not be pointing to the correct pages.
- Images are not included correctly.
- YouTube videos will not be included correctly.
- Highlighted sections will not show correctly.
- Code blocks don't have syntax highlighting.

## Evaluating the website locally

If you make changes that you want to evaluate prior to publishing them, you have to install Ruby, Bundler and Jekyll. Subsequently you can do

    bundle config set path '.bundle'
    bundle install
    bundle exec jekyll serve --incremental --livereload

which will convert the Markdown into HTML and serve your local copy of the website on <http://localhost:4000>.

## Checking for broken links and missing images

    wget --spider -r -nd -nv -o spider.log http://localhost:4000
    grep -B1 'broken link!' spider.log  | grep http > broken.log
