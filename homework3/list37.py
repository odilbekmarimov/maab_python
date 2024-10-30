*list1,=map(int,input("enter the list (separator 'space'): ").split())
sum = 0
for i in range (len(list1)):
    if list1[i]<0:
        sum += list1[i]
print(sum)