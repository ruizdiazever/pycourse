# REMUNERACION ASIGNADA
print("\n")
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

# REMUNERACIONES
antiguedad = 324.41
presentismo = 2729.39
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
print("Monto plus: ", monto_plus)
print("Monto plus descontado: ", monto_plus_des,"\n")

print("Jubilacion: ",jubilacion)
print("Ley 19032: ", ley_19032)
print("Obra Social: ", obra_social)
print("S.E.C.: ",sec)
print("F.A.E.C.Y.S.: ", faecys, "\n")

print("Descuentos: ",descuentos)
print("Su sueldo bruto es: ",bruto)
print("Su salario neto es:", neto, "\n")