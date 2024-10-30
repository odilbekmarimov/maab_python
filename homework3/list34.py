*list1,=map(int,input("enter the list (separator 'space'): ").split())
list2 = []
for i in range (len(list1)-1):
    list2.append(list1[i+1])
list2.append(list1[0])
print(list2)