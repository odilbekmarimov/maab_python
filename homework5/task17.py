list1 = []
filename = "demo.txt"

with open(filename, 'r') as file:
    for line in file:
        list1.append(line.strip())  

print(list1)
