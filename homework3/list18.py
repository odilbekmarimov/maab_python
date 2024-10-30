*list1,=map(int,input("enter the list (separator 'space'): ").split())
*list2,=map(int,input("enter the sublist (separator 'space'): ").split())
contains = False
for i in range (1+len(list1)-len(list2)):
    if list1[i : i + len(list2)]==list2:
        contains = True
print (contains)