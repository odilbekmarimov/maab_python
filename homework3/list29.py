*list1,=map(int,input("enter the list (separator 'space'): ").split())
index = int(input("enter index to remove: "))

if(len(list1)>index): 
    list1.pop(index)

print(list1)

#v2

if -1 < index < len(list1):
    list2 = []
    for i in range(len(list1)):
        if i != index:
            list2.append(list1[i])
    
    print(list2)
