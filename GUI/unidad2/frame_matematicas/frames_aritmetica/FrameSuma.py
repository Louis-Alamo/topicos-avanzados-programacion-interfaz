from tkinter import messagebox
from GUI.unidad2.frame_matematicas.frames_aritmetica.FrameAritmetica import FrameAritmetica
from logic.matematica.aritmetica import Aritmetica

class FrameSuma(FrameAritmetica):
    """
    Clase que representa un marco para realizar la operación de suma.

    Esta clase es una subclase de FrameAritmetica y proporciona una interfaz para realizar la operación de suma
    entre dos números ingresados por el usuario.

    Args:
        master: El widget padre al que pertenece este marco.

    """

    def __init__(self, master):
        """
        Inicializa un nuevo FrameSuma.

        Args:
            master: El widget padre al que pertenece este marco.

        """
        super().__init__(master=master)

        # Configura el título del marco
        self._etiqueta_titulo.configure(text="Suma")

    def _calcular_resultado(self):
        """
        Calcula el resultado de la suma e inserta el resultado en el campo correspondiente.

        """
        try:
            # Obtiene los números ingresados por el usuario
            num1 = float(self._elemento1.obtener_texto())
            num2 = float(self._elemento2.obtener_texto())

            # Realiza la operación de suma
            resultado = Aritmetica().sumar(num1, num2)

            # Inserta el resultado en el campo de resultado
            self._resultado.insertar_texto(f"{resultado}")

        except ValueError as e:
            # Muestra un mensaje de advertencia si los valores ingresados no son válidos
            messagebox.showwarning("ValueError", "Valores ingresados no válidos")

        except Exception as e:
            # Muestra un mensaje de error si se produce una excepción no reconocida
            messagebox.showerror("Exception", "Excepción no reconocida")
            print(e)
