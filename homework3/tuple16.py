tuple1 = (5, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 0)
sorted = True
for i in range(len(tuple1)-1):
    if tuple1[i]>tuple1[i+1]:
        sorted = False
        break
print(sorted)