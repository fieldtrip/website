# Redirect Path Update Script

This document describes the script created to update `redirect_from` paths in Jekyll markdown files.

## Purpose

The script `_scripts/update_redirect_paths.py` was created to safely update internal links in the `redirect_from` YAML frontmatter sections of markdown files. It changes paths from `/oldpath/` to `/newpath/` while ensuring that:

1. Only `redirect_from` sections are modified
2. Other content in the files remains unchanged
3. YAML structure and formatting is preserved
4. Files without frontmatter or `redirect_from` sections are skipped

## Usage

```bash
# Basic usage (changes /oldpath/ to /newpath/)
python3 _scripts/update_redirect_paths.py .

# Custom paths
python3 _scripts/update_redirect_paths.py . "/legacy/" "/updated/"

# Dry run to see what would be changed
python3 _scripts/update_redirect_paths.py . "/oldpath/" "/newpath/" --dry-run
```

## What the script does

The script processes all markdown files (`.md`) recursively in the specified directory and:

1. **Identifies markdown files with YAML frontmatter** - Files must start with `---`
2. **Locates files with redirect_from sections** - Only files containing `redirect_from:` are processed
3. **Safely replaces paths** - Uses regex to target only the redirect_from section
4. **Preserves everything else** - Content, other frontmatter fields, and formatting remain unchanged

## Example

### Before:
```yaml
---
title: My Page
redirect_from:
  - /oldpath/
  - /other/path/
---

Content mentioning /oldpath/ remains unchanged.
```

### After:
```yaml
---
title: My Page
redirect_from:
  - /newpath/
  - /other/path/
---

Content mentioning /oldpath/ remains unchanged.
```

## Repository Status

As of the script creation, the repository contains:
- **1,335 markdown files** total
- **420 files** with `redirect_from` entries
- **0 files** with the literal path `/oldpath/`

The script was tested successfully and is ready for use if/when `/oldpath/` entries need to be updated in the future.