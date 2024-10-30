#Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements
*list1,=map(int,input("enter the list (separator 'space'): ").split())
if len(list1)%2==0:
    print(list1[int(len(list1)/2-1)], ', ', list1[int(len(list1)//2)])
else :
    print(list1[int(len(list1)/2)])