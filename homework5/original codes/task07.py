filename = input("enter file name: ")
filearray = []
file = open(filename, "r")
for line in file:
    filearray.append(line.strip())
    
print (filearray)
file.close()  
