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
- Start with Schedular1.py for understanding time and datetime basics
- Progress to Schedular4.py for task scheduling automation

## **Notes**
- The schedule module requires a continuous loop to execute scheduled tasks
- Tasks run according to their scheduled intervals
- Use time.sleep() to prevent high CPU usage
- Useful for creating automated maintenance and task execution scripts
