"""
Unit tests for the `check_permissions` function in the `permissions` module.

This module tests the functionality of checking file permissions in a directory.
It includes tests for checking permissions on files in a valid directory and handling errors
when the directory does not exist.

Functions:
    test_check_permissions: Tests checking permissions on files in a directory.
    test_check_permissions_directory_not_found: Tests the case when the directory does not exist.
"""

from unittest.mock import patch
import pytest
from file_system_analyzer.analyzer.permissions import check_permissions
from file_system_analyzer.analyzer.errors import DirectoryNotFoundError

@patch('file_system_analyzer.analyzer.permissions.os.path.isdir')
@patch('file_system_analyzer.analyzer.permissions.traverse_directory')
@patch('file_system_analyzer.analyzer.permissions.os.stat')
def test_check_permissions(mock_stat, mock_traverse_directory, mock_isdir):
    """
    Tests checking file permissions in the `check_permissions` function.

    This test mocks the directory existence check, the directory traversal, and file permission
    checking using `os.stat`. It simulates finding files with permissions and asserts that the
    function returns the correct files.
    """
    mock_isdir.return_value = True
    mock_traverse_directory.return_value = ['/path/to/file1.txt', '/path/to/file2.sh']
    mock_stat.return_value.st_mode = 0o777

    result = check_permissions('/path/to/directory')

    assert result == ['/path/to/file2.sh']

def test_check_permissions_directory_not_found():
    """Tests the case when the directory does not exist"""
    with pytest.raises(DirectoryNotFoundError):
        check_permissions('/invalid/directory')
