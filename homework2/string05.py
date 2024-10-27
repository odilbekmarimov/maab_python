a = input("enter a string: ")
print(f"{a} is palyndrome" if a == a[::-1] else "not palyndrome")