def main():
    try:
        open("Demo.txt")
        print("Filesngets successfully opened")
    except FileNotFoundError:
        print("Unable to oprn file as there is no such file")

    
    finally:
        print("End of application")



if __name__=="__main__":
    main()