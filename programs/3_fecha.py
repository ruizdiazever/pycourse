# Pedir el día, mes & año de una fecha e indicar si la fecha es correcta. Suponiendo que todos los meses de 30 días.
print("Ingrese porfavor la fecha.")

try:
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    year = int(input("Ingrese el año: "))

        # DIA
    while (True):
        if dia > 0 and dia < 30:
            break
        else:
            dia = int(input("Error! Ingrese el dia correctamente: "))
    # MES
    while (True):
        if mes > 0 and mes <= 12:
            break
        else:
            mes = int(input("Error! Ingrese el mes correctamente: "))
    # AÑO
    while (True):
        if year > 0 and year < 3000:
            break
        else:
            year = int(input("Error! Ingrese el año correctamente: "))
    print("La fecha ingresada es {}/{}/{}".format(dia, mes, year))
except Exception as e:
    print("ERROR!")
    print(type(e).__name__)




