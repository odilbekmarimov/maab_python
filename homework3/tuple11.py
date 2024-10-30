tuple1 = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
check = int (input("check: "))
for i in range (len(tuple1)):
    if tuple1[i]==check:
        print("at index:", i)
print("\nover")