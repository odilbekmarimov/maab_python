def factors(a: int):
    for i in range (1, int(a/2+1)):
        #print(i)
        if a%i==0:
            print(f"{i} is a factor of {a}")
    print (f"{a} is a factor of {a}")    

a = int (input ("Enter a positive integer: "))
while a < 0:
    a = int (input ("Enter a positive integer: "))
    
factors (a)