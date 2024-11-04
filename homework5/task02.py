filename = input ("enter filename: ")
n = int (input("enter number of lines: "))
file = open(filename, "r")
line = file.readline()
for i in range (n):
    if not line:
        print("\nfile ended")
        break
    print (line, end = "")
    line = file.readline()
file.close()  

