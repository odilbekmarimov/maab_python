def division (a:float, b:float):
    try:
        print(f"{a} / {b} is {a/b}")
    except ZeroDivisionError:
        print ("Cannot divide to a zero")
        
def getint (a:int):
    try:
        a = int (a)
        return a
    except ValueError:
        print ("invalid value")
     
def fileopening(filename):
    try:
        file = open(filename, 'r')
        print(file.readline()) #first line only
        file.close()
    except FileNotFoundError:
        print("File not found")

def type_error ():
    try:
        a = float (input ("enter a: "))
        b = float (input ("enter b: "))
        return a, b
    except ValueError:
        print ("Wrong input value")

def permission_request (filename):
    try:
        file = open (filename, 'r')
        print (file.read())
        file.close
    except PermissionError:
        print ("You dont have permissions")
        
def itemAtIndex (items, index):
    try:
        print (items[index])
    except IndexError:
        print ("required index is out of range")

def userinterruption(a: list):
    while True:
        
        try:
            b = input("Enter a value: ")
            a.append(b)
            if b == "3":  # Exit condition
                print("Exit")
                break
        except KeyboardInterrupt:
            print("Canceled by user")
            break


def aritherror (a:float, b:float):
    try: 
        print (f"{a} / {b} is {a/b}")
    except ArithmeticError:
        print ("Arithmetic error occured")

def read_file(filename, decoding):
    try:
        file = open(filename, "r", encoding = decoding)
        print (file.read())
        file.close()
    except UnicodeDecodeError:
        print("Error decoding file as {endoding}")

##read_file('demo.txt', "decode")

def listattribute (a:list, b:str):
    try:
        print (getattr(a, b))
    except AttributeError:
        print (f"list does not have attribute called {b}")
#listattribute([1, 2, 3], "append")

    

        