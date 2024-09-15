"""
This module provides functionality for categorizing files based on their MIME types. 

Functions:
- categorize_file(file_path): Returns the category of the file based on its MIME type. 

Example:
    >>> categorize_file('/path/to/file.txt')
    'text'
    
    >>> categorize_file('/path/to/file.jpg')
    'image'
    
    >>> categorize_file('/path/to/file')
    'unknown'
"""

import mimetypes

def categorize_file(file_path):
    """Categorizes a file based on its MIME type."""
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        return mime_type.split('/')[0]
    return 'unknown'
