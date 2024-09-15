# File System Analyzer

`file_system_analyzer` is a Python package that analyzes and reports on the structure and usage of a file system.

## Features

- **Directory Traversal:** Walk through a directory structure and collect details about the files.
- **Size Analysis:** Calculate the total size of files in a directory, grouped by file type (e.g., text, image).
- **Large File Identification:** Find files larger than a given size threshold.
- **Permissions Check:** Identify files with specific permissions in a directory.
- **Error Handling:** Graceful error handling for invalid directories and invalid size thresholds.

## Installation

Clone the repository and install the necessary dependencies:

```sh
cd file_system_analyzer
pip install .
```

## Running
```sh
python3 file_system_analyzer /path/to/dir/to/analyze/ --size-threshold 50000
```

## Arguments
```sh
positional arguments:
  directory             Directory to analyze

options:
  -h, --help            show this help message and exit
  --size-threshold SIZE_THRESHOLD
                        Size threshold for large files (bytes)
```

## Help
```sh
python3 file_system_analyzer --help
```
