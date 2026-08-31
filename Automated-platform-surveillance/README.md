## Automated Platform Surveillance System

### About

- Complete automated platform surveillance system for system resource monitoring
- Tracks CPU, RAM, Disk, Network usage and running processes
- Generates comprehensive timestamped log files
- Implements scheduled automation for continuous monitoring
- Marvellous Infosystems production-grade system monitoring solution

### Purpose

- Learn comprehensive system monitoring using `psutil` module
- Understand process scanning and detailed system metrics
- Master automated log generation and scheduling
- Build production-ready platform surveillance applications

### Programs Included

#### SystemSurvellance.py (Version 1)

- Implements basic process scanning functionality
- Displays running processes with PID, name, and status
- Uses `psutil` for process iteration
- Provides the foundation for the surveillance system

#### SystemSurvellanceX.py (Version 2)

- Provides enhanced process information collection
- Captures detailed process attributes such as username, CPU%, and Memory%
- Converts epoch time into a readable date and time format
- Handles process exceptions gracefully
- Stores process information in a list structure

#### surveillance.py (Version 3 - Final Production Version)

- Implements a complete system surveillance solution
- Monitors CPU, RAM, Disk, and Network metrics
- Performs detailed process logging with multiple attributes
- Generates comprehensive timestamped log files
- Provides command-line interface with help and usage flags
- Supports scheduled execution at specified intervals
- Includes documentation and comments for better understanding

### How to Run

#### Basic Execution

```bash
python SystemSurvellance.py
python SystemSurvellanceX.py
```

## Scheduled Surveillance (Production Version)
# Display help
python surveillance.py --h

# Display usage
python surveillance.py --u

# Start surveillance with 5-minute intervals
python surveillance.py 5 Marvellous

### Key Concepts

- **Process Scanning** – Iterating through running processes
- **`psutil` Module** – System and process monitoring library
- **Process Attributes** – PID, name, username, status, CPU%, Memory%
- **Epoch Time Conversion** – Converting timestamps into readable date and time
- **Exception Handling** – Managing process access and permission errors
- **Timestamped Logging** – Creating unique log files with dates and times
- **Scheduled Automation** – Running monitoring tasks at regular intervals
- **System Metrics** – Monitoring CPU, RAM, Disk, and Network usage

### Technologies Used

- Python 3.x
- `psutil` module – System and process monitoring
- `schedule` module – Task scheduling
- `os` module – File operations
- `time` module – Timestamps and time formatting
- `sys` module – Command-line argument handling

### Dependencies

```bash
pip install psutil schedule
```

### Learning Path & Version Progression

- **Version 1 (`SystemSurvellance.py`)** – Basic process scanning
- **Version 2 (`SystemSurvellanceX.py`)** – Enhanced process details collection
- **Version 3 (`surveillance.py`)** – Complete system monitoring with logging

### System Metrics Monitored

- **CPU Usage** – Processor utilization percentage
- **RAM Usage** – Virtual memory utilization
- **Disk Usage** – Storage utilization per partition
- **Network Usage** – Data sent and received
- **Process Details** – PID, name, username, status, CPU%, Memory%
- **Timestamps** – Log creation time and process start time

### Production Features

- CLI interface with help and usage options
- Automatic directory creation for logs
- Timestamped unique log filenames
- Exception handling for process access issues
- Scheduled periodic execution
- Comprehensive system and process reports
- Professional formatted log output

### Notes

- `psutil` requires system-level access for accurate metrics
- Process CPU% may require a warm-up measurement for accurate results
- Some processes may be inaccessible due to system permissions
- Network statistics are cumulative since system boot
- Log files can grow over time, so cleanup should be implemented for long-term usage
- Press `Ctrl+C` to stop scheduled execution gracefully

## Author

**Ishwari Vijaykumar Surve**



