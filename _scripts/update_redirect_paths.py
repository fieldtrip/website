#!/usr/bin/env python3
"""
Script to update redirect_from paths in Jekyll markdown files.
This script safely replaces old paths with new paths only in redirect_from YAML frontmatter sections.

Usage:
  python3 update_redirect_paths.py <directory> [old_path] [new_path]

Examples:
  python3 update_redirect_paths.py . "/oldpath/" "/newpath/"
  python3 update_redirect_paths.py ./content "/legacy/" "/new/"

The script will:
- Only modify paths in redirect_from sections of YAML frontmatter
- Leave all other content unchanged
- Preserve YAML structure and formatting
- Skip files without frontmatter or redirect_from sections
"""

import re
import os
import sys
from pathlib import Path

def update_redirect_from_paths(file_path, old_path, new_path):
    """
    Update redirect_from paths in a single markdown file.
    
    Args:
        file_path: Path to the markdown file
        old_path: The old path to replace
        new_path: The new path to replace with
    
    Returns:
        bool: True if file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, IOError):
        # Skip files that can't be read
        return False
    
    # Check if file has YAML frontmatter
    if not content.startswith('---'):
        return False
    
    # Split content into frontmatter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    frontmatter = parts[1]
    body = parts[2]
    
    # Check if frontmatter contains redirect_from
    if 'redirect_from:' not in frontmatter:
        return False
    
    # Replace old_path with new_path only in redirect_from sections
    original_frontmatter = frontmatter
    
    # Pattern to match redirect_from section and capture the content
    # This handles both single-line and multi-line redirect_from sections
    redirect_pattern = r'(redirect_from:\s*(?:\n(?:\s*-\s*[^\n]+\n)*|\s*[^\n]+\n))'
    
    def replace_in_redirect_section(match):
        redirect_section = match.group(1)
        # Replace old_path with new_path in this section only
        updated_section = redirect_section.replace(old_path, new_path)
        return updated_section
    
    updated_frontmatter = re.sub(redirect_pattern, replace_in_redirect_section, frontmatter, flags=re.MULTILINE)
    
    # Check if anything was actually changed
    if updated_frontmatter == original_frontmatter:
        return False
    
    # Reconstruct the file content
    updated_content = '---' + updated_frontmatter + '---' + body
    
    # Write the updated content back to file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    except IOError:
        return False

def process_directory(directory_path, old_path, new_path, dry_run=False):
    """
    Process all markdown files in a directory recursively.
    
    Args:
        directory_path: Path to the directory to process
        old_path: The old path to replace
        new_path: The new path to replace with
        dry_run: If True, only report what would be changed without modifying files
    
    Returns:
        tuple: (files_processed, files_modified, modified_files)
    """
    files_processed = 0
    files_modified = 0
    modified_files = []
    
    for file_path in sorted(Path(directory_path).rglob('*.md')):
        files_processed += 1
        
        # For dry run, check if file would be modified
        if dry_run:
            # Read and check file without modifying
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if (content.startswith('---') and 
                    '---' in content[3:] and 
                    'redirect_from:' in content.split('---', 2)[1] and
                    old_path in content.split('---', 2)[1]):
                    files_modified += 1
                    modified_files.append(str(file_path))
                    print(f"Would modify: {file_path}")
            except (UnicodeDecodeError, IOError):
                pass
        else:
            # Actually modify the file
            if update_redirect_from_paths(file_path, old_path, new_path):
                files_modified += 1
                modified_files.append(str(file_path))
                print(f"Modified: {file_path}")
    
    return files_processed, files_modified, modified_files

def main():
    """Main function to handle command line arguments and execute the script."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    directory_path = sys.argv[1]
    old_path = sys.argv[2] if len(sys.argv) > 2 else "/oldpath/"
    new_path = sys.argv[3] if len(sys.argv) > 3 else "/newpath/"
    
    # Check for --dry-run flag
    dry_run = '--dry-run' in sys.argv
    
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        sys.exit(1)
    
    print(f"Processing directory: {directory_path}")
    print(f"Replacing '{old_path}' with '{new_path}' in redirect_from sections...")
    if dry_run:
        print("DRY RUN MODE - no files will be modified")
    print()
    
    files_processed, files_modified, modified_files = process_directory(
        directory_path, old_path, new_path, dry_run
    )
    
    print(f"\nSummary:")
    print(f"Files processed: {files_processed}")
    print(f"Files {'that would be ' if dry_run else ''}modified: {files_modified}")
    
    if files_modified > 0 and not dry_run:
        print(f"\nModified files:")
        for file_path in modified_files:
            print(f"  - {file_path}")

if __name__ == "__main__":
    main()