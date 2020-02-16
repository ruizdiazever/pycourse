# Pedir el día, mes & año de una fecha e indicar si la fecha es correcta. Suponiendo que todos los meses de 30 días.
print("Ingrese porfavor la fecha.")

while(True):
    try:
        day = int(input("Ingrese el dia: "))
        month = int(input("Ingrese el mes: "))
        year = int(input("Ingrese el año: "))

        if (day > 0 and day <= 30) and (month > 0 and month <= 12) and (year > 0 and year < 3000):
            print("La fecha ingresada es: {}/{}/{}".format(day,month,year))
        else:
            print("ERROR! Fecha invalida.")

    except ValueError:
        print("ERROR! Introduzca un numero valido.")
    except Exception as e:
        print(type(e).__name__)
    else:
        break





