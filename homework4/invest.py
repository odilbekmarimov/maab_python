def invest(amount:float, rate:float, years:int):
    print ("\n")
    sum = amount
    for i in range (years):
        multiplier = 1 + rate
        sum = sum * multiplier

        print (f"year {i+1}: ${'{:.2f}'.format(sum)}")
    print("\n")
    
    
    
amount = float (input ("Enter initial amount of money: "))
rate = float (input ("Enter value of rate (in format 0.{rate}): "))
years = int (input ("Enter number of years: "))

invest(amount, rate, years)
