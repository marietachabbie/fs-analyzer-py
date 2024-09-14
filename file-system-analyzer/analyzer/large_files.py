"""
file_analyzer

This module provides functionality for finding large files within a specified directory.

Functions:
- find_large_files(directory, size_threshold): Returns a list of file paths that are
larger than the specified size threshold.

Example:
    >>> find_large_files('/path/to/directory', 1048576)  # 1 MB threshold
      ['/path/to/directory/large_file1.bin',
      '/path/to/directory/large_file2.mp4']
"""

import os
from analyzer.traversal import traverse_directory

def find_large_files(directory, size_threshold):
    """Finds files larger than the specified size threshold."""
    large_files = []
    for file_path in traverse_directory(directory):
        if os.path.getsize(file_path) > size_threshold:
            large_files.append(file_path)
    return large_files
