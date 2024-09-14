"""
file-system-analyzer

This module provides a command-line tool for analyzing and reporting on file system
structure and usage. It performs size analysis, checks for unusual file permissions,
and identifies large files.

Functions:
- main(): Parses command-line arguments, and performs file system analysis by calling
`calculate_size`, `check_permissions`, and `find_large_files`.

Example:
    $ python file-system-analyzer /path/to/directory --size-threshold 2000000
    Size Analysis: {'text': 123456, 'image': 789012, 'unknown': 345678}
    Files with Unusual Permissions: ['/path/to/directory/world_writable_file1.txt',
      '/path/to/directory/world_writable_file2.sh']
    Large Files: ['/path/to/directory/large_file1.bin',
      '/path/to/directory/large_file2.mp4']
"""

import argparse
from analyzer.size_analysis import calculate_size
from analyzer.permissions import check_permissions
from analyzer.large_files import find_large_files

def main():
    """Parses command-line arguments and performs file system analysis.
    Command-line arguments:
    - directory: Directory to analyze (required)
    - --size-threshold: Size threshold for large files in bytes (default: 1,000,000 bytes)
    """
    parser = argparse.ArgumentParser(
      description="Analyze and report on file system structure and usage.")
    parser.add_argument(
      "directory", help="Directory to analyze")
    parser.add_argument(
      "--size-threshold", type=int, default=1000000, help="Size threshold for large files (bytes)")

    args = parser.parse_args()

    directory = args.directory
    size_threshold = args.size_threshold

    # Call functions here (size analysis, permissions check, etc.)
    print("Size Analysis:", calculate_size(directory))
    print("Files with Unusual Permissions:", check_permissions(directory))
    print("Large Files:", find_large_files(directory, size_threshold))

if __name__ == "__main__":
    main()
