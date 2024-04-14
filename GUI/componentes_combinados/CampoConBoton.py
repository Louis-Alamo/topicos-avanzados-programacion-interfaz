from GUI.componentes_graficos.JEntry import JEntry
from GUI.componentes_graficos.JButton import JButton
from tkinter import *


class CampoConBoton(Frame):
    """
    Clase que representa un componente que combina un campo de entrada y un botón.

    Args:
        master: El widget padre al que pertenece este componente.
        nombre_boton (str): El texto que se mostrará en el botón.
        funcion (callable): La función que se llamará cuando se haga clic en el botón.

    Attributes:
        master: El widget padre al que pertenece este componente.
        _campo (JEntry): El campo de entrada asociado a este componente.
        _boton (JButton): El botón asociado a este componente.

    """

    def __init__(self, master, nombre_boton, funcion):
        """
        Inicializa un nuevo CampoConBoton.

        Args:
            master: El widget padre al que pertenece este componente.
            nombre_boton (str): El texto que se mostrará en el botón.
            funcion (callable): La función que se llamará cuando se haga clic en el botón.

        """
        super().__init__(master=master)

        # Configura las propiedades del componente
        self.configure(bg="#ffffff")

        # Crea el campo de entrada
        self._campo = JEntry(self)
        self._campo.pack(side='left', expand=True, fill=X, padx=10)

        # Crea el botón
        self._boton = JButton(self, nombre_boton=nombre_boton, funcion=funcion)
        self._boton.pack(side='right', padx=10, expand=True)

    def obtener_texto(self):
        """
        Obtiene el texto ingresado en el campo de entrada.

        Returns:
            str: El texto ingresado en el campo de entrada.
        """
        return self._campo.obtener_texto()
