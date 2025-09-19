#!/usr/bin/env python3
#
# This script will recursively walk the directory structure twice. On the first run, it will search for
# the `redirect_from` in the YAML frontmatter of all markdown files and collect the old and new links.
# On the second run, it will update the markdown files with the new links.
#
# Installation:
#   conda create -n website python==3.10
#   conda activate website
#   pip install python-frontmatter pyyaml

import os
import frontmatter
import yaml

rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)));
print(f"Updating redirected links in {rootdir}")

redirects = {}

# pass 1: collect redirects
for (root,dirs,files) in os.walk(rootdir, topdown=True):
    for file in files:
        if file.endswith(".md") and not '.' in root: # skip hidden directories, like .git and .bundle
            page = frontmatter.load(os.path.join(root, file))
            if 'redirect_from' in page.keys() and isinstance(page['redirect_from'], list):
                for old_link in page['redirect_from']:
                    if old_link.endswith("/"):
                        old_link = old_link[:-1] # remove trailing slash
                    new_link = os.path.join(root, file[:-3])
                    new_link = os.path.relpath(new_link, rootdir)
                    new_link = "/" + new_link.replace(os.sep, "/")
                    print(f"Redirecting {old_link} to {new_link}")
                    redirects[old_link] = new_link

# pass 2: update markdown files
for (root,dirs,files) in os.walk(rootdir, topdown=True):
    for file in files:
        if file.endswith(".md") and not '.' in root: # skip hidden directories, like .git and .bundle
            filepath = os.path.join(root, file)
            with open(filepath, "r") as f:
                content = f.read()
            original_content = content

            # Update the content with the new links
            for old_link, new_link in redirects.items():
                # only replace full links, i.e. [text](old_link)
                # this may miss some cases, like links to anchors in the page
                old_link = f']({old_link})'
                new_link = f']({new_link})'
                content = content.replace(old_link, new_link)

            if content != original_content:
                print(f"Updating links in {filepath}")
                with open(filepath, "w")  as fw:
                    fw.write(content)
            
print("Done.")
