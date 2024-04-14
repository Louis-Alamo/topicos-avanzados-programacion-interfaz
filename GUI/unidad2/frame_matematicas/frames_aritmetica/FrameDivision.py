from tkinter import messagebox
from GUI.unidad2.frame_matematicas.frames_aritmetica.FrameAritmetica import FrameAritmetica
from logic.matematica.aritmetica import Aritmetica

class FrameDividir(FrameAritmetica):
    """
    Clase que representa un marco para realizar la operación de división.

    Esta clase es una subclase de FrameAritmetica y proporciona una interfaz para realizar la operación de división
    entre dos números ingresados por el usuario.

    Args:
        master: El widget padre al que pertenece este marco.

    """

    def __init__(self, master):
        """
        Inicializa un nuevo FrameDividir.

        Args:
            master: El widget padre al que pertenece este marco.

        """
        super().__init__(master=master)

        # Configura el título del marco
        self._etiqueta_titulo.configure(text="Division")

    def _calcular_resultado(self):
        """
        Calcula el resultado de la división e inserta el resultado en el campo correspondiente.

        """
        try:
            # Obtiene los números ingresados por el usuario
            numero1 = float(self._elemento1.obtener_texto())
            numero2 = float(self._elemento2.obtener_texto())

            # Realiza la operación de división
            resultado = Aritmetica().dividir(numero1, numero2)

            # Inserta el resultado en el campo de resultado
            self._resultado.insertar_texto(f"{resultado}")

        except ValueError:
            # Muestra un mensaje de advertencia si los valores ingresados no son válidos
            messagebox.showwarning("ValueError", "Valores ingresados no válidos")

        except ZeroDivisionError:
            # Muestra un mensaje de información si se intenta dividir por cero
            messagebox.showinfo("ZeroDivisionError", "No se permite la división entre cero")

        except Exception as e:
            # Muestra un mensaje de error si se produce una excepción no reconocida
            messagebox.showerror("Exception", "Excepción no reconocida")
            print(e)
