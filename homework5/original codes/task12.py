filename = input ("enter filename: ")
*list1,=map(str, input("enter the list (separator 'space'): ").split())
file = open (filename, "a")


for i in range (len(list1)-1):
    file.write(list1[i] + "\n")
file.write(list1[len(list1)-1])


print (list1)
file.close()
file = open (filename, "r")
print(file.read())