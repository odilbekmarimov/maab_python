*list1,=map(int,input("enter the list (separator 'space'): ").split())
counter = 0
for i in range (0, len(list1)):
    if (i+1)%2!=0:
        counter+=1
        
print (counter)