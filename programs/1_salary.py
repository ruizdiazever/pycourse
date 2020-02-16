# REMUNERACION ASIGNADA
print("\nBienvenido")
while(True):
    try:
        salario = float(input("Ingrese su salario: "))
        # PLUS
        monto_plus_des = 0
        plus = input("Posee algun plus? ")
        if (plus == "si") or (plus == "Si") or (plus == "SI"):
            monto_plus = float(input("Ingrese el monto del plus: "))
            # EXENTO
            plus = input("El plus esta exenta de descuentos? ")
            if (plus == "si") or (plus == "Si") or (plus == "SI"):
                monto_plus = monto_plus
            else:
                monto_plus_des = monto_plus 
        else:
            monto_plus = 0
    except ValueError:
        print("Error! Ha introducido una cadena de texto.")
    except Exception as e:
        print(type(e).__name__)
    else:
        print("Ingresado correctamente.")
        break




# REMUNERACIONES
antiguedad = (salario * 1) / 100
presentismo = ((salario + antiguedad) * 8.33) / 100
bruto = salario + antiguedad + presentismo + monto_plus_des

# DESCUENTOS
jubilacion = (bruto * 11) / 100
ley_19032 = (bruto * 3) / 100
obra_social = (bruto * 3) / 100
sec = (bruto * 2) / 100
faecys = (bruto * 0.5) / 100
descuentos = jubilacion + ley_19032 + obra_social + sec + faecys + monto_plus_des

# NETO
neto = (bruto + monto_plus) - descuentos
print("\n")
print("Monto plus: {:.2f}".format(monto_plus))
print("Monto plus descontado: {:.2f}".format(monto_plus_des),"\n")
print("Jubilacion: {:.2f}".format(jubilacion))
print("Ley 19032: {:.2f}".format(ley_19032))
print("Obra Social: {:.2f}".format(obra_social))
print("S.E.C.: {:.2f}".format(sec))
print("F.A.E.C.Y.S.: {:.2f}".format(faecys), "\n")
print("Descuentos: {:.2f}".format(descuentos), "\n")
print("Su sueldo bruto es: {:.2f}".format(bruto))
print("Su salario neto es: {:.2f}".format(neto))