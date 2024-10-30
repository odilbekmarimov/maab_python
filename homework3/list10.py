*list1,=map(int,input("enter the list (separator 'space'): ").split())
list1.sort()
list2 = []
for i in range(0,len(list1)):
    list2.append(list1[i])
print(list2)