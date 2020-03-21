import datetime
import time
import os


while(True):
    os.system('cls') # Esta funcion de 'os' limpia el terminal
    tiempo = datetime.datetime.now()
    print("La hora es {}:{}:{}".format(tiempo.hour, tiempo.minute, tiempo.second))
    time.sleep(1) # Esta funcion del modulo 'time' frena por segundos determinados la siguiente linea..