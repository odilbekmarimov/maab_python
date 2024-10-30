from copy import copy
*list1,=map(int,input("enter the list (separator 'space'): ").split())
*list2,=map(int,input("enter the list (separator 'space'): ").split())

list3 = list1 + list2
list3.sort()
print(list3)

#v2

list4 = copy(list1)
list4.extend(list2)
list4.sort()
print(list4)