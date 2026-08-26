def main():
    fobj = None

    try:
        fobj=open("Hello.txt","w")
        print("Filesngets successfully opened")

        fobj.write("Jay Ganesh Marvellous....")

        fobj.close()

    except FileNotFoundError:
        print("Unable to oprn file as there is no such file")

    
    finally:
        print("End of application")
        



if __name__=="__main__":
    main()