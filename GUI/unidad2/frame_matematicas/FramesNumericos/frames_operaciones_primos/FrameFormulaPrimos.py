# Importaciones de librerías de Python
from tkinter import messagebox
from tkinter import *

# Importaciones de librerías de usuario
from GUI.componentes_graficos.JLabel import JLabel
from GUI.componentes_combinados.CampoConBoton import CampoConBoton
from GUI.componentes_graficos.JTextBox import JTextBox
from logic.matematica.numericos.operaciones_primos.OperacionesPrimos import Primos
from excepciones.NegativeNumberException import NegativeNumberException

class FrameFormulaPrimos(Frame):
    """
    Clase que representa un marco para ejecutar la fórmula de números primos.

    Esta clase crea una interfaz gráfica que permite al usuario ingresar un número inicial y luego ejecutar
    la fórmula para generar los números primos utilizando la lógica implementada en la clase Primos.

    Args:
        master: El widget padre al que pertenece este marco.
    """

    def __init__(self, master):
        """
        Inicializa un nuevo FrameFormulaPrimos.

        Args:
            master: El widget padre al que pertenece este marco.
        """
        super().__init__(master=master)

        # Configuración del marco
        self.config(bg="#FFFFFF")

        # Título del marco
        titulo_frame = JLabel(self, texto="Formula de primos")
        titulo_frame.configure(font=("Arial", 24, "bold"))
        titulo_frame.pack(pady=20, padx=20, fill=X, expand=True)

        # Etiqueta para ingresar el número inicial
        etiqueta = JLabel(self, texto="Ingrese el número inicial")
        etiqueta.pack(pady=10, padx=20, fill=X, expand=True)

        # Campo de entrada con botón para procesar
        self.campo = CampoConBoton(self, nombre_boton="Procesar", funcion=lambda: self._procesar())
        self.campo.pack(pady=10, padx=20, fill=X, expand=True)

        # Área de texto para mostrar los resultados
        self.area_texto = JTextBox(self)
        self.area_texto.pack(padx=10, pady=10, fill=BOTH, expand=True)


    def _procesar(self):
        """
        Ejecuta la fórmula de números primos y muestra los resultados en el área de texto.
        """
        try:
            # Obtiene el número inicial ingresado por el usuario
            valor_inicial = int(self.campo.obtener_texto())

            # Genera la lista de números primos utilizando la fórmula
            lista = Primos().formula_primos(valor_inicial, [])

            # Limpia el área de texto y muestra los resultados
            self.area_texto.eliminar_texto()
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
