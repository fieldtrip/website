#!/usr/bin/env python3
#
# This script will recursively walk the directory structure of a Jekyll website 
# and check all markdown files for correct use of the headings as indicated 
# with one or more hashes (#). 
# 
# H1 headings should not be present, since those are automatically added as 
# page title by the layout.
#
# H3 or higher headings should only be present if the corresponding lower level 
# heading (e.g., H2) is also present.
#
# Installation:
#   conda create -n website python==3.10
#   conda activate website

import os
import re

rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)));
print(f"Checking for headers in {rootdir}")

# list of files to exclude from the check
# these contain for example Bash or Python code snippets with comments
exclude_files = []
exclude_files.append("README.md")
exclude_files.append("COPYING.md")
exclude_files.append("index.md")
exclude_files.append("workshop/nigeria2025/stimuluspresentation.md")
exclude_files.append("tutorial/source/sourcemodel.md")
exclude_files.append("development/git.md")
exclude_files.append("development/realtime/biosemi.md")
exclude_files.append("faq/matlab/compile.md")
exclude_files.append("example/other/bids_mous.md")

# keep track of the total count of incorrect headings
count = 0

for (root,dirs,files) in os.walk(rootdir, topdown=True):
    for file in files:
        if file.endswith(".md") and not '.' in root: # skip hidden directories, like .git and .bundle
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:

                reldir = root[len(rootdir)+1:]
                if reldir.startswith("_posts") or reldir.startswith("_includes"):
                    continue

                relfile = os.path.join(root, file)
                relfile = relfile[len(rootdir)+1:]
                if relfile in exclude_files:
                    continue

                content = f.read()

                h1 = h2 = h3 = h4 = h5 = h6 = 0
                for line in content.splitlines():
                    h1 += len(re.findall("^# ", line))
                    h2 += len(re.findall("^## ", line))
                    h3 += len(re.findall("^### ", line))
                    h4 += len(re.findall("^#### ", line))
                    h5 += len(re.findall("^##### ", line))
                    h6 += len(re.findall("^###### ", line))

                if h1 > 0:
                    print(f"Warning: H1 heading found in {relfile}")
                    count += 1
                if h3 > 0 and h2 == 0:
                    print(f"Warning: H3 heading found without H2 in {relfile}")
                    count += 1
                if h4 > 0 and h3 == 0:
                    print(f"Warning: H4 heading found without H3 in {relfile}")
                    count += 1
                if h5 > 0 and h4 == 0:
                    print(f"Warning: H5 heading found without H4 in {relfile}")
                    count += 1
                if h6 > 0 and h5 == 0:
                    print(f"Warning: H6 heading found without H5 in {relfile}")
                    count += 1

print(f"Found {count} files with incorrect headings")

if count > 0:
    # return an error code to allow external tools to detect the issue
    exit(1)