"""
Unit tests for the `calculate_size` function in the `size_analysis` module.

This module tests the functionality of calculating the size of files within a
directory, grouped by file type. It includes tests for successful size
calculation and error handling when the directory does not exist.

Functions:
    test_calculate_size: Tests the size calculation of files in a
    directory by file type.
    test_calculate_size_directory_not_found: Tests the case when
    the directory does not exist.
"""

from unittest.mock import patch
import pytest
from file_system_analyzer.analyzer.size_analysis import calculate_size
from file_system_analyzer.analyzer.errors import DirectoryNotFoundError

@patch('file_system_analyzer.analyzer.size_analysis.os.path.isdir')
@patch('file_system_analyzer.analyzer.size_analysis.traverse_directory')
@patch('file_system_analyzer.analyzer.size_analysis.categorize_file')
@patch('file_system_analyzer.analyzer.size_analysis.os.path.getsize')
def test_calculate_size(mock_getsize, mock_categorize_file, mock_traverse_directory, mock_isdir):
    """
    Tests calculating the size of files in the `calculate_size` function.

    This test mocks the directory existence check, directory traversal, file
    categorization, and file size retrieval using `os.path.getsize`. It
    simulates different file types and sizes, and asserts that the function
    correctly returns the total size of each file type.
    """
    mock_isdir.return_value = True
    mock_traverse_directory.return_value = ['/path/to/file1.txt', '/path/to/file2.jpg']
    mock_categorize_file.side_effect = ['text', 'image']
    mock_getsize.side_effect = [100, 200]

    result = calculate_size('/path/to/directory')
    print("no")

    expected = {'text': 100, 'image': 200}
    assert result == expected

def test_calculate_size_directory_not_found():
    """Tests the case when the directory does not exist"""
    with pytest.raises(DirectoryNotFoundError):
        calculate_size('/invalid/directory')
