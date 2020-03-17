from setuptools import setup

setup(
    name="paquete",
    version="0.1",
    description="Este es un paquete ejemplo",
    author="Ever Ruiz Diaz",
    author_name="ruizdiaz.oe@gmail.com",
    url="sinconmasver.pythonanywhere.com",
    scripts=[], # En caso de que contenga y querramos integrarlo, ejemplo: 'script.py'
    packages=["paquete","paquete.adios","paquete.hola"] #  Lo mas importante! Paquete y subpaquete que estamos referenciando.
)

# Para ejecutarlo hay que abrir CMD en la direccion de este archivo y poner el comando:
# 'python setup.py sdist'
# Este comando va a crear una carpeta llamada dist
# Ingresamos en esa carpeta con CMD y despues para su ejecucion con el comando:
# 'pip3 install paquete-0.1.tar'
# 'pip install paquete-0.1.tar.gz' si el otro no funcion, prestar atencion a la extension del archivo.

# Para desinstalar paquete:
# 'pip uninstall paquete'