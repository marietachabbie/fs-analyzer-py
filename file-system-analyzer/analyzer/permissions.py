"""
permission_checker

This module provides functionality for identifying files with world-writable
permissions in a specified directory.

Functions:
- check_permissions(directory): Returns a list of file paths that have
world-writable permissions.

Example:
    >>> check_permissions('/path/to/directory')
      ['/path/to/directory/world_writable_file1.txt',
      '/path/to/directory/world_writable_file2.sh']
"""

import os
import stat
from analyzer.traversal import traverse_directory

def check_permissions(directory):
    """Finds files with world-writable permissions."""
    unusual_permissions = []
    for file_path in traverse_directory(directory):
        st = os.stat(file_path)
        if bool(st.st_mode & stat.S_IWOTH):
            unusual_permissions.append(file_path)
    return unusual_permissions
