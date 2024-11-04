filename = input("enter file name: ")
filelist = []
file = open(filename, "r")
for line in file:
    filelist.append(line.strip())
    
print (filelist)
file.close()  
