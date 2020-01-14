while True:
    try:
        x= int(input("Enter a value"))
        break
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("keybopard interrupt")
    finally:
        print("Terminating program")


#Accessing error messege

a,b=map(int,input('Enter two integers :').split())
try:
    res=a/b
    print("res is {}".format(res))
except Exception as e:
    print("error occured {}".format(e))
finally:
    pass
