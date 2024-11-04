filename = input ("enter filename: ")
file = open(filename, "a")
line = "A"
while line != "break":
    line = input ("input line to append ('break' to break): ")
    if line == "break":
        break
    file.write(line + "\n")
file.close()
file = open(filename, "r")
print(file.read())
file.close()
