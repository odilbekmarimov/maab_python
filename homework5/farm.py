class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."
    
    def display_info(self):
        return f"{self.name} is a {self.age} years old {self.species}."

    

class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age, "Cow")
        self.milk_production = milk_production

    def grazing(self):
        return f"{self.name} is grazing."


class Sheep(Animal):
    def __init__(self, name, age, wool_amount):
        super().__init__(name, age, "Sheep")
        self.wool_amount = wool_amount

    def shear(self):
        return f"{self.name} gave {self.wool_amount} kg of wool."


class Chicken(Animal):
    def __init__(self, name, age, egg_production):
        super().__init__(name, age, "Chicken")
        self.egg_production = egg_production

    def sleep(self):
        return f"{self.name} is sleeping."

    def lay_egg(self):
        return f"{self.name} laid {self.egg_production} eggs this week."
    
bessy = Cow(name="mol", age=5, milk_production=25.0)
dolly = Sheep(name="qoy", age=3, wool_amount=5.0)
hen = Chicken(name="tovuq", age=2, egg_production=6)

print(bessy.eat())
print(dolly.shear())
print(hen.lay_egg())

