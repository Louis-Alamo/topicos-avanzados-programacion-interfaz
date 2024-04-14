# Importaciones de librerías de Python
from tkinter import Frame, messagebox, Tk
from tkinter import *

# Importaciones de librerías de usuario
from GUI.componentes_combinados.CampoConTitulo import CampoConTitulo
from GUI.componentes_graficos.JLabel import JLabel
from GUI.componentes_graficos.JButton import JButton
from logic.matematica.numericos.Potencias import Potencias

class FramePotencias(Frame):
    """
    Clase que representa un marco para calcular potencias.

    Esta clase crea una interfaz gráfica que permite al usuario ingresar la base y el exponente de una potencia,
    y luego calcular y mostrar el resultado.

    Args:
        master: El widget padre al que pertenece este marco.
    """

    def __init__(self, master):
        """
        Inicializa un nuevo FramePotencias.

        Args:
            master: El widget padre al que pertenece este marco.
        """
        super().__init__(master=master)

        # Configura el fondo del marco
        self.config(bg="#FFFFFF")

        # Título del marco
        titulo_frame = JLabel(self, texto="Potencia")
        titulo_frame.configure(font=("Arial",24,"bold"))
        titulo_frame.pack(pady=20,padx=20,fill=X, expand=True)

        # Campo de entrada para la base
        self.elemento_base = CampoConTitulo(self,texto="Ingrese la base: ", posicion='left')
        self.elemento_base.pack(padx=20, pady=10, expand=True, fill=X)

        # Campo de entrada para el exponente
        self.elemento_potencia = CampoConTitulo(self, texto="Ingrese el exponente: ", posicion='left')
        self.elemento_potencia.pack(padx=20, pady=10, expand=True, fill=X)

        # Botón para calcular la potencia
        boton = JButton(self, nombre_boton="Procesar", funcion=lambda: self.calcular())
        boton.pack(padx=20, pady=10, expand=True, fill=X)

        # Campo para mostrar el resultado
        self.elemento_resultado = CampoConTitulo(self, texto="Resultado: ")
        self.elemento_resultado.pack(padx=20, pady=10, expand=True, fill=X)

    def calcular(self):
        """
        Calcula la potencia y muestra el resultado.
        """
        try:
            base = float(self.elemento_base.obtener_texto())
            exponente = float(self.elemento_potencia.obtener_texto())

            # Calcula la potencia
            resultado = Potencias().potencias(base,exponente)

            # Muestra el resultado en el campo correspondiente
            self.elemento_resultado.insertar_texto(resultado)

        except ValueError:
            # Muestra un mensaje de advertencia si el valor ingresado no es válido
            messagebox.showwarning("InvalidValueError", "El valor ingresado en un campo no es válido.")

        except Exception as e:
            # Muestra un mensaje de error si se produce una excepción no reconocida
            messagebox.showerror("UnhandledException", "Se ha producido una excepción no reconocida.")
            print(e)
