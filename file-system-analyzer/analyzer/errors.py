"""
errors

This module defines custom exceptions used in the file system analyzer application.

Exceptions:
- FileAnalyzerError: Base class for all exceptions in this module.
- DirectoryNotFoundError: Raised when the specified directory is not found or is not
  a directory.
- InvalidThresholdError: Raised for invalid size threshold values.

Example:
    To raise a custom exception:
        raise DirectoryNotFoundError("The specified directory does not exist.")
"""

class FileAnalyzerError(Exception):
    """Base class for exceptions in this module."""

class DirectoryNotFoundError(FileAnalyzerError):
    """Exception raised when the specified directory is not found."""

class InvalidThresholdError(FileAnalyzerError):
    """Exception raised for invalid size threshold values."""
