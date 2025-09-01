#!/usr/bin/env python3
#
# This script updates the _data/menu.yaml file. It will recursively 
# walk the directory structure and build a tree of the directories
# and files. The tree will then be converted to a menu structure.
#

import os
import frontmatter
import yaml

rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)));
print(f"Updating menu in {rootdir}")


def build_tree(paths):
    tree = {}
    for path in paths:
        parts = path.split('/')
        current_level = tree
        for part in parts:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
    return tree


def tree_to_menu(tree, base=""):
    menu = []
    for key, subtree in sorted(tree.items()):
        if key.endswith('.md'):
            filename =f"{rootdir}/{base}/{key}".replace("//", "/")
            dirname = filename[:-3]
        else:
            filename =f"{rootdir}/{base}/{key}.md".replace("//", "/")
            dirname = filename[:-3]
        item = {}
        if os.path.exists(filename):
            page = frontmatter.load(filename)
        else:
            page = {}
        if "title" in page and page["title"]:
            item["title"] = page["title"]
        else:
            item["title"] = key
        item["link"] = '/' + dirname[len(rootdir)+1:] + '/'
        if "nav_order" in page and page["nav_order"]:
            item["nav_order"] = page["nav_order"]
        else:
            item["nav_order"] = 0
        if subtree:
            item["menu"] = tree_to_menu(subtree, f"{base}/{key}")
        if key.endswith('.md') and os.path.exists(dirname) and os.path.exists(filename):
            pass
        elif "nav_exclude" in page and page["nav_exclude"]:
            pass
        else:
            menu.append(item)
    menu.sort(key=lambda x: (x["nav_order"], x["title"]))
    return menu


paths = []
for (root,dirs,files) in os.walk(rootdir, topdown=True):

    for file in files:
        filepath = root[len(rootdir)+1:]
        if not file.endswith('.md'):
            continue
        if file.startswith('COPYING') or file.startswith('LICENSE') or file.startswith('README'):
            continue
        if filepath.startswith('.') or filepath.startswith('_') or filepath.startswith('assets') or filepath.startswith('error') or filepath.startswith('tag') or filepath.startswith('category'):
            continue
        paths.append(os.path.join(filepath, file))

# Build the tree structure
tree = build_tree(paths)

# Convert tree to menu format
menu = tree_to_menu(tree)

# Output the result as YAML
# print(yaml.dump(menu, sort_keys=False))
with os.fdopen(os.open(f"{rootdir}/_data/menu.yml", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644), 'w') as f:
    f.write(yaml.dump(menu, sort_keys=False))