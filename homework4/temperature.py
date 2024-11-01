
def convert_far_to_cel(f:float):
    c = "{:.2f}".format((f - 32 ) * 5 / 9)
    return c
def convert_cel_to_far(C:float):
    F = "{:.2f}".format(C * 9 / 5 + 32)
    return F

f =  float (input ("Enter a temperature in degrees F: "))
print (f"{f} degrees F = {convert_far_to_cel(f)} degrees C","\n")

C = float (input ("Enter a temperature in degrees C: "))
print(f"{C} degrees in C = {convert_cel_to_far(C)} degrees F")
