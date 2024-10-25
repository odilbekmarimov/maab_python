import math
x1 = float (input ("enter first x coordinate: "))
y1 = float (input ("enter first y coordinate: "))
x2 = float (input ("enter second x coordinate: "))
y2 = float (input ("enter second y coordinate: "))
x3 = float (input ("enter third x coordinate: "))
y3 = float (input ("enter third y coordinate: "))
a = ((x1-x2)**2+(y1-y2)**2)**0.5
b = ((x1-x3)**2+(y1-y3)**2)**0.5
c = ((x2-x3)**2+(y2-y3)**2)**0.5
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-c)*(p-b))
print("area is: ", s)