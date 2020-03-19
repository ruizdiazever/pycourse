import datetime

# 1, creamos un objeto datetime
dt = datetime.datetime.now()    # ahora
print("1.   ", dt)              # todo
print("2.   ", dt.year)         # año
print("2.   ", dt.month)        # mes
print("2.   ", dt.day)          # dia
print("2.   ", dt.hour)         # hora
print("2.   ", dt.minute)       # minuto
print("2.   ", dt.second)       # segundo
print("2.   ", dt.microsecond)  # microsegundos

# 2, zona horaria
print("2.   ", dt.tzinfo)

# 3, ejemplo de uso..
print("3.    La hora es: {}:{}:{}".format(dt.hour,dt.minute,dt.second))
print("3.    La fecha es: {}/{}/{}".format(dt.day,dt.month,dt.year))

# 4, fecha de manera manual
dt_2 = datetime.datetime(2000,1,1) # creamos la fecha
print("4.   ", dt_2)

# 4.1, podemos reemplazar de forma manual
dt_2 = dt_2.replace(year=3000)
print("4.   ", dt_2)

# 5, formateos
dt_3 = datetime.datetime.now()
dt_3 = dt_3.isoformat()
print("5.   ", dt_3)

# 6, formateo personal: en el link de abajo hay codigos para el formateo, va dentro del parametro.
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
dt_4 = datetime.datetime.now()
dt_4 = dt_4.strftime("%A %d %B %Y %I:%M")
print("6.   ", dt_4)

# 7, modulo de idioma, llamado locale
# https://www.science.co.il/language/Locale-codes.php
# https://docs.microsoft.com/es-es/cpp/c-runtime-library/language-strings?view=vs-2019
import locale
locale.setlocale(locale.LC_ALL, 'es-AR') # ejemplo
print("7.   ", locale.setlocale(locale.LC_ALL, 'es-es'))
print("7.   ", locale.setlocale(locale.LC_ALL, '')) # Si dejamos en vacio va a utilizar el lenguaje de la maquina

# 8, modulo de idioma, caso de uso real
locale.setlocale(locale.LC_ALL, 'es')
dt_5 = datetime.datetime.now()
dt_5 = dt_5.strftime("%A %d %B %Y %I:%M")
print("8.   ", dt_5)

locale.setlocale(locale.LC_ALL, 'zh-CN')
dt_6 = datetime.datetime.now()
dt_6 = dt_6.strftime("%A %d %B %Y %I:%M")
print("8.   ", dt_6, "esto seria una hora en chino simplificado.")

# 9, modulo de idioma, personalizado
locale.setlocale(locale.LC_ALL, 'es-AR')
dt_7 = datetime.datetime.now()
dt_7 = dt_7.strftime("%A %d de %B del %Y - %H:%M")
print("9.   ", dt_7)

# 10, suma de tiempos, IMPORTANTE
t = datetime.timedelta(days=14, hours=4, seconds=1000)
dentro_de_dos_semanas = dt + t
print("10.  ", dentro_de_dos_semanas)
print("10.  ", dentro_de_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))

# 11, zonas horarias, vamos a usar un modulo extra llamado: pytz
# Se instala a travez de terminal: pip install pytz
import pytz
print(pytz.all_timezones)
time_roma = datetime.datetime.now(pytz.timezone('Europe/Rome'))
print("11.  En Roma, Italia es", time_roma.strftime("%A %d de %B del %Y - %H:%M"))
