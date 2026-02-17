---
title: Ensure that all website pages exist
---

{% include /shared/development/warning.md %}

There should not be any internal links that are broken.  

Now that the website is built with Jekyll, it is possible to check for broken links and missing images with:

    wget --spider -r -nd -nv -o spider.log http://localhost:4000
    grep -B1 'broken link!' spider.log  | grep http > broken.log
