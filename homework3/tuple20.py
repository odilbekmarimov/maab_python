tuple1 = (5, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 0)
size = int(input("Enter the size: "))
tuple2 = ()

for i in range(0, len(tuple1), size):
    subtuple = tuple1[i:i + size]
    tuple2 += (subtuple,)

print( tuple2)
