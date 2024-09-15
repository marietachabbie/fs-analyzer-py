"""
size_calculator

This module provides functionality for calculating the total size of files
categorized by their file type.

Functions:
- calculate_size(directory): Returns a dictionary with file categories as keys
and their total sizes as values.

Example:
    >>> calculate_size('/path/to/directory')
    {'text': 123456, 'image': 789012, 'unknown': 345678}
"""

import os
from collections import defaultdict
from analyzer.traversal import traverse_directory
from analyzer.file_categorization import categorize_file
from analyzer.errors import DirectoryNotFoundError

def calculate_size(directory):
    """Calculates the total size of files categorized by file type."""
    if not os.path.isdir(directory):
        raise DirectoryNotFoundError(
          f"The specified directory '{directory}' does not exist or is not a directory."
        )

    sizes = defaultdict(int)
    for file_path in traverse_directory(directory):
        category = categorize_file(file_path)
        sizes[category] += os.path.getsize(file_path)
    return dict(sizes)
