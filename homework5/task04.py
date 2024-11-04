filename = input("enter file name: ")
n = int (input("enter last n numbers to read: "))

file = open("demo.txt", "r")
line_count = sum(1 for line in file)
file.close()
file = open("demo.txt", "r")

for i in range (line_count-n):
    line = file.readline()
    
for j in range (n+1):
    line = file.readline()
    print (line, end = "")
file.close()  
