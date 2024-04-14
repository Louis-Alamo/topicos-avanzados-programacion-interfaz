from logic.evaluacion.MergeSort import MergeSort
from GUI.componentes_combinados.CampoConTitulo import CampoConTitulo
from GUI.componentes_graficos.JLabel import JLabel
from GUI.componentes_graficos.JButton import JButton
from GUI.componentes_graficos.JTextBox import JTextBox
from tkinter import *

class FrameEvaluacion(Frame):
    """
    Clase que representa el marco de la evaluación.

    Attributes:
        _etiqueta_titulo (JLabel): Etiqueta del título.
        _cantidad_lista_1_entry (CampoConTitulo): Campo para ingresar la cantidad de elementos de la lista 1.
        _cantidad_lista_2_entry (CampoConTitulo): Campo para ingresar la cantidad de elementos de la lista 2.
        _boton_ejecutar (JButton): Botón para ejecutar el algoritmo.
        area_resultados (JTextBox): Área para mostrar los resultados.
        n (MergeSort): Instancia del algoritmo MergeSort.
    """

    def __init__(self, master=None):
        """
        Inicializa una nueva instancia de FrameEvaluacion.

        Args:
            master (optional): El padre de este marco.
        """
        super().__init__(master)
        self.config(bg="#ffffff")

        self._etiqueta_titulo = JLabel(self, "Evaluación")
        self._etiqueta_titulo.pack(padx=10, pady=10, fill=X, expand=True)

        self._cantidad_lista_1_entry = CampoConTitulo(self, "Cantidad de elementos lista 1","left")
        self._cantidad_lista_1_entry.pack(padx=10, pady=10, fill=X, expand=True)

        self._cantidad_lista_2_entry = CampoConTitulo(self, "Cantidad de elementos lista 2", "left")
        self._cantidad_lista_2_entry.pack(padx=10, pady=10, fill=X, expand=True)

        self._boton_ejecutar = JButton(self, "Ejecutar", lambda: self._ejecutar())
        self._boton_ejecutar.pack(padx=10, pady=10, fill=X, expand=True)

        self.area_resultados = JTextBox(self)
        self.area_resultados.pack(padx=10, pady=10, fill=BOTH, expand=True)

    def _ejecutar(self):
        """
        Ejecuta el algoritmo MergeSort con las cantidades ingresadas y muestra los resultados.
        """
        cantidad1 = int(self._cantidad_lista_1_entry._campo.obtener_texto())
        cantidad2 = int(self._cantidad_lista_2_entry._campo.obtener_texto())
        self.area_resultados.eliminar_texto()
        if cantidad1 > 100 or cantidad2 > 100:
            self.area_resultados.eliminar_texto()
            self.area_resultados.insertar_texto("La cantidad de elementos no puede ser mayor a 100 para una lista")
        else:
            self.n = MergeSort(cantidad1, cantidad2)
            self.n.inicio_algoritmo()
            self.mostrar_resultados()

    def mostrar_resultados(self):
        """
        Muestra los resultados del algoritmo MergeSort en el área de resultados.
        """
        self.area_resultados.insertar_texto_concatenado("Lista 1: ")
        self.area_resultados.insertar_texto_concatenado("------------------------------------------")
        self.area_resultados.insertar_texto_lista(self.n.get_lista1())
        self.area_resultados.insertar_salto_linea()

        self.area_resultados.insertar_texto_concatenado("Lista 2: ")
        self.area_resultados.insertar_texto_concatenado("------------------------------------------")
        self.area_resultados.insertar_texto_lista(self.n.get_lista2())
        self.area_resultados.insertar_salto_linea()

        self.area_resultados.insertar_texto_concatenado("Lista 1 ordenada: ")
        self.area_resultados.insertar_texto_concatenado("------------------------------------------")
        self.area_resultados.insertar_texto_lista(self.n.get_lista1_ordenada())
        self.area_resultados.insertar_salto_linea()

        self.area_resultados.insertar_texto_concatenado("Lista 2 ordenada: ")
        self.area_resultados.insertar_texto_concatenado("------------------------------------------")
        self.area_resultados.insertar_texto_lista(self.n.get_lista2_ordenada())
        self.area_resultados.insertar_salto_linea()

        self.area_resultados.insertar_texto_concatenado("Lista final: ")
        self.area_resultados.insertar_texto_concatenado("------------------------------------------")
        self.area_resultados.insertar_texto_lista(self.n.get_lista_final())
        self.area_resultados.insertar_salto_linea()


        self.area_resultados.insertar_texto_concatenado("Fin de la evaluación")