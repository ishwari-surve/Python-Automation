# File Operations

# **About**
- Collection of Python programs demonstrating file and path operations
- Uses os module for file management utilities
- Covers path validation, existence checking, and file removal
- Essential for automation and file management tasks

## Purpose
- Learn file operation utilities using os module
- Understand absolute and relative paths
- Master file existence checking and removal
- Build file management automation scripts

## Programs Included

**FileIOPath.py**
- Determines if file path is absolute or relative
- Uses os.path.isabs() function
- Takes file name as user input
- Displays path type classification

**FilePathChange.py**
- Checks if file exists before processing
- Uses os.path.exists() function
- Converts relative path to absolute path
- Uses os.path.abspath() for path conversion
- Displays updated absolute path

**FileIORemove.py**
- Removes file from system
- Uses os.path.exists() to verify file
- Uses os.remove() to delete file
- Handles file deletion with validation

**FileIOExists.py**
- Verifies file existence before opening
- Uses os.path.exists() function
- Opens file only if it exists
- Displays appropriate messages

## How to Run
```bash
- python FileIOPath.py
- python FilePathChange.py
- python FileIORemove.py
- python FileIOExists.py
```

## Key Concepts
- os.path.isabs(): Check if path is absolute
- os.path.exists(): Verify file or directory existence
- os.path.abspath(): Convert relative to absolute path
- os.remove(): Delete file from system
- Absolute path: Complete path from root directory
- Relative path: Path from current working directory
- Path validation: Checking path before operations

## Technologies Used
- Python 3.x
- os module (built-in)
- Path manipulation functions
- File system operations

## Learning Path
- Start with FileIOPath.py (path classification)
- Learn FileIOExists.py (existence checking)
- Progress to FilePathChange.py (path conversion)
- Master FileIORemove.py (file deletion)

## Notes
- Always check file existence before operations
- Use absolute paths for reliable file operations
- Relative paths depend on current working directory
- Path operations are OS-independent with os module
- Be careful with file removal - it's permanent
