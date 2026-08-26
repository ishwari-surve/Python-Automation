def main():
    fobj = None

    try: 
        fobj=open("Hello.txt","r")
        print("Filesngets successfully opened")

        Data = fobj.read()

        print("Data from file is:",Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to oprn file as there is no such file")

    
    finally:
        print("End of application")
        



if __name__=="__main__":
    main()
