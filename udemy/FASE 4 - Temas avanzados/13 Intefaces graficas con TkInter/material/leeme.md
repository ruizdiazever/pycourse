Widgets en Tkinter
    Representan los componentes graficos en las interfaces y se gestionan formando jerarquias.

    - Tk        - Radiobutton
    - Frame     - Checkbutton
    - Label     - Menu
    - Entry     - Boxes
    - Text      - Dialogs
    - Button

El módulo Tkinter cuenta con una serie de componentes gráficos llamados Widgets, gracias a los cuales podemos diseñar nuestras interfaces.

Los widgets deben seguir una jerarquía a la hora de añadirse a la interfaz. Por ejemplo, un Marco (frame) forma parte del objeto raíz Tk. Y a su vez, un botón (button) puede formar parte de un contenedor como la raíz o un marco.

Los que veremos en esta introducción a Tkinter son:

    -   Tk: Contenedor base o raíz de todos los widgets que forman la interfaz. No tiene tamaño propio sino que se adapta a los widgets que contiene.

    -   Frame: Marco contenedor de otros widgets. Puede tener tamaño propio y posicionarse en distintos lugares de otro contenedor (ya sea la raíz u otro marco).

    -   Label: Etiqueta dónde podemos mostrar algún texto estático.

    -   Entry: Campo de texto sencillo para escribir texto corto. Nombres, apellidos, números.

    -   Text: Campo de texto multilínea para escribir texto largo. Descripciones, comentarios.

    -   Button: Botón con un texto sobre el cual el usuario puede hacer clic.

    -   Radiobutton: Botón radial que se usa en conjunto donde es posible marcar una opción.

    -   Checkbutton: Botón cuadrado que se puede marcar con un tic.

    -   Menu: Estructura de botones centrados en la composición de menús superiores.

    -   Dialogs: Ventanas emergentes que permiten desde mostrar información al usuario (típico mensaje de alerta o de confirmación) hasta ofrecer una forma gráfica de interactuar con el sistema operativo (seleccionar un fichero de un directorio para abrirlo).

    -   Hay otros widgets, pero estos son los más importantes.