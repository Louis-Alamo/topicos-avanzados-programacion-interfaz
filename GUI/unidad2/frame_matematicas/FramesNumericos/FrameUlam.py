# Importaciones de librerías de Python
from tkinter import messagebox
from tkinter import *

# Importaciones de librerías de usuario
from GUI.componentes_graficos.JTextBox import JTextBox
from GUI.componentes_graficos.JEntry import JEntry
from GUI.componentes_graficos.JButton import JButton
from GUI.componentes_graficos.JLabel import JLabel
from logic.matematica.numericos.Ulam import Ulam
from excepciones.NegativeNumberException import NegativeNumberException


class FrameUlam(Frame):
    """
    Clase que representa un marco para calcular la secuencia de Ulam.

    Esta clase crea una interfaz gráfica que permite al usuario ingresar un número y calcular la secuencia
    de Ulam correspondiente a ese número.

    Args:
        master: El widget padre al que pertenece este marco.
    """

    def __init__(self, master):
        """
        Inicializa un nuevo FrameUlam.

        Args:
            master: El widget padre al que pertenece este marco.
        """
        super().__init__(master=master)

        # Configura el fondo del marco
        self.config(bg="#FFFFFF")

        # Título del marco
        titulo_frame = JLabel(self, texto="Ulam")
        titulo_frame.pack(pady=20,padx=20,fill=X, expand=True)

        # Etiqueta para ingresar un número
        etiqueta1 = JLabel(self, texto="Ingrese un número: ")
        etiqueta1.pack(padx=20, pady=10, expand=True, fill=X)

        # Campo de entrada para el número
        self.entrada_texto = JEntry(self)
        self.entrada_texto.pack(padx=20, pady=10, expand=True, fill=X)

        # Botón para procesar el cálculo
        boton = JButton(self, nombre_boton="Procesar", funcion=lambda: self.calcular())
        boton.pack(padx=20, pady=10, expand=True, fill=X)

        # Área de texto para mostrar la secuencia de Ulam
        self.area_texto = JTextBox(self)
        self.area_texto.pack(padx=10, pady=10, expand=True, fill=X)

    def calcular(self):
        """
        Calcula la secuencia de Ulam y la muestra en el área de texto.
        """
        try:
            # Obtiene el número ingresado por el usuario
            num = int(self.entrada_texto.obtener_texto())

            # Calcula la secuencia de Ulam para el número ingresado
            lista = Ulam().ulam(num)

            # Muestra la secuencia de Ulam en el área de texto
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
