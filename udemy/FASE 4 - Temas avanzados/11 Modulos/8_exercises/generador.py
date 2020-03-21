import random
import math

""" def leer_numero(inicio, fin, mensaje):
    print("=============================")
    num = int(input("Ingrese un numero: "))

    while num < inicio or num > fin:
        print("Incorrecto, debe introducir un numero dentro de los parametros de la funcion.")
        num = int(input("Ingrese un numero: "))
    else:
        print("Frase ingresado:", mensaje)
        print("Numero ingresado: ", num)
        print("=============================") """

def leer_numero(inicio,fin,mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except:
            pass
        else:
            if valor >= inicio and valor <= fin:
                break
    return valor


def generador():
    numeros = leer_numero(1,20,"¿Cuantos números quieres generar del 1 al 20?\n")
    modo = leer_numero(1,3,"¿Cómo quieres redondear los números? 1: alza, 2: baja, 3: normal\n")

    lista = []

    print("\n")
    for i in range(numeros):
        num = random.uniform(0,101)
        if modo == 1:
            print(i+1,"- {} => {}".format(num, math.ceil(num)))
            num = math.ceil(num)
        elif modo == 2:
            print(i+1, "- {} => {}".format(num, math.floor(num)))
            num = math.floor(num)
        else:
            print(i+1, "- {} => {}".format(num, round(num)))
            num = round(num)
        lista.append(num)
    return lista

generador()