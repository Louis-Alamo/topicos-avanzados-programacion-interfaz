from GUI.componentes_graficos.JEntry import JEntry
from GUI.componentes_graficos.JLabel import JLabel
from tkinter import *


class CampoConTitulo(Frame):
    """
    Clase que representa un componente que combina un campo de entrada y una etiqueta.

    Args:
        master: El widget padre al que pertenece este componente.
        texto (str): El texto que se mostrará en la etiqueta.
        posicion (str): La posición relativa del campo de entrada con respecto a la etiqueta ('up', 'left', 'right', 'down').

    Attributes:
        master: El widget padre al que pertenece este componente.
        _etiqueta (JLabel): La etiqueta asociada a este componente.
        _campo (JEntry): El campo de entrada asociado a este componente.

    """

    def __init__(self, master, texto, posicion=None):
        """
        Inicializa un nuevo CampoConTitulo.

        Args:
            master: El widget padre al que pertenece este componente.
            texto (str): El texto que se mostrará en la etiqueta.
            posicion (str): La posición relativa del campo de entrada con respecto a la etiqueta ('up', 'left', 'right', 'down').

        """
        super().__init__(master=master)

        # Configura las propiedades del componente
        self.configure(bg="#ffffff")

        # Crea la etiqueta y el campo de entrada
        self._etiqueta = JLabel(self, texto=texto)
        self._campo = JEntry(self)

        # Determina la posición relativa del campo de entrada con respecto a la etiqueta
        if posicion == None or posicion == "up":
            self._etiqueta.pack(fill=X, expand=True)
            self._campo.pack(fill=X, expand=True)

        elif posicion == 'left':
            self._etiqueta.pack(side='left', expand=True,padx=10)
            self._campo.pack(side='right', fill=X, expand=True)

        elif posicion == 'right':
            self._etiqueta.pack(side='right', expand=True,padx=10)
            self._campo.pack(side='left', fill=X, expand=True)

        elif posicion == 'down':
            self._campo.pack(fill=X, expand=True)
            self._etiqueta.pack(fill=X, expand=True)

        else:
            self._etiqueta.pack(fill=X, expand=True)
            self._campo.pack(fill=X, expand=True)

    def obtener_texto(self):
        """
        Obtiene el texto ingresado en el campo de entrada.

        Returns:
            str: El texto ingresado en el campo de entrada.
        """
        return self._campo.obtener_texto()

    def insertar_texto(self, texto):
        """
        Muestra el texto especificado en el campo de entrada.

        Args:
            texto (str): El texto que se mostrará en el campo de entrada.
        """
        self._campo.mostrar_texto(texto)
