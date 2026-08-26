def main():
    fobj = None

    try:
        fobj=open("Hello.txt","a")
        print("Filesngets successfully opened")

        fobj.write("Python Automation")

        fobj.close()

    except FileNotFoundError:
        print("Unable to oprn file as there is no such file")

    
    finally:
        print("End of application")
        



if __name__=="__main__":
    main()