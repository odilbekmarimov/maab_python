a1 = int ( input ("a1 = "))
b1 = int ( input ("b1 = "))
c1 = int ( input ("c1 = "))


a2 = int ( input ("a2 = "))
b2 = int ( input ("b2 = "))
c2 = int ( input ("c2 = "))

d = a1 * b2 - b1 * a2

x = (c1*b2 - c2*b1) / d
y = (a1*c2 - a2*c1) / d

print("x = ", x)
print("y = ", y)