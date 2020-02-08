v = "otro texto"
n = 10
s = "\n"
print("Un texto,",v,"y un numero",n)

# Existe lo que se llama "Formateo de escritura de las cadenas de caracteres"

# PRIMER EJEMPLO
c = "Un texto, {} y un numero {}".format(v,n)
print(c)

# SEGUNDO EJEMPLO
name = "Ever"
edad = 27
profesion = "Estudiante de Software"
respuesta = "{} de {} es {}"
print(respuesta.format(name,edad,profesion))

# CUARTO EJEMPLO: cambiar orden
bebe = "Hannah"
mama = "Valentina"
print("{1} es una bebe hermosa y la mama {0} tambien.".format(mama,bebe)) # El orden esta asignano en el format

# QUINTO EJEMPLO
n2 = 850
p = "clasica"
print("Una poesia '{poesia}' y sus '{antiguedad}' años".format(poesia=p,antiguedad=n2)) # Podemos referenciar tambien alreves

# SEXTO EJEMPO
n3 = 850
print("{n3}, {n3}, {n3}".format(n3=n3))

# TERCER EJEMPLO
""" nombre = input("Introduzca su nombre: ")
old = int(input("Introduzca su edad: "))
ocupacion = input("A que se dedica: ")
answer = "'{}' de '{}' de edad es '{}'"
print(answer.format(nombre,old,ocupacion)) """

# ALINAMIENTO Y TRUNCAMIENTO
print("{:>30}".format("palabra")) # Alineamiento a la derecha en 30 caracteres.
print("{:<30}".format("palabra")) # Alineamiento a la izquierda en 30 caracteres.
print("{:^30}".format("palabra")) # Alineamiento al centro en 30 caracteres.
print("{:.3}".format("palabra")) # Truncamiento a 3 caracteres.
print("{:>30.3}".format("palabra")) # Alineamiento a la derecha en 30 caracteres con truncamiento de 3 caracteres.


# FORMATEO DE NUMEROS ENTEROS, rellenados con espacios
print("{:4d}".format(10)) # d hace referencia a digitos
print("{:4d}".format(100))
print("{:4d}".format(1000))

# Rellenados con ceros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

# FORMATEO DE NUMEROS FLOTANTES
print("{}".format(3.1415926))
print("{:.2f}".format(3.1415926)) # f hace refencia a flotante
print("{:.2f}".format(153.21)) # Lo rellena con 0

# ALINEAR DECIMALES
print("{:7.2f}".format(3.1415926)) # "." punto cuenta como caracter
print("{:7.2f}".format(153.21)) # Lo rellena con 0

# RELLENAR con 0
print("{:07.2f}".format(3.1415926)) # "." punto cuenta como caracter
print("{:07.2f}".format(153.21)) # Lo rellena con 0