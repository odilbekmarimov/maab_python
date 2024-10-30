*list1,=map(int,input("enter the list (separator 'space'): ").split())
size = int (input("enter size of sublist: "))
list2 = []

for i in range (0, len(list1), size):
    list2.append(list1[i:i + size])
    
print(list2)