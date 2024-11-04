filename = input("Enter filename: ")
file = open(filename, "r")

current_line = "" 

for line in file:
    current_line = line.strip() 
    print(current_line)

print("End")
file.close()  