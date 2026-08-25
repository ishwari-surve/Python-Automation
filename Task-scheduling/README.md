# Task Scheduling

## **About**
- Collection of Python programs demonstrating time, datetime, and task scheduling
- Uses the time, datetime, and schedule modules
- Foundation for building automated task execution systems

## **Purpose**
- Learn and practice working with time and datetime in Python
- Understand how to schedule tasks at regular intervals
- Build automation systems that run tasks automatically

## **Programs Included**

**1. Schedular1.py**
- Demonstrates time module basics
- Displays current timestamp using time.time()
- Shows human-readable time format using time.ctime()
- Displays current datetime using datetime.datetime.now()

## **Schedular2.py**
-Implements basic task scheduling automation
-Schedules function execution at 20-second intervals
-Uses schedule module for task management
-Runs tasks in an infinite loop

## **Schedular3.py**
- Advanced task scheduling with continuous execution
- Executes functions at fixed time intervals
- Demonstrates loop-based task runner
- Real-time task monitoring and execution

**2. Schedular4.py**
- Implements task scheduling automation
- Schedules functions to run at specific intervals
- Runs tasks every minute and every hour
- Uses an infinite loop to continuously check scheduled tasks
  
## **How to Run**

**Schedular1.py**
```bash
python Schedular1.py
```

**Schedular2.py**
```bash
python Schedular2.py
```
**Schedular3.py**
```bash
python Schedular3.py
```
**Schedular4.py**
```bash
python Schedular4.py
```

## **Key Concepts**
- time.time(): Returns current time in seconds since the epoch
- time.ctime(): Converts time into a human-readable format
- datetime.datetime.now(): Gets the current date and time object
- schedule.every(): Sets up recurring task schedules
- schedule.run_pending(): Checks and runs scheduled tasks
- Task Intervals: Supports minutes, hours, days, and weeks for scheduling

## **Technologies Used**
- Python 3.x
- time module (built-in)
- datetime module (built-in)
- schedule module (third-party)

## **Dependencies**
- pip install schedule
  
## **Learning Path**
- Start with Schedular1.py (time and datetime basics)
- Progress to Schedular2.py (basic task scheduling)
- Learn Schedular3.py (continuous task execution)
- Master Schedular4.py (multiple interval scheduling)

## **Notes**
- The schedule module requires a continuous loop to execute scheduled tasks
- Tasks run according to their scheduled intervals
- Use time.sleep() to prevent high CPU usage
- Useful for creating automated maintenance and task execution scripts
