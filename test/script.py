class Persona:
    def __init__(self, name, email, edad):
        self.name = name
        self.email = email
        self.edad = edad

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nEdad: {self.edad}"

ever = Persona("Ever", "ruizdiaz.oe@gmail.com", 27)
ever.edad = 28

print(ever)