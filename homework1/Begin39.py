from math import sqrt
A = int (input ("A = "))
B = int (input ("B = "))
C = int (input ("C = "))
D = B**2 - 4*A*C
if D>0: #noldan katta bolsa deyilgan ekan
    x1 = -B + sqrt(D)
    x2 = -B - sqrt(D)
    print ( "x1 = ", x1)
    print ( "x2 = ", x2)
else:
    print("D<=0")