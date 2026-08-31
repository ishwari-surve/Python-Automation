# Automated Platform Surveillance System
# - Complete Final Version

import psutil
import sys
import os
import time 
import schedule

# ============================================================
# FUNCTION 1: ProcessScan()
# Scans all running processes and collects their details
# ============================================================
def ProcessScan():
    
    Data = []

    # Step A: Warm-up CPU percent (first call starts measurement)
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    # Small delay so second call gives accurate CPU %
    time.sleep(0.2)

    # Step B: Scan all processes and collect info
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username", "status", "create_time"])

            # Step C: Convert create_time (epoch) to readable date-time
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"

            # Step D: Get CPU% and Memory%
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            Data.append(info)

        # Step E: Handle common process exceptions
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return Data


# ============================================================
# FUNCTION 2: CreateLog(FolderName)
# Main logging function - creates one complete log file
# ============================================================
def CreateLog(FolderName):

    Border = "-" * 50

    # Step A: Check if folder exists
    Ret = os.path.exists(FolderName)

    # Step B: If exists, confirm it is a directory
    if Ret == True:
        Ret = os.path.isdir(FolderName)
        if Ret == False:
            print("Unable to create folder - a file with same name exists")
            return
    else:
        # Step C: If folder doesn't exist, create it
        os.mkdir(FolderName)
        print("Directory for log files created successfully")

    # Step D: Create timestamp-based unique log filename
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "SysAudit_%s.log" % timestamp)
    print("Log file created:", FileName)

    # Step E: Open file in write mode
    fobj = open(FileName, "w")

    # Step F: Write Header
    fobj.write(Border + "\n")
    fobj.write("---- Automated Platform Surveillance System -----\n")
    fobj.write("Log created at : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

    # --------------------------------------------------------
    # SYSTEM REPORT SECTION
    # --------------------------------------------------------
    fobj.write("SYSTEM REPORT\n")
    fobj.write(Border + "\n")

    # CPU Usage
    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())

    # RAM Usage
    mem = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" % mem.percent)

    # Disk Usage for all partitions
    fobj.write("\nDisk Usage Report:\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n" % (part.mountpoint, usage.percent))
        except:
            pass

    # Network Usage
    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage:\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Recv : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))

    fobj.write(Border + "\n\n")

    # --------------------------------------------------------
    # PROCESS REPORT SECTION
    # --------------------------------------------------------
    fobj.write("PROCESS REPORT\n")
    fobj.write(Border + "\n")

    Data = ProcessScan()

    for info in Data:
        fobj.write("PID          : %s\n" % info.get("pid"))
        fobj.write("Name         : %s\n" % info.get("name"))
        fobj.write("Username     : %s\n" % info.get("username"))
        fobj.write("Status       : %s\n" % info.get("status"))
        fobj.write("Start Time   : %s\n" % info.get("create_time"))
        fobj.write("CPU %%        : %s\n" % info.get("cpu_percent"))
        fobj.write("Memory %%     : %s\n" % info.get("memory_percent"))
        fobj.write(Border + "\n")

    fobj.write("\nEnd of Log File\n")
    fobj.write(Border + "\n")

    fobj.close()

    print("Log file written successfully!")


# ============================================================
# FUNCTION 3: main()
# Handles CLI arguments and starts scheduling
# ============================================================
def main():

    Border = "-" * 50
    print(Border)
    print("---- Automated Platform Surveillance System -----")
    print(Border)

    # Case 1: Only 1 argument - help or usage
    if len(sys.argv) == 2:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to:")
            print("1. Create automatic system log files periodically")
            print("2. Log CPU, RAM, Disk, Network usage")
            print("3. Log details of all running processes")
            print("4. Store logs with timestamp-based filenames")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Usage:")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : Time in minutes for periodic scheduling")
            print("DirectoryName: Name of folder to store log files")
            print("Example: python surveillance.py 5 SystemLogs")

        else:
            print("Invalid option! Please use --h or --u for help.")

    # Case 2: 2 arguments - actual automation run
    # Example: python surveillance.py 5 SystemLogs
    elif len(sys.argv) == 3:

        print("Time Interval  :", sys.argv[1], "minutes")
        print("Directory Name :", sys.argv[2])

        # Schedule the CreateLog function every N minutes
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print(Border)
        print("Platform Surveillance System Started Successfully!")
        print("Time Interval in minutes :", sys.argv[1])
        print("Press Ctrl + C to Stop")
        print(Border)

        # Infinite loop - keeps running until Ctrl+C
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments!")
        print("Please use --h or --u for help.")

    print(Border)
    print("------ Thank you for using our script --------")
    print(Border)


if __name__ == "__main__":
    main()
