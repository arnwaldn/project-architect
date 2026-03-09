#!/usr/bin/env python3
"""Auto-sync plugin source files to Claude Code plugin cache.

Usage: python sync-cache.py [file_path]
  - With file_path: sync only that file (if it's inside the plugin source)
  - Without args: sync all plugin files to cache
"""
import sys, os, shutil

SOURCE = r"C:\Users\arnau\Documents\projets\skill project-architect"
CACHE = os.path.expanduser(r"~\.claude\plugins\cache\local\project-architect\1.0.0")

# Directories to sync (relative to SOURCE)
SYNC_DIRS = ["commands", "templates", "data", "agents", ".claude-plugin"]


def sync_file(rel_path):
    """Copy a single file from source to cache."""
    src = os.path.join(SOURCE, rel_path)
    dst = os.path.join(CACHE, rel_path)
    if not os.path.isfile(src):
        return False
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    return True


def sync_all():
    """Sync all plugin files to cache."""
    count = 0
    for d in SYNC_DIRS:
        src_dir = os.path.join(SOURCE, d)
        if not os.path.isdir(src_dir):
            continue
        for f in os.listdir(src_dir):
            rel = os.path.join(d, f)
            if sync_file(rel):
                count += 1
    return count


def remove_orphan_marker():
    """Remove .orphaned_at marker if present."""
    marker = os.path.join(CACHE, ".orphaned_at")
    if os.path.exists(marker):
        os.remove(marker)
        return True
    return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        # Normalize paths for comparison
        norm_file = os.path.normpath(file_path)
        norm_source = os.path.normpath(SOURCE)
        if norm_file.startswith(norm_source):
            rel = os.path.relpath(norm_file, norm_source)
            # Only sync files in known directories
            top_dir = rel.split(os.sep)[0]
            if top_dir in SYNC_DIRS:
                if sync_file(rel):
                    remove_orphan_marker()
                    print("[sync-cache] %s -> cache" % rel)
            # Silently skip files outside sync dirs (e.g. .gitignore)
        # Silently skip files outside plugin source
    else:
        count = sync_all()
        removed = remove_orphan_marker()
        print("[sync-cache] %d files synced%s" % (count, ", orphan marker removed" if removed else ""))
