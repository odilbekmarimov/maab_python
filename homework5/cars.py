class Car:
    def __init__(self, year_model, make):
        self.year_model = year_model  
        self.make = make              
        self.speed = 0                

    def accelerate(self):
        self.speed += 5
                       
    def brake(self):
        self.speed -= 5               
        if self.speed < 0:            
            self.speed = 0

def main():
    
    my_car = Car(2024, "chevy")

   
    print("Accelerating:")
    for i in range(5):
        my_car.accelerate()
        print(f"speed: {my_car.speed} km/h")

    print("Braking:")
    for i in range(5):
        my_car.brake()
        print(f"speed: {my_car.speed} km/h")
        
main()
