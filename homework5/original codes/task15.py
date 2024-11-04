import random
filename = input("input filename: ")
with open(filename, 'r') as file:
    lines = file.readlines()
    if lines:
        print(random.choice(lines).strip())
    else:
        print("out of range")