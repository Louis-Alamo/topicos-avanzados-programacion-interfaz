# Importaciones de librerías de Python
from tkinter import messagebox
from tkinter import *

# Importaciones de librerías de usuario
from GUI.componentes_graficos.JTextBox import JTextBox
from GUI.componentes_combinados.CampoConTitulo import CampoConTitulo
from GUI.componentes_graficos.JLabel import JLabel
from GUI.componentes_graficos.JButton import JButton
from logic.matematica.numericos.Fibonacci import Fibonacci
from excepciones.NegativeNumberException import NegativeNumberException


class FrameFibonacci(Frame):
    """
    Clase que representa un marco para calcular la serie de Fibonacci.

    Esta clase crea una interfaz gráfica que permite al usuario ingresar las semillas y la cantidad de números
    en la serie de Fibonacci, y luego ejecutar el cálculo para mostrar la serie generada.

    Args:
        master: El widget padre al que pertenece este marco.
    """

    def __init__(self, master):
        """
        Inicializa un nuevo FrameFibonacci.

        Args:
            master: El widget padre al que pertenece este marco.
        """
        super().__init__(master=master)

        # Configura el fondo del marco
        self.config(bg="#FFFFFF")

        # Etiqueta del título del marco
        etiqueta = JLabel(self, texto="Fibonacci")
        etiqueta.configure(font=("Arial", 25, "bold"))
        etiqueta.pack(pady=20, padx=20, fill=X, expand=True)

        # Frames para organizar los elementos
        frame_izquierdo = Frame(self, bg="#FFFFFF")
        frame_izquierdo.pack(side='left')

        frame_derecho = Frame(self)
        frame_derecho.pack(side='right')

        # Campos de entrada para las semillas y la cantidad de números en la serie
        self.campo_semilla1 = CampoConTitulo(frame_izquierdo, texto="Semilla 1: ")
        self.campo_semilla1.pack(padx=20, pady=10, expand=True, fill=X)

        self.campo_semilla2 = CampoConTitulo(frame_izquierdo, texto="Semilla 2: ")
        self.campo_semilla2.pack(padx=20, pady=10, expand=True, fill=X)

        self.campo_cantidad = CampoConTitulo(frame_izquierdo, texto="Cantidad: ")
        self.campo_cantidad.pack(padx=20, pady=10, expand=True, fill=X)

        # Botón para ejecutar el cálculo de Fibonacci
        boton = JButton(frame_izquierdo, nombre_boton="Ejecutar", funcion=lambda: self.calcular())
        boton.pack(padx=20, pady=10, expand=True, fill=X)

        # Área de texto para mostrar los resultados
        self.area_texto = JTextBox(master=self)
        self.area_texto.pack(padx=10, pady=10, expand=True, fill=X)

    def calcular(self):
        """
        Ejecuta el cálculo de la serie de Fibonacci y muestra los resultados en el área de texto.
        """
        try:
            # Obtiene las semillas y la cantidad de números desde los campos de entrada
            semilla1 = int(self.campo_semilla1.obtener_texto())
            semilla2 = int(self.campo_semilla2.obtener_texto())
            cantidad = int(self.campo_cantidad.obtener_texto())

            # Calcula la serie de Fibonacci
            lista = Fibonacci().fibonacci(semilla1, semilla2, cantidad)

            # Muestra la serie en el área de texto
            self.area_texto.insertar_texto_lista(lista)

        except ValueError:
            # Muestra un mensaje de advertencia si el valor ingresado no es válido
            messagebox.showwarning("InvalidValueError", "El valor ingresado en un campo no es válido.")

        except NegativeNumberException:
            # Muestra un mensaje de advertencia si se ingresa un número negativo
            messagebox.showwarning("NegativeNumberError", "No se permiten cantidades negativas")

        except Exception as e:
            # Muestra un mensaje de error si se produce una excepción no reconocida
            messagebox.showerror("UnhandledException", "Se ha producido una excepción no reconocida.")
            print(e)
