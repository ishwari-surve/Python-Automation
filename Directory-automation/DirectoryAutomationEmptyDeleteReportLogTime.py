import sys
import os
import time

 
def DirectoryScanner(DirName = "Marvellous"):
        Border = "-"*50
        timestamp = time.ctime()

        fobj = open ("Marvellous.log","w")

        fobj.write(Border+"\n")
        fobj.write("This is a log file created by Marvellous Automation\n")
        fobj.write("This is a Directory Cleaner Script\n")
        fobj.write((Border+"\n"))


        Ret = False

        Ret = os.path.exists(DirName)
        if(Ret == False):
         print("There is no such directory")
        return
    
        Ret = os.path.isdir(DirName)
        if(Ret == False):
          print("It is not a directory")
        return 
    
        FileCount = 0
        EmptyFileCount = 0

        for FolderName,SubFolder,FileName in os.walk(DirName):
        

            for fname in FileName:
                FileCount = FileCount + 1

            fname = os.path.join(FolderName,fname)
            print("File name :",fname)
            print("File sixe :",os.path.getsize(fname))   #Path issue

            if(os.path.getsize(fname)==0):
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)

        
        fobj.write("Totalempty files found:"+str(EmptyFileCount)+"\n")
        fobj.write("Total files scanned:",str(FileCount)+"\n")
        fobj.write("This log file generated")
        

def main():

    print(Border)
    print("-------Marvellous Directory Automation------------")
    print(Border)

    if(len(sys.argv)!=2):
        print("Invalid Number of arguments")
        print("Please specify the name of directory")
        return

    DirectoryScanner(sys.argv[1])
    print(Border)
    print("-------Marvellous Directory Automation------------")
    print(Border)

if __name__ == "__main__":
    main()
