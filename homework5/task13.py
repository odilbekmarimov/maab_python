list1 = []
filename = input ("original filename: ")
file = open(filename, "r")
for line in filename:
    list1.append(file.readline())
file.close()

filename = input("new file name: ")
file = open(filename, "w")
for i in range (len(list1)):
    file.write(list1[i])
file.close()


file = open(filename, "r")

print(file.read())
print(list1)