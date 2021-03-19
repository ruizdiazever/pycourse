class Machine:
    def __init__(self, type):
        self.type = type
        

class Car(Machine):
    def __init__(self, type, brand, model, year):
        self.type = type
        self.brand = brand
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"The {self.type} is a {self.brand}, model {self.model} of {self.year} year."

c = Car('Car', 'Tesla', 'S', '2021')

print(c)