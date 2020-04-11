while(True):
    try:
        n = float(input("Introduzca un numero: "))
        5/n
        break
    
    except TypeError:
        print("No se puede dividir un numero por una cadena.")

    except ValueError:
        print("No se puede dividir una cadena.")

    except ZeroDivisionError:
        print("No se puede dividir un numero por 0.")

    except Exception as e:
        print("Error")
        print(type(e).__name__)