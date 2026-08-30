#Command line input

import psutil
import sys
import os 
import time
import schedule

def Createlog(FolderName):
   
   Ret = False

   Ret = os.path.exists(FolderName)

   if(Ret == True):
      Ret = os.path.isdir(FolderName )
      if(Ret == False):
         print("Unable to create folder")
         return
   else:
      os.mkdir(FolderName)
      print("Directory for log files gets created successfully")
   
   timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
   FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
   print("Log file gets created with name:",FileName)

   fobj = open(FileName,"w")

 



   if not os.path.exists(FolderName):
      os.mkdir(FolderName)

def main():
  Border = "-"*50
  print(Border)
  print("-------Marvellous Platform Surveillance System------")
  print(Border)

  if (len(sys.argv)==2):
     if(sys.argv[1]=="--h"or sys.argv[1]=="--H"):
        print("This script is used to ")
        print("T1:Create automatic logs ")
        print("2: Executes periodically")
        print("3: Sends mail information with the log")
        print("4: Store information about processess")
        print("5: Store information about CPU")
        print("6: Store information about RAM usage")
        print("7: Store information about secondary storage")


     elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
        print("Use the automation script as")
        print("ScriptName.py TimeInterval DirectoryName")
        print("TimeInterval: The time in minutes for periodic scheduling")
        print("DirectoryName: Name of directory to cretae auto logs")

     else:
      print("Unable to process as there is no such option")
      print("Please use --h or --u to get more details")
  
  elif(len(sys.argv)==3):
    print("Inside projects logic")
    print("Time interval:",sys.argv[1])
    print("Directory name:",sys.argv[2])
   
   #Apply the scheduler
    schedule.every(int(sys.argv[1])).minutes.do(Createlog,sys.argv[2])

    print("Platform Surveillance System started successfully")
    print("Directory created with name:",sys.argv[2])
    print("Time interval in minutes : ",sys.argv[1])
    print("Press Ctrl + C to Stop the execution")


    #Wait till abort
    while True:
       schedule.run_pending()
       time.sleep(1)
                                                                   


  else:
    print("Invalid number of command line arguments")
    print("Unable to process as there is no such option")
    print("Please use --h or --u to get more details")
    
  

  print(Border)
  print("------Thank you for usimg our script--------")
  print(Border)

if __name__ =="__main__":
    main()
