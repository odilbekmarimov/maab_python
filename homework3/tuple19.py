tuple1 = (5, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 0)
num = int(input("enter a number: "))

b = list(tuple1)

if num in b:
    b.pop(b.index(num))
else:
    print("no number")

b = tuple(b)
print( b)
