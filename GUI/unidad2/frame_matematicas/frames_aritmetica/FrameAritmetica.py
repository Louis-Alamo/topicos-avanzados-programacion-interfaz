from abc import abstractmethod, ABC
from tkinter import *
from GUI.componentes_combinados.CampoConTitulo import CampoConTitulo
from GUI.componentes_graficos.JButton import JButton
from GUI.componentes_graficos.JLabel import JLabel


class FrameAritmetica(Frame, ABC):
    """
    Clase que representa un marco para realizar operaciones aritméticas.

    Esta clase es una superclase abstracta que define la estructura básica de un marco para realizar operaciones aritméticas.
    Debe ser subclasificada e implementar el método abstracto 'calcular_resultado' para realizar operaciones específicas.

    Args:
        master: El widget padre al que pertenece este marco.

    Attributes:
        master: El widget padre al que pertenece este marco.
        _etiqueta_titulo (JLabel): La etiqueta de título del marco.
        _elemento1 (CampoConTitulo): El primer campo de entrada del marco.
        _elemento2 (CampoConTitulo): El segundo campo de entrada del marco.
        _boton (JButton): El botón de cálculo del marco.
        _resultado (CampoConTitulo): El campo de resultado del marco.

    """

    def __init__(self, master):
        """
        Inicializa un nuevo FrameAritmetica.

        Args:
            master: El widget padre al que pertenece este marco.

        """
        super().__init__(master=master)

        # Configura las propiedades del marco
        self.configure(bg="#ffffff")

        # Crea la etiqueta de título del marco
        self._etiqueta_titulo = JLabel(self, texto="Aritmetica")
        self._etiqueta_titulo.configure(font=("Arial", 24, "bold"))
        self._etiqueta_titulo.pack(pady=20, expand=True, fill=X)

        # Crea los campos de entrada para los números
        self._elemento1 = CampoConTitulo(self, "Numero 1 ", posicion="left")
        self._elemento1.pack(padx=20, pady=10, expand=True, fill=X)

        self._elemento2 = CampoConTitulo(self, "Numero 2", posicion="left")
        self._elemento2.pack(padx=20, pady=10, expand=True, fill=X)

        # Crea el botón para realizar el cálculo
        self._boton = JButton(master=self, nombre_boton="Calcular",
                              funcion=lambda: self._calcular_resultado())
        self._boton.pack(pady=30, padx=20, expand=True, fill=X)

        # Crea el campo de resultado
        self._resultado = CampoConTitulo(self, "Resultado", posicion="left")
        self._resultado.pack(padx=20, pady=10, expand=True, fill=X)

    @abstractmethod
    def _calcular_resultado(self):
        """
        Método abstracto para calcular el resultado de la operación aritmética.

        Este método debe ser implementado por las subclases para realizar operaciones aritméticas específicas.

        """
        pass


