import os

def main():
    FileName= input("Enter the name of file:")
    
    if(os.path.exists(FileName)):
        Ret = os.path.isabs(FileName)

        os.remove(FileName)
        print("File gets delete")
        
    else:
        print("There is no such file")

if __name__=="__main__":
    main()