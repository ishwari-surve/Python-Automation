# Directory Automation

## About

- Collection of Python programs for directory scanning and automated file management
- Covers directory traversal, file listing, and empty file cleanup
- Includes logging and scheduling capabilities
- Helps in automating directory maintenance tasks

## Purpose

- Learn directory scanning and traversal techniques
- Understand file management automation
- Learn empty file detection and removal
- Implement scheduled directory maintenance scripts

## Programs Included

### DirectoryScan.py

- Performs basic directory scanning using user input
- Lists all files present in a directory recursively
- Uses `os.walk()` for directory traversal

### DirectoryScan2.py

- Implements directory scanning using a separate function
- Encapsulates scanning logic for better code organization
- Improves program readability and reusability

### DirectoryScan3.py

- Provides advanced directory scanning
- Uses default parameters
- Validates whether the specified path exists
- Uses `os.path.isdir()` to verify that the path is a directory

### DirectoryAutomation1.py

- Performs directory automation using command-line arguments
- Accepts the directory name as a command-line argument
- Lists all files recursively using `os.walk()`

### DirectoryAutomation2_.py

- Calculates and displays the size of each file
- Uses `os.path.getsize()` to obtain file size in bytes
- Displays file names along with their sizes

### DirectoryAutomations2.py

- Provides enhanced file size reporting
- Displays file information with size details
- Demonstrates practical file management operations

### DirectoryAutomation3.py

- Displays complete file paths along with file sizes
- Uses `os.path.join()` to construct complete file paths
- Helps perform accurate file operations using full paths

### DirectoryAutomationEmptyDelete.py

- Detects empty files inside a directory
- Identifies files having 0 bytes
- Removes empty files automatically
- Validates file size before deletion

### DirectoryAutomationEmptyReport.py

- Detects empty files inside a directory
- Counts the total number of files
- Counts the number of empty files
- Generates a cleanup report

### DirectoryAutomationEmptyDeleteReportlog.py

- Detects and deletes empty files
- Generates a log file
- Records details of file deletion operations

### DirectoryAutomationEmptyDeleteReportLogTimeStamp.py

- Detects and deletes empty files
- Generates timestamped log files
- Records the date and time of cleanup operations
- Maintains a history of automated operations

### DirectoryAutomationEmptyDeleteReportLogTime.py

- Provides time-based logging for directory cleanup
- Records operation details along with time information
- Maintains comprehensive cleanup history

### Ishwari.py

- Implements scheduled directory automation
- Runs directory cleanup operations at regular intervals
- Uses the `schedule` module for task scheduling
- Generates timestamped log files
- Records details of automated cleanup operations

## How to Run

### Basic Directory Scanning

```bash
python DirectoryScan.py
python DirectoryScan2.py
python DirectoryScan3.py
```
### Directory Automation

```bash
python DirectoryAutomation1.py /path/to/directory
python DirectoryAutomation2_.py /path/to/directory
python DirectoryAutomation3.py /path/to/directory
```

### Empty File Cleanup

```bash
python DirectoryAutomationEmptyReport.py /path/to/directory
python DirectoryAutomationEmptyDeleteReportLogTimeStamp.py /path/to/directory
```

### Scheduled Automation
```bash
python Ishwari.py /path/to/directory
```

## Key Concepts

- **`os.walk()`** – Recursively traverses directories
- **`os.path.exists()`** – Checks whether a specified path exists
- **`os.path.isdir()`** – Checks whether the specified path is a directory
- **`os.path.getsize()`** – Returns the size of a file in bytes
- **`os.path.join()`** – Creates a valid file path
- **`os.remove()`** – Deletes a specified file
- **File Logging** – Records operations and cleanup activities
- **Time Tracking** – Records the date and time of operations
- **Scheduling** – Executes tasks automatically at specified intervals

## Technologies Used

- Python 3.x
- `os` module
- `time` module
- `schedule` module
- File I/O operations

## Dependencies

```bash
pip install schedule
```

## Learning Path

- Start with `DirectoryScan.py` for basic directory scanning
- Practice `DirectoryScan2.py` for function-based organization
- Learn `DirectoryScan3.py` for path validation
- Practice `DirectoryAutomation1.py` for command-line arguments
- Learn `DirectoryAutomation2_.py` for file size calculation
- Practice `DirectoryAutomation3.py` for complete file paths
- Learn `DirectoryAutomationEmptyReport.py` for empty file statistics
- Practice `DirectoryAutomationEmptyDelete.py` for file deletion
- Learn logging programs for operation tracking
- Advance to `Ishwari.py` for scheduled directory automation

## Notes

- Empty files have 0 bytes size
- Always validate the directory path before performing file operations
- Use `os.path.join()` for cross-platform compatibility
- Log files help track automated operations
- The `schedule` module requires a continuous loop
- Use `os.walk()` for recursive directory scanning


