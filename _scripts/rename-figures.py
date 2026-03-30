#!/usr/bin/env python3
#
# This script renames figure files in a markdown page. It will print the
# commands to rename the figures and update the references in the page.
# The user of the script should check the commands prior to execution.
#
# Use as:
#   python _scripts/rename_figures.py <page.md>

from __future__ import annotations

import os
import sys


def main() -> int:
    if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
        return 1

    page = sys.argv[1]

    with open(page, "r", encoding="utf-8") as f:
        lines = f.readlines()

    figures: list[str] = []
    for line in lines:
        if "include image" in line:
            parts = line.split('"')
            if len(parts) >= 2:
                figures.append(parts[1])

    n = 1
    for figure in figures:
        oldname = os.path.basename(figure)
        parts = oldname.split(".")
        ext = parts[1] if len(parts) >= 2 else oldname

        dirname = os.path.dirname(figure)
        newname = f"{dirname}/figure{n}.{ext}" if dirname else f"figure{n}.{ext}"

        print(f"git mv .{figure} .{newname}")
        print(f"sed -i .bak s~{figure}~{newname}~g {page}")

        n += 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
