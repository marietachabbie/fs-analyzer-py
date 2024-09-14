"""
directory_traversal

This module provides functionality for recursively traversing a directory and
yielding file paths.

Functions:
- traverse_directory(directory): Yields file paths for all files within the
specified directory and its subdirectories.

Example:
    >>> list(traverse_directory('/path/to/directory'))
      ['/path/to/directory/file1.txt',
      '/path/to/directory/subdir/file2.jpg',
      '/path/to/directory/subdir/file3.pdf']
"""

import os

def traverse_directory(directory):
    """Recursively traverses a directory and yields file paths."""
    # pylint: disable=W0612:unused-variable
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)
