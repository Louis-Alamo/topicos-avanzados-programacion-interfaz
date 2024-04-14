# Importaciones de librerías de Python
from tkinter import messagebox
from tkinter import *

# Importaciones de librerías de usuario
from GUI.componentes_combinados.CampoConTitulo import CampoConTitulo
from GUI.componentes_graficos.JButton import JButton
from GUI.componentes_graficos.JLabel import JLabel
from GUI.componentes_graficos.JTextBox import JTextBox
from logic.matematica.numericos.operaciones_primos.OperacionesPrimos import Primos
from excepciones.NegativeNumberException import NegativeNumberException
from excepciones.InvalidRangeException import InvalidRangeException

class FrameSerieNumerosNoPrimos(Frame):
    """
    Clase que representa un marco para generar la serie de números no primos en un rango dado.

    Esta clase crea una interfaz gráfica que permite al usuario ingresar un rango de números y luego generar
    la serie de números no primos dentro de ese rango utilizando la lógica implementada en la clase Primos.

    Args:
        master: El widget padre al que pertenece este marco.
    """

    def __init__(self, master):
        """
        Inicializa un nuevo FrameSerieNumerosNoPrimos.

        Args:
            master: El widget padre al que pertenece este marco.
        """
        super().__init__(master=master)
        self.config(bg="#FFFFFF")

        # Título del marco
        etiqueta_titulo = JLabel(self, texto="Serie mayor no primos")
        etiqueta_titulo.configure(font=("Arial", 24, "bold"))
        etiqueta_titulo.pack(pady=20, padx=20, expand=True, fill=BOTH)

        # Campo de entrada para el límite inferior del rango
        self.campo1 = CampoConTitulo(self, texto="Limite inferior: ", posicion='left')
        self.campo1.pack(padx=20, pady=10, expand=True, fill=X)

        # Campo de entrada para el límite superior del rango
        self.campo2 = CampoConTitulo(self, texto="Limite superior: ", posicion='left')
        self.campo2.pack(padx=20, pady=10, expand=True, fill=X)

        # Botón para iniciar el proceso de generación de la serie de números no primos
        boton = JButton(self, nombre_boton="Procesar", funcion=lambda: self._procesar())
        boton.pack(padx=20, pady=10, expand=True, fill=X)

        # Área de texto para mostrar los números generados y la serie de números no primos
        self.area_texto = JTextBox(self)
        self.area_texto.pack(padx=10, pady=10, expand=True, fill=X)

    def _procesar(self):
        """
        Ejecuta el proceso de generación de números no primos y muestra los resultados en el área de texto.
        """
        try:
            limite_inferior = int(self.campo1.obtener_texto())
            limite_superior = int(self.campo2.obtener_texto())

            lista, serie = Primos().serie_numeros_no_primos(limite_inferior, limite_superior)

            # Formatea la lista de números no primos y la serie de números no primos para mostrarlos en el área de texto
            lista_resultados = ["Numeros primos: "] + lista + ["Serie mayor no primos: "] + serie

            # Muestra los resultados en el área de texto
            self.area_texto.insertar_texto_lista(lista_resultados)

        except ValueError:
            messagebox.showwarning("InvalidValueError", "El valor ingresado en un campo no es válido.")

        except NegativeNumberException:
            messagebox.showwarning("NegativeNumberError", "No se permiten cantidades negativas")

        except InvalidRangeException:
            messagebox.showwarning("InvalidRangeError", "El límite inferior no puede ser mayor que el límite superior")

        except Exception as e:
            messagebox.showerror("UnhandledException", "Se ha producido una excepción no reconocida.")
            print(e)
