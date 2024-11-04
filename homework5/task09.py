filename = input("enter file name: ")

file = open("demo.txt", "r")
line_count = sum(1 for line in file)
file.close()
print (line_count)