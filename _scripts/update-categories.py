#!/usr/bin/env python3
#
# This script will update the category files in _data/category/ with the categories found in the
# frontmatter of the markdown files in the site.
#
# The script will walk the directory tree starting from the directory where it is
# located and will look for markdown files. If a file has a 'category' field in the
# frontmatter, it will add the file to the list of files for that category.
#
# Installation:
#   conda create -n website python==3.10
#   pip install python-frontmatter pyyaml

import os
import frontmatter
import yaml

rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)));
print(f"Updating categories in {rootdir}")

allcategories = {}

for (root,dirs,files) in os.walk(rootdir, topdown=True):
    for file in files:
        if os.path.splitext(file)[1] == '.md':
            page = frontmatter.load(os.path.join(root,file))
            if 'category' in page.keys() and 'title' in page.keys():
                categories = page['category']  # each item should belong to only a single category
                if type(categories) is not list:
                    categories = [categories]
                for category in categories:
                    if category not in allcategories:
                        allcategories[category] = []
                    item = {}
                    item['title'] = page['title']
                    item['link'] = os.path.join(root,file)
                    item['link'] = item['link'].replace(rootdir, '')
                    allcategories[category].append(item)

for category in allcategories:
    allcategories[category].sort(key=lambda x: x['title'])

for category in allcategories:
    with open(f"{rootdir}/_data/category/{category}.yml", 'w') as file:
        yaml.dump(allcategories[category], file)
