#!/usr/bin/env python3
#
# This script will update the tag files in _data/tag/ with the tags found in the
# frontmatter of the markdown files in the site.
#
# The script will walk the directory tree starting from the directory where it is
# located and will look for markdown files. If a file has a 'tags' field in the
# frontmatter, it will add the file to the list of files for that tag.
#
# Installation:
#   conda create -n website python==3.10
#   pip install python-frontmatter pyyaml

import os
import frontmatter
import yaml

rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)));
print(f"Updating tags in {rootdir}")

alltags = {}

for (root,dirs,files) in os.walk(rootdir, topdown=True):
    for file in files:
        if os.path.splitext(file)[1] == '.md':
            page = frontmatter.load(os.path.join(root,file))
            if 'tags' in page.keys() and 'title' in page.keys():
                tags = page['tags']
                if type(tags) is not list:
                    tags = [tags]
                for tag in tags:
                    if tag not in alltags:
                        alltags[tag] = []
                    item = {}
                    item['title'] = page['title']
                    item['link'] = os.path.join(root,file)
                    item['link'] = item['link'].replace(rootdir, '')
                    alltags[tag].append(item)

for tag in alltags:
    alltags[tag].sort(key=lambda x: x['title'])

for tag in alltags:
    with open(f"{rootdir}/_data/tag/{tag}.yml", 'w') as file:
        yaml.dump(alltags[tag], file)
