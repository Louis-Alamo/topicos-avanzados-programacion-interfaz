# Importaciones de librerías de Python
from tkinter import  messagebox
from tkinter import *

# Importaciones de librerías de usuario
from GUI.componentes_combinados.CampoConBoton import CampoConBoton
from GUI.componentes_graficos.JLabel import JLabel
from logic.textos.Palindromo import Palindromo
from excepciones.EmptyFieldException import EmptyFieldException

class FramePalindromo(Frame):
    """
    Clase que representa un marco para verificar si una palabra es un palíndromo.

    Esta clase crea una interfaz gráfica que permite al usuario ingresar una palabra
    y luego verifica si esa palabra es un palíndromo utilizando la lógica implementada en la clase Palindromo.

    Args:
        master: El widget padre al que pertenece este marco.
    """

    def __init__(self, master):
        """
        Inicializa un nuevo FramePalindromo.

        Args:
            master: El widget padre al que pertenece este marco.
        """
        super().__init__(master=master)

        # Configura el fondo del marco
        self.config(bg="#FFFFFF")

        # Título del marco
        etiqueta_titulo = JLabel(self, texto="Palindromo")
        etiqueta_titulo.configure(font=("Arial", 24, "bold"))
        etiqueta_titulo.pack(pady=20,padx=20,fill=X, expand=True)

        # Etiqueta para ingresar la palabra
        etiqueta = JLabel(self, texto="Ingresa la palabra: ")
        etiqueta.pack(padx=20, pady=10, expand=True, fill=X)

        # Campo de entrada con botón para procesar
        self.campo = CampoConBoton(self, nombre_boton="Procesar", funcion=lambda: self.calcular())
        self.campo.pack(padx=20, pady=10, expand=True, fill=X)

    def calcular(self):
        """
        Verifica si la palabra ingresada es un palíndromo y muestra el resultado.
        """
        try:
            palabra = self.campo.obtener_texto()

            # Verifica si el campo está vacío
            if palabra == "":
                raise EmptyFieldException()

            # Verifica si la palabra es un palíndromo
            if Palindromo().palindromo(palabra):
                messagebox.showinfo("Palindromo", "La palabra es palindromo")
            else:
                messagebox.showinfo("Palindromo", "La palabra no es palindromo")

        except EmptyFieldException:
            # Muestra un mensaje de advertencia si el campo está vacío
            messagebox.showwarning("EmptyFieldError", "No se permiten campos vacíos.")

        except Exception as e:
            # Muestra un mensaje de error si se produce una excepción no reconocida
            messagebox.showerror("UnhandledException", "Se ha producido una excepción no reconocida.")
            print(e)
