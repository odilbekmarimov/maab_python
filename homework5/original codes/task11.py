import os
file = (input("filename: "))
statinfo = os.stat(file)
print (statinfo.st_size, " bytes" )