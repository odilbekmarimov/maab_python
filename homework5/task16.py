filename = input ("filename: ")
file = open(filename, "r")
if file.closed:
    print("closed")
else:
    print("not closed")