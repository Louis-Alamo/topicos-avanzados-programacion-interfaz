# Importaciones de librerías de Python
from tkinter import messagebox, Frame
from tkinter import *

# Importaciones de librerías de usuario
from GUI.componentes_graficos.JLabel import JLabel
from GUI.componentes_graficos.JTextBox import JTextBox
from GUI.componentes_combinados.CampoConBoton import CampoConBoton
from logic.matematica.numericos.operaciones_primos.OperacionesPrimos import Primos
from excepciones.NegativeNumberException import NegativeNumberException

class FrameCribaHeratostenes(Frame):
    """
    Clase que representa un marco para ejecutar la Criba de Eratóstenes.

    Esta clase crea una interfaz gráfica que permite al usuario ingresar la cantidad de números impares a generar
    y luego ejecutar el algoritmo de la Criba de Eratóstenes para encontrar los números primos en ese rango.

    Args:
        master: El widget padre al que pertenece este marco.
    """

    def __init__(self, master):
        """
        Inicializa un nuevo FrameCribaHeratostenes.

        Args:
            master: El widget padre al que pertenece este marco.
        """
        super().__init__(master=master)

        # Configura el fondo del marco
        self.config(bg="#FFFFFF")

        # Etiqueta del título del marco
        titulo_frame = JLabel(self, texto="Criba de Eratóstenes")
        titulo_frame.configure(font=("Arial", 24, "bold"))
        titulo_frame.pack(pady=20, padx=20, expand=True, fill=X)

        # Etiqueta para ingresar la cantidad de impares a generar
        etiqueta = JLabel(self, texto="Cuantos impares a generar: ")
        etiqueta.pack(pady=10, padx=10, expand=True, fill=X)

        # Campo de entrada con botón para procesar
        self.campo = CampoConBoton(self, nombre_boton="Procesar", funcion=lambda: self._procesar())
        self.campo.pack(pady=20, padx=10, expand=True, fill=X)

        # Área de texto para mostrar los resultados
        self.area_texto = JTextBox(self)
        self.area_texto.pack(padx=10, pady=10, expand=True, fill=BOTH)


    def _procesar(self):
        """
        Ejecuta el proceso de la Criba de Eratóstenes y muestra los resultados en el área de texto.
        """
        try:
            cuantos_impares = int(self.campo.obtener_texto())

            # Ejecuta la Criba de Eratóstenes para generar los números impares y encontrar los primos
            lista_impares, lista_primos = Primos().criba_de_heratostenes(cuantos_impares)

            # Formatea los resultados para mostrar en el área de texto
            lista = ["Numeros impares: "] + lista_impares + ["Numeros primos: "] + lista_primos

            # Inserta los resultados en el área de texto
            self.area_texto.insertar_texto_lista(lista)

        except ValueError:
            # Muestra un mensaje de advertencia si el valor ingresado no es válido
            messagebox.showwarning("InvalidValueError", "El valor ingresado en un campo no es válido.")

        except NegativeNumberException:
            # Muestra un mensaje de advertencia si se ingresa una cantidad negativa
            messagebox.showwarning("NegativeNumberError", "No se permiten cantidades negativas")

        except Exception as e:
            # Muestra un mensaje de error si se produce una excepción no reconocida
            messagebox.showerror("UnhandledException", "Se ha producido una excepción no reconocida.")
            print(e)
