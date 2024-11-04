file = open("new.txt", "w")
n = int(input("n: "))
for i in range (65, 65+26):
    for j in range (n):
        file.write(chr(i))
    file.write("\n")
file.close()
file = open("new.txt", "r")
print(file.read())