*list1,=map(int,input("enter the list (separator 'space'): ").split())
is_sorted = True

for i in range (len(list1)-1):
    if list1[i]>list1[i+1]:
        is_sorted = False
        break

print(is_sorted)