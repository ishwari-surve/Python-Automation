# System Monitoring

## About

- Collection of Python programs for system resource monitoring and logging
- Tracks CPU usage, memory (RAM), disk space, and network statistics
- Implements automated log generation with timestamps
- Uses `psutil` module for real-time system metrics
- Includes command-line interface and scheduling capabilities

## Purpose

- Learn system resource monitoring using `psutil` module
- Understand log file creation and management
- Master platform surveillance automation
- Build comprehensive system monitoring applications

## Programs Included

### ProcessorloggerCommandLine.py

- Platform surveillance system with CLI interface
- Implements help (`--h`) and usage (`--u`) flags
- Accepts time interval and directory as arguments
- Displays feature descriptions and usage instructions

### Processorloggerlogfile.py

- Creates log directory structure
- Implements directory creation logic
- Validates folder existence before logging
- Provides a foundation for log file management

### ProcessorloggerlogfileTimeStamp.py

- Generates timestamped log files
- Creates unique log filenames with date and time
- Stores logs in the specified directory
- Uses `time.strftime()` for timestamp formatting

### ProcessorloggerScheduler.py

- Implements scheduled log execution
- Runs logging at specified time intervals
- Uses `schedule` module for automation
- Continues execution until interrupted

### CPULOG.py

- Monitors CPU usage metrics
- Generates logs containing CPU information
- Records timestamps of monitoring operations
- Implements scheduling for periodic monitoring

### MemoryLog.py

- Tracks RAM (virtual memory) usage
- Logs memory percentage utilization
- Combines CPU and memory monitoring
- Supports scheduled execution for continuous tracking

### Diskusage.py

- Monitors all disk partitions
- Reports disk usage for each partition
- Tracks available and used storage space
- Provides comprehensive disk statistics

### DiskusageException.py

- Provides enhanced disk usage monitoring
- Implements exception handling
- Handles inaccessible partitions gracefully
- Uses `try-except` for error management
- Provides robust system monitoring

### ProcessLoggerwithsysteminfo.py

- Implements a complete platform surveillance system
- Monitors CPU, RAM, disk, and network metrics
- Generates comprehensive system reports
- Records network sent and received statistics
- Provides complete system information logging

## How to Run

```bash
# Display help information
python ProcessorloggerCommandLine.py --h

# Display usage instructions
python ProcessorloggerCommandLine.py --u

# Start system monitoring with scheduling
python ProcessorloggerScheduler.py 5 /path/to/logs
python CPULOG.py 5 /path/to/logs
python MemoryLog.py 5 /path/to/logs
python Diskusage.py 5 /path/to/logs
python ProcessLoggerwithsysteminfo.py 5 /path/to/logs
```

## Key Concepts

- **`psutil` module** – Python library for system monitoring
- **CPU Usage** – Processor utilization percentage
- **Virtual Memory** – RAM usage statistics
- **Disk Partitions** – Storage device information
- **Network Counters** – Data sent and received metrics
- **Timestamp Logging** – Recording operation times
- **Scheduled Execution** – Periodic automation
- **Exception Handling** – Error management in monitoring
- **Log Files** – Persistent records of system metrics

## Technologies Used

- Python 3.x
- `psutil` module – System monitoring
- `schedule` module – Task scheduling
- `os` module – File operations
- `time` module – Timestamp generation
- Command-line arguments

## Dependencies

```bash
pip install psutil schedule
```

## Learning Path

- Start with `ProcessorloggerCommandLine.py` for CLI basics
- Learn `Processorloggerlogfile.py` for directory management
- Progress to `ProcessorloggerlogfileTimeStamp.py` for timestamped logs
- Master `CPULOG.py` for CPU monitoring
- Practice `MemoryLog.py` for memory monitoring
- Learn `Diskusage.py` for disk monitoring
- Advance to `DiskusageException.py` for exception handling
- Master `ProcessLoggerwithsysteminfo.py` for complete system monitoring

## Notes

- `psutil` provides access to system resource information
- Log files should be stored in an accessible directory
- Timestamps use system time for logging operations
- Disk partitions may vary depending on the operating system
- Network statistics track cumulative data sent and received
- Exception handling prevents crashes on restricted partitions
- The `schedule` module requires continuous loop execution
- CPU usage percentage can fluctuate based on system load

## Author

- **Ishwari Vijaykumar Surve**
