# Importaciones de librerías de Python
from tkinter import messagebox, Frame
from tkinter import *

# Importaciones de librerías de usuario
from GUI.componentes_graficos.JLabel import JLabel
from GUI.componentes_combinados.CampoConTitulo import CampoConTitulo
from GUI.componentes_graficos.JButton import JButton
from GUI.componentes_graficos.JTextBox import JTextBox
from logic.matematica.numericos.operaciones_primos.OperacionesPrimos import Primos
from excepciones.NegativeNumberException import NegativeNumberException
from excepciones.InvalidRangeException import InvalidRangeException

class FrameGenerarNumerosPrimos(Frame):
    """
    Clase que representa un marco para generar números primos en un rango dado.

    Esta clase crea una interfaz gráfica que permite al usuario ingresar un rango de números y luego generar
    todos los números primos dentro de ese rango utilizando la lógica implementada en la clase Primos.

    Args:
        master: El widget padre al que pertenece este marco.
    """

    def __init__(self, master):
        """
        Inicializa un nuevo FrameGenerarNumerosPrimos.

        Args:
            master: El widget padre al que pertenece este marco.
        """
        super().__init__(master=master)

        # Configura el fondo del marco
        self.config(bg="#FFFFFF")

        # Título del marco
        etiqueta_titulo = JLabel(self, texto="Generar números primos")
        etiqueta_titulo.configure(font=("Arial",24,"bold"))
        etiqueta_titulo.pack(padx=20, pady=20, expand=True, fill=X)

        # Campo de entrada para el límite inferior del rango
        self.campo_limite_inferior = CampoConTitulo(self,texto="Límite inferior: ", posicion="left")
        self.campo_limite_inferior.pack(padx=20,pady=10, expand=True, fill=X)

        # Campo de entrada para el límite superior del rango
        self.campo_limite_superior = CampoConTitulo(self,texto="Límite superior: ", posicion="left")
        self.campo_limite_superior.pack(padx=20,pady=10, expand=True, fill=X)

        # Botón para iniciar el proceso de generación de números primos
        boton = JButton(self, nombre_boton="Procesar", funcion=lambda: self._procesar())
        boton.pack(padx=20,pady=10, expand=True, fill=X)

        # Área de texto para mostrar los números primos generados
        self.area_texto = JTextBox(self)
        self.area_texto.pack(padx=10,pady=10, expand=True, fill=BOTH)


    def _procesar(self):
        """
        Ejecuta el proceso de generación de números primos y muestra los resultados en el área de texto.
        """
        try:
            # Obtiene los límites del rango ingresados por el usuario
            limite_inferior = int(self.campo_limite_inferior.obtener_texto())
            limite_superior = int(self.campo_limite_superior.obtener_texto())

            # Genera la lista de números primos dentro del rango especificado
            lista = Primos().generar_numeros_primos_rango(limite_inferior, limite_superior)

            # Muestra los resultados en el área de texto
            self.area_texto.insertar_texto_lista(lista)

        except ValueError:
            # Muestra un mensaje de advertencia si el valor ingresado no es válido
            messagebox.showwarning("InvalidValueError", "El valor ingresado en un campo no es válido.")

        except NegativeNumberException:
            # Muestra un mensaje de advertencia si se ingresa una cantidad negativa
            messagebox.showwarning("NegativeNumberError", "No se permiten cantidades negativas")

        except InvalidRangeException:
            # Muestra un mensaje de advertencia si el límite inferior es mayor que el límite superior
            messagebox.showwarning("InvalidRangeError", "El límite inferior no puede ser mayor que el límite superior")

        except Exception as e:
            # Muestra un mensaje de error si se produce una excepción no reconocida
            messagebox.showerror("UnhandledException", "Se ha producido una excepción no reconocida.")
            print(e)
