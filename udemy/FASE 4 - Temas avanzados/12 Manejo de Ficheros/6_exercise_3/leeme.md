Ejercicio original en:
    https://docs.hektorprofe.net/python/manejo-de-ficheros/ejercicios/


Utilizando como base el ejercicio de los personajes que hicimos, en este ejercicio tendrás que crear un gestor de personajes gestor.py para añadir y borrar la información de los siguientes personajes:

Argumentos (vida, ataque, defensa, alcance)
    - Caballero (4,2,4,2)
    - Guerrero  (2,4,2,4)
    - Arquero   (2,4,1,8)


Deberás hacer uso del módulo pickle y todos los cambios que realices se irán guardando en un fichero binario personajes.pckl, por lo que aunque cerremos el programa los datos persistirán.

    -   Crea dos clases, una Personaje y otra Gestor.

    -   La clase Personaje deberá permitir crear un personaje con el nombre (que será la clase), y sus propiedades de vida, ataque, defensa y alcance (que deben ser números enteros mayor que cero obligatoriamente).

    -   Por otro lado la clase Gestor deberá incorporar todos los métodos necesarios para añadir personajes, mostrarlos y borrarlos (a partir de su nombre por ejemplo, tendrás que pensar una forma de hacerlo), además de los métodos esenciales para guardar los cambios en el fichero personajes.pckl que se deberían ejecutar automáticamente.

    -   En caso de que el personaje ya exista en el Gestor entonces no se creará.


Una vez lo tengas listo realiza las siguientes prueba en tu código:

    -   Crea los tres personajes de la tabla anterior y añádelos al Gestor.
    -   Muestra los personajes del Gestor.
    -   Borra al Arquero.
    -   Muestra de nuevo el Gestor.