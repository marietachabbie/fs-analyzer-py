"""
Unit tests for the `find_large_files` function in the `large_files` module.

This module tests the functionality of finding large files in a directory based on a specified
size threshold. It also checks for handling invalid directory paths and invalid size thresholds.

Functions:
    test_find_large_files: Tests finding files larger than a given threshold.
    test_find_large_files_directory_not_found: Tests the case when the directory does not exist.
    test_find_large_files_invalid_threshold: Tests the case when the size threshold is invalid
    (negative value).
"""

from unittest.mock import patch
import pytest
from file_system_analyzer.analyzer.large_files import find_large_files
from file_system_analyzer.analyzer.errors import DirectoryNotFoundError, InvalidThresholdError

@patch('file_system_analyzer.analyzer.large_files.os.path.getsize')
@patch('file_system_analyzer.analyzer.large_files.traverse_directory')
@patch('file_system_analyzer.analyzer.large_files.os.path.isdir')
def test_find_large_files(mock_isdir, mock_traverse_directory, mock_getsize):
    """
    Tests finding files larger than a given threshold in the `find_large_files` function.
    
    This test mocks the directory existence check, the directory traversal, and file size
    determination to simulate the behavior of the function. It asserts that the function correctly
    identifies files larger than the specified threshold.
    """
    mock_isdir.return_value = True
    mock_traverse_directory.return_value = ['/path/to/file1.txt', '/path/to/file2.jpg']
    mock_getsize.side_effect = [500000, 2000000]

    result = find_large_files('/path/to/directory', 1000000)

    print("Mock isdir return value:", mock_isdir.return_value)
    print("Mock isdir called with:", mock_isdir.call_args)
    mock_isdir.assert_called_with('/path/to/directory')

    print("Result:", result)
    assert result == ['/path/to/file2.jpg']

def test_find_large_files_directory_not_found():
    """Tests the case when the directory does not exist"""
    with pytest.raises(DirectoryNotFoundError):
        find_large_files('/invalid/directory', 1000000)

@patch('file_system_analyzer.analyzer.large_files.os.path.isdir')
def test_find_large_files_invalid_threshold(mock_isdir):
    """Tests the case when the size threshold is invalid (negative value)"""
    mock_isdir.return_value = True

    with pytest.raises(InvalidThresholdError):
        find_large_files('/path/to/directory', -100)
